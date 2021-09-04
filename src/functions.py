import requests as r
from bs4 import BeautifulSoup

def getContent(url):
    #collect all the content
    response = r.get(url)
    return response.content

def cleanContent(rawContent):
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
    
    output = output.replace("\n", "")
    output = output.replace(",", "")
    output = output.replace("'", "")

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

def findSentences(cleanContent, numCharacters):
    array = []
    for e in cleanContent:
        sentence = e.replace(" ", "")
        if len(sentence)>= numCharacters:
            array.append(sentence)
        else:
            continue
    return array

def createPassword(sentence, numbers, speCharacters):
    #code
    pass

def passwordGenerator(url, digits, numbers, speCharacters):
    if digits:
        password = fs.digitsPassword(digits)
        return password
    else:
        rawContent = fs.getContent(url)
        cleanContent = fs.cleanContent(rawContent)
        sentences = fs.findSentences(cleanContent)
        password = createPassword(sentences, numbers, speCharacters)
        return password

def digitsPassword(numDigits):
    #code
    pass
