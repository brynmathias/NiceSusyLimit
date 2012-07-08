#!/usr/bin/env python

import ROOT as r

def setup() :
    r.gErrorIgnoreLevel = 2000
    r.gROOT.SetBatch(True)
    
def susyCanvas(fileName = "GridTanb10_v1.root", canvasName = "GridCanvas") :
    f = r.TFile(fileName)
    canvas = f.Get(canvasName).Clone("%s_clone"%canvasName)
    f.Close()
    return canvas

def go(outFile = "") :
    setup()
    canvas = susyCanvas()

    canvas.Draw()
    canvas.Print(outFile)

go(outFile = "RA1_CMSSM.pdf")
