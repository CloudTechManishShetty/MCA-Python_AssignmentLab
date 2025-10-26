correct_password = "Manish@12";
attempts = 3;

for i in range(attempts):
    entered = input("Enter password: ");
    if entered == correct_password:
        print("Login Successful");
        break;
    else:
        print("Incorrect password. Attempts left:", attempts - i - 1);
else:
    print("Account Locked");