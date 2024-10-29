def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.lower().split()
    
    def convert_word(word):
        if word[0] in vowels:
            return word + "yay"
        
        first_vowel = next((i for i, letter in enumerate(word) if letter in vowels), -1)
        
        if first_vowel == -1:
            return word + "ay"
        
        return word[first_vowel:] + word[:first_vowel] + "ay"
    
    return ' '.join(convert_word(word) for word in words)

english_sentence = input("Enter a sentence: ")
print(pig_latin(english_sentence))
