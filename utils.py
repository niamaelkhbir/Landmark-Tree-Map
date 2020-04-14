"""
@Author : Niama ELKHBIR
@Last update : 22/03/2020
"""
## TODO :

# Globals :
M = 100

# Imports :
import cv2

##

def getFileName(n):
    if 0 <= n and n < 10:
        return '00000'+str(n)+'.png'
    elif 10 <= n and n < 100:
        return '0000'+str(n)+'.png'
    elif 100 <= n and n < 1000:
        return '000'+str(n)+'.png'
    elif 1000 <= n and n < 10000:
        return '00'+str(n)+'.png'
    else:
        # something went wrong :/
        print("GetFileName : Something went wrong!")
        return ''
        
def save_keypoints(path, source, target):
    img = cv2.imread(path+source)
    kp, descriptors = cv2.BRISK_create(M).detectAndCompute(img,None)
    mg=cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite(path+ target,mg)
    return