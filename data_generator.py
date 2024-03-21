import random
#from array import array
#import constants

def list_gen(size):
    list_gen = [x for x in range(0,size+1)]
    return list_gen
def target_gen(size):
    targets = []
    for i in range(0, size):
        targets.append(random.randint(0,size))
    return targets


