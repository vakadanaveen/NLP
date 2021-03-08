from util import *

# Add your import statements here


import re
from nltk.tokenize import TreebankWordTokenizer

class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		#Fill in code here
		a=[]
		for txt in text:
			l=re.split('([-!/\?.;:\s,()"])', txt)
			l=list(map(lambda x:x.strip(),l))
			l=list(filter(lambda x: True if len(x) > 0 else False, l))
			a.append(l)

		tokenizedText=a
		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []

		#Fill in code here
		for sent in text:
			tokenizedText.append(TreebankWordTokenizer().tokenize(sent))

		return tokenizedText
t=Tokenization()
"""print(t.naive(["Hello world! how are you?","Hai what is this"]))
print(t.pennTreeBank(["Hello world! (how) are you?","where are you ?"]))
print(t.naive(["Co-education helps cut down costs of running separate schools."]))
print(t.naive(["It is your choice to work from home/office."]))
print(t.pennTreeBank(["Co-education helps cut down costs of running separate schools."]))
print(t.pennTreeBank(["It is your choice to work from home/office."]))
print(t.pennTreeBank(["https://www.cse.iitm.ac.in/course_details.php?arg=MjI="]))
print(t.pennTreeBank(["cs20s016@smail.iitm.ac.in"]))"""