import collections
from nltk.corpus import stopwords
import pickle
import string
import sys

with open(sys.argv[1]) as f:
	data = f.readlines()

words = []
for d in data:
	if d != "\n":
		no_punc = d.translate(str.maketrans('', '', string.punctuation))
		lower = no_punc.lower()
		parsed = lower.translate(str.maketrans('', '', string.digits))

		spaced_out_tokens = ''
		for c in range(len(parsed)):
			if ord(parsed[c]) > 122: # if emoji
				flag_left, flag_right = False, False
				if c-1 >= 0 and ord(parsed[c-1]) <= 122: # if char right before was alphabetic
					spaced_out_tokens += " " + parsed[c] # pad out with space
					flag_left = True
				if c+1 < len(parsed) and ord(parsed[c+1]) <= 122: # if char right after is alphabetic
					spaced_out_tokens += parsed[c] + " " # pad out with space
					flag_right = True
				if not (flag_left and flag_right):
					spaced_out_tokens += parsed[c]
			else:
				spaced_out_tokens += parsed[c]
		words.append(spaced_out_tokens)

word_emojis = collections.defaultdict(list)
training_data = ' '.join(words)

t = 0
tokens = training_data.split()
while t < len(tokens):
	word = tokens[t]
	if word.isalpha():
		t += 1
		while t < len(tokens) and tokens[t] != '':
			if ord(tokens[t][0]) > 122: # if next token starts out with an emoji
				word_emojis[word].append(tokens[t])
				break
			t += 1
	t += 1

# Remove stopwords
for stopword in stopwords.words('english'):
	if stopword in word_emojis:
		del word_emojis[stopword]

# Save dict to use to emojify later
with open('emojidict.pickle', 'wb') as f:
	pickle.dump(word_emojis, f, protocol=pickle.HIGHEST_PROTOCOL)
