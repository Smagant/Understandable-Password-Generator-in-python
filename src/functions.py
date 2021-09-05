import requests as r
from bs4 import BeautifulSoup
from random import randint
import random
import string


#Main function of the passwordGenerator
def passwordGenerator(url, numCharacters=25, digits=False, numbers=0, punctuation=False):
    if digits:
        password = digitsPassword(numbers)
        if password == False:
            print("The input numbers is incorrect")
        return password
    else:
        rawContent = getContent(url)
        cleanCt = cleanContent(rawContent)
        sentences = findSentences(cleanCt, numCharacters)
        passwords = createPassword(sentences, numbers, punctuation)
        return passwords


#Extract all the content of a webpage.
def getContent(url):
    response = r.get(url)
    return response.content

def remove_tags(html):
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


#Clean the content of the page to take only the text.
#Then store the clean content into an array of sentences.
def cleanContent(rawContent):
    output = remove_tags(rawContent)
    """
    html_page = rawContent
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    
    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script']
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    """
    digits = ['\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for e in digits:
        output = output.replace(e, "")
    
    for e in string.punctuation:
        if e != '.':
            output = output.replace(e, "")
    
    array = []
    for e in output:
        if e.isupper():
            sentence = ''
            sentence += e
        elif e == '.':
            array.append(sentence)
            sentence = ''
        else:
            sentence += e

    return array


#Filter the array of sentences based on the number of characters we want.
def findSentences(cleanContent, numCharacters):
    array = []
    for e in cleanContent:
        sentence = e.replace(" ", "")
        if len(sentence)>= numCharacters:
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
