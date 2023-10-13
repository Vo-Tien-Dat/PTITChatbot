from utils.SynonymMapper import *



synonyms = SynonymMapper()


word = "nghiên cứu khoa học"
def formated_word(word): 
    new_word = word.strip()
    return new_word
word = formated_word(word)
print(synonyms.mapping_text(word))