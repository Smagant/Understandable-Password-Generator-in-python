# Password generator
Generate understandable and secure passwords easily and quickly.

### Requirements
Download the files. Then with your terminal, go to the ```src``` file.
Enter this command to install all the dependencies of the project.
```bash
pip install -r requirements.txt
```
Then run the program with this command :
```bash
python3 main.py
```

### Motivation
We know that good passwords are long passwords and not complicated passwords. But in order to build good passwords, we can't write something related to us (like our interests for example). To be sure that we can't create passwords that are related to us, we have to let the computer build the password for ourselves.

### Problem - Secure AND NOT understandable passwords
On the one hand, it's easy to create a password that is secure and not related to us. We just have to generate randomly a series of letters and numbers with a choosen length. But nobody wants a WIFI key as a password.

### Problem - Understandable AND NOT secure passwords
On the other hand generate understandable passwords may lead to security breaches because it's easy to choose something that is related to our interests or something else... Maybe you can create something totally secure and understandable. But if you have to change all your passwords urgently, It could be hard to do it yourself.

### Solution - Understandable AND secure password
How to generate with a computer something that is on the hand humanly understandable and on the other hand totally secure. The answer is Internet.

### How it works
The program will scrape content on the web (based on the url you give to it), clean it, store all the sentences, add numbers and special characters at the end of each sentence if you want. Then it finally returns a list of passwords that satisfy all your conditions (in terms of number of characters, number of digits, etc...)

