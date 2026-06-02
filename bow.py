from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

corpus = [
    "Jhonny Jhonny yes pappa",
    "Eating sugar no pappa",
    "Telling lies no pappa",
    "Open your mouth"
]

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(corpus)

vocab = vectorizer.get_feature_names_out()
df_bow = pd.DataFrame(bow_matrix.toarray(),columns = vocab)
print("Vocabulary : ",vocab)
print("Vocabulary size: ",len(vocab))
print("Bag of words matrix: ")
print(df_bow)