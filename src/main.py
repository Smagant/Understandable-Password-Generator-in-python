import functions as fs


def continueOP():
    answer = input("Do you want to continue ? (y or n)")
    if answer == "y":
        return continue
    elif answer == "n":
        return break
    else:
        print("Sorry I don't understand your answer... Please try again")
        continueOP()

def digits():
    print("How many digits do you want in your code ?")
    n = int(input("Enter the number of digits:"))
    password = fs.digitsPassword(n)
    print(password)

def Password():
    url = input("Enter the url : ")
    numChar = int(input("Enter the minimum number of characters for your password : "))
    numbers = int(input("How many numbers do you want in your password ? : "))
    punc = input("Do you want to add a special character ? (y or n) : ")
    if punc == 'y':
        punc = True
    elif punc == 'n':
        punc = False
    passwords = fs.passwordGenerator(url, numChar, numbers, punc)
`   i = 0
    while i < len(passwords):
        print(passwords[i])
        i += 1
    
def main():
    while(1):
        digits = input("Do you want a code of digits ? (y or n) : ")

        if digits == 'y':
            digits()
            continueOP()

        elif digits == 'n':
            Password()
            continueOP()



