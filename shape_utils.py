#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:34:16 2019

@author: omaralmutirdi
"""
import numpy as np
import math

class Rectangle : 
    
    
    def __init__ (self,x,y,h,w,asPoints = False , x2 = -1 ,y2 = -1):
        if asPoints == False : 
            self.h = h
            self.w = w
            self.x = x
            self.y = y

            
        if asPoints == True : 
            self.x = x
            self.y = y
            self.h = abs(y2-y)
            self.w = abs(x2 -x)
            w = self.w
            h = self.h
            


        
        self.p = [Point(x,y),Point(x+w,y),Point(x,y+h),Point(x+w,y+h)]
        self.l1 = [self.p[0].x,self.p[0].y,self.p[1].x,self.p[1].y]
        self.l2 = [self.p[1].x,self.p[1].y,self.p[2].x,self.p[2].y]
        self.l3 = [self.p[2].x,self.p[2].y,self.p[3].x,self.p[3].y]
        self.l4 = [self.p[3].x,self.p[3].y,self.p[0].x,self.p[0].y]
        self.area = self.h * self.w

        
    def pushDown(self,amount):
        self.y = self.y + amount
        self.__init__(self.x,self.y,self.h,self.w)
        
    def pushRight(self,amount):
        self.x = self.x + amount
        self.__init__(self.x,self.y,self.h,self.w)
        

class Point : 

    def __init__ (self,x,y):
        self.x = x
        self.y = y
        
    def getPoints(self):
        return (self.x,self.y)
        
class HoughLine:
    
    def __init__(self,line=[],p1=-1,p2=-1):
        if(p1 == -1) :
            self.line = line
            self.p1 = Point(line[0],line[1])
            self.p2 = Point(line[2],line[3])
        else :
            self.line =  np.array([p1.x,p1.y,p2.x,p2.y])
            self.p1 = p1
            self.p2 = p2
        
        
    def getSlope(self):
        self.slope = (self.p2.y  - self.p1.y) / (self.p2.x - self.p1.x)
        return self.slope
         
    
        
        
        
