"""
@Author : Niama ELKHBIR
@Last update : 25/03/2020
"""
## TODO : 

# Globals :
path = '//home//hp-elitebook-8570p//Desktop//Project//'
N = 50 # Number of samples < 1101

# Imports :
from os import chdir
chdir(path)
from utils import *
from Classes.Image import *
from Classes.Viewframe import *
from Classes.Ltreemap import *

##

ltreemap = Ltreemap(None,[])

# Processing database images :

for i in range(N):
    print("Processing: "+str(i))
    image = Image("DataBase//"+getFileName(i))
    viewframe = image.getViewframe()
    ltreemap.add(viewframe)
print("Done !")

# Test of correctness :

# number of biffurcations

print("Number of biffurcations : "+str(ltreemap.nbBiff()))


# must all be equal to N!

print("Number of leafs : "+str(ltreemap.nbLeafs()))
print("Number of viewframes (static method) : "+str(ltreemap.nbViewframes))
print("Number of viewframes (dynamic method) : "+str(len(ltreemap.viewframes)))

# mean depth of the tree :

print("Mean depth : "+str(ltreemap.meanDepth()))


# Plotting the direction vector :

ltreemap.plotDirectionVector()


# Plotting keypoint above a source image :

save_keypoints(path, '000000.png', 'new.png')

