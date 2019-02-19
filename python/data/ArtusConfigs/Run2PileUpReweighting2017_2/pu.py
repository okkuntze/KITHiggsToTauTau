#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import copy
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
import importlib
import os

import HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.ArtusConfigUtility as ACU

def build_config(nickname):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))
  
  config["Quantities"] = [
    "npu",
    "numberGeneratedEventsWeight",
    #"crossSectionPerEventWeight",
    "generatorWeight",
    "npartons",
    "genbosonmass",
    "1genBoson1DaughterPt",
    "genPVx","1genBosonDaughterSize",

		"1genBoson1DaughterPt",
		"1genBoson1DaughterPz",
		"1genBoson1DaughterEta",
		"1genBoson1DaughterPhi",
		"1genBoson1DaughterMass",
		"1genBoson1DaughterCharge",
		"1genBoson1DaughterEnergy",
		"1genBoson1DaughterPdgId",
		"1genBoson1DaughterStatus",

		"1genBoson2DaughterPt",
		"1genBoson2DaughterPz",
		"1genBoson2DaughterEta",
		"1genBoson2DaughterPhi",
		"1genBoson2DaughterMass",
		"1genBoson2DaughterEnergy",
		"1genBoson2DaughterPdgId",
		"1genBoson2DaughterStatus",

		"1genBoson1DaughterGranddaughterSize",

		"1genBoson1Daughter1GranddaughterPt",
		"1genBoson1Daughter1GranddaughterPz",
		"1genBoson1Daughter1GranddaughterEta",
		"1genBoson1Daughter1GranddaughterPhi",
		"1genBoson1Daughter1GranddaughterMass",
		"1genBoson1Daughter1GranddaughterEnergy",
		"1genBoson1Daughter1GranddaughterPdgId",
		"1genBoson1Daughter1GranddaughterStatus",

		"1genBoson1Daughter2GranddaughterPt",
		"1genBoson1Daughter2GranddaughterPz",
		"1genBoson1Daughter2GranddaughterEta",
		"1genBoson1Daughter2GranddaughterPhi",
		"1genBoson1Daughter2GranddaughterMass",
		"1genBoson1Daughter2GranddaughterEnergy",
		"1genBoson1Daughter2GranddaughterPdgId",
		"1genBoson1Daughter2GranddaughterStatus",

		"1genBoson1Daughter3GranddaughterPt",
		"1genBoson1Daughter3GranddaughterPz",
		"1genBoson1Daughter3GranddaughterEta",
		"1genBoson1Daughter3GranddaughterPhi",
		"1genBoson1Daughter3GranddaughterMass",
		"1genBoson1Daughter3GranddaughterEnergy",
		"1genBoson1Daughter3GranddaughterPdgId",
		"1genBoson1Daughter3GranddaughterStatus",

		"1genBoson1Daughter4GranddaughterPt",
		"1genBoson1Daughter4GranddaughterPz",
		"1genBoson1Daughter4GranddaughterEta",
		"1genBoson1Daughter4GranddaughterPhi",
		"1genBoson1Daughter4GranddaughterMass",
		"1genBoson1Daughter4GranddaughterEnergy",
		"1genBoson1Daughter4GranddaughterPdgId",
		"1genBoson1Daughter4GranddaughterStatus",

		"1genBoson2DaughterGranddaughterSize",

		"1genBoson2Daughter1GranddaughterPt",
		"1genBoson2Daughter1GranddaughterPz",
		"1genBoson2Daughter1GranddaughterEta",
		"1genBoson2Daughter1GranddaughterPhi",
		"1genBoson2Daughter1GranddaughterMass",
		"1genBoson2Daughter1GranddaughterEnergy",
		"1genBoson2Daughter1GranddaughterPdgId",
		"1genBoson2Daughter1GranddaughterStatus",

		"1genBoson2Daughter2GranddaughterPt",
		"1genBoson2Daughter2GranddaughterPz",
		"1genBoson2Daughter2GranddaughterEta",
		"1genBoson2Daughter2GranddaughterPhi",
		"1genBoson2Daughter2GranddaughterMass",
		"1genBoson2Daughter2GranddaughterEnergy",
		"1genBoson2Daughter2GranddaughterPdgId",
		"1genBoson2Daughter2GranddaughterStatus",

		"1genBoson2Daughter3GranddaughterPt",
		"1genBoson2Daughter3GranddaughterPz",
		"1genBoson2Daughter3GranddaughterEta",
		"1genBoson2Daughter3GranddaughterPhi",
		"1genBoson2Daughter3GranddaughterMass",
		"1genBoson2Daughter3GranddaughterEnergy",
		"1genBoson2Daughter3GranddaughterPdgId",
		"1genBoson2Daughter3GranddaughterStatus",

		"1genBoson2Daughter4GranddaughterPt",
		"1genBoson2Daughter4GranddaughterPz",
		"1genBoson2Daughter4GranddaughterEta",
		"1genBoson2Daughter4GranddaughterPhi",
		"1genBoson2Daughter4GranddaughterMass",
		"1genBoson2Daughter4GranddaughterEnergy",
		"1genBoson2Daughter4GranddaughterPdgId",
		"1genBoson2Daughter4GranddaughterStatus",

		"1genBoson1Daughter2GranddaughterGrandGranddaughterSize",

		"1genBoson1Daughter2Granddaughter1GrandGranddaughterPdgId",
		"1genBoson1Daughter2Granddaughter1GrandGranddaughterStatus",

		"1genBoson1Daughter2Granddaughter2GrandGranddaughterPdgId",
		"1genBoson1Daughter2Granddaughter2GrandGranddaughterStatus",

		"1genBoson1Daughter2Granddaughter3GrandGranddaughterPdgId",
		"1genBoson1Daughter2Granddaughter3GrandGranddaughterStatus",

		"1genBoson1Daughter2Granddaughter4GrandGranddaughterPdgId",
		"1genBoson1Daughter2Granddaughter4GrandGranddaughterStatus",

		"1genBoson1Daughter2Granddaughter5GrandGranddaughterPdgId",
		"1genBoson1Daughter2Granddaughter5GrandGranddaughterStatus",

		"1genBoson1Daughter2Granddaughter6GrandGranddaughterPdgId",
		"1genBoson1Daughter2Granddaughter6GrandGranddaughterStatus",

		"1genBoson2Daughter2GranddaughterGrandGranddaughterSize",
		"genPVy",
		"genPVz",

		"genPhiStarCP",
		"genPhiStar",
		"genOStarCP",
		"genPhiCP",
		"genPhi",
		"genOCP",
		"genPhiCPLab",
		
		"genIP1x",
		"genIP1y",
		"genIP1z",
		"genIP2x",
		"genIP2y",
		"genIP2z",

		"genCosPsiPlus",
		"genCosPsiMinus",

		"genPhiStarCP_rho",
		"genPhiCP_rho",
		"genPhiStar_rho",
		"genPhi_rho",

		"gen_yTau",
		"gen_posyTauL",
		"gen_negyTauL",

		"TauMProngEnergy",
		"TauPProngEnergy",

		"Tau1OneProngsSize",
		"Tau2OneProngsSize",
		
		"Tau1DecayMode",
		"Tau2DecayMode",

		"OneProngChargedPart1Pt",
		"OneProngChargedPart1Pz",
		"OneProngChargedPart1Eta",
		"OneProngChargedPart1Phi",
		"OneProngChargedPart1Mass",
		"OneProngChargedPart1Energy",
		"OneProngChargedPart1PdgId",

		"OneProngChargedPart2Pt",
		"OneProngChargedPart2Pz",
		"OneProngChargedPart2Eta",
		"OneProngChargedPart2Phi",
		"OneProngChargedPart2Mass",
		"OneProngChargedPart2Energy",
		"OneProngChargedPart2PdgId",

		"genZPlus",
		"genZMinus",
   		"genZs",

		"leadingGenMatchedTauNProngs",
		"genMatchedTau1NProngs",
		"posGenMatchedTauNProngs",
		"leadingGenMatchedTauNPi0s",
		"genMatchedTau1NPi0s",
		"posGenMatchedTauNPi0s"
#		"TaunProngs",
#		"Tau2nProngs",
#		"TaudecayMode",
#		"Tau2decayMode",
#		"TaunPi0s",
#		"Taus2nPi0s"
  ]
  
  
  
  config["Consumers"] = ["KappaLambdaNtupleConsumer"]
  
  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('pu', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.syst_shifts_nom").build_config(nickname))
