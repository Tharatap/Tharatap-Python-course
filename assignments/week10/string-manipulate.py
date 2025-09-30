"""

Build a Text Analysis Tool that performs the following operations on user input text:
Core Features:

1. Character Analysis:
    - Count total characters (with and without spaces)
    - Count vowels and consonants separately
    - Find most frequent character

2. Word Analysis:
    - Count total words
    - Find longest and shortest words
    - Count words starting with vowels vs consonants

3. String Transformations:
    - Convert to title case, upper case, lower case
    - Create acronym from first letter of each word
    - Reverse the entire string and each word individually
    
Example Result

Enter text: The Quick Brown Fox Jumps Over The Lazy Dog

=== TEXT ANALYSIS REPORT ===
Character Analysis:
- Total characters: 43 (with spaces), 35 (without spaces)
- Vowels: 12 (e, u, i, o, o, u, o, e, e, a, o)
- Consonants: 23
- Most frequent: 'o' (appears 4 times)

Word Analysis:
- Total words: 9
- Longest word: "Quick" (5 letters)
- Shortest word: "The" (3 letters)
- Words starting with vowels: 1 ("Over")
- Words starting with consonants: 8

Transformations:
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog
- Upper Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
- Lower Case: the quick brown fox jumps over the lazy dog
- Acronym: TQBFJOTLD
- Reversed Text: goD yzaL ehT revO spmuJ xoF nworB kciuQ ehT
- Words Reversed: ehT kciuQ nworB xoF spmuJ revO ehT yzaL goD

USE: len(), split(), count(), upper(), lower(), title(), slicing operations

"""
def character_Analysit(text):
    text_space = len(text) # นับคำรวมช่องว่าง
    text = text.replace(" ","") # ตัดช่องว่างทิ้ง
    text_out_space = len(text) # นับคำไม่รวมช่องว่าง
    text = text.lower()
    # นับสระพยัญชนะ
    count_vowels = 0
    vowels = []
    consonants = 0
    for i in text:
        if i == 'a' or i =='e' or i == 'i' or i == 'o' or i == 'u':
            count_vowels += 1
            vowels.append(i) # add vowels to list
        else:
            consonants +=1
    
    return text_space,text_out_space,vowels,count_vowels,consonants

def Word_Analysis(text):
    #นับคำ
    total_words = len(text.split()) # นับจำนวนว่ามีกี่คำ
    long_word = 0
    short_word = 0
    for i in text.split():
        if i



text = "The Quick Brown Fox Jumps Over The Lazy Dog"
text_space, text_out_space , vowels, consonants = character_Analysit(text)
print(text_space,text_out_space,vowels,consonants)