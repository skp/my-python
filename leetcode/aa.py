#-------------------------------------------------------------------------------
# Name:        deco.py
# Purpose:     demo of decoration in python
#
# Author:      qin.shuq
#
# Created:     27/10/2014
#-------------------------------------------------------------------------------

import traceback

def robust(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except:
            print('Error execute: %s' % actual_do.__name__)
            #traceback.print_exc()
    return add_robust

@robust
def simple():
    return 5 / 0

@robust
def readFile(filename):
    f = open(filename, "r")
    print(len(f.readlines()))
    f.close()

def add(a,b):
    return int(a)+int(b)

@robust
def assertSumIsPositive(*args):
    # sum = reduce(add, *args)
    assert sum >= 0

@robust
def checkLen(**keyargs):
    if len(keyargs) < 3:
        raise Exception('Number of key args should more than 3.')

if __name__ == '__main__':
    simple()
    readFile("UnexistFile.txt")
    # assertSumIsPositive(1,2,-3,-4)
    checkLen(a=5,b=2)
    print('Yet still reach here.')