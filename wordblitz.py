word_arr = [['s','r','e','y'],
['u','e','s','i'],
['b','n','i','u'],
['e','n','a','h']]

words = set()
for word in open('wordlist.txt').readlines():
    words.add(word[:-1])

print(words)
