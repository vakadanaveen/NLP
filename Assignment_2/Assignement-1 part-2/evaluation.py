import json
import math

from util import *

# Add your import statements here
from collections import defaultdict



class Evaluation():
	def __init__(self):
		self.qr=None
	def build_qr(self,q_rels):
		qr = defaultdict(list)
		print(q_rels)
		for dc in q_rels:
			qr[int(dc['query_num'])].append(int(dc['id']))
		self.qr=qr
	def get_docid(self,query_id,qrels):
		result = list(filter(lambda query: query['query_num'] == query_id, qrels))
		doc_id = []
		for d in result:
			for k, v in d.items():
				if k == "id":
					doc_id.append()
		print(doc_id)
		return doc_id

	def get_rel_score(self, query_id,element, qrels):
		result = list(filter(lambda query: query['query_num'] == query_id, qrels))
		rel_score = []
		rel_position = 0
		i = 0
		for d in result:
			for k, v in d.items():
				if k == "position":
					rel_score.append()
				elif k == "id" and v == element:
					rel_position = i
					break
			i = i + 1
		print(rel_score[rel_position])
		return rel_score[rel_position]

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
		for element in query_doc_IDs_ordered:
			if count <= k:
				if element in true_doc_IDs:
					precision = precision + 1
			count = count + 1
		print(precision)
		precision = precision / k
		print("Precision: ",precision)

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
		for list in doc_IDs_ordered:
			doc_id = self.get_docid(query_ids[n], qrels)
			sum = sum + self.queryPrecision(list, query_ids[n], doc_id, k)
			n = n + 1
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
		count = 0
		for element in query_doc_IDs_ordered:
			if count <= k:
				if element in true_doc_IDs:
					recall = recall + 1
			count = count + 1
		recall = recall / len(true_doc_IDs)
		print("Recall: ", recall)

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
		for list in doc_IDs_ordered:
			doc_id = self.get_docid(query_ids[n], qrels)
			sum = sum + self.queryRecall(list,query_ids[n],doc_id,k)
			n = n + 1
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
		precision = self.precision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.recall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
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
		for list in doc_IDs_ordered:
			doc_id = self.get_docid(query_ids[n], qrels)
			sum = sum + self.queryFscore(list, query_ids[n], doc_id, k)
			n = n + 1
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
		n = len(query_doc_IDs_ordered)
		DCG = 0
		IDCG = 0
		qrels = json.load(open("cranfield" + "cran_qrels.json", 'r'))[:]
		doc_id = self.get_docid(query_id, qrels)
		count = 0
		for element in query_doc_IDs_ordered:
			if count <= k:
				if element in doc_id:
					DCG = DCG + (self.get_rel_score(query_id, element, qrels) / math.log(count + 1))
		count = 0
		for element in doc_id:
			count = count + 1
			IDCG = IDCG + (self.get_rel_score(query_id,element,qrels) / math.log(count + 1))
		nDCG = DCG / IDCG
		print (nDCG)
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

