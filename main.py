# should you date Hamlet?
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

tokens = sent_tokenize(hamlet) # we've gotta tokenize hamlet before we can use it

hamlet = nltk.Text(tokens) # now we turn it into an nltk text so we can actually use it


def getFullLine(index):
    """
    This takes in an index of a character's speech tag and then grabs all their text until it runs into the next
    character's speech tag. It does not include either tags in the list it returns. 
    """
    firstLine = word_tokenize(hamlet[index])
    sentenceList = [firstLine]
    while True:
        index += 1
        line = word_tokenize(hamlet[index])
        if line[0].isupper():
            return sentenceList
        else:
            sentenceList.append(line)
      

    return sentenceList

# this function returns True if the argument is HAMLET
# case sensitive
def isHamletLine(line):
    """
     determines if a sentence is a HAMLET speech tag
        I can rewrite it for any other character
     """
    print (line)
    for s in line:
        if "HAMLET" in line:
            if len(line) < 15:
                
                return True
            else:
                return False


# this line grabs all of Hamlet's speech tags throughout the play 
hamletSpeechTags = [i for i, sent in enumerate(hamlet) if isHamletLine(sent)]


# this line adds one to each of the index so that it starts at the correct place
# we don't want each string to begin with HAMLET.
allHamletLinesIndex = [x+1 for x in hamletSpeechTags]


finalString = ""

for i in allHamletLinesIndex:    
    fullLine = getFullLine(i)   
    flat_list = [item for sublist in fullLine for item in sublist]
    asString = " ".join(flat_list)
    finalString = finalString + asString
    

tokenized_finalString = word_tokenize(finalString)

hamletsLines = nltk.Text(tokenized_finalString)

    
fdist = nltk.FreqDist(hamletsLines)

mostCommon = fdist.most_common(150)

print(mostCommon[3][0])

longerMostCommon = [w for w in mostCommon if len(w[0]) > 4 ]

print(longerMostCommon)
