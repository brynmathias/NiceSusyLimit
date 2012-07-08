#!/usr/bin/env python

import ROOT as r
import points

def setup() :
    r.gErrorIgnoreLevel = 2000
    r.gROOT.SetBatch(True)
    
def susyCanvas(fileName = "GridTanb10_v1.root", canvasName = "GridCanvas") :
    #http://arxiv.org/abs/1202.6580
    #https://twiki.cern.ch/twiki/bin/view/CMS/SUSY42XSUSYScan#mSUGRA_Templates
    f = r.TFile(fileName)
    canvas = f.Get(canvasName).Clone("%s_clone"%canvasName)
    f.Close()
    return canvas

def enclosedBand(graph1 = None, graph2 = None) :
    #inspired by http://root.cern.ch/phpBB3/viewtopic.php?f=3&t=6346&p=26175
    out = r.TGraph()
    out.SetName("%s_%s"%(graph1.GetName(), graph2.GetName()))

    x = r.Double()
    y = r.Double()

    n1 = graph1.GetN()
    n2 = graph2.GetN()

    for i in range(n1) :
        graph1.GetPoint(i, x, y)
        out.SetPoint(i, float(x), float(y))

    for i in range(n2) :
        graph2.GetPoint(n2-i-1, x, y)
        out.SetPoint(n1+i, float(x), float(y))
    return out

def tgraph(points = [], title = "") :
    graph = r.TGraph()
    for i,(x,y) in enumerate(points) :
        graph.SetPoint(i, x, y)
    return graph

def spline(points = [], title = "") :
    return r.TSpline3(title, tgraph(points, title))

def go(outFile = "", bandOutline = False) :
    #ROOT
    setup()

    #clone and draw template from SUSY group
    canvas = susyCanvas()
    canvas.Draw()

    #define legend
    legend = r.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)

    #expected band
    expM = tgraph(points.expectedLimitMinus(), "expected_minus")
    expP = tgraph(points.expectedLimitPlus(), "expected_plus")
    band = enclosedBand(expM, expP)
    band.SetFillStyle(3001)
    band.SetFillColor(r.kGreen-9)
    band.Draw("fsame")

    if bandOutline :
        for exp in [expM, expP] :
            exp.SetLineColor(r.kBlue)
            exp.SetLineStyle(1)
            exp.SetLineWidth(1)
            exp.Draw("lsame")

    #median expected limit
    exp = spline(points.expectedLimit(), title = "Median Expected Limit #pm 1 #sigma")
    exp.SetLineColor(r.kGreen+3)
    exp.SetLineStyle(7)
    exp.SetLineWidth(2)
    exp.Draw("lsame")

    #legend entry for expected curves/band
    expLeg = exp.Clone("%s_clone"%exp.GetName())
    expLeg.SetFillStyle(band.GetFillStyle())
    expLeg.SetFillColor(band.GetFillColor())

    #observed limit
    obs = spline(points.observedLimit(), "Observed Limit (95% C.L.)")
    obs.SetLineWidth(3)
    obs.Draw("lsame")

    #populate and draw legend
    legend.AddEntry(obs, obs.GetTitle(), "l")
    legend.AddEntry(expLeg, expLeg.GetTitle(), "fl")
    legend.Draw()

    #print to file
    canvas.Print(outFile)



#the points defining the curves are stored in points.py
go(outFile = "RA1_CMSSM.pdf", bandOutline = False)
