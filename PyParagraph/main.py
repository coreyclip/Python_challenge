"""
Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

    * [x]Import a text file filled with a paragraph of your choosing.
	* Assess the passage for each of the following:
		* [x]Approximate word count
		* [x]Approximate sentence count
		* [x]Approximate letter count (per word)
		* [x]Average sentence length (in words)

	* As an example, this passage:

“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, 
stood with his great sword point upwards, the red raiment of his office flapping around
 him like the red wings of an archangel. And the King saw, he knew not how, something new and 
 overwhelming. The great green trees and the great red robes swung together in the wind.
 The preposterous masquerade, born of his own mockery, towered over him and embraced the world. 
 This was the normal, this was sanity, this was nature, and he himself, with his rationality, 
 and his detachment and his black frock-coat, he was the exception and the accident - 
 a blot of black upon a world of crimson and gold.”

...would yield these results:
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.56557377049
Average Sentence Length: 24.4


"""
import os
import re

filepath = os.path.join("ZenOfPython.txt")
with open(filepath) as file:
    text = file.read()

print("Input Text:")
print("<o>" * 30)
print(text)
print("<o>" * 30)

WordList = text.split(" ")

WordCount = len(WordList)

def AverageCount(List, char=True):
    """
    Summary: Returns the average of a count of strings
    
    Paramenters:
        List [{list}] - A list of strings
        char=True - If False it's assumed that we are counting words and not 
                    characters in words
    """
    
    lenS = []
    for x in List:
        if char is True:
            elements = list(x)
        else: 
            elements = x.split(' ')
        NumOfElements = len(elements)
        lenS.append(NumOfElements)
    return sum(lenS) / len(List)
        
        
AvgLenWords = round(AverageCount(WordList), 2) 
    


def split_into_sentences(text):
    '''
    from: https://stackoverflow.com/questions/4576077/python-split-text-on-sentences
    
    exhaustively accounts for all situations in which a "." might mean something
    other than a sentence break. 
    
    '''
    caps = "([A-Z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"
    text = " " + text + "  "
    text = text.replace("\n"," ") #remove new line characters
    text = re.sub(prefixes,"\\1<prd>",text) 
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


SentenceList = split_into_sentences(text)
AvgLenSentences = round(AverageCount(SentenceList,char=False))
SentenceNumber = len(SentenceList)

print()
print("==" * 5 + " Paragraph Analysis " + "==" * 5)
print(f"Approximate word count: {WordCount}")
print(f"Number of Sentences: {SentenceNumber}")
print(f"Average Character Count: {AvgLenWords}")
print(f"Average Length of Sentences: {AvgLenSentences}")