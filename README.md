# PasswordGenerator
Generic offline password generator made using python. I do not intend on updating this generator unless:
- Bugs in the code are reported to me or
- I decide to update it to make it more efficient by:
- - Adding a visual GUI
- - Making the code more efficient
- - Adding a standalone .exe that runs the programm without any need of installation

## Version 1.1
This version includes the following updates and improvements:
- Input validation for `typeChar` and `length`
- Dictionary to map `typeChar` options to their corresponding character sets
- Meaningful variable names and avoidance of hardcoding values
- Resetting the `password` variable for each new password generation
- Comments explaining the purpose of each section
- Use of the `secrets` module for generating random characters
- Option to include or exclude specific character sets in the generated password
- Function to check the strength of the generated password
- Option to save the generated password to a file or copy it to the clipboard
- Character sets and other constants defined in a separate configuration file
- Functions for each major task
- Error handling for unexpected input or issues during execution

## Installation
You have three methods of installing.
### First method - `.py` execution
- Download the main `.py` [file](https://github.com/Normolo/PasswordGenerator/blob/main/Password%20Generator/PassGenerator.py) in the repository.
- If not already downloaded/installed, [download Python 3.X](https://www.python.org/downloads/release/python-397/)
- Execute the `.py` file via python
### Second Method - `.exe` `7z` installation 
- Download the `.exe` [file](https://github.com/Normolo/PasswordGenerator/releases/download/v1.0/Password.Generator.7z.exe) found in the [release section](https://github.com/Normolo/PasswordGenerator/releases/tag/v1.0).
- Execute the downloaded file
- Execute the `python-3.9.7-amd64` file in order to install python.
- Execute the password generator file with python.
### Third Method - `.exe` `IExpress` installation
- Download the `.exe` [file](https://github.com/Normolo/PasswordGenerator/releases/download/v1.0/Password.Generator.IEM.exe) found in the [release section](https://github.com/Normolo/PasswordGenerator/releases/tag/v1.0).
- Execute the downloaded file
- Execute the `python-3.9.7-amd64` file in order to install python.
- Execute the password generator file with python.

## Usage
1. Run the script using Python 3.x.
2. Select the character range from the following options: `all`, `numbers`, `special`, `letters`, `onlySmallLetters`, `onlyCapsLetters`.
3. Enter the desired length of the password (must be a positive integer).
4. The generated password will be displayed along with its strength.
5. Optionally, save the generated password to a file or copy it to the clipboard.

## Input Validation and Error Handling
- The script includes input validation for `typeChar` and `length`.
- If an invalid option is entered for `typeChar`, an error message will be displayed, and the user will be prompted to enter a valid option.
- If an invalid input is entered for `length`, an error message will be displayed, and the user will be prompted to enter a valid integer.

## Password Strength Checker
- The script includes a function to check the strength of the generated password.
- The password strength is evaluated based on length and character variety.
- The strength is categorized as `Strong`, `Medium`, or `Weak`.

## Saving the Generated Password
- The script includes an option to save the generated password to a file.
- If the user chooses to save the password, it will be saved to a file named `password.txt`.

## Code Structure and Organization
- The character sets and other constants are defined in a separate configuration file (`config.json`).
- The script includes functions for each major task, such as getting user input, generating the password, and displaying the password.
- The script includes error handling to gracefully handle unexpected input or issues during execution.

## Running Unit Tests
- The repository includes unit tests to ensure the script works as expected.
- To run the unit tests, use the following command:
  ```
  python -m unittest discover tests
  ```

## License
This project is licensed under the Creative Commons Legal Code CC0 1.0 Universal.

## Running the Raw Source Code
To run the raw source code on your desktop quickly, follow these steps:
1. Download the main `.py` [file](https://github.com/Normolo/PasswordGenerator/blob/main/Password%20Generator/PassGenerator.py) and the `config.json` [file](https://github.com/Normolo/PasswordGenerator/blob/main/Password%20Generator/config.json) in the repository.
2. If not already downloaded/installed, [download Python 3.X](https://www.python.org/downloads/release/python-397/).
3. Open a terminal or command prompt and navigate to the directory where the downloaded files are located.
4. Run the script using the following command:
   ```
   python PassGenerator.py
   ```
