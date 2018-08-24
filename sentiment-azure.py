
'''Azure API KEY '''
key_1="XYZABCEFJ12345678"
subscription_key = key_1 
assert subscription_key

text_analytics_base_url = "https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/"


language_api_url = text_analytics_base_url + "languages"

#print(language_api_url)

documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
    { 'id': '3', 'text': '这是一个用中文写的文件' },
    { 'id': '4', 'text': 'Olá, isso é um texto em algum idioma' }
]}

import requests
import json
from pprint import pprint
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
#pprint(languages)

#print(table)

sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)

f = open("sentence.txt", "r")
count = 1
documents = {'documents':[]}

for frase in f:
	frase = frase.replace("\r","").replace("\n","")
	print("id:%d\t %s" % (count,frase))
	documents['documents'].append({'id':str(count),'language': 'pt', 'text': frase})
	count += 1


headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()

#pprint(sentiments)

for n in sentiments['documents']:
	if n['score'] <= 0.0 and n['score'] <= 0.20:
		print("id=>%s \tsentiment=Red\tscore=>%s" % (n['id'], n['score'])) 
	
	if n['score'] >= 0.21 and n['score'] <= 0.70:
		print("id=>%s \tsentiment=Yellow\tscore=>%s" % (n['id'], n['score'])) 

	if n['score'] >= 0.71:
		print("id=>%s \tsentiment=Green\tscore=>%s" % (n['id'], n['score'])) 
