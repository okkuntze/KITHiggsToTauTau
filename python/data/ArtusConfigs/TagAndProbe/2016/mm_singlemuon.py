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

def build_config(nickname, **kwargs):
  btag_eff = True if "sub_analysis" in kwargs and kwargs["sub_analysis"] == "btag-eff" else False

  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))

  # define frequently used conditions
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  isData = datasetsHelper.isData(nickname) and (not isEmbedded)
  isTTbar = re.search("TT(To|_|Jets)", nickname)
  isDY = re.search("DY.?JetsToLLM(10to50|50)", nickname)
  isWjets = re.search("W.?JetsToLNu", nickname)
  isSignal = re.search("HToTauTau",nickname)

  ## fill config:
  # includes
  includes = [
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseElectronID",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseMuonID",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsElectronID",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsVetoMuonID",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMuonID",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauID",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJEC",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsSvfit",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJetID",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsBTaggedJetID",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauES",
   # "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMinimalPlotlevelFilter_mt"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)

  # explicit configuration
  config["Channel"] = "MM"
  config["MinNMuons"] = 2
  # HltPaths_comment: The first path must be the single lepton trigger. A corresponding Pt cut is implemented in the Run2DecayChannelProducer..
  config["HltPaths"] = [
          "HLT_IsoMu22",
          "HLT_IsoTkMu22",
          "HLT_IsoMu22_eta2p1",
          "HLT_IsoTkMu22_eta2p1",
          #"HLT_IsoMu19_eta2p1_LooseIsoPFTau20",
          #"HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1"
  ]

  # Muon Requirements
  config["MuonIsoTypeUserMode"] = "fromcmsswr04"
  config["MuonIsoType"] = "none"
  config["MuonIsoSignalConeSize"] = 0.4
  config["MuonID"] = "none"
  config["MuonIso"] = "none"
  config["MuonDeltaBetaCorrectionFactor"] = 0.5
  config["MuonTrackDxyCut"] = 0.0
  config["MuonTrackDzCut"] = 0.0
  config["MuonLowerPtCuts"] = ["10.0"]
  config["MuonUpperAbsEtaCuts"] = ["2.4"]
  config["DiTauPairMinDeltaRCut"] = 0.5

  config["Year"] = 2016
    
  config["MuonTriggerFilterNames"] = [
          "HLT_IsoMu22_v:hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09",
          "HLT_IsoTkMu22_v:hltL3fL1sMu20L1f0Tkf22QL3trkIsoFiltered0p09",
          "HLT_IsoMu22_eta2p1_v:hltL3crIsoL1sSingleMu20erL1f0L2f10QL3f22QL3trkIsoFiltered0p09",
          "HLT_IsoTkMu22_eta2p1_v:hltL3fL1sMu20erL1f0Tkf22QL3trkIsoFiltered0p09",
          #"HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v:hltL3crIsoL1sMu18erTauJet20erL1f0L2f10QL3f19QL3trkIsoFiltered0p09",
          #"HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v:hltOverlapFilterIsoMu19LooseIsoPFTau20",
          #"HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v:hltL3crIsoL1sSingleMu18erIorSingleMu20erL1f0L2f10QL3f19QL3trkIsoFiltered0p09",
          #"HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v:hltOverlapFilterSingleIsoMu19LooseIsoPFTau20"
    ]

  config["HLTBranchNames"] = [
      "trg_t_IsoMu22:HLT_IsoMu22_v",
      "trg_t_IsoMu22:HLT_IsoTkMu22_v",
      "trg_t_IsoMu22:HLT_IsoMu22_eta2p1_v",
      "trg_t_IsoMu22:HLT_IsoTkMu22_eta2p1_v",
      "trg_p_IsoMu22:HLT_IsoMu22_v",
      "trg_p_IsoMu22:HLT_IsoTkMu22_v",
      "trg_p_IsoMu22:HLT_IsoMu22_eta2p1_v",
      "trg_p_IsoMu22:HLT_IsoTkMu22_eta2p1_v"
  ]

  config["CheckTagTriggerMatch"] = [
      "trg_t_IsoMu22"
  ]
  config["CheckProbeTriggerMatch"] = [
      "trg_p_IsoMu22"
  ]

  
  config["TagAdditionalCriteria"] = [
    "pt:23.0",
    "id:Medium",
    "dxy:0.045",
    "dz:0.2",
    "iso_sum:0.15"]

  config["ProbeAdditionalCriteria"] = [
    "id:isTrackerMuon"]

  config["InvalidateNonMatchingElectrons"] = False
  config["InvalidateNonMatchingMuons"] = True
  config["InvalidateNonMatchingTaus"] = False
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  config["EventWeight"] = "eventWeight"

  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.TagAndProbe.Includes.TagAndProbeQuantitiesMM").build_list(2016)

  config["Processors"] =   ["producer:ValidMuonsProducer",
                            "filter:ValidMuonsFilter",
                            "producer:MuonTriggerMatchingProducer",
                            "filter:MinMuonsCountFilter",
                            "producer:NewMMTagAndProbePairCandidatesProducer",
                            "filter:ValidDiTauPairCandidatesFilter"]

  config["Consumers"] = [#"KappaLambdaNtupleConsumer",
                         "NewMMTagAndProbePairConsumer",
                         "cutflow_histogram"]

  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('mm_new', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.syst_shifts_nom").build_config(nickname))
