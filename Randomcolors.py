# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 01:40:06 2022

@author: dcmol
"""

from PIL import Image
import random

def permutation(rgb,r):
    if r==1:
        rng=(rgb[2],rgb[0],rgb[1],rgb[3])
        return rng
    if r==2:
        rng=(rgb[1],rgb[2],rgb[0],rgb[3])
        return rng
    if r==3:
        rng=(rgb[0],rgb[2],rgb[1],rgb[3])
        return rng
    if r==4:
        rng=(rgb[1],rgb[0],rgb[2],rgb[3])
        return rng
    if r==5:
        rng=(rgb[2],rgb[1],rgb[0],rgb[3])
        return rng
    if r==6:
        return rgb
def randomscale(rgb,s):
    rng=[]
    for i in range(3):
        rng.append(int(min(s[i]*rgb[i],255)))
    rng.append(rgb[3])
    return tuple(rng)
def randomize_tiles(k):
    tileset=Image.open("Untitled-1.png")
    print(tileset.size)
    size_x,size_y=tileset.size
    pixs=[(a,b) for a in range(size_x) for b in range(size_y)]
    r=random.randint(1,6)
    s1=0.5+random.random()
    s2=0.5+random.random()
    s3=0.5+random.random()
    print((k,r,s1,s2,s3))
    for i in pixs:
        pixel=tileset.getpixel(i)        
        pixel2=permutation(pixel,r)
        pixel3=randomscale(pixel2,(s1,s2,s3))
        tileset.putpixel(i,pixel3)
    tileset.save("Modified"+str(k)+".png")
for i in range(10):
    randomize_tiles(i)
    