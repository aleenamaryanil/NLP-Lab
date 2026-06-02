import nltk
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = "Aleena is living in London. She works as the CEO of a company"

tokens = word_tokenize(text.lower())
print(tokens)

stopwords = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stopwords]
print(filtered_tokens)

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print(lemmatized_tokens)

pos_tags = pos_tag(lemmatized_tokens)
print(pos_tags)