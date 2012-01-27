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
                "xVals":[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000],
                "yVals":[650,650,630,620,600,570,560,520,450,400 ,340 , 320, 310, 300, 280, 280, 270, 250, 250, 250],
                "LineColor":r.kRed,
                "LineStyle":None,
                "Legend":("Observed 95\% Confidence limit","L"),
                "FillStyle":None,
                "FillColor":None
                },
    "b_PlusOneSigma":{
                "xVals":[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000],
                "yVals":[640,640,640,620,590,570,540,480,390, 360, 340, 320, 320, 290, 280, 270, 270, 270, 260, 260],
                "LineColor":r.kAzure-9,
                "LineStyle":None,
                "Legend":None,#
                "FillStyle":3001,
                "FillColor":None
                },
    "d_MinusOnesigma":{
                "xVals":[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000],
                "yVals":[560,560,560,550,520,500,450,380,340, 320, 260, 240, 240, 240, 240, 220, 220, 220, 220, 200,],
                "LineColor":r.kAzure-9,
                "LineStyle":None,
                "Legend":None,
                "FillStyle":1000,#3001
                "FillColor":10
                },
     "c_Expected":{
                "xVals":[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000],
                "yVals":[600,600,600,600,570,540,480,420,380, 320, 320, 290, 280, 270, 270, 260, 240, 240, 240, 240],
                "LineColor":r.kBlue+3,
                "LineStyle":4,
                "Legend":("Median Expected Limit #pm 1 #sigma","FL"),
                "FillStyle":3001,
                "FillColor":r.kAzure-9
                },
     }
}






a = MakeLimitPlot(limit)



