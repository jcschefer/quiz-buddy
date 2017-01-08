#!/usr/bin/python3
try:
    while True:
        fname = input().strip()
        print('_'.join(fname.split(' ')))
        with open('../test/' + '_'.join(fname.split(' ')), 'wb') as f:
            with open(fname, 'rb') as g:
                f.write(g.read())
except EOFError:
    print("done")
#except:
#    print("rip")
