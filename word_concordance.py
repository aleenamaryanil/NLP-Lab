text = input("Enter the text: ")
stopwords = ['a','the','an','he','she','it','is','and','or','was','were','be','been']
punctuation = ',.:;"/?\'|'
window_size = input('Enter window size: ')
target = input('Enter target word: ')
new_text = text.lower()
for p in punctuation:
    new_text = new_text.replace(p,' ')
tokens = new_text.split()
filtered_tokens = []
for token in tokens:
    if token not in stopwords:
        filtered_tokens.append(token)
print()
print("Concordance for the given word: ")
for i,token in enumerate(filtered_tokens):
    if token == target:
        left_index = i-window_size
        if left_index < 0:
            left_index = 0
        left_context = filtered_tokens[left_index:i]
        right_index = i + window_size + 1
        right_context = filtered_tokens[i+1:right_index]
        line = " ".join(left_context)+" "+ token.upper() +" "+" ".join(right_context)
        print(line)