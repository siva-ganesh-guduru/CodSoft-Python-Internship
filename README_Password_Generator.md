#Password Generator

#Task-3

We import the random module to generate random characters and the string module to access the predefined sets of ASCII characters.

The generate_password() function takes the desired length as input and generates a password by randomly selecting characters from the set of ASCII letters, digits, and punctuation. It then returns the generated password.

In the main() function, we display a welcome message and prompt the user to input the desired password length. We use a while loop with a try-except block to ensure that the user enters a positive integer as the password length. If the input is not a valid positive integer, an error message is displayed until the user provides a valid input.

Once the valid password length is obtained, we call the generate_password() function to generate the password and store it in the variable password.

Finally, we display the generated password on the screen.

When the user runs the script, they will be prompted to enter the desired password length. After providing a valid length, the password generator will create a random password and display it on the screen. The user can use this generated password for their accounts, ensuring strong security and reducing the risk of password attacks.
