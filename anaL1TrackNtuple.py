import argparse
import ROOT
ROOT.gROOT.SetBatch(True) #Do not display any graphics
from DataFormats.FWLite import Events, Handle
#import FWCore.ParameterSet.Config as cms

parser = argparse.ArgumentParser(description='Analyses L1TrackNtuples and produces some performance plots')
parser.add_argument('--i',help='Input Filename',required=True)
parser.add_argument('--o',help='Output Filename',required=True)
args = parser.parse_args()

#input_files = "file:"+args.inFile
input_files = args.i
output_file = args.o

print "Reading Input: ",input_files
print "Saving Output: ",output_file

# for f in input_files:
#     print "File: ",f
# events=Events(input_files)
# for nEv,event in enumerate(events):
#     event.getByLabel()
# for event in file:
#     print event

trackPt=ROOT.TH1D("trackPt","trackPt",100,0.0,100.0)
trackEta=ROOT.TH1D("trackEta","trackEta",100,-5.0,5.0)
trackPhi=ROOT.TH1D("trackPhi","trackPhi",80,-4.0,4.0)
trackChi2=ROOT.TH1D("trackChi2","trackChi2",100,0.0,100.0)
trackMVA=ROOT.TH1D("trackMVA","trackMVA",100,0.0,1.0)

trackFake=ROOT.TH1D("trackFake","trackFake",3,0.0,3.0)
pvReco=ROOT.TH1D("pvReco","pvReco",256,-15.0,15.0)
pvMC=ROOT.TH1D("pvMC","pvMC",256,-15.0,15.0)
pvRes=ROOT.TH1D("pvRes","pvRes",256,-15.0,15.0)

outputFile = ROOT.TFile(output_file,'RECREATE')

file = ROOT.TFile(input_files,'read')
# for f in input_files:
    # print "f: ",f
    # file = ROOT.TFile(f,'read')
tree = file.Get("L1TrackNtuple/eventTree")
# tree.Print()

counter=0
### Go through events in the tree and loop over vectors of tracks to fill plots: ###
for event in tree:
    if counter>20: break
    # for pt in event.trk_pt: trackPt.Fill(pt)
    # for eta in event.trk_eta: trackEta.Fill(eta)
    # for phi in event.trk_phi: trackPhi.Fill(phi)
    # for chi2 in event.trk_chi2: trackChi2.Fill(chi2)
    # for mva in event.trk_MVA1: trackMVA.Fill(mva)
    for trkFake in event.trk_fake: trackFake.Fill(trkFake)
    pvMC.Fill(event.pv_MC[0])
    pvReco.Fill(event.pv_L1reco[0])
    pvRes.Fill(event.pv_MC[0]-event.pv_L1reco[0])
    print "event.pv_MC: ", event.pv_MC[0],
    print "\tevent.pv_L1reco: ", event.pv_L1reco[0],
    print "\tres(MC-Reco): ", event.pv_MC[0]-event.pv_L1reco[0]
    counter+=1

outputFile.cd()
# trackPt.Write()
# trackEta.Write()
# trackPhi.Write()
# trackChi2.Write()
# trackMVA.Write()

trackFake.Write()
pvReco.Write()
pvMC.Write()
pvRes.Write()
outputFile.Close()
