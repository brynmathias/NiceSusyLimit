#! /usr/bin/env python
import ROOT as r
from LimitTools import MakeLimitPlot
r.gROOT.SetStyle("Plain")
r.gStyle.SetOptStat(0)


# Note that the draw order is important, so we put a single charachter in the line key to order the keys

limit = {
    "intLumi":4.65,
    "tanB":10,
    "A0":-1,
    "NSquarkGluinoLines":5,
    "LimitLines":{

     "a_Observedlimit":{
                "xVals":[  0,100,300,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,2800,3000],
                "yVals":[640,640,640,600,560,480, 400, 360, 340, 320, 320, 320, 320, 320, 320, 320],
                "LineColor":r.kBlue+3,
                "LineStyle":None,
                "Legend":("Observed Limit","L"),
                "FillStyle":None,
                "FillColor":None
                },

     "b_Observedlimit":{
                "xVals":[  0,100,300,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,2800,3000],
                "yVals":[660,660,660,620,580,520, 440, 380, 360, 340, 340, 340, 340, 340, 340, 340],
                "LineColor":r.kOrange,
                "LineStyle":None,
                "Legend":("Cross Section + 1 #sigma","L"),
                "FillStyle":None,
                "FillColor":None
                },

     "c_Observedlimit":{
                "xVals":[  0,100,300,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,2800,3000],
                "yVals":[620,620,620,580,540,440, 360, 340, 320, 300, 300, 300, 300, 300, 300, 300],
                "LineColor":r.kOrange,
                "LineStyle":None,
                "Legend":("Cross Section - 1 #sigma","L"),
                "FillStyle":None,
                "FillColor":None
                },



     "h_BtagExpected":{
                "xVals":[  0,100,300,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,2800,3000],
                "yVals":[620,622,600,580,540,480, 380, 340, 320, 320, 300, 300,300, 300, 300, 300],
                "LineColor":r.kGreen+3,
                "LineStyle":4,
                "Legend":("Median Expected Limit #pm 1 #sigma","FL"),
                "FillStyle":3001,
                "FillColor":r.kGreen-9
                },

     "i_BtagExpectedPlusOneSigma":{
                "xVals":[  0,100,300,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,2800,3000],
                "yVals":[640,640,640,620,580,520, 440, 390, 370, 360, 340, 340, 340, 340, 340, 340],
                "LineColor":r.kGreen+3,
                "LineStyle":None,
                "Legend":None,
                "FillStyle":None,#3003,
                "FillColor":None,#r.kGreen-9
                },
     "j_BtagExpectedMinusOneSigma":{
                "xVals":[  0,100,300,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,2800,3000],
                "yVals":[580,580,560,540,500,380, 330, 300, 280, 280, 280, 280, 280, 280, 280, 280],
                "LineColor":r.kGreen+3,
                "LineStyle":None,
                "Legend":None,
                "FillStyle":None,#3003,
                "FillColor":None
                },




     }
}






a = MakeLimitPlot(limit)



