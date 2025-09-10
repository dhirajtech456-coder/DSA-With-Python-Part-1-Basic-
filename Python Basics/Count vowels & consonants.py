word=input("Enter your word : ")
vowel=0
for char in word:
    if char.lower() in 'a,i,e,o,u':
        vowel=vowel+1
print(vowel)