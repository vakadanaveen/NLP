from util import *

# Add your import statements here
import re
import nltk.data


class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		#Fill in code here
		a=re.split('([!?."]+)',text)
		# Contains the segmented sentences.
		b = []

		for i in range(0,len(a)-1,2):
			b.append(a[i].strip()+a[i+1].strip())
		"""To handle odd number of segments"""
		if (len(a)%2)==1:b.append(a[-1].strip())

		"""To handle empty strings passed as input"""
		segmentedText = list(filter(lambda x: True if len(x) > 0 else False, b))

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = None

		#Fill in code here
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		segmentedText=sent_detector.tokenize(text.strip())

		return segmentedText
s = SentenceSegmentation()
'''print(s.naive("Hello world! how are you?"))
print(s.punkt("Hello world! how are you?"))
print('Here naive fails: ',s.naive("Hello world! I have $10.67"))
print('punkt:',s.punkt("Hello world! I have $10.67"))
print(s.punkt("hello world!!! how Are You? I am (having a Party' 's) 1.1_2 ' s"))
print(s.naive("Hello world!!! how Are You? I am (having a party) 1.1.2 fig"))'''