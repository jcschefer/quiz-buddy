#question_parser.py       12/15/16: Ruyan Zhang
#First draft for finding links between quizbowl questions
#Used on new trier question format
import time
import sys
import os
import re
import string
import json 
import pickle

#from node_builder import makePacket
# ['answer': set() , 'keywords': set() , 'neighbors': set() , 'rank' : int] -> Node -> Packets -> Folder (or Tournament)
#
#
def main():
    #folder = parseFolder( './txtQuestions/' ) 
    nodelist = []
    #nodelist = [ node for packet in folder for node in packet ] 
#    os.remove( './nodelist.p' )
#    with open( 'nodelist.p' , 'w' ) as f :
#        pickle.dump( nodelist , f )
    nodelist = pickle.load( open( 'nodelist.p' , 'rb' ) ) 

    #checking if the answer is another answer's keyword is pretty good!
    length = len( nodelist )
    num = 0

    answers = set()
    for node in nodelist:
        answers.add( node['raw_answer'] )

    print 'total answers: ' , length
    print 'unique answers: ' , len( answers ) 
    print '% unique answer: ' , float( len( answers )) / length * 100

    tick = time.time()
    lengthList = []

    for target_node in nodelist:
        lengthList.append( (len( target_node['keywords'] ), target_node['keywords'] , target_node['raw_answer'] ) )

#    for item in sorted( lengthList ):
#        print item
#        print "--------------------------------"
    
#    for target_node in nodelist:
#        num += 1
#        if num % 100 == 0:
#            print str( num ) , ' / ', length 
#        if len( target_node['keywords'] ) > len( maxNode['keywords'] ) :
#            maxNode = target_node
#        for candidate_node in nodelist:
#            #if target_node['answer'] == candidate_node['answer'] and target_node != candidate_node :
#            #threshold = ( len( target_node['keywords']) + len( candidate_node['keywords']) ) / 4
#            #keywordMatch = len(target_node['keywords'] & candidate_node['keywords']) 
#            if len( target_node['answer'] & candidate_node['keywords'] ) >= 2 and not areSameNode( target_node , candidate_node ):
#                target_node['neighbors'].add( candidate_node['raw_answer'] )
#                matches += 1
#
#            #if( len( target_node['keywords'] & candidate_node['keywords'] ) >= ( (len( target_node['keywords']) + len( candidate_node['keywords']) ) / 8 ) and len( target_node['answer'] & candidate_node['answer'] ) == 0 and matches < 200 ) :
#    toc = time.time()
#
#    for node in nodelist:
#        if node['neighbors'] != set():
#            print node['raw_answer'] 
#            print node['neighbors'] 
#            print( "---------------------------------------------" )
#
#    print "maxNode:"
#    print maxNode 
#    print matches        
#    print len( nodelist )
#
#    print ( toc - tick )
#

def areSameNode( node1 , node2 ):
    if node1['raw_answer'] != node2['raw_answer']:
        return False
    if node1['packet'] != node2['packet']:
        return False
    elif node1['answer'] != node2['answer']:
        return False
    elif node1['keywords'] != node2['keywords']:
        return False
    else:
        return True
#
#
def parseFolderExplicit( folder_name ):
    packet = [ ( packetname , parsePacketExplicit( folder_name + packetname ) for packetname in os.listdir( folder_name ) ) ]
    return packet
#
#
def parsePacketExplicit( packetname ) :
    raw_question_text = open( packetname , 'r' ).read()
    #regex = re.compile(r'(\d+\..+?)\n(Answer:[^\n]+)\n', re.MULTILINE | re.DOTALL) #original samuel magic!
    regex = re.compile(r'(\d+\..+?)\n((Answer:|ANSWER)[^\n]+)\n', re.MULTILINE | re.DOTALL)
    raw_packet = regex.findall( raw_question_text )

    packet = [ makeNodeExplicit( question , packetname ) for question in raw_packet ]

    return packet
#
#
def makeNodeExplicit( question , packetname ): #depends on commonWords.p and trivialWords.p
    commonWords = pickle.load( open( 'commonWords.p' , 'rb' ))   #top 7500 words
    trivialWords = pickle.load( open( 'trivialWords.p' , 'rb' ))    #top 48 words plus prompt and accept
    #
    question_text = question[ 0 ] 
    answer_text = question[ 1 ]

    node =  {
            'answer' : parseAnswers( answer_text , trivialWords ) , 
            'raw_answer' : answer_text ,
            'keywords' : parseKeywords( question_text , commonWords ) ,
            'neighbors' : set() ,
            'rank' : -1 , 
            'packetname' : packetname
            }    

    return node


#
#
#
#
#
#
def parseFolder( folder_name ):
    packet = [ parsePacket( folder_name + packetname ) for packetname in os.listdir( folder_name ) ]

    return packet 
#
#
def parsePacket( packetname ):
    raw_question_text = open( packetname , 'r' ).read()
    #regex = re.compile(r'(\d+\..+?)\n(Answer:[^\n]+)\n', re.MULTILINE | re.DOTALL) #original samuel magic!
    regex = re.compile(r'(\d+\..+?)\n((Answer:|ANSWER)[^\n]+)\n', re.MULTILINE | re.DOTALL)
    raw_packet = regex.findall( raw_question_text )

    packet = [ makeNode( question , packetname ) for question in raw_packet ]

    return packet
#
#
def makeNode( question , packetname ): #depends on commonWords.p and trivialWords.p
    commonWords = pickle.load( open( 'commonWords.p' , 'rb' ))   #top 7500 words
    trivialWords = pickle.load( open( 'trivialWords.p' , 'rb' ))    #top 48 words plus prompt and accept
    #
    question_text = question[ 0 ] 
    answer_text = question[ 1 ]

    node =  {
            'answer' : parseAnswers( answer_text , trivialWords ) , 
            'raw_answer' : answer_text ,
            'keywords' : parseKeywords( question_text , commonWords ) ,
            'neighbors' : set() ,
            'rank' : -1 , 
            'packetname' : packetname
            }    

    return node
#
#
def parseKeywords( question_text , commonWords ): #takes question raw text string -> set of keywords
    #   rareWords: words that don't show up in first 5000 (subject to change) most common words
    #   capWords: all capitalized words that aren't at the start of the sentence 
    formattedQuestion =  re.sub("[\(\[].*?[\)\]]" , " ", question_text).translate( None , "0123456789" ).replace("\n" , " ")  #regex gets rid of all things in [], like pronunciation
    rareWords = set( [word for word in formattedQuestion.translate( None, string.punctuation ).strip().split(" ") if ( word not in commonWords and word.islower())]) 
    capWords = set( re.findall( r'(?<!\.\s)\b[A-Z][a-z]*\b',  formattedQuestion )) 

    return capWords.union( rareWords )
# 
#
def parseAnswers( answer_text , trivialWords): #similar treatment as parseKeywords
    formattedAnswer = set(word for word in answer_text.lower().translate( None , string.punctuation ).replace("answer" , " ").split() if word not in trivialWords )

    return formattedAnswer
#
#
#
#
if name == '__main__': main()

