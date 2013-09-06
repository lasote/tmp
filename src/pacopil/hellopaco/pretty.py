'''
Created on 17/07/2013

@author: drodri
'''
import hello
import sys
import majortom.hello


def pretty():
    sys.stdout.write('* ')
    hello.hello()
    sys.stdout.write(' *')

    
sys.stdout.write('==> ')
majortom/hello.pretty()

