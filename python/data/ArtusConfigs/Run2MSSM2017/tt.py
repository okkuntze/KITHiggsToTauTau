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
  config = jsonTools.JsonDict()
  config["EventWeight"]="eventWeight"
  config["Channel"] = "TT"
  
  
  config["Quantities"] = []
  
  config["Quantities"].extend([
                        "EventTauPnPi0s",
                        "EventTauNnPi0s",
                        "EventTauPnProngs",
                        "EventTauNnProngs",
                        "EventTauPE",
                        "EventTauNE",
                        "EventTauPvisE",
                        "EventTauNvisE",
                        "CosThetaN",
                        "CosThetaP",
                        "Omega"
  ])
  
  config["Processors"] = [
  ]
  
  config["Consumers"] = ["KappaLambdaNtupleConsumer",
                         "cutflow_histogram"]

  

  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('tt', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.nominal").build_config(nickname)) 
        