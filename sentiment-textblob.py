from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

f = open("sentence.txt", "r")
count = 1
sentiment = {'documents':[]}

for frase in f:
	frase = frase.replace("\r","").replace("\n","")
	print("id:%d\t %s" % (count,frase))
	frase = TextBlob(frase)
	traducao = str(TextBlob(str(frase.translate(to='en'))))
	blob = TextBlob(traducao)
	sentiment['documents'].append({'id':str(count),'language': 'pt', 'text': frase, 'score': blob.sentiment.polarity })
	count += 1

for n in sentiment['documents']:
        if n['score'] <= -0.1 :
                print("id=>%s \tsentiment=Red\tscore=>%s" % (n['id'], n['score']))

        if n['score'] >= 0.0 and n['score'] <= 0.65:
                print("id=>%s \tsentiment=Yellow\tscore=>%s" % (n['id'], n['score']))

        if n['score'] >= 0.66:
                print("id=>%s \tsentiment=Green\tscore=>%s" % (n['id'], n['score']))

