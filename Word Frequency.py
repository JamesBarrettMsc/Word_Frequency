# Word Frequency
from collections import Counter
import re

def get_frequency(text:str)->list[str,int]:
    
    lower_text=text.lower()
    words_by_frequency:list =[]
    
    for word in set(text.split()):
        words_by_frequency.append(f"{word} = {text.count(word)}")
        
    
    return words_by_frequency




def main()->None:
    print(get_frequency("the quick brown fox jumped over the lazy dog"))
    


if __name__=="__main__":
    main()

