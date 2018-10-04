# should you date Hamlet?
import nltk, re, pprint
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import brown
from urllib import request
from str import join

url = "http://www.gutenberg.org/files/1524/1524-0.txt"

response = request.urlopen(url)

hamlet = response.read().decode('utf8')



tokens = sent_tokenize(hamlet)


hamlet = nltk.Text(tokens)

type(hamlet)


def getFullLine(index):
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
    print (line)
    for s in line:
        if "HAMLET" in line:
            if len(line) < 15:
                
                return True
            else:
                return False



hamletSpeechTags = [i for i, sent in enumerate(hamlet) if isHamletLine(sent)]


for i in hamletSpeechTags:
    print(hamlet[i] + " " + str(i))

print(hamlet[3490])

allHamletLinesIndex = [x+1 for x in hamletSpeechTags]


for i in allHamletLinesIndex:    
    fullLine = getFullLine(i)
    flat_list = [item for sublist in fullLine for item in sublist]
    finalString = " ".join(flat_list)
    print(finalString)





fdist = nltk.FreqDist(allOfHamletsLines)

'''
1297, 1302, 1307, 1311, 1315, 1320, 1324, 1327, 1331, 1335, 1356, 1378, 1383, 1394, 1401, 1409, 1416, 1421, 1428, 1512, 1525, 1530, 1535, 1540, 1544, 1548, 1554, 1559, 1570, 1575, 1584, 1616, 1626, 1633, 1644, 1649, 1654, 1658, 1676, 1685, 1689, 1694, 1700, 1707, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1742, 1762, 1767, 1771, 1777, 1781, 1798, 1818, 1826, 1830, 1835, 1839, 1850, 1854, 1858, 1864, 1871, 1882, 1887, 1892, 1897, 1901, 1910, 1913, 1917, 1921, 1925, 1929, 1934, 1938, 1945, 1950, 1955, 1960, 1964, 1971, 1976, 1980, 1984, 1990, 1999, 2003, 2007, 2011, 2015

'''


    

