import nltk
from nltk.tokenize import word_tokenize
from nltk import ne_chunk,pos_tag

text = "Aleena is living in London. She works as the CEO of a company"

tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

ner_tree = ne_chunk(pos_tags)
print(ner_tree)

for subtree in ner_tree:
    if hasattr(subtree, 'label'):
        entity_name = " ".join([word for word, tag in subtree.leaves()])
        entity_type = subtree.label()
        print(f"{entity_name} -> {entity_type}")