import functions as fs

url = 'https://en.wikipedia.org/wiki/Blog'
rawContent = fs.getContent(url)
cleanContent = fs.cleanContent(rawContent)
print(fs.findSentences(cleanContent, 25))

#building a flask api

