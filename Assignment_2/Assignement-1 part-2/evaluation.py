import json
import math
import os
from util import *

# Add your import statements here
from collections import defaultdict



class Evaluation():
	def __init__(self):
		self.qr=None
	def build_qr(self,q_rels):
		qr = defaultdict(list)
		#print(q_rels)
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
		#print(doc_id)
		return doc_id

	def get_rel_score(self, query_id,element, qrels):
		self.build_qr(qrels)
		for k, v in self.qr.items():
				if k == query_id:
					rel_score = v

		try:
			relavant_score = rel_score.index(element)+1
		except:
			relavant_score = 4
		print("Relavant Score: ",relavant_score)
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
		# print("Inside query PRecision")
		# print("true Doc IDs: ",true_doc_IDs)
		# print("Predicted order of relevance to query id ",query_id,"is: ",query_doc_IDs_ordered)
		for element in query_doc_IDs_ordered:
			if count <= k:
				# print("Count: ",count)
				# print("Doc id in Predicted list: ",element)
				if str(element) in true_doc_IDs:
					# print("Matched!!")
					precision = precision + 1
			count = count + 1
		#print(precision)
		precision = precision / k
		# print("Precision: ",precision)

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
		# print("Inside Mean Precision")
		for list in doc_IDs_ordered:
			doc_id = self.get_docid(query_ids[n], qrels)
			#print("K= ",k)
			sum = sum + self.queryPrecision(list, query_ids[n], doc_id, k)
			n = n + 1
		meanPrecision = sum / len(doc_IDs_ordered)
		# print("sum: ",sum,"n= ",n,"Mean Precision calculated: ",meanPrecision)
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
		# print("Inside query Recall")
		# print("true Doc IDs: ", true_doc_IDs)
		# print("Predicted order of relevance to query id ", query_id, "is: ", query_doc_IDs_ordered)
		for element in query_doc_IDs_ordered:
			if count <= k:
				# print("Count: " + str(count))
				# print("Doc id in Predicted list: ", element)
				if str(element) in true_doc_IDs:
					# print("Matched!!")
					recall = recall + 1
			count = count + 1
		# print("len(true Doc ids): ",len(true_doc_IDs))
		recall = recall / len(true_doc_IDs)
		# print("Recall: ", recall)

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
			# print("K= ",k)
			sum = sum + self.queryRecall(list,query_ids[n],doc_id,k)
			n = n + 1
		meanRecall = sum / len(doc_IDs_ordered)
		#print("sum=",sum,"n= ",n,"Mean Recall Calculated: ",meanRecall)
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
		fscore = (2 * precision * recall) / (precision + recall + 1e-11)

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
			# print("K= ",k)
			sum = sum + self.queryFscore(list, query_ids[n], doc_id, k)
			n = n + 1
		meanFscore = sum / len(doc_IDs_ordered)
		#print("sum",sum,"n= ",n,"Mean fscore calculated: ",meanFscore)
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
		#print("IDs of documents in their predicted order: ",query_doc_IDs_ordered)
		#print("Path: ",path)
		qrels = json.load(open(path, 'r'))[:]
		# doc_id = self.get_docid(query_id, qrels)
		#print("IDs of documents in their actual order: ", true_doc_IDs)
		print("CALCULATING DCG: ")
		count = 1
		for element in query_doc_IDs_ordered:
			if count <= k:
				if element in true_doc_IDs:
					# print("i= ",count)
					DCG = DCG + (self.get_rel_score(query_id, element, qrels) / math.log(count + 1))
				count = count + 1
		count = 1
		print("CALCULATING IDCG: ")
		for element in true_doc_IDs:
			# print("i= ", count)
			IDCG = IDCG + (self.get_rel_score(query_id,element,qrels) / math.log(count + 1))
			count = count + 1
		print("DCG: ",DCG,"IDCG: ",IDCG)
		nDCG = DCG / (IDCG + 1e-11)
		print(nDCG)
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
			true_doc_IDs = self.get_docid(query_ids[n], qrels)
			nDCG=self.queryNDCG(list, query_ids[n], true_doc_IDs, k)
			sum = sum + nDCG
			#print("nDCG for k= ",k,nDCG)
			n = n + 1
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

