import random

def nchoices(iterable, num_items):
    item_list =[]
    how_long = input('Whats the range? ') 
    iterable = range(int(how_long))
    
    num_items = int(input('How big should the board be? '))    
    
    while len(item_list) < num_items:
        num = random.choice(iterable)
        item_list.append(num)
    print(item_list)
    return item_list

nchoices(12,2)

