import functions as fs


url = 'https://en.wikipedia.org/wiki/Blog'
"""
rawContent = fs.getContent(url)
cleanContent = fs.cleanContent(rawContent)
arr = fs.findSentences(cleanContent, 25))
password =  
"""
passwords = fs.passwordGenerator(url, 20, False, 4, True)
print(passwords)

#print(fs.digitsPassword(5))
#building a flask api

