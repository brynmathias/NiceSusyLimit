#! /usr/bin/env python
import ROOT as r
import array

        
def ExclusionCurve(xVals = None, yVals = None):
    """Define an exclusion curve based on an array of xvalues and y values. Smooth with a tspline3"""
    if len(xVals) is not len(yVals): assert "N XVals != N YVals, please correct"
    graph = r.TGraph(len(xVals),array.array('d',xVals),array.array('d',yVals))
    spline = r.TSpline3("spline",graph)
    spline.SetLineWidth(3)
    return spline
    pass
    


def StauRegion(TanBeta = None):
    """Make the stau LSP region for limit plots"""
    graph = None
    st_m0_tanBeta3 = array.array('d',[0,10,20,30,40,50,60,70,80,90,100,0])
    st_m12_tanBeta3 = array.array('d',[337,341,356,378,406,439,473,510,548,587,626,626])

    st_m0_tanBeta10 =  array.array('d',[0,   10, 20, 30, 40, 50, 60, 70, 80,90, 100,110,130,150,0])
    st_m12_tanBeta10 = array.array('d',[213,220,240,275,312,352,393,435,476,518,559,600,682,763,763])

    st_m0_tanBeta50 = array.array('d',[200,210,220,230,240,250,260,270,280,290,310,325,200,200])
    st_m12_tanBeta50 = [206,226,246,267,288,310,332,354,376,399,450,500,500,206]

    st_m0_tanBeta40 = array.array('d',[380,450,380])
    st_m12_tanBeta40 = array.array('d',[590,780,780])
    if int(TanBeta) is 3:
      graph =r.TGraph(len(st_m12_tanBeta3),st_m0_tanBeta3,st_m12_tanBeta3)
    if int(TanBeta) is 10:
      graph= r.TGraph(len(st_m0_tanBeta10),st_m0_tanBeta10,st_m12_tanBeta10)
    if int(TanBeta) is 50:
      graph =r.TGraph(len(st_m12_tanBeta50),st_m0_tanBeta50,st_m12_tanBeta50)
    if int(TanBeta) is 40:
      graph =r.TGraph(len(st_m12_tanBeta40),st_m0_tanBeta40,st_m12_tanBeta40)
    graph.SetFillColor(40)
    graph.SetFillStyle(1001)
    
    
    ypos_1 = 0.455 if TanBeta == 10 else 0.143 if TanBeta == 40 else 0.76 
    ypos_2 = 0.465 if TanBeta == 10 else 0.153 if TanBeta == 40 else 0.78
    xpos_1 = 0.46  if TanBeta == 10 else 0.83  if TanBeta == 40 else 0.16
    xpos_2 = 0.1   if TanBeta == 10 else 0.85  if TanBeta == 40 else 0.17
 

    legst = r.TLegend(xpos_1,ypos_1,xpos_2,ypos_2);
    legst.SetHeader("#tilde{#tau} = LSP")
    legst.SetFillStyle(0)
    legst.SetBorderSize(0)
    legst.SetTextSize(0.03)
    legst.SetTextAngle(80)
    if TanBeta == 40: legst.SetTextAngle(75);
    
    
    
    
    
    return graph,legst


def Const_Squark_Gluino(TanBeta = None, Line = None):
  """Produce the lables and lines for the contours of constant squark and gluino mass, for tan beta 10 or 40"""
  pass
  # ---lines of constant gluino/squark
  SquarkCoef1 = [2.54068e+04, 5.86979e+04, 1.07751e+05, 1.81108e+05, 2.64621e+05]
  SquarkCoef2 = [1.88535e-01, 1.93101e-01, 2.00899e-01, 2.21128e-01, 2.21160e-01]
  SquarkCoef3 = [2.54068e+04, 5.86979e+04, 1.07751e+05, 1.81108e+05, 2.64621e+05]


  if int(TanBeta) is 10 :lnsq = r.TF1("lnsq_%i"%Line,"sqrt([0]-x*x*[1]+[2])",0,2000)
  if int(TanBeta) is 40 :lnsq = r.TF1("lnsq_%i"%Line,"sqrt([0]-x*x*[1]+[2])",380,2000)
  lnsq.SetParameter(0,SquarkCoef1[Line])
  lnsq.SetParameter(1,SquarkCoef2[Line])
  lnsq.SetParameter(2,SquarkCoef3[Line])
  lnsq.SetLineWidth(1)
  lnsq.SetLineColor(r.kGray)



  GluinoCoef1 = [201.77, 311.027, 431.582, 553.895, 676.137]
  GluinoCoef2 = [-0.0146608, -0.01677, -0.022244, -0.0271851, -0.0292212]
    
  if (TanBeta == 10): lngl = r.TF1("lngl_%i"%Line,"[0]+x*[1]",0,2000)
  if (TanBeta == 40): lngl = r.TF1("lngl_%i"%Line,"[0]+x*[1]",380,2000)

  lngl.SetParameter(0,GluinoCoef1[Line])
  lngl.SetParameter(1,GluinoCoef2[Line])
  lngl.SetLineWidth(1)
  lngl.SetLineColor(r.kGray)

  place_x = 170
  if int(TanBeta) == 40 :place_x = 390
  t3 =r.TLatex(place_x+10*Line,lnsq.Eval(-50+place_x+10*Line)+5,"#font[12]{#tilde{g}}#font[92]{(%i)GeV}"%(500+250*Line))
  t3.SetTextSize(0.03)
  t3.SetTextAngle(-30+Line*5)
  if int(TanBeta) == 40:  t3.SetTextAngle(-40+Line*5)
  t3.SetTextColor(r.kGray+2)

  place_x = 423
  place_y = 18
  if int(TanBeta) == 10:
    place_x = 1650
    place_y = 10
  
  if int(TanBeta) == 40:
    place_x = 1700
    place_y = 10
  
  t4 = r.TLatex(place_x,place_y+lngl.Eval(800+Line*100),"#font[12]{#tilde{g}}#font[92]{(%i)GeV}"%(500+250*Line))
  t4.SetTextSize(0.03)
  t4.SetTextAlign(13)
  t4.SetTextColor(r.kGray+2)

  return lnsq,lngl,t3,t4




class MakeLimitPlot(object):
    """Make a CMS susy limit plot, for tan beta = 10 or 40"""
    def __init__(self, settingsDict):
        super(MakeLimitPlot, self).__init__()
        self.settings = settingsDict
        self.hist = r.TH2F("","",100,0,2000,80,100,750) if self.settings["tanB"] == 10 else r.TH2F("h1","h1",80,400,2000,100,0,750)
        self.c1 = r.TCanvas()
        self.obList = []
        self.lumilabel = r.TLatex(0.35 if self.settings['tanB'] == 40 else 0.35,0.85,"CMS,  %.2f fb^{-1},  #sqrt{s} = 7 TeV"%(self.settings['intLumi']));
        self.lumilabel.SetNDC()
        self.cmsParams = r.TLatex(0.35,0.65,"tan#beta = %i, A_{0} = 0 GeV, #mu > 0"%(self.settings['tanB']))
        self.cmsParams.SetNDC()
        self.CurveLegend = r.TLegend(0.33,0.7,0.70,0.84,"","brNDC");
        self.LegendSetUp()
        self.MakePlot()

    def LegendSetUp(self):
      """Set up our legend, this contains the info about the limit curves"""
      # self.CurveLegend.SetHeader("95\% CL limits:")
      self.CurveLegend.SetFillColor(0);
      self.CurveLegend.SetShadowColor(0);
      self.CurveLegend.SetTextSize(0.03);
      self.CurveLegend.SetBorderSize(0);
      self.hist.GetYaxis().SetTitle("m_{0} GeV")
      self.hist.GetXaxis().SetTitle("m_{1/2} GeV")

    def MakePlot(self):
        """docstring for MakePlot
        Loop though the limit curves twice, the first time drawing with a fill for the expected limit.
        Then draw the Gluino/squark constant lines.
        Draw the limit curves again.
        Go though the legend in the correct order and set up the legend, with the fill style so that it looks correct, all because of more root faf.
        append each of our plots to an out list, so that they dont get garbage collected
        """

        self.c1.cd()
        self.hist.Draw()
        # Ok Lets make the plot look good.
        # We want the filled area for the pm 1sigma to be behind the gluino squark lines, but the limit lines to be in front
        # Draw lines and fill, we fill the lower limit with solid white as a work around for trying to fill between two lines
        for a in sorted(self.settings['LimitLines']):
            print (self.settings['LimitLines'])[a]
            l = ExclusionCurve(((self.settings['LimitLines'])[a])['xVals'],((self.settings['LimitLines'])[a])['yVals'])
            l.SetLineColor((self.settings['LimitLines'])[a]['LineColor'])
            if (self.settings['LimitLines'])[a]['FillStyle'] is not None:
                l.SetFillStyle((self.settings['LimitLines'])[a]['FillStyle'])
                l.SetFillColor((self.settings['LimitLines'])[a]['LineColor'])
                if (self.settings['LimitLines'])[a]['FillColor'] is not None:
                    l.SetFillColor((self.settings['LimitLines'])[a]['FillColor'])
                self.obList.append(l)
            
                l.Draw("same")
        
        for i in range(self.settings['NSquarkGluinoLines']):
            for ob in Const_Squark_Gluino(TanBeta = self.settings['tanB'], Line = i):
                self.obList.append(ob)
                ob.Draw("same")
        for ob in StauRegion(TanBeta = self.settings['tanB']):
          self.obList.append(ob)
          ob.Draw("fsame")
        
        
        # Draw lines only, no fill
        for a in sorted(self.settings['LimitLines']):
            print (self.settings['LimitLines'])[a]
            lf = ExclusionCurve(((self.settings['LimitLines'])[a])['xVals'],((self.settings['LimitLines'])[a])['yVals'])
            lf.SetLineColor((self.settings['LimitLines'])[a]['LineColor'])
            if (self.settings['LimitLines'])[a]['LineStyle'] is not None: lf.SetLineStyle((self.settings['LimitLines'])[a]['LineStyle'])
            self.obList.append(lf)
            lf.Draw("same")
            
            
            # Here we do the faf for making sure that the legend is in the correct order and is filled in the legend
            if "Obs" in a or "Expected" in a:
                print "adding legend for ", a
                leg = ExclusionCurve(((self.settings['LimitLines'])[a])['xVals'],((self.settings['LimitLines'])[a])['yVals'])
                leg.SetLineColor((self.settings['LimitLines'])[a]['LineColor'])
                if (self.settings['LimitLines'])[a]['FillStyle'] is not None:
                    leg.SetFillStyle((self.settings['LimitLines'])[a]['FillStyle'])
                    leg.SetFillColor((self.settings['LimitLines'])[a]['LineColor'])
                    if (self.settings['LimitLines'])[a]['FillColor'] is not None:
                        leg.SetFillColor((self.settings['LimitLines'])[a]['FillColor'])
                if (self.settings['LimitLines'])[a]['LineStyle'] is not None: leg.SetLineStyle((self.settings['LimitLines'])[a]['LineStyle'])
                self.obList.append(leg)
                if (self.settings['LimitLines'])[a]["Legend"] is not None:
                    self.CurveLegend.AddEntry(leg,((self.settings['LimitLines'])[a]["Legend"])[0],((self.settings['LimitLines'])[a]["Legend"])[1])


        
        
        self.CurveLegend.Draw("same")
        self.lumilabel.Draw("same")
        self.cmsParams.Draw("same")
        self.c1.SaveAs("Limit_tanB_%i_A0_%i_Lumi_%s.pdf"%(self.settings['tanB'],self.settings["A0"],self.settings["intLumi"]))
    pass



