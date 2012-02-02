#! /usr/bin/env python
import ROOT as r
from LimitTools import *
r.gStyle.SetOptStat(0)


# Note that the draw order is important, so we put a single charachter in the line key to order the keys

limit = {
    "intLumi":4.65,
    "tanB":10,
    "A0":0,
    "NSquarkGluinoLines":5,
    "LimitLines":{
    
    "a_Observed":{
                "xVals":[0  ,200,400,600,800,1000,1200,1400,1600,1800,2000],
                "yVals":[660,660,620,570,520,400 , 320, 300, 280, 250, 250],
                "LineColor":r.kRed,
                "LineStyle":None,
                "Legend":("Observed 95\% Confidence limit","L"),
                "FillStyle":None,
                "FillColor":None
                },
    "b_PlusOneSigma":{
                "xVals":[0  ,200,400,600,800,1000,1200,1400,1600,1800,2000],
                "yVals":[640,640,620,570,480, 360, 320, 290, 270, 270, 260],
                "LineColor":r.kAzure-9,
                "LineStyle":None,
                "Legend":None,#
                "FillStyle":3001,
                "FillColor":None
                },
    "d_MinusOneSigma":{
                "xVals":[0,  200,400,600,800,1000,1200,1400,1600,1800,2000],
                "yVals":[560,560,550,500,380, 320, 240, 240, 220, 220, 200],
                "LineColor":r.kAzure-9,
                "LineStyle":None,
                "Legend":None,
                "FillStyle":1000,#3001
                "FillColor":10
                },
     "c_Expected":{
                "xVals":[0,  200,400,600,800,1000,1200,1400,1600,1800,2000],
                "yVals":[600,600,600,540,420, 320, 290, 270, 260, 240, 240],
                "LineColor":r.kBlue+3,
                "LineStyle":4,
                "Legend":("Median Expected Limit #pm 1 #sigma","FL"),
                "FillStyle":3001,
                "FillColor":r.kAzure-9
                },
     }
}






a = MakeLimitPlot(limit)



