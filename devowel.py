word_list = []
output = []
vowels = list('aeiou')
def show_list():
  print(word_list)
  print("There are {} elements".format(len(word_list)))
  
while True:
  new_word = input("> ")
  if new_word == "DONE": 
      show_list()
      break
    
  else:
      word_list += new_word.split(",")
      show_list()

for w in word_list:
	word_list2 = list(w.lower())
   
	for c in vowels:
		while True:
			try:
				 word_list2.remove(c)
			except:
				 break
         
	output.append(''.join(word_list2).capitalize())
print(output)