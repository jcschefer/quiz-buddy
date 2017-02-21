#quinterest_json_maker.py       2/16/17: Ruyan Zhang
#makes giant ass json of all quinterest questions
import time
import sys
import os
import re
import string
import json 
import pickle
import subprocess

def main():
    #folder = parseFolder( './txtQuestions/' ) 
    master_folder = '/home/rz5000/name_pending/parser/www.quizbowlpackets.com/'
    all_tournaments = []
    for tournament_name in os.listdir( master_folder ):
        print tournament_name
        
        all_tournaments.append(( tournament_name , parseTournament( master_folder + tournament_name )))

    with open( 'all_tournaments.json' , 'w' ) as outfile:
        json.dump( all_tournaments, outfile ) 


#
#
#
def parseTournament( tournament_name ):
    tournament = []
    
    if os.path.isdir( tournament_name ):
        for round_name in os.listdir( tournament_name ):
            if '.pdf' in round_name:
                tournament.append( ( round_name , parseRound( tournament_name + '/' + round_name ) ) )

        return tournament
#
#
def parseRound( round_name ) :
    #convert_command = 'pdftotext ' + str( round_name ) + ' ' + str(round_name).replace('.pdf' , '.txt' ) 
    #convert_command = 'pdftotext ' + str( round_name ) + ' -' 

    p1 = subprocess.Popen(['pdftotext' , str( round_name ) , '-' ] , stdout=subprocess.PIPE).communicate()[0]

    
    #raw_text = open( os.system( str( convert_command ) ) , 'r' ).read()
    #regex = re.compile(r'(\d+\..+?)\n(Answer:[^\n]+)\n', re.MULTILINE | re.DOTALL) #original samuel magic!
    regex = re.compile(r'(\d+\..+?)\n((Answer:|ANSWER)[^\n]+)\n', re.MULTILINE | re.DOTALL) #creates tuple of question and answer
    #formatted_round = regex.findall( raw_question_text )
    formatted_round = regex.findall( p1 ) 

    return formatted_round
#
#
#
#
#
#
#
main()
