import numpy
import ROOT
from ROOT import *

### Macros ###
def plot(canvas,name):
    canvas.Print(name+".pdf","pdf")
#    canvas.Print(name+".png","png")
#    canvas.Print(name+".eps","eps")

def setStyle(hist,value):
    hist.SetLineColor(value)
    hist.SetLineWidth(2)
    hist.SetMarkerColor(value)
    hist.SetMarkerStyle(20)
    hist.SetMarkerSize(0.8)
    # hist.SetMarkerSize(1.0)
    hist.Draw("")
    hist.Paint("")
    hist.GetXaxis().SetTitleOffset(1.4)
    hist.GetYaxis().SetTitleOffset(1.65)

def setCanvas(canvas):
    canvas.SetLeftMargin(0.12)
    canvas.SetBottomMargin(0.12)
    canvas.SetRightMargin(0.08)
    canvas.SetTopMargin(0.08)


### Binning ###
PtBins=numpy.array([0.0, 20.0, 22.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 125.0, 150.0, 200.0, 400.0])
nPtBins=len(PtBins)-1

EtaBins=numpy.array([-2.5,-2.1,-1.6,-1.2,-0.9,-0.3,0.3,0.9,1.2,1.6,2.1,2.5])
nEtaBins=len(EtaBins)-1

pi=3.14
PhiBins=numpy.array([-pi,-(11.0/12.0)*pi,-(9.0/12.0)*pi,-(7.0/12.0)*pi,-(5.0/12.0)*pi,-(3.0/12.0)*pi,-(1.0/12.0)*pi,(1.0/12.0)*pi,(3.0/12.0)*pi,(5.0/12.0)*pi,(7.0/12.0)*pi,(9.0/12.0)*pi,(11.0/12.0)*pi,pi])
PhiBins=numpy.array([-pi,-(11.0/12.0)*pi,-(9.0/12.0)*pi,-(7.0/12.0)*pi,-(5.0/12.0)*pi,-(3.0/12.0)*pi,-(1.0/12.0)*pi,(1.0/12.0)*pi,(3.0/12.0)*pi,(5.0/12.0)*pi,(7.0/12.0)*pi,(9.0/12.0)*pi,(11.0/12.0)*pi,pi])
nPhiBins=len(PhiBins)-1

### Style ###
gStyle.SetOptStat("")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

### Make plots ###
# f=ROOT.TFile("/Users/benjamin/Library/Mobile Documents/com~apple~CloudDocs/Work/TrackTrigger/Histos.root")
# f=ROOT.TFile("/Users/benjamin/Library/Mobile Documents/com~apple~CloudDocs/Work/TrackTrigger/HistosNew.root")
# f=ROOT.TFile("/Users/benjamin/Library/Mobile Documents/com~apple~CloudDocs/Work/TrackTrigger/L1TObjNtuple_TTbar_NN.root")
# fNN=ROOT.TFile("PVPlots_NN_400.root")
# fFH=ROOT.TFile("PVPlots_FH_400.root")
fNN=ROOT.TFile("PVPlots_NN.root")
fFH=ROOT.TFile("PVPlots_FH.root")


# cPt = TCanvas("cPt", "cPt", 700, 700)
# setCanvas(cPt)
# f.cd()
# trackPt=f.Get("trackPt")
# trackPt.SetTitle("Track p_{T};Track p_{T} [GeV];Number of tracks/GeV")
# setStyle(trackPt,1)
# trackPt.GetXaxis().SetRangeUser(0.0,20.0)
# plot(cPt,"TrackPt")

# cEta = TCanvas("cEta", "cEta", 700, 700)
# setCanvas(cEta)
# f.cd()
# trackEta=f.Get("trackEta")
# trackEta.SetTitle("Track #eta;Track #eta;Number of tracks")
# setStyle(trackEta,1)
# trackEtaRebinned=trackEta.Rebin(nEtaBins,'',EtaBins)
# trackEtaRebinned.GetXaxis().SetRangeUser(-2.6,2.6)
# trackEtaRebinned.Draw("ep")
# plot(cEta,"trackEta")

# cPhi = TCanvas("cPhi", "cPhi", 700, 700)
# setCanvas(cPhi)
# f.cd()
# trackPhi=f.Get("trackPhi")
# trackPhi.SetTitle("Track #phi;Track #phi;Number of tracks")
# setStyle(trackPhi,1)
# trackPhi.Rebin(41)
# # trackPhiRebinned=trackPhi.Rebin(nPhiBins,'',PhiBins)
# trackPhi.GetXaxis().SetRangeUser(-3.4,3.4)
# trackPhi.Draw("ep")
# plot(cPhi,"TrackPhi")

# cMVA = TCanvas("cMVA", "cMVA", 700, 700)
# setCanvas(cMVA)
# f.cd()
# trackMVA=f.Get("trackMVA")
# trackMVA.SetTitle("Track MVA;Track MVA;Number of tracks")
# setStyle(trackMVA,1)
# # trackMVA.Rebin(41)
# # trackMVARebinned=trackMVA.Rebin(nMVABins,'',MVABins)
# # trackMVA.GetXaxis().SetRangeUser(-3.4,3.4)
# trackMVA.Draw("ep")
# plot(cMVA,"TrackMVA")

cTrkFakeFH = TCanvas("cTrkFakeFH", "cTrkFakeFH", 700, 700)
setCanvas(cTrkFakeFH)
fFH.cd()
trackFakeFH=fFH.Get("trackFake")
trackFakeFH.SetTitle("Track Fakes;Fake Quality;Number of tracks")
setStyle(trackFakeFH,1)
trackFakeFH.Draw("")
fNN.cd()
trackFakeNN=fNN.Get("trackFake")
setStyle(trackFakeNN,2)
trackFakeNN.Draw("same")
plot(cTrkFakeFH,"TrackFakes")

#################################################
#### Plot the Z0 of the PV from MC and Reco: ####
cPVRecoFH = TCanvas("cPVRecoFH", "cPVRecoFH", 700, 700)
setCanvas(cPVRecoFH)
fFH.cd()
pvRecoFH=fFH.Get("pvReco")
pvMCFH=fFH.Get("pvMC")
pvRecoFH.SetTitle(";z0 [cm];AU")
setStyle(pvRecoFH,1)
setStyle(pvMCFH,4)
pvRecoFH.Rebin(4)
pvMCFH.Rebin(4)
pvRecoFH.Draw("")
pvMCFH.Draw("same")
plot(cPVRecoFH,"PVZ0FH")

cPVRecoNN = TCanvas("cPVRecoNN", "cPVRecoNN", 700, 700)
setCanvas(cPVRecoNN)
fNN.cd()
pvRecoNN=fNN.Get("pvReco")
pvMCNN=fNN.Get("pvMC")
pvRecoNN.SetTitle(";z0 [cm];AU")
setStyle(pvRecoNN,2)
setStyle(pvMCNN,4)
pvRecoNN.Rebin(4)
pvMCNN.Rebin(4)
pvRecoNN.Draw("")
pvMCNN.Draw("same")
plot(cPVRecoNN,"PVZ0NN")

##############################################
#### Plot the Z0 Resolution of FH and NN: ####
cPVRes = TCanvas("cPVRes", "cPVRes", 700, 700)
setCanvas(cPVRes)
fFH.cd()
pvResFH=fFH.Get("pvRes")
pvResFH.SetTitle(";z_{0}^{PV} Residual [cm];Events")
setStyle(pvResFH,1)
#pvRes.Rebin(4)

fNN.cd()
pvResNN=fNN.Get("pvRes")
setStyle(pvResNN,2)

pvResFH.Draw("")
pvResNN.Draw("same")

leg = ROOT.TLegend(0.18,0.78,0.38,0.88)
leg.AddEntry(pvResFH,"FH","l")
leg.AddEntry(pvResNN,"NN","l")
leg.SetTextFont(42)
leg.SetTextSize(0.04)
leg.SetMargin(0.15)
leg.SetFillColor(0)
leg.SetLineColor(1)
leg.SetLineStyle(1)
leg.SetLineWidth(0)
leg.Draw("hist")

dEntpvResFH    = "Entries:\t\t"+('%.0f' % pvResFH.GetEntries())
dMeanpvResFH   = "Mean:\t\t\t\t"+('%.3f' % pvResFH.GetMean())
dStdDevpvResFH = "StdDev:\t"+('%.3f' % pvResFH.GetStdDev())

dEntpvResNN    = "Entries:\t\t"+('%.0f' % pvResNN.GetEntries())
dMeanpvResNN   = "Mean:\t\t\t\t"+('%.3f' % pvResNN.GetMean())
dStdDevpvResNN = "StdDev:\t"+('%.3f' % pvResNN.GetStdDev())


ptpvResFH = TPaveText(0.68,0.77,0.88,0.88,"NDC")
ptpvResFH.AddText(dEntpvResFH)
ptpvResFH.AddText(dMeanpvResFH)
ptpvResFH.AddText(dStdDevpvResFH)
ptpvResFH.SetBorderSize(1)
ptpvResFH.SetFillColor(0)
ptpvResFH.SetLineColor(kBlack)
ptpvResFH.SetTextAlign(12)
ptpvResFH.SetTextColor(kBlack)
ptpvResFH.SetTextFont(42)
ptpvResFH.SetTextSize(0.03)
ptpvResFH.Draw("same")

ptpvResNN = TPaveText(0.68,0.66,0.88,0.77,"NDC")
# ptpvResNN = TPaveText(0.68,0.47,0.88,0.58,"NDC")
ptpvResNN.AddText(dEntpvResNN)
ptpvResNN.AddText(dMeanpvResNN)
ptpvResNN.AddText(dStdDevpvResNN)
ptpvResNN.SetBorderSize(1)
ptpvResNN.SetFillColor(0)
ptpvResNN.SetLineColor(kRed)
ptpvResNN.SetTextAlign(12)
ptpvResNN.SetTextColor(kRed)
ptpvResNN.SetTextFont(42)
ptpvResNN.SetTextSize(0.03)
ptpvResNN.Draw("same")


plot(cPVRes,"PVRes")
cPVRes.SetLogy()
plot(cPVRes,"PVRes-LogY")
