import requests
import hashlib
import getpass
import concurrent.futures
import time
import argparse

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}. Invalid Syntax.')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5char)
    return get_password_leaks_count(response, tail)

def mask_password(password):
    if len(password) <= 2:
        return '*' * len(password)
    return password[0] + '*' * (len(password) - 2) + password[-1]

def display_summary(results):
    compromised = sum(1 for count in results if count > 0)
    safe = len(results) - compromised
    print(f"\nSummary: {compromised} passwords were found to be compromised, {safe} passwords were safe.")

def main():
    parser = argparse.ArgumentParser(description='Check if passwords have been exposed in data breaches.')
    parser.add_argument('-f', '--file', type=str, help='Path to a file containing passwords (one per line)')
    parser.add_argument('passwords', nargs='*', help='Passwords to check')
    args = parser.parse_args()

    passwords = []
    if args.file:
        try:
            with open(args.file, 'r') as file:
                passwords = [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return
    else:
        passwords = args.passwords

    if not passwords:
        while True:
            password = getpass.getpass('Enter a password to check (or press Enter to finish): ')
            if not password:
                break
            passwords.append(password)
    
    if not passwords:
        print("No passwords entered. Exiting...")
        return

    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_password = {executor.submit(pwned_api_check, password): password for password in passwords}
        for future in concurrent.futures.as_completed(future_to_password):
            password = future_to_password[future]
            try:
                count = future.result()
                results.append(count)
                masked_password = mask_password(password)
                if count:
                    print(f'{masked_password} was found {count} times... you should probably change your password!')
                else:
                    print(f'{masked_password} was not found! Good password!')
            except Exception as exc:
                print(f'Error checking password {password}: {exc}')
            time.sleep(1)  # Prevent rate limiting

    display_summary(results)

if __name__ == '__main__':
    main()
