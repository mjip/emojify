import pickle
import random
import sys

with open('emojidict.pickle', 'rb') as f:
	emoji_dict = pickle.load(f)

to_emojify = [l.rstrip('\n') for l in sys.stdin]
to_emojify_tokens = ' '.join(to_emojify).split()

emojified = []
for token in to_emojify_tokens:
	emojified.append(token)
	if token in emoji_dict:
		emojified.append(random.choice(emoji_dict[token]))

print(' '.join(emojified))
