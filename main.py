def main(): # Nakisha Paulin
    while True: # Prints Menu
        print("Menu")  
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            new_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {decode(new_password)}.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please choose again.")

def encode(password):
    new_password = ""
    length = len(password) # Length of the password
    for i in range(0, length):  # Range is from 0 to length of password
        new_num = (int(password[i]) + 3) % 10  # Used for values over 9 to get remainder
        new_password += str(new_num)  # Int to string, and added to end of string
    return new_password

def decode(new_password):  
    original_password = ''
    for num in new_password:
            original_number = str((int(new_password[num]) - 3 ) % 10)
            original_password += original_number
    return original_password


if __name__ == '__main__':
    main()
