
def result():
    sqlist= [x*x for x in range(1, 11) if x%2 != 0]
    word = [l.upper() for l in 'comprehension' if l not in 'aeiou']
    wordlist = ['cat', 'dog', 'rabbit']
    letterlist = []
    #word2 = [letterlist.append(aletter) for aword in wordlist for aletter in word]
    word2 = [word[i] for word in wordlist for i in range(len(word))]

    print(word2)

result()
'''
wordlist = ['cat','dog','rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)'''