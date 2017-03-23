#!/usr/bin/env python2
#this isn't important enough to license
#Does bogobogosort, which is a highly unoptimized and/or generally bad sort algo
#Basically, bogo sort, which bogobogo is based off of, sorts by randomly shuffling
#the input until it ends up sorted. bogobogo goes further by recursively doing that
#for all ranges of the list from 0 to n. So it first bogo sorts just the 1st
#element, then the 1st 2 elements, and so on until it sorts the entire array.
#Read more here http://www.dangermouse.net/esoteric/bogobogosort.html
import math
import rospy
#All of this taken from https://github.com/Pizzorni/Bogo
import random

def Bogosort(list):
	while(not isSorted(list)):
		random.shuffle(list)
	return list

def Bogobogosort(list):
	index = 2
	while(not isSorted(list)):
		Bogosort(list[:index])
		index += 1
		if(not isSorted(list[:index])):
			random.shuffle(list)
			index = 2
	return list

def isSorted(list):
	prev = None
	for x in list:
		if(prev != None and (prev > x)):
			return False
		prev = x
	return True
#borrowed stuff ends here



def badmath():
    listy = []
    x = int(0)
    while(x < 20): 
        listy.append(random.randint(0,100))
	x = x + 1
    Bogobogosort(listy)
if __name__ == '__main__':
    badmath()
