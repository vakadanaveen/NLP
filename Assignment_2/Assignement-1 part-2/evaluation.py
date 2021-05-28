import json
import math
import os
from util import *

# Add your import statements here
from collections import defaultdict



class Evaluation():
	def __init__(self):
		self.qr=None #This dictionary holds the list of relevant documents for a particular query
	def build_qr(self,q_rels):
		#This function populates the self.qr dictionary which has relevant document lists as values and
		#query ids as keys of the dictionary
		qr = defaultdict(list)
		for dc in q_rels:
			qr[int(dc['query_num'])].append(int(dc['id']))
		self.qr=qr
	def get_docid(self,query_id,qrels):
		result = list(filter(lambda query: query['query_num'] == str(query_id), qrels))
		doc_id = []
		for d in result:
			for k, v in d.items():
				if k == "id":
					doc_id.append(v)
		return doc_id

	def get_rel_score(self, query_id,element, qrels):
		result = list(filter(lambda query: query['query_num'] == str(query_id), qrels))
		doc_id = []
		rel_score = []
		for d in result:
			for k, v in d.items():
				if k == "id":
					doc_id.append(v)
				if k == "position":
					# Measuring the relevance score in a scale of 0-3 where integer with higher value has greater relevance
					rel_score.append(4-int(v))

		relavant_score = rel_score[doc_id.index(element)]
		return relavant_score

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = 0

		#Fill in code here
		count = 1
		for element in query_doc_IDs_ordered:
			# Find the number of relevant documents in top k results
			if count <= k:
				# if the document is present in the relevant document list then increment precision count by 1.
				if str(element) in true_doc_IDs:
					precision = precision + 1
			count = count + 1
		if k== 0:
			precision = 1
		else:
			# Dividing precision by number of documents retrieved at rank 'k'
			precision = precision / k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		n = 0
		sum = 0
		for list in doc_IDs_ordered:
			doc_id = self.get_docid(query_ids[n], qrels)
			sum = sum + self.queryPrecision(list, query_ids[n], doc_id, k)
			n = n + 1
		if len(doc_IDs_ordered) == 0:
			meanPrecision = 1
		else:
			# Finding the average of all precision values corresponding to different queries
			meanPrecision = sum / len(doc_IDs_ordered)
		return meanPrecision


	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = 0

		#Fill in code here
		count = 1
		for element in query_doc_IDs_ordered:
			# Find the number of relevant documents in top k results
			if count <= k:
				# if the document is present in the relevant document list then increment recall count by 1.
				if str(element) in true_doc_IDs:
					recall = recall + 1
			count = count + 1
		if len(true_doc_IDs) == 0:
			recall = 1
		else:
			# Dividing recall by number of relevant documents
			recall = recall / len(true_doc_IDs)

		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		n = 0
		sum = 0
		for list in doc_IDs_ordered:
			doc_id = self.get_docid(query_ids[n], qrels)
			sum = sum + self.queryRecall(list,query_ids[n],doc_id,k)
			n = n + 1
		if len(doc_IDs_ordered) == 0:
			meanRecall = 1
		else:
			# Finding the average of all recall values corresponding to different queries
			meanRecall = sum / len(doc_IDs_ordered)
		return meanRecall

	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		# This will happen when there are no relevant documents in top k results
		if precision + recall == 0:
			fscore = 0
		else:
			fscore = (2 * precision * recall) / (precision + recall)

		return fscore

	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		# Fill in code here
		n = 0
		sum = 0
		for list in doc_IDs_ordered:
			doc_id = self.get_docid(query_ids[n], qrels)
			sum = sum + self.queryFscore(list, query_ids[n], doc_id, k)
			n = n + 1
		# Finding the average of all fscore values corresponding to different queries
		meanFscore = sum / len(doc_IDs_ordered)
		return meanFscore


	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here
		DCG = 0
		IDCG = 0
		path=os.path.join(os.getcwd(),"cranfield","cran_qrels.json")
		qrels = json.load(open(path, 'r'))[:]
		count = 1
		for element in query_doc_IDs_ordered:
			if count <= k:
				# if a document is not presented in true_doc_IDs then it means that the document is irrelevant so its relevance score is 0. 
				# Hence we will ignore such documents during DCG calculation.
				if str(element) in true_doc_IDs:
					DCG = DCG + (self.get_rel_score(query_id, str(element), qrels) / math.log2(query_doc_IDs_ordered.index(element) + 2))
				count = count + 1
		count = 1
		for element in true_doc_IDs:
			if count <= k:
				IDCG = IDCG + (self.get_rel_score(query_id,element,qrels) / math.log2(count + 1))
				count = count + 1
		# When there are no documents ideally relevant to the query then there are no documents to display.
		# Thus the relevance score is 1.
		if IDCG == 0:
			return 0
		nDCG = DCG / IDCG
		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		n = 0
		sum = 0
		for list in doc_IDs_ordered:
			result = list(filter(lambda query: query['query_num'] == str(query_ids[n]), qrels))
			true_doc_IDs = []
			for d in result:
				for ky, val in d.items():
					if ky == "id":
						true_doc_IDs.append(val)
			nDCG=self.queryNDCG(list, query_ids[n], true_doc_IDs, k)
			sum = sum + nDCG
			n = n + 1
		# Finding the average of all nDCG values corresponding to different queries
		meanNDCG = sum/len(doc_IDs_ordered)
		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		pdl=query_doc_IDs_ordered
		rdl=true_doc_IDs
		for j in range(len(pdl)):
			if pdl[j] in rdl:
				pdl[j] = 1
			else:
				pdl[j] = 0
		ap = 0
		for j in range(len(pdl)):
			ap += (sum(pdl[:(j + 1)]) * 1.0 / (j + 1))
		ap /= len(pdl)
		avgPrecision=ap
		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		MAP = 0
		# preprocess q_rels
		self.build_qr(q_rels)
		qr = self.qr

		for i in range(len(query_ids)):
			# print(len(doc_IDs_ordered_all),len(query_ids))
			pdl = doc_IDs_ordered[i][:k]
			rdl = qr[int(query_ids[i])]
			#print(pdl[:10], rdl)
			for j in range(len(pdl)):
				if pdl[j] in rdl:
					pdl[j] = 1
				else:
					pdl[j] = 0
			ap = 0
			for j in range(len(pdl)):
				ap += (sum(pdl[:(j + 1)]) * 1.0 / (j + 1))
			ap /= len(pdl)
			MAP += ap
		MAP /= len(query_ids)
		meanAveragePrecision=MAP


		return meanAveragePrecision

