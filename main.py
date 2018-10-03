# should you date Hamlet?
import nltk, re, pprint
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import brown
from urllib import request

url = "http://www.gutenberg.org/files/1524/1524-0.txt"

response = request.urlopen(url)

hamlet = response.read().decode('utf8')

print(hamlet[:100])

tokens = sent_tokenize(hamlet)

print(tokens[34][0])


hamlet = nltk.Text(tokens)

type(hamlet)


# this function returns True if the argument is HAMLET
# case sensitive
def isHamletLine(line):
 for s in line:
    if "HAMLET" in line:
        return True
    else:
        return False

string = "this is Hamlet"

print (isHamletLine(string))



hamletSpeechTags = [i for i, sent in enumerate(hamlet) if isHamletLine(sent)]

allHamletLinesIndex = [x+1 for x in hamletSpeechTags]

print(hamlet[allHamletLinesIndex[7]])

