from util import *

# Add your import statements here

from nltk.corpus import stopwords
from inflectionReduction import *

class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = None

		#Fill in code here
		swl=stopwords.words('english')
		a=[]
		for sent in text:
			l=list(filter(lambda x:x not in swl,sent))
			a.append(l)
		stopwordRemovedText=list(filter(lambda x:True if len(x)>0 else False,a))
		return stopwordRemovedText


''' text=["hello world! ","how are you feeling ?","I am running"]
x=InflectionReduction()
t=Tokenization()
s=StopwordRemoval()
tkns=t.naive(text)
rtkns=x.reduce(tkns)
print(s.fromList(rtkns)) '''

	