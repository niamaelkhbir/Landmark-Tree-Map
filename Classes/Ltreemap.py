"""
@Author : Niama ELKHBIR
@Last update : 25/03/2020
"""
## TODO :

# Globals :
path = '//home//hp-elitebook-8570p//Desktop//Project//'

# Imports :
from os import chdir
chdir(path)
from Classes.Landmark import *
from Classes.Viewframe import *
from numpy import array
import matplotlib.pyplot as plt

##

class Ltreemap:
    
    # root : landmark
    # childs : list of Ltreemaps
    def __init__(self , root , childs):
        self.root = root
        self.childs = childs
        self.nbViewframes = 0
        self.viewframes = []
        for c in childs:
            for v in c.viewframes:
                self.viewframes.append(Viewframe([root]+v.landmarks))
                self.nbViewframes += 1
    
    # adds the viewframe to self
    def add(self , viewframe):
        # Recursivity :
        
        if viewframe.landmarks == []:
            return
            
        if self.childs != []:
            for c in self.childs:
                if c.root in viewframe.landmarks:
                    
                    c.add(Viewframe([l for l in viewframe.landmarks if l != self.root]))
                    
                    self.nbViewframes += 1
                    self.viewframes.append(viewframe)
                    return
        
        flatten = Ltreemap.toTree(Viewframe([l for l in viewframe.landmarks if l != self.root]))
        if flatten != []:
            
            self.childs.append(flatten.pop())
            
            self.nbViewframes += 1
            self.viewframes.append(viewframe)
            return 
        
    # Changes a viewframe to a flat vertical tree
    def toTree(viewframe):
        res = []
        n = len(viewframe.landmarks)
        for i in range(n):
            res = [Ltreemap(viewframe.landmarks[n-i-1],res)]
        return res

    # Counts the number of biffurcations in a tree
    def nbBiff(self):
        # DE : depth exploration
        pile = [] #DE
        pile.append(self) #DE
        
        nb = 0
        
        while pile != []: #DE
            cur = pile.pop() #DE
            
            if len(cur.childs)>1:
                nb += 1
                
            for c in cur.childs: #DE
                pile.append(c) #DE
                
        return nb
        
    # Counts the number of leafs in a tree, must be equal to the number of viewframes !
    def nbLeafs(self):
        # DE : depth exploration
        pile = [] #DE
        pile.append(self) #DE
        
        nb = 0
        
        while pile != []: #DE
            cur = pile.pop() #DE
            
            if len(cur.childs)<1:
                nb += 1
                
            for c in cur.childs: #DE
                pile.append(c) #DE
                
        return nb
    
    # Plots the y-coordinates of the direction vector as a function of the x-coordinates of the direction vector
    def plotDirectionVector(self):
        # X = np.array([i for i in range(self.nbViewframes)])
        T2 = array([v.t() for v in self.viewframes])
        T1 = array(list(T2)[1:]+[array([0,0])])
        T = T2-T1
        Tx = [t[0] for t in T]
        Ty = [t[1] for t in T]
        plt.plot(Tx,Ty)
        plt.title("Direction vector in time")
        plt.xlabel("x coordinate of the direction vector")
        plt.ylabel("y coordinate of the direction vector")
        plt.show()
        
    def meanDepth(self):
        return 1+(sum([len(v.landmarks) for v in self.viewframes]))/self.nbViewframes