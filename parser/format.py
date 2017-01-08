#format.py      12/21/2016: Ruyan Zhang
#Creates pickled set of n most commmon english words from words10k.txt
#   max possible = 10,000

import pickle
import os

os.remove( "./commonWords.p" )
num = 7500
words = set(open( 'words10k.txt' , 'r').read().split()[:num])
#temp = open( 'words10k.txt' , 'r').read().split()[:num] + ['prompt' , 'accept']
#words = set( temp ) 

with open ('trivialWords.p' , 'w') as f :
    pickle.dump( words , f )

