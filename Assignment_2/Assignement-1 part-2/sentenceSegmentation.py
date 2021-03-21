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

#print(s.naive('Consider fig 2.3.1. It is in page 36.'))
'''
print('top-down performs better: ')
print('naive: ',s.naive('Rao is vising USA.He will arrive here today.'))

print('punkt: ',s.punkt('Rao is vising USA.He will arrive here today.'))

print('punkt performs better: ')
print('naive: ',s.naive('Mr. Rao is vising USA. He will arrive here today.'))

print('punkt: ',s.punkt('Mr. Rao is vising USA. He will arrive here today.'))
'''