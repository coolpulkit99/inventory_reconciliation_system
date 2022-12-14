import shelve
import random

# Using pickle for local data storage for demo
# Can be replaced with respective database functions to store against respective products

def storeData(id,data):
    s = shelve.open( "data" )
    s[str(id)]=data
    s.close()


def retreiveData(id):
    s = shelve.open( "data" )
    data = s[str(id)]
    s.close()
    return data

def getRandomData():
    s = shelve.open( "data" )
    randomKey = random.choice(s.keys())
    s.close()
    return randomKey