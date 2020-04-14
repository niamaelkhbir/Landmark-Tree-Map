"""
@Author : Niama ELKHBIR
@Last update : 21/03/2020
"""
## TODO :

# Globals :
path = '//home//hp-elitebook-8570p//Desktop//Project//'

# Imports :
from os import chdir
chdir(path)
from Classes.Landmark import *
from numpy import array

##

# The viewframe is an image abstracted as its landmarks
class Viewframe:
    
    # landmarks : list of landmarks
    def __init__(self , landmarks):
        self.landmarks = landmarks
        
    # adding a new landmark to self
    def add(self,landmark):
        self.landmarks.append(landmark)
            
    # direction vector of self
    def t(self):
        N = len(self.landmarks)
        if N != 0:
            return array([sum([l.cos() for l in self.landmarks])/N , sum([l.sin() for l in self.landmarks])/N])
        else:
            return array([0, 0])