sentence = input("Enter a sentence:")
vowels = "A,a,E,e,I,i,O,o,U,u"

print ("=== TEXT ANALYZER ===")

print (f"Enter a sentence: {sentence}")

print ("--- Analysis Results ---")
print (f"total characters (with spaces):    {len(sentence)}")

print (f"total characters (without spaces): {len(sentence.replace (" ", ""))}")

print (f"Number of words:                   {len(sentence.split())}")

vowels = "aeiou"
vowel_count = sum(1 for char in sentence.lower() if char in vowels)
print ("Number of vowels:                 ",vowel_count)

sentence_upper = sentence.upper() 
print ("Uppercase version:                ", sentence_upper)

sentence_lower = sentence.lower()
print ("Lowercase version:                ",sentence_lower)

reversed_sentence = sentence[::-1]
print ("Reversed version:                 ", reversed_sentence)

starts_capital= "Yes" if sentence and sentence[0].isupper() else "No"
print ("Starts with capital?:             ", starts_capital)

punctuation = ('.', '!', '?')
ends_with_punctuation = "Yes" if sentence.endswith(punctuation) else "No"
print ("Ends with punctuation?:           ", ends_with_punctuation)
