import functions as fs


url = 'https://en.wikipedia.org/wiki/Blog'
#html = fs.getContent(url)
#tags = fs.remove_tags(html)
#print(fs.cleanContent(tags))

passwords = fs.passwordGenerator(url, 20, False, 0, False)
print(passwords)

#print(fs.digitsPassword(5))
#building a flask api

