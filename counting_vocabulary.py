import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokennize

nltk.download('gutenberg')
nltk.download('punkt')

content = gutenberg.raw('austen-emma.txt')

tokens = word_tokenize(content)
words = []
for token in tokens:
    words.append(token.lower())

print("Numbe of words in the text: ",len(words))

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Number of different words in text: ",len(frequency))

search1 = input("Enter the word to search count: ")
if search1 in frequency:
    count = frequency[search1]
    print(f"Count of {search1} : ",count)
else:
    print(f"{search1} is not found")

search2 = input("Enter the word to search percentage: ")
if search2 in frequency:
    percentage = (frequency[search2]/len(words)*100)
    print(percentage)
else:
    print(f"{search2} is not found")