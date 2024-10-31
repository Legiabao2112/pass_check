# Password Security Check

This Python script checks if passwords have been exposed in data breaches using the "Have I Been Pwned" API. It helps users determine if their passwords are secure or if they need to be changed.


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
- Passwords are not sent directly to the API; only the first 5 characters of the SHA-1 hash are sent, so you don't have to worry about security issues.
