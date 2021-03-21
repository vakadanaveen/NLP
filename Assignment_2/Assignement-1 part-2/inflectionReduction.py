from util import *

# Add your import statements here

from nltk.stem import PorterStemmer
from tokenization import *

class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []

		#Fill in code here

		ps = PorterStemmer()

		for sent in text:
			reducedText	.append(list(map(lambda x:ps.stem(x),sent)))
		
		return reducedText

'''text=["hello world","how are you","I am running"]
x=InflectionReduction()
t=Tokenization()
tkns=t.naive(text)
print(x.reduce(tkns))'''