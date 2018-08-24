sentilexpt = open("./SentiLex-flex-PT01.txt",'r')

dic_palavra_polaridade = {}

for i in sentilexpt.readlines():
	pos_ponto = i.find('.')
	palavra = (i[:pos_ponto])
	palavra = palavra.split(',')[0]
	#print(palavra)
	pol_pos = i.find('POL')
	polaridade = (i[pol_pos+4:pol_pos+6]).replace(';', '')
	dic_palavra_polaridade[palavra] = polaridade

#print (dic_palavra_polaridade)
#print (dic_palavra_polaridade.get('abusivo'))

def Score_sentimento(frase):
	frase = frase.lower()
	l_sentimento = []
	for p in frase.split():
		l_sentimento.append(int(dic_palavra_polaridade.get(p, 0)))
		#print("palavra=%s polaridade=%s" % (p,int(dic_palavra_polaridade.get(p, 0))))

	score = sum(l_sentimento)
	if score > 0:
		return "Green"
	elif score == 0:
		return "Yellow"
	else:
		return "Red"


count = 1
sentiment = {'documents':[]}

f = open("sentence.txt", "r")

for frase in f:
	frase = frase.replace("\r","").replace("\n","")
	print("id:%d\t %s" % (count,frase))
	score = Score_sentimento(frase)
	sentiment['documents'].append({'id':str(count),'language': 'pt', 'text': frase, 'score': score })
	count += 1


for n in sentiment['documents']:
	print("id=>%s \tsentiment=%s" % (n['id'], n['score']))


