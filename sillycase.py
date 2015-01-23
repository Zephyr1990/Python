def sillycase():
        new_word=input("Give me a word: ")
        how_long = len(new_word)
        print("The word is {} characters long.".format(len(new_word)))
        half = int(round(how_long/2.0))
        lower_half = new_word[:half].lower()
        upper_half = new_word[half:].upper()
        print(lower_half + upper_half)
        return lower_half + upper_half
        
sillycase()
