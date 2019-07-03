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

def build_config(nickname, **kwargs):

  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))
  year = datasetsHelper.base_dict[nickname]["year"]

  ## fill config:
  # includes
  includes = [
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)

  # explicit configuration
  config["JetID"] = "none"
  config["JetIDVersion"] = str(year)
  config["PuJetIDs"] = []
  config["PuJetIDFullDiscrName"] = "pileupJetIdUpdatedfullDiscriminant" # the same as version stored in MiniAOD: pileupJetIdfullDiscriminant
  config["JetTaggerLowerCuts"] = []
  config["JetTaggerUpperCuts"] = []
  config["JetLowerPtCuts"] = ["20.0"] # Used for all jets, including b jets
  # config["JetOfflineLowerPtCut"] = 30.0 # Used for non b jet quantities 
  config["JetUpperAbsEtaCuts"] = ["2.4"]
  config["JetLeptonLowerDeltaRCut"] = -1.
  config["JetPUIDForEENoiseName"] = "pileupJetIdUpdatedfullId"
  config["JetPUIDForEENoiseWP"] = "loose"
  config["JetApplyEENoiseVeto"] = False
  config["JetApplyPUIDForEENoise"] = False

  return config
