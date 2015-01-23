def freq():
    sentence = input("Give me your sentence: ").lower().replace('/n/r',' ')
    wordlist = sentence.split()
    wordfreq = [wordlist.count(p) for p in wordlist]
    dictionary = dict(zip(wordlist,wordfreq))
    aux = [(dictionary[key], key) for key in dictionary]
    aux.sort()
    aux.reverse()

    for a in aux:
        print(a)


freq()
