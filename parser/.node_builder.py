#node_builder.py      12/21/2016: Ruyan Zhang
#Given standard question input -> builds question data structure
#Depends on commonWords.p, trivialWords.p 
import sys
import os
import string
import re
#import json
import pickle
#from question_parser import getPacket

#json question example
# node = json-like = { 'answer': set() , 'keywords': set() , 'neighbors': set() , 'rank': int] 
#Packet contains nodes which are ^^json-like structures

commonWords = pickle.load( open( 'commonWords.p' , 'rb' ))   #top 7500 words
trivialWords = pickle.load( open( 'trivialWords.p' , 'rb' ))    #top 48 words plus prompt and accept
#
def main():
    return -1
#
def makePacket( packet ):
   return [ makeNode( question ) for question in packet ]
#
def makeNode( question ):
    question_text = question[ 0 ] 
    answer_text = question[ 1 ]
    
    node =  {
                'answer' : parseAnswers( answer_text ) , 
                'keywords' : parseKeywords( question_text ) ,
                'neighbors' : set() ,
                'rank' : -1
            }    
    return node
#
def parseKeywords( question_text ): #takes question raw text string -> set of keywords
    #   rareWords: words that don't show up in first 5000 (subject to change) characters
    #   capWords: all capitalized words that aren't at the start of the sentence 
    formattedQuestion =  re.sub("[\(\[].*?[\)\]]" , " ", question_text).translate(None , "0123456789").replace("\n" , " ")  #regex gets rid of all things in [], like pronunciation
    rareWords = set( [word for word in formattedQuestion.translate( None, string.punctuation ).strip().split(" ") if ( word not in commonWords and word.islower())]) 
    capWords = set( re.findall(r'(?<!\.\s)\b[A-Z][a-z]*\b',  formattedQuestion)) #re finds capitalized words not at the beginning of sentences
    return capWords.union( rareWords )
# 
def parseAnswers( answer_text ): #similar treatment as parseKeywords
    formattedAnswer = set(word for word in answer_text.lower().translate( None , string.punctuation ).replace("answer" , " ").split() if word not in trivialWords )
    return formattedAnswer
#rank 

def findNeighbors():
    return -1
#
def findRank():
    return -1
#
#
main() 
