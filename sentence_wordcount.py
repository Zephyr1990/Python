from collections import Counter

def word_count():
    sentence_origin = input("Give me a sentence and I'll sort the words: ").lower()
    sentence = sentence_origin.rstrip('\n')
    print(sentence)
    word_list = sentence.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    print(word_dict)
        
        
        
    
word_count()
