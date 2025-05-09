# Word Frequency
from collections import Counter
import re

def get_frequency(text:str)->list[str,int]:
    
    lower_text=text.lower()
    words_by_frequency:list =[]
    
    for word in set(text.split()):
        words_by_frequency.append(f"{word} = {text.count(word)}")
        
    
    return words_by_frequency

def read_text_file(file_path:str)->str:
    
    text=""
    try:
        with open(file_path) as f:
            text=f.read(file_path)
    except Exception as e:
        print(e)
    else:
        return file_path

def main()->None:
    print(get_frequency("the quick brown fox jumped over the lazy dog"))
    


if __name__=="__main__":
    main()

