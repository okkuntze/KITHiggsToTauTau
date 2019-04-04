
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
import importlib
import os

def build_config(nickname, **kwargs):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))
  
  # define frequently used conditions
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  isData = datasetsHelper.isData(nickname) and (not isEmbedded)
  isTTbar = re.search("TT(To|_|Jets)", nickname)
  isDY = re.search("DY.?JetsToLLM(10to50|50|150)", nickname)
  isWjets = re.search("W.?JetsToLNu", nickname)
  
  
  ## fill config:
  # includes
  
  includes = [
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsSvfit",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauES",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMinimalPlotlevelFilter_tt",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.settingsKappa"
]
  
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)

  config["Channel"] = "TT"
  config["MinNTaus"] = 2

  # explicit configuration
  config["SkipEvents"] = 0
  config["EventCount"] = -1
  config["InputIsData"] = False
  BosonPdgIds = {
      "DY.?JetsToLL|EWKZ2Jets|Embedding(2016|MC)" : [
        23
      ],
      "^(GluGlu|GluGluTo|VBF|Wminus|Wplus|Z)(HToTauTau|H2JetsToTauTau)" : [
        25
      ],
      "W.?JetsToLN|EWKW" : [
        24
      ],
      "SUSY(BB|GluGlu|GluGluTo)(BB)?HToTauTau" : [
        25,
        35,
        36
        ]
  }
  config["BosonPdgIds"] = [0]
  for key, pdgids in BosonPdgIds.items():
    if re.search(key, nickname): config["BosonPdgIds"] = pdgids
  
  config["BosonStatuses"] = [62]
  
  config["OutputPath"] = "output1.root"
  
  config["Processors"] = []
  config["Processors"].append(                                    "producer:NicknameProducer")
  config["Processors"].extend((                                  # "producer:CrossSectionWeightProducer",
                                                                  "producer:GeneratorWeightProducer",
                                                                  "producer:NumberGeneratedEventsWeightProducer"))
  if isWjets or isDY:                config["Processors"].append( "producer:GenBosonFromGenParticlesProducer")
  if isDY or isEmbedded:             config["Processors"].append( "producer:GenDiLeptonDecayModeProducer")
  config["Processors"].extend((                                   "producer:GenParticleProducer",
                                                                  "producer:HttValidGenTausProducer",
                                                                  "producer:GenPartonCounterProducer",
                                                                  "producer:GenTauDecayProducer",
                                                                  "producer:ValidGenTausProducer",
                                                                  "producer:GenTauCPProducer",
                                                                  "producer:ValidTausProducer",
                                                                  "filter:ValidTausFilter",
                                                                  "producer:TauTriggerMatchingProducer",
                                                                  "filter:MinTausCountFilter",
                                                                  "producer:ValidElectronsProducer",
                                                                  "producer:ValidMuonsProducer",
                                                                  "producer:NewValidTTPairCandidatesProducer",
                                                                  "filter:ValidDiTauPairCandidatesFilter",
                                                                  "producer:Run2DecayChannelProducer"
                                                                  ))
  if isWjets or isDY or isEmbedded:  config["Processors"].append("producer:GenBosonDiLeptonDecayModeProducer")

  config["Consumers"] = [ "KappaLambdaNtupleConsumer",
                        "cutflow_histogram"]

  # pipelines - channels including systematic shifts
  config["Pipelines"] = jsonTools.JsonDict()
  config["Pipelines"] += importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2PileUpReweighting2017_2.pu").build_config(nickname)

  return config

