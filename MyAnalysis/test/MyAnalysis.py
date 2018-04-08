#!/usr/bin/env python

from __future__ import print_function
import sys, os, shutil, re, subprocess
import ROOT
from DataFormats.FWLite import Events, Handle
import numpy as np

def main():

  from FWCore.ParameterSet.VarParsing import VarParsing
  
  options = VarParsing ('analysis')
  options.inputFiles = ["/afs/cern.ch/work/d/devdatta/CMSREL/Flashgg/CMSSW_9_4_2/src/flashgg/myMicroAODOutputFile.root"]
  options.maxEvents = -1
  options.outputFile = "fout.root"
  options.parseArguments()

  events = Events(options.inputFiles)
  nevents = 0
  for event in events:

    if options.maxEvents > 0 and nevents > options.maxEvents: break

    ### Find gen particles
    h_prunedGenpar = Handle("std::vector<reco::GenParticle>")
    event.getByLabel("flashggPrunedGenParticles", h_prunedGenpar)

    particles = h_prunedGenpar.product()
    for p in particles:
      print('prunedgenparticles P pid = {} status = {}'.format(p.pdgId(), p.status()))

    h_photons = Handle("std::vector<flashgg::Photon>")
    event.getByLabel("flashggRandomizedPhotons", h_photons)
    print("N(photons) = {}".format(len(h_photons.product())))
    photons = h_photons.product()
    for gam in photons:
      print('photon pt = {}'.format(gam.pt()))

    h_packedGenpar = Handle("std::vector<pat::PackedGenParticle>")
    event.getByLabel("flashggGenPhotons", h_packedGenpar)
    particles = h_packedGenpar.product()
    for p in particles:
      print('packedgenparticles P pid = {} status = {}'.format(p.pdgId(), p.status()))

    h_jets = Handle("std::vector<std::vector<flashgg::Jet> >")
    event.getByLabel("flashggFinalJets", h_jets)

    print( "N(jets) = %i" % len(h_jets.product()) )
    jets = h_jets.product()[0]
    for jet in jets:
      print( "jet pt = %f DeepCSVBDisc = %f" % (jet.pt(), jet.bDiscriminator("pfDeepCSVJetTags:probb")+jet.bDiscriminator("pfDeepCSVJetTags:probbb")) )

    h_dipho = Handle("std::vector<flashgg::DiPhotonCandidate>")
    event.getByLabel("flashggDiPhotons", h_dipho)

    diphos = h_dipho.product()
    print( "N(diphotons) = %i" %len(diphos) )
    for dipho in diphos:
      print( "Diphoton pt = %f" % dipho.pt() )

    nevents+=1

if __name__ == "__main__":
    main()
