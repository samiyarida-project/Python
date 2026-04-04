import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag


sent ="Tokenization refers to breaking down the text into smaller units." 
print(word_tokenize(sent))
print(sent_tokenize(sent))


# Create an object of class PorterStemmer
porter = PorterStemmer()
print(porter.stem("playing"))
print(porter.stem("plays"))
print(porter.stem("played"))

# Part Of Speech Tagging
text = "It is a Computer Science platform."
tokenized_text = word_tokenize(text)
tags = pos_tag(tokenized_text)
print(tags)

output:
['Tokenization', 'refers', 'to', 'breaking', 'down', 'the', 'text', 'into', 'smaller', 'units', '.']
['Tokenization refers to breaking down the text into smaller units.']
play
play
play
[('It', 'PRP'), ('is', 'VBZ'), ('a', 'DT'), ('Computer', 'NNP'), ('Science', 'NNP'), ('platform', 'NN'), ('.', '.')]

