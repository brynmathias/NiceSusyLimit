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
                "xVals":[200,300,400],
                "yVals":[200,300,400],
                "LineColor":r.kRed,
                "LineStyle":None,
                "Legend":("Observed 95\% Confidence limit","L"),
                "FillStyle":None,
                "FillColor":None
                },
    "b_PlusOneSigma":{
                "xVals":[200,300,400],
                "yVals":[300,400,500],
                "LineColor":r.kAzure-9,
                "LineStyle":None,
                "Legend":None,#
                "FillStyle":3001,
                "FillColor":None
                },
    "d_MinusOnesigma":{
                "xVals":[200,300,400],
                "yVals":[100,200,300],
                "LineColor":r.kAzure-9,
                "LineStyle":None,
                "Legend":None,
                "FillStyle":1000,#3001
                "FillColor":10
                },
     "c_Expected":{
                "xVals":[200,300,400],
                "yVals":[205,303,408],
                "LineColor":r.kBlue+3,
                "LineStyle":4,
                "Legend":("Median Expected Limit #pm 1 #sigma","FL"),
                "FillStyle":3001,
                "FillColor":r.kAzure-9
                },
     }
}






a = MakeLimitPlot(limit)



