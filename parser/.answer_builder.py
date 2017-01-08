#question_parser.py       12/15/16: Ruyan Zhang
#First draft for finding links between quizbowl questions
#Depends on node_builder.py
import sys
import os
import re
import json 
#from node_builder import makePacket
# ['answer': set() , 'keywords': set() , 'neighbors': set() , 'rank' : int] -> Node -> Packets -> Tournament
#

def main():
    #print (os.listdir( '/home/rz5000/Drive/12th/SysLab/new_trier_test_questions' ) )
    tournament = parseTournament( '/home/rz5000/Drive/12th/SysLab/new_trier_test_questions/' ) 
    answerlist = [ node['answer'] for packet in tournament for node in packet ] 
    print answerlist

    for answer in answerlist:
        temp_answer = answer
        for answer_comp in answer:
         one = 1
            
    #print( [ node['answer'] for node in nodeList ] )
#
def parseTournament( folder_name ):
    return [ parsePacket( folder_name + filename ) for filename in os.listdir(folder_name)]
#
def parsePacket( filename ):
    raw_question_text = open( filename , 'r' ).read()
    regex = re.compile(r'(\d+\..+?)\n(Answer:[^\n]+)\n', re.MULTILINE | re.DOTALL)
    raw_packet = regex.findall( raw_question_text )

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
#
main()
