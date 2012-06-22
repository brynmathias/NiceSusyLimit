#! /usr/bin/env python
import ROOT as r
from LimitTools import MakeLimitPlot
r.gROOT.SetStyle("Plain")
r.gStyle.SetOptStat(0)


# Note that the draw order is important, so we put a single charachter in the line key to order the keys

limit = {
    "intLumi":4.65,
    "tanB":10,
    "A0":0,
    "NSquarkGluinoLines":5,
    "LimitLines":{
    
    "y_Observed":{
                "xVals":[  0,100,300,500,700,900,1100,1300,1500,1700,1900,2000],
                "yVals":[645,640,625,600,560,440, 340, 320, 300, 290, 282, 280],
                "LineColor":r.kRed,
                "LineStyle":None,
                "Legend":("Observed 95% Confidence limit","L"),
                "FillStyle":None,
                "FillColor":None
                },
                
        
   "b_PlusOneSigma":{
               "xVals":[0  ,200,400,600,800,1000,1200,1400,1600,1800,2000],
               "yVals":[645,640,620,580,480, 400, 340, 320, 320, 322, 320],
               "LineColor":r.kAzure-9,
               "LineStyle":None,
               "Legend":None,#
               "FillStyle":3001,
               "FillColor":None
               },
   "c_MinusOneSigma":{
               "xVals":[0,  200,400,600,800,1000,1200,1400,1600,1800,2000],
               "yVals":[580,580,560,500,400, 340, 300, 280, 250, 242, 240],
               "LineColor":r.kAzure-9,
               "LineStyle":None,
               "Legend":None,
               "FillStyle":1000,#3001
               "FillColor":10
               },
     "d_Expected":{
                "xVals":[  0,200,400,600,800,1000,1200,1400,1600,1800,2000],
                "yVals":[600,600,590,540,460, 370, 320, 300, 280, 272, 270],
                "LineColor":r.kBlue+3,
                "LineStyle":4,
                "Legend":("Median Expected Limit #pm 1 #sigma","FL"),
                "FillStyle":3001,
                "FillColor":r.kAzure-9
                },





#     "e_PLobs":{
#                "xVals":[  0,200,400,600,800,1000,1200,1400,1600,1800,2000],
#                "yVals":[630,620,615,580,500, 390, 340, 310, 300, 295, 290],
#                "LineColor":r.kGreen,
#                "LineStyle":1,
#                "Legend":("Median Expected Limit #pm 1 #sigma","FL"),
#                "FillStyle":3001,                "FillColor":r.kAzure-9
#                },
     }
}






a = MakeLimitPlot(limit)



