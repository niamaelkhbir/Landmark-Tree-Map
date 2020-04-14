"""
@Author : Niama ELKHBIR
@Last update : 25/03/2020
"""

# Globals :

# Imports :
from math import cos, sin, pi

##

class Landmark:
    
    ANGLES_THRESHOLD = 0.01
    DESCRIPTOR_THRESHOLD = 0.38
    
    # angles : list of floats, with size 360
    # descriptors : list of floats, with size 64
    def __init__(self , angles = [], descriptor = []):
        self.angles = angles
        self.descriptor = descriptor
        
    def __eq__(self, l):
        angles_size = len(self.angles)
        descriptor_size = len(self.descriptor)
        return isinstance(l,Landmark) and angles_size == len(l.angles) and descriptor_size == len(l.descriptor) and abs(1-(self.cos()*l.cos()+self.sin()*l.sin())) <= Landmark.ANGLES_THRESHOLD and sum([1 for i in range(descriptor_size) if self.descriptor[i] != l.descriptor[i]])/descriptor_size <= Landmark.DESCRIPTOR_THRESHOLD
        
    # Mean cosinus of the angles of self
    def cos(self):
        Z = sum([a for a in self.angles])
        if Z != 0:
            return sum([self.angles[i]*cos(i*pi/180) for i in range(len(self.angles))])/Z
        else:
            return 0
            
    # Mean sinus of the angles of self
    def sin(self):
        Z = sum([a for a in self.angles])
        if Z != 0:
            return sum([self.angles[i]*sin(i*pi/180) for i in range(len(self.angles))])/Z
        else:
            return 0