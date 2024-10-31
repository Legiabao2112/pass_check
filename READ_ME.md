# Password Security Check

This Python script checks if passwords have been exposed in data breaches using the "Have I Been Pwned" API. It helps users determine if their passwords are secure or if they need to be changed.

## Features
- Supports multiple passwords through command-line arguments, file input, or interactive input.
- Uses the "Have I Been Pwned" API to check for compromised passwords.
- Masks passwords in output for improved privacy.
- Provides a summary of compromised and safe passwords at the end of execution.

## Requirements
- Python 3.x
- `requests` library

To install the required library, run:
```sh
pip install requests
```

## Usage

### Command-Line Arguments

1. **Check passwords directly as arguments**:
   ```sh
   python checkmypass.py password1 password2
   ```

2. **Check passwords from a file**:
   ```sh
   python checkmypass.py -f passwords.txt
   ```
   The file should contain one password per line.

3. **Interactive password input**:
   Simply run the script without arguments to enter passwords interactively:
   ```sh
   python checkmypass.py
   ```
   You will be prompted to enter passwords one by one.

## Example
```sh
python checkmypass.py 123456 password123
```
Output:
```
1******6 was found 12345 times... you should probably change your password!
p*********3 was not found! Good password!

Summary: 1 password was found to be compromised, 1 password was safe.
```

## Notes
- The script uses the k-anonymity model provided by the "Have I Been Pwned" API to securely check if a password has been compromised.
- Passwords are not sent directly to the API; only the first 5 characters of the SHA-1 hash are sent, ensuring greater privacy.
- The rate limiting (`time.sleep(1)`) is used to avoid overwhelming the API with too many requests at once.


## Disclaimer
This script is for educational purposes only. The author is not responsible for any misuse of this tool or any consequences resulting from using weak or compromised passwords. Always use strong, unique passwords and consider using a password manager for better security.