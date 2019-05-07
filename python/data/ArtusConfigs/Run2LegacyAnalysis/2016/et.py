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
  
  
  # define frequently used conditions
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  isData = datasetsHelper.isData(nickname) and (not isEmbedded)
  isTTbar = re.search("TT(To|_|Jets)", nickname)
  isDY = re.search("(DY.?JetsToLL|EWKZ2Jets)", nickname)
  isWjets = re.search("W.?JetsToLNu", nickname)
  isGluonFusion = re.search("GluGluHToTauTauM125", nickname)
  
  
  ## fill config:
  # includes
  includes = [
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsLooseElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsLooseMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsVetoElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsMinimalPlotlevelFilter_et",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsSvfit",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.settingsTauES",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.settingsMVATestMethods"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["Channel"] = "ET"
  config["MinNElectrons"] = 1
  config["MinNTaus"] = 1
  # HltPaths_comment: The first path must be the single lepton trigger. A corresponding Pt cut is implemented in the Run2DecayChannelProducer.
  if re.search("Run2016|Summer16", nickname): config["HltPaths"] = [
          "HLT_Ele25_eta2p1_WPTight_Gsf"]
  elif isEmbedded: config["HltPaths"] = [
          ""]
  config["HLTBranchNames"] = ["trg_singleelectron:HLT_Ele25_eta2p1_WPTight_Gsf_v"]
  config["NoHltFiltering"] = True if isEmbedded else False
  config["TauID"] = "TauIDRecommendation13TeV"
  config["TauUseOldDMs"] = True
  config["ElectronLowerPtCuts"] = ["26.0"]
  config["ElectronUpperAbsEtaCuts"] = ["2.1"]
  config["TauLowerPtCuts"] = ["30.0"]
  config["TauUpperAbsEtaCuts"] = ["2.3"]
  config["TriggerObjectLowerPtCut"] = -1.0
  config["DiTauPairMinDeltaRCut"] = 0.5
  config["DiTauPairIsTauIsoMVA"] = True
  config["DiTauPairLepton1LowerPtCuts"] = ["HLT_Ele25_eta2p1_WPTight_Gsf_v:26.0"]
  config["DiTauPairHltPathsWithoutCommonMatchRequired"] = ["HLT_Ele25_eta2p1_WPTight_Gsf_v"]
  config["DiTauPairNoHLT"] = True if isEmbedded else False
  config["DiTauPairHLTLast"] = True
  config["EventWeight"] = "eventWeight"
  config["RooWorkspace"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_sm_moriond_v2.root"
  config["RooWorkspaceWeightNames"] = [
    "0:triggerWeight",
    "0:idIsoWeight",
    "0:trackWeight"
  ]
  config["RooWorkspaceObjectNames"] = [
    "0:e_trgEle25eta2p1WPTight_desy_ratio",
    "0:e_idiso0p1_desy_ratio",
    "0:e_trk_ratio"
  ]
  config["RooWorkspaceObjectArguments"] = [
    "0:e_pt,e_eta",
    "0:e_pt,e_eta",
    "0:e_pt,e_eta"
  ]
  config["TriggerEfficiencyData"] = [
    "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_Run2016_Electron_Ele25WPTight_eff.root"]
  config["TriggerEfficiencyMc"] = [
    "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_MC_Electron_Ele25WPTight_eff.root"]
  config["IdentificationEfficiencyData"] = [
    "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/identificationWeights/identificationEfficiency_Run2016_Electron_IdIso_IsoLt0p1_eff.root"]
  config["IdentificationEfficiencyMc"] = [
    "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/identificationWeights/identificationEfficiency_MC_Electron_IdIso_IsoLt0p1_eff.root"]
  
  config["IdentificationEfficiencyMode"] = "multiply_weights"
  config["TauTauRestFrameReco"] = "collinear_approximation"
  config["TriggerEfficiencyMode"] = "multiply_weights"
  config["EleTauFakeRateWeightFile"] = ["1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/antiElectronDiscrMVA6FakeRateWeights.root"]
  
  config["ElectronTriggerFilterNames"] = ["HLT_Ele25_eta2p1_WPTight_Gsf_v:hltEle25erWPTightGsfTrackIsoFilter"]
  
  config["InvalidateNonMatchingElectrons"] = False
  config["InvalidateNonMatchingMuons"] = False
  config["InvalidateNonMatchingTaus"] = False
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  config["UseUWGenMatching"] = "true"
  
  config["Quantities"] =      importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.fourVectorQuantities").build_list()
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.syncQuantities").build_list(isMC = (not isData) and (not isEmbedded)))
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.svfitSyncQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
  config["Quantities"].extend([
      "nVetoElectrons",
      "nLooseElectrons",
      "nLooseMuons",
      "nDiTauPairCandidates",
      "nAllDiTauPairCandidates",
      "trg_singleelectron",
      "lep1ErrD0",
      "lep1ErrDz",
      "lep2ErrD0",
      "lep2ErrDz",
      "PVnDOF",
      #"PVchi2",
      "drel0_1",
      "drel0_2",
      "drelZ_1",
      "drelZ_2",
      "idisoweight_1",
      #"htxs_stage0cat",
      #"htxs_stage1cat",
      "flagMETFilter",
      "pt_ttjj"
  ])
  if re.search("HToTauTauM125", nickname):
    config["Quantities"].extend([
      "htxs_stage0cat",
      "htxs_stage1cat"
    ])
  if isGluonFusion:
    config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.Includes.ggHNNLOQuantities").build_list())

  
  config["OSChargeLeptons"] = True
  
  config["Processors"] = [                                    "producer:HltProducer",
                                                              "producer:MetSelector"]
  if not isData:                 config["Processors"].append( "producer:ElectronCorrectionsProducer")
  config["Processors"].extend((                               "producer:ValidElectronsProducer",
                                                              "filter:ValidElectronsFilter",
                                                              "producer:ElectronTriggerMatchingProducer",
                                                              "filter:MinElectronsCountFilter",
                                                              "producer:ValidMuonsProducer"))
  if not isData:                 config["Processors"].append( "producer:TauCorrectionsProducer")
  config["Processors"].extend((                               "producer:ValidTausProducer",
                                                              "filter:ValidTausFilter",
                                                              "producer:TauTriggerMatchingProducer",
                                                              "filter:MinTausCountFilter",
                                                              "producer:NewValidETPairCandidatesProducer",
                                                              "filter:ValidDiTauPairCandidatesFilter",
                                                              "producer:HttValidVetoElectronsProducer",
                                                              "producer:HttValidLooseElectronsProducer",
                                                              "producer:HttValidLooseMuonsProducer",
                                                              "producer:Run2DecayChannelProducer",
                                                              "producer:DiVetoElectronVetoProducer",
                                                              "producer:TaggedJetCorrectionsProducer",
                                                              "producer:ValidTaggedJetsProducer",
                                                              "producer:ValidBTaggedJetsProducer",
                                                              "producer:GroupedJetUncertaintyShiftProducer"))
  if not isData and not isEmbedded:                 config["Processors"].append( "producer:MetCorrector") #"producer:MvaMetCorrector"
  config["Processors"].extend((                               "producer:TauTauRestFrameSelector",
                                                              "producer:DiLeptonQuantitiesProducer",
                                                              "producer:DiJetQuantitiesProducer"))
  if not isData:                 config["Processors"].extend(("producer:SimpleEleTauFakeRateWeightProducer",
							      "producer:SimpleMuTauFakeRateWeightProducer"))
  if isTTbar:                    config["Processors"].append( "producer:TopPtReweightingProducer")
  if isDY:                       config["Processors"].append( "producer:ZPtReweightProducer")
  config["Processors"].extend((                               "filter:MinimalPlotlevelFilter",
                                                              "producer:SvfitProducer",
                                                              "producer:ImpactParameterCorrectionsProducer")) #"producer:MVATestMethodsProducer"
  if not isData:                 config["Processors"].append( "producer:RooWorkspaceWeightProducer")
  config["Processors"].append(                                "producer:EventWeightProducer")
  if isGluonFusion:              config["Processors"].append( "producer:SMggHNNLOProducer")
  
  
  config["AddGenMatchedParticles"] = True
  config["AddGenMatchedTaus"] = True
  config["AddGenMatchedTauJets"] = True
  config["BranchGenMatchedElectrons"] = True
  config["BranchGenMatchedTaus"] = True
  config["Consumers"] = ["KappaLambdaNtupleConsumer",
                         "cutflow_histogram"]
  
  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.nominal").build_config(nickname)) + \
         ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.eleES_shifts").build_config(nickname)) + \
         ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.JECunc_shifts").build_config(nickname)) + \
         ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.METunc_shifts").build_config(nickname)) + \
         ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.METrecoil_shifts").build_config(nickname)) + \
         ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.tauESperDM_shifts").build_config(nickname)) + \
         ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.tauEleFakeESperDM_shifts").build_config(nickname)) + \
         ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.tauJetFakeESIncl_shifts").build_config(nickname)) + \
         ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2LegacyAnalysis.btagging_shifts").build_config(nickname))
