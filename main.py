# should you date Hamlet?
# try principle component analysis and classifiers
# you take some data and graph it 
# How is this data broken up into sub groups?
# finds things that generally fit into certain groups
# It can classify
# Data classifiers
# recognize the similarities of texts
# there's an edx course on it
import nltk, re, pprint
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import brown
from urllib import request
from str import join

# url for project gutenberg's hamlet
# NLTK actually has a corpora of Shakespeare's plays
# but I don't know how to look at the plan txt files for that
# and it makes my job so much easier if I can actually look at the 
# text I'm working with
# also, I just like loading things over the internet
url = "http://www.gutenberg.org/files/1524/1524-0.txt"

response = request.urlopen(url) # checks for response

hamlet = response.read().decode('utf8') # puts it into utf

tokens = word_tokenize(hamlet) # we've gotta tokenize hamlet before we can use it

hamlet = nltk.Text(tokens) # now we turn it into an nltk text so we can actually use it

#def getSpeechIndexes

hamlet = hamlet[500:41890] # sets hamlet to be just the text of the actual play

print(','.isalpha())

allCharacterLines = []

for idx, val in enumerate(hamlet):
    if isCharacter('hamlet', val):
        fullLine = getFullLine(idx)
        allCharacterLines.append(fullLine)
        
print(len(allCharacterLines))
    
for i in allCharacterLines:
    if "jest" in i:
        print(i)

def isSpeechTag(word):
    if word.isupper():
        if len(word) > 2:
            return True
    return False

def isCharacter(characterInPlay, word):
    characterInPlay = characterInPlay.upper() # makes sure the name is in uppercase
    
    if word == characterInPlay:
        return True
    else:
        return False


def getFullLine(index):
    index += 1 # moves us past the original value 
    fullLine = "" # puts first word in there
    while True: 
        index += 1 # increments index      
        currentWord = hamlet[index]
        
        if isSpeechTag(currentWord):
            return fullLine[1:]
        else:
            if currentWord.isalpha():
                fullLine += " " + currentWord
            else:
                fullLine += currentWord

print(getFullLine(9951))
