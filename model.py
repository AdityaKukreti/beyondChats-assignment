import requests


class SentenceTransformer:

	def __init__(self):
		self.__API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-mpnet-base-v2"
		self.__headers = {"Authorization": "Bearer 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"}

	def query(self,sourceSentence,sentences):
		response = requests.post(self.__API_URL, headers=self.__headers, json={'inputs':{'source_sentence':sourceSentence,'sentences':sentences}})
		return response.json()
	