# L1TP2_PVML_Utils
Collection of scripts to help with the work on implementing ML for PV reconstruction at L1T for P2

## anaL1TrackNtuple.py
This script will run over ntuples created from L1Trigger/L1TTrackMatch/test/L1TrackObjectNtupleMaker.cc and plot useful quantities

*--i* = the input ntuple file

*--o* = the output plot file

## plotTracks.py
This script runs of the plot file created by anaL1TrackNtuple.py and prints them nicely

## tfShape.py
This script runs over a TensorFlow network file (extension .pb) and prints out the shape of the network

*--i* = the input pb tensorflow file
