from random import randint


def split(word): 
    return [char for char in word]



def misspelling(word):
  word_chars = [""]
  your_list = ["your'e", "your", "youre","ur","you'r","you're", "yo'ur're"]
  common_letters = {"a": "e", "e": "i",  "y": "i", "i": "y"}
  misspelled_count = 0
  misspelled_max = len(word) - 2
  if "your" in word:
    word = your_list[randint(0,len(your_list))]
    return word
  word_chars = split(word)
  for count,letter in enumerate(word_chars):
    print(count)
    print(len(word_chars))
    if misspelled_count == misspelled_max:
      print(misspelled_count, misspelled_max)
      word = ""
      for letter in word_chars:
        print(letter)
        word += letter
      return word
    if count == len(word_chars) and letter == "e":
      del word_chars[count]
      print("e")
      misspelled_count += 1
      continue
    try:
      if word_chars[count] == word_chars[count + 1]:
        print("yes")
        word_chars.remove(letter)
        misspelled_count += 1
        continue
    except:
      print("END OF STRING")
      break
    if letter in common_letters.keys():
      print("common")
      word_chars[count] = common_letters[letter]
      misspelled_count += 1
      continue
    if letter.upper() == letter:
      word_chars[count] = letter.lower()




  word = ""
  for letter in word_chars:
    print(letter)
    word += letter
  return word


def convert(lst): 
    return (lst[0].split()) 


def misspell_sentence(sentence):
  #Unpacking our sentence into a list of words
  sentence_words = []
  sentence_words.append(sentence)
  sentence_words = convert(sentence_words)
  print(sentence_words)
  #NOW, to process the sentence!
  for count,word in enumerate(sentence_words):
    sentence_words[count] = misspelling(word)
  #FINALLY, we slap the string back together
  sentence = ""
  for word in sentence_words:
    print(word)
    sentence += word
    sentence += " "
  return sentence

misspelled = misspell_sentence(str(input('Enter a Sentence.')))
print(misspelled)



  
