# sentiment-benchmark-PT

This project helps to evaluate the various techniques of analysis of sentiment in Portuguese.

We know that the Portuguese language is very rich, but at the same time little used around the world. When we talk about NLP (Natural Language Processing), we still have a lot to improve the algorithms and libraries, for this reason I decided to create this project to help people choose between the various options we have and know their pros and cons.

## Method One  - Python textBlob Library

TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more. (Official description)

In this case, we first translated the sentences (Google Translation) and then submitted the translated sentences for sentiment analysis and returned a thermometer with the labels (Red/Yellow/Green).

## Method Two - Azure Sentiment Analyses

Microsoft Azure is rich in APIs for cognitive computing, but it has costs and does not always fit in all projects.

## Method Tree - Polarity with Portuguese Lexico

This method is the fastest, but what else should be careful, because with the low amounts of people contributing as the Lexico, we can have an error rate greater than the others.

### Exemple

```bash
[root@devspfortics sentiment-benchmark-PT]# python sentiment-azure.py &&  python sentiment-polarity.py && python sentiment-textblob.py
### AZURE ###
https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment
id:1     Eu estou muito triste com a atuação de empresa, seus produtos estão com problemas e seu suporte é uma droga
id:2     Nós aqui na empresa estamos todos muito tristes com a atuação de empresa, seus produtos estão com problemas e seu suporte é uma droga
id:3     Excelente filme, um dos melhores, indico demais, :-)
id:4     Esse produto é muito bom, excelente... muito melhor, muito agradavel eu acredito demais ... estão de parabéns, é um texto longo, quero ver como se comporta assim
id:5     Este artigo é muito ruim, pobre, estou muito triste, é muito ruim, é uma droga.
id:6     Não estou dizendo nada demais, apenas algumas coisas para encher linguiça, é apenas um teste.
id:7     Bom dia, sou o Edison da empresa Fortics, estou entrando em contato para reportar um problema que estou sofrendo no sistema. Acontece que, quando eu tento acessar o sistema, eu recebo a mensagem de erro
id:8     Bom dia, sou o Edison da empresa Fortics, estou muito insatisfeito com o atendimento, ninguem me retorna, só problemas, lentidão, uma decepção droga de atendimento
id:9     Muito bom seu sistema, estão de parabéns, maravilhoso ... ;)
id:10    Percebi que nos ultimos dias o sistema está mais lento, não obtive respostas do suporte.
id=>1   sentiment=Red   score=>0.0
id=>2   sentiment=Yellow        score=>0.3693081736564636
id=>3   sentiment=Green score=>1.0
id=>4   sentiment=Green score=>0.8846153616905212
id=>5   sentiment=Red   score=>0.0
id=>6   sentiment=Yellow        score=>0.21497052907943726
id=>7   sentiment=Yellow        score=>0.2142857164144516
id=>9   sentiment=Green score=>1.0
id=>10  sentiment=Yellow        score=>0.34923967719078064
### POLARITY ####
id:1     Eu estou muito triste com a atuação de empresa, seus produtos estão com problemas e seu suporte é uma droga
id:2     Nós aqui na empresa estamos todos muito tristes com a atuação de empresa, seus produtos estão com problemas e seu suporte é uma droga
id:3     Excelente filme, um dos melhores, indico demais, :-)
id:4     Esse produto é muito bom, excelente... muito melhor, muito agradavel eu acredito demais ... estão de parabéns, é um texto longo, quero ver como se comporta assim
id:5     Este artigo é muito ruim, pobre, estou muito triste, é muito ruim, é uma droga.
id:6     Não estou dizendo nada demais, apenas algumas coisas para encher linguiça, é apenas um teste.
id:7     Bom dia, sou o Edison da empresa Fortics, estou entrando em contato para reportar um problema que estou sofrendo no sistema. Acontece que, quando eu tento acessar o sistema, eu recebo a mensagem de erro
id:8     Bom dia, sou o Edison da empresa Fortics, estou muito insatisfeito com o atendimento, ninguem me retorna, só problemas, lentidão, uma decepção droga de atendimento
id:9     Muito bom seu sistema, estão de parabéns, maravilhoso ... ;)
id:10    Percebi que nos ultimos dias o sistema está mais lento, não obtive respostas do suporte.
id=>1   sentiment=Red
id=>2   sentiment=Red
id=>3   sentiment=Green
id=>4   sentiment=Yellow
id=>5   sentiment=Yellow
id=>6   sentiment=Yellow
id=>7   sentiment=Green
id=>8   sentiment=Red
id=>9   sentiment=Green
id=>10  sentiment=Yellow
### textBlob ###
id:1     Eu estou muito triste com a atuação de empresa, seus produtos estão com problemas e seu suporte é uma droga
id:2     Nós aqui na empresa estamos todos muito tristes com a atuação de empresa, seus produtos estão com problemas e seu suporte é uma droga
id:3     Excelente filme, um dos melhores, indico demais, :-)
id:4     Esse produto é muito bom, excelente... muito melhor, muito agradavel eu acredito demais ... estão de parabéns, é um texto longo, quero ver como se comporta assim
id:5     Este artigo é muito ruim, pobre, estou muito triste, é muito ruim, é uma droga.
id:6     Não estou dizendo nada demais, apenas algumas coisas para encher linguiça, é apenas um teste.
id:7     Bom dia, sou o Edison da empresa Fortics, estou entrando em contato para reportar um problema que estou sofrendo no sistema. Acontece que, quando eu tento acessar o sistema, eu recebo a mensagem de erro
id:8     Bom dia, sou o Edison da empresa Fortics, estou muito insatisfeito com o atendimento, ninguem me retorna, só problemas, lentidão, uma decepção droga de atendimento
id:9     Muito bom seu sistema, estão de parabéns, maravilhoso ... ;)
id:10    Percebi que nos ultimos dias o sistema está mais lento, não obtive respostas do suporte.
id=>1   sentiment=Red   score=>-0.42500000000000004
id=>2   sentiment=Red   score=>-0.2833333333333334
id=>3   sentiment=Green score=>0.675
id=>4   sentiment=Yellow        score=>0.6280000000000001
id=>5   sentiment=Red   score=>-0.5919999999999999
id=>6   sentiment=Yellow        score=>0.0
id=>7   sentiment=Green score=>0.7
id=>8   sentiment=Yellow        score=>0.3
id=>9   sentiment=Green score=>0.7200000000000001
id=>10  sentiment=Yellow        score=>0.0

```