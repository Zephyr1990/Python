from collections import Counter

def word_count():
    sentence = input("Give me a sentence and I'll sort the words: ").lower()
    print(sentence)
    word_list = sentence.split('\n\r')
    word_dict = {}
    cnt = Counter(word_list)
    for word in word_list:
        cnt[word] +=1
    print(cnt)
    
        
        
        
    
word_count()
