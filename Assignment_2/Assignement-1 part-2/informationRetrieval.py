from util import *

# Add your import statements here
from collections import defaultdict
from sentenceSegmentation import *
from tokenization import *
import math

class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.tfidf=None
		self.ts=None
		self.terms=None
		self.D=None
		self.did=None
	def wtv(self,word):
		word=word.lower()
		a=[0]*128
		for x in word:
			a[ord(x)]+=1
		vs=""
		for x in a:
			vs+=str(x)
		return vs
	def dtv(self,doc):
		dv=[0]*self.ts
		terms=self.terms
		for s in doc:
			for wd in s:
				w = self.wtv(wd)
				if w in terms:
					dv[terms.index(w)] += 1
		for j in range(len(dv)):
			dv[j] = dv[j] * math.log(self.D/ (len(self.index[terms[j]])+1))
		return dv
	def build_tfidf(self,docs,docIDs):
		terms=list(self.index.keys())
		self.ts=len(terms)
		self.terms=terms
		self.D=len(docs)
		#print(terms)
		tfidf={}
		for i in range(len(docs)):
			dv=[0]*len(terms)
			d=docs[i]
			dv=self.dtv(d)
			tfidf[docIDs[i]]=dv
		self.tfidf=tfidf
		return




	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = defaultdict(list)

		#Fill in code here
		for i in range(len(docs)):
			d=docs[i]
			did=docIDs[i]
			for s in d:
				for w in s:
					vts = self.wtv(w)
					if did not in index[vts]:
						index[vts].append(did)

		self.index = index
		self.build_tfidf(docs,docIDs)
		#print("docIds in buildIndex: ",docIDs)
		self.did=docIDs
		#print("in buildIndex", self.did)
		print("index built successfully !")
		return

	def csim(self,a,b):
		ab=0
		for i in range(len(a)):ab+=a[i]*b[i]
		ma,mb=0,0
		for i in range(len(a)):
			ma+=a[i]**2
			mb+=b[i]**2
		ma,mb=math.sqrt(ma),math.sqrt(mb)
		return ab/((ma*mb)+1e-9)

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered_all = []

		#Fill in code here
		c=0
		for query in queries:
			c+=1
			qv=self.dtv(query)
			csl = []
			intermediate_list = []
			for doc in self.did:
				#print("In rank: ",self.did, "Query: ",qv)
				dv=self.tfidf[doc]
				csl.append((self.csim(qv , dv),doc))
			csl.sort(reverse=True)
			for cosval, did in csl:
				intermediate_list.append(did)
			doc_IDs_ordered_all.append(intermediate_list)
			if (c%25)==0:
				print("processed "+str(c)+" queries.")
		#print("csl: ",csl)

		#print("Ranks: ",doc_IDs_ordered_all)
		return doc_IDs_ordered_all

'''

ir=InformationRetrieval()
d1="Hello world. This is my first information retrieval system."
d2="This is a good place. It is far away from cities."
d3="The wind is amazing. I can feel the sweetness of the flowers."
query= "Flowers are sweet"
sg=SentenceSegmentation()
tk= Tokenization()
crp=[tk.pennTreeBank(sg.punkt(d1)),tk.pennTreeBank(sg.punkt(d2)),tk.pennTreeBank(sg.punkt(d3))]
ir.buildIndex(crp,[11,12,13])
queries=[tk.pennTreeBank(sg.punkt(d1)),tk.pennTreeBank(sg.punkt(d2)),tk.pennTreeBank(sg.punkt(d3)),tk.pennTreeBank(sg.punkt(query))]

print(ir.tfidf)
print(ir.dtv(crp[0]))
print(ir.csim(ir.tfidf[11],ir.tfidf[12]))
print(ir.csim(ir.tfidf[12],ir.tfidf[13]))

print(ir.rank(queries))
'''