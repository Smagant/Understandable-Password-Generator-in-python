import requests as r
from bs4 import BeautifulSoup
from random import randint
import random
import string


#Main function of the passwordGenerator
def passwordGenerator(url, numCharacters=25, numbers=0, punctuation=False):
    raw = getContent(url)
    clean = cleanContent(raw)
    sentences = findSentences(clean, numCharacters)
    passwords = createPassword(sentences, numbers, punctuation)
    return passwords


#Extract all the content of a webpage.
def getContent(url):
    response = r.get(url)
    return response.content


#Clean the content of the page to take only the text.
#Then store the clean content into an array of sentences.
def cleanContent(raw):
    global sentence
    digits = ['–','’','\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    #remove the html and css tags
    soup = BeautifulSoup(raw, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
    output = ' '.join(soup.stripped_strings)
    
    #remove digits and \n
    for e in digits:
        output = output.replace(e, "")
    
    #remove punctuation except the '.' 
    for e in string.punctuation:
        if e != '.':
            output = output.replace(e, "")
    
    #isolate sentences 
    array = []
    for e in output:
        if e.isupper():
            sentence = ''
            lower = e.lower()
            sentence += lower
        elif e == '.':
            array.append(sentence)
            sentence = ''
        else:
            try:
                sentence += e
            except:
                continue

    return array


#Filter the array of sentences based on the number of characters we want.
def findSentences(clean, numCharacters):
    array = []
    for e in clean:
        sentence = e.replace(" ", "")
        if (len(sentence)>= numCharacters) and (len(sentence)<=numCharacters + 10):
            array.append(sentence)
        else:
            continue
    return array


#Create an array containing the final passwords
def createPassword(sentences, numbers, punctuation):
    passwords = []
    for sentence in sentences:
        if numbers > 0:
            digits = digitsPassword(numbers)
        else:
            digits = ""

        if punctuation:
            punc = random.choice(string.punctuation)
        else:
            punc = ""
        password = sentence + str(digits) + punc
        passwords.append(password)

    return passwords


#Create a code of digits
def digitsPassword(n):
    if n > 0:
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    else:
        return False
