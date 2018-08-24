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