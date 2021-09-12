import functions as fs

def main():
    while(1):
        digits = input("\nDo you want a code of digits ? (y or n): ")
        if digits == 'y':
            digiCode()
            if continueOP():
                continue
            else:
                break

        elif digits == 'n':
            password()
            if continueOP():
                continue
            else:
                break

def continueOP():
    answer = input("\nDo you want to continue ? (y or n) ")
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("\nSorry I don't understand your answer... Please try again")
        continueOP()

def digiCode():
    print("\nHow many digits do you want in your code ?")
    n = int(input("Enter the number of digits: "))
    password = fs.digitsPassword(n)
    print("\n", password)

def password():
    url = input("\nEnter the url: ")
    numChar = int(input("\nEnter the minimum number of characters for your password: "))
    numbers = int(input("\nHow many numbers do you want in your password ?: "))
    punc = input("\nDo you want to add a special character ? (y or n): ")
    if punc == 'y':
        punc = True
    elif punc == 'n':
        punc = False
    passwords = fs.passwordGenerator(url, numChar, numbers, punc)
    print("\nList of passwords:")
    i = 0
    while i < len(passwords):
        print(passwords[i])
        i += 1
    

if __name__ == "__main__":
    main()
