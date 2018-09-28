#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
#import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def build_list():
  quantities_list = [
#    "Flag_HBHENoiseFilter",
#    "Flag_HBHENoiseIsoFilter",
#    "Flag_EcalDeadCellTriggerPrimitiveFilter",
#    "Flag_goodVertices",
#    "Flag_BadPFMuonFilter",
#    "Flag_BadChargedCandidateFilter",
#    "Flag_eeBadScFilter",
#    "Flag_ecalBadCalibFilter",
#    "Flag_globalTightHalo2016Filter",
    "flagMETFilter",
    "nickname",
    "input",
    "run",
    "lumi",
    "event",
    "evt",
    "npv",
    "npu",
    "rho",
    "puweight",
    "weight",
    "m_vis",
    "diLepMass",
    "diLepMassSmearUp",
    "diLepMassSmearDown",
    "diLepGenMass",
    "mt_tot",
    "m_sv",
    "pt_sv",
    "eta_sv",
    "phi_sv",
    "mt_tt",
    "pt_1",
    "phi_1",
    "eta_1",
    "m_1",
    "q_1",
    "iso_1",
    "d0_1",
    "dZ_1",
    "mt_1",
    "pt_2",
    "phi_2",
    "eta_2",
    "m_2",
    "q_2",
    "iso_2",
    "d0_2",
    "dZ_2",
    "mt_2",
    "met",
    "metphi",
    "mvamet",
    "mvametphi",
    "pzetavis",
    "pzetamiss",
    "pZetaMissVis",
    "metcov00",
    "metcov01",
    "metcov10",
    "metcov11",
    "mvacov00",
    "mvacov01",
    "mvacov10",
    "mvacov11",
    "jpt_1",
    "jeta_1",
    "jphi_1",
    "jrawf_1",
    "jmva_1",
    "jpfid_1",
    "jpuid_1",
    "jcsv_1",
    "bpt_1",
    "beta_1",
    "bphi_1",
    "brawf_1",
    "bmva_1",
    "bpfid_1",
    "bpuid_1",
    "bcsv_1",
    "jm_1",
    "jpt_2",
    "jeta_2",
    "jphi_2",
    "jrawf_2",
    "jmva_2",
    "jpfid_2",
    "jpuid_2",
    "jcsv_2",
    "bpt_2",
    "beta_2",
    "bphi_2",
    "brawf_2",
    "bmva_2",
    "bpfid_2",
    "bpuid_2",
    "bcsv_2",
    "jm_2",
    "jcsv_3",
    "jcsv_4",
    "mjj",
    "jdeta",
    "njetingap",
    "njetingap20",
    "jdphi",
    "dijetpt",
    "dijetphi",
    "hdijetphi",
    "visjeteta",
    "ptvis",
    "nbtag",
    "njets",
    "njetspt20",
    "njetspt30",
    "njetspt20eta2p4",
    "ElectronMVAEstimatorRun2Fall17NoIsoV1Values_1",
    "ElectronMVAEstimatorRun2Fall17IsoV1Values_1",
    "ecalTrkEnergyPostCorr_1",
    "trigweight_1",
    "crossTriggerMCEfficiencyWeight_1",
    "crossTriggerDataEfficiencyWeight_1",
    "crossTriggerMCEfficiencyWeight_vvloose_MVA_1",
    "crossTriggerDataEfficiencyWeight_vvloose_MVA_1",
    "crossTriggerMCEfficiencyWeight_vloose_MVA_1",
    "crossTriggerDataEfficiencyWeight_vloose_MVA_1",
    "crossTriggerMCEfficiencyWeight_loose_MVA_1",
    "crossTriggerDataEfficiencyWeight_loose_MVA_1",
    "crossTriggerMCEfficiencyWeight_medium_MVA_1",
    "crossTriggerDataEfficiencyWeight_medium_MVA_1",
    "crossTriggerMCEfficiencyWeight_tight_MVA_1",
    "crossTriggerDataEfficiencyWeight_tight_MVA_1",
    "crossTriggerMCEfficiencyWeight_vtight_MVA_1",
    "crossTriggerDataEfficiencyWeight_vtight_MVA_1",
    "crossTriggerMCEfficiencyWeight_vvtight_MVA_1",
    "crossTriggerDataEfficiencyWeight_vvtight_MVA_1",
    "crossTriggerEmbeddedEfficiencyWeight_medium_MVA_1",
    "crossTriggerEmbeddedEfficiencyWeight_medium_MVA_2",
    "crossTriggerEmbeddedEfficiencyWeight_tight_MVA_1",
    "crossTriggerEmbeddedEfficiencyWeight_tight_MVA_2",
    "singleTriggerMCEfficiencyWeight_1",
    "singleTriggerDataEfficiencyWeight_1",
    "singleTriggerMCEfficiencyWeightKIT_1",
    "singleTriggerDataEfficiencyWeightKIT_1",
    "singleTriggerEmbeddedEfficiencyWeight_1",
    "singleTriggerEmbeddedEfficiencyWeight_1",
    "singleTriggerEmbeddedEfficiencyWeightKIT_1",
    "singleTriggerEmbeddedEfficiencyWeightKIT_1",
    "trackWeight_1",
    "idWeight_1",
    "isoWeight_1",
    "idisoweight_1",
    "eRatio_1",
    "leadingTrackChi2_1",
    "chargedIsoPtSum_1",
    "neutralIsoPtSum_1",
    "puCorrPtSum_1",
    "againstMuonLoose3_1", "againstMuonTight3_1",
    "againstElectronLooseMVA6_1", "againstElectronMediumMVA6_1", "againstElectronTightMVA6_1",
    "againstElectronVLooseMVA6_1", "againstElectronVTightMVA6_1",
    "byCombinedIsolationDeltaBetaCorrRaw3Hits_1",
    "byLooseCombinedIsolationDeltaBetaCorr3Hits_1", "byMediumCombinedIsolationDeltaBetaCorr3Hits_1",
    "byTightCombinedIsolationDeltaBetaCorr3Hits_1", "byIsolationMVArun2v1DBoldDMwLTraw_1", "byVLooseIsolationMVArun2v1DBoldDMwLT_1", "byLooseIsolationMVArun2v1DBoldDMwLT_1",
    "byMediumIsolationMVArun2v1DBoldDMwLT_1", "byTightIsolationMVArun2v1DBoldDMwLT_1", "byVTightIsolationMVArun2v1DBoldDMwLT_1",
    "decayModeFinding_1", "decayModeFindingNewDMs_1",
    "ElectronMVAEstimatorRun2Fall17NoIsoV1Values_2",
    "ElectronMVAEstimatorRun2Fall17IsoV1Values_2",
    "ecalTrkEnergyPostCorr_2",
    "trigweight_2",
    "crossTriggerMCEfficiencyWeight_2",
    "crossTriggerDataEfficiencyWeight_2",
    "crossTriggerMCEfficiencyWeight_vvloose_MVA_2",
    "crossTriggerDataEfficiencyWeight_vvloose_MVA_2",
    "crossTriggerMCEfficiencyWeight_vloose_MVA_2",
    "crossTriggerDataEfficiencyWeight_vloose_MVA_2",
    "crossTriggerMCEfficiencyWeight_loose_MVA_2",
    "crossTriggerDataEfficiencyWeight_loose_MVA_2",
    "crossTriggerMCEfficiencyWeight_medium_MVA_2",
    "crossTriggerDataEfficiencyWeight_medium_MVA_2",
    "crossTriggerMCEfficiencyWeight_tight_MVA_2",
    "crossTriggerDataEfficiencyWeight_tight_MVA_2",
    "crossTriggerMCEfficiencyWeight_vtight_MVA_2",
    "crossTriggerDataEfficiencyWeight_vtight_MVA_2",
    "crossTriggerMCEfficiencyWeight_vvtight_MVA_2",
    "crossTriggerDataEfficiencyWeight_vvtight_MVA_2",
    "singleTriggerMCEfficiencyWeight_2",
    "singleTriggerDataEfficiencyWeight_2",
    "singleTriggerMCEfficiencyWeightKIT_2",
    "singleTriggerDataEfficiencyWeightKIT_2",
    "trackWeight_2",
    "idWeight_2",
    "isoWeight_2",
    "idisoweight_2",
    "eRatio_2",
    "leadingTrackChi2_2",
    "chargedIsoPtSum_2",
    "neutralIsoPtSum_2",
    "puCorrPtSum_2",
    "againstMuonLoose3_2", "againstMuonTight3_2",
    "againstElectronLooseMVA6_2", "againstElectronMediumMVA6_2", "againstElectronTightMVA6_2",
    "againstElectronVLooseMVA6_2", "againstElectronVTightMVA6_2",
    "byCombinedIsolationDeltaBetaCorrRaw3Hits_2",
    "byLooseCombinedIsolationDeltaBetaCorr3Hits_2", "byMediumCombinedIsolationDeltaBetaCorr3Hits_2",
    "byTightCombinedIsolationDeltaBetaCorr3Hits_2", "byIsolationMVArun2v1DBoldDMwLTraw_2", "byVLooseIsolationMVArun2v1DBoldDMwLT_2", "byLooseIsolationMVArun2v1DBoldDMwLT_2",
    "byMediumIsolationMVArun2v1DBoldDMwLT_2", "byTightIsolationMVArun2v1DBoldDMwLT_2", "byVTightIsolationMVArun2v1DBoldDMwLT_2",
    "decayModeFinding_2", "decayModeFindingNewDMs_2",

    "byCombinedIsolationDeltaBetaCorrRaw3Hits_1",
    "byLooseCombinedIsolationDeltaBetaCorr3Hits_1",
    "byMediumCombinedIsolationDeltaBetaCorr3Hits_1",
    "byTightCombinedIsolationDeltaBetaCorr3Hits_1",
    "againstElectronLooseMVA6_1",
    "againstElectronMediumMVA6_1",
    "againstElectronTightMVA6_1",
    "againstElectronVLooseMVA6_1",
    "againstElectronVTightMVA6_1",
    "againstMuonLoose3_1",
    "againstMuonTight3_1",
    "byIsolationMVArun2v1DBoldDMwLTraw_1",
    "byVLooseIsolationMVArun2v1DBoldDMwLT_1",
    "byLooseIsolationMVArun2v1DBoldDMwLT_1",
    "byMediumIsolationMVArun2v1DBoldDMwLT_1",
    "byTightIsolationMVArun2v1DBoldDMwLT_1",
    "byVTightIsolationMVArun2v1DBoldDMwLT_1",
    "byVVTightIsolationMVArun2v1DBoldDMwLT_1",
    "byIsolationMVArun2017v2DBoldDMwLTraw2017_1",
    "byVVLooseIsolationMVArun2017v2DBoldDMwLT2017_1",
    "byVLooseIsolationMVArun2017v2DBoldDMwLT2017_1",
    "byLooseIsolationMVArun2017v2DBoldDMwLT2017_1",
    "byMediumIsolationMVArun2017v2DBoldDMwLT2017_1",
    "byTightIsolationMVArun2017v2DBoldDMwLT2017_1",
    "byVTightIsolationMVArun2017v2DBoldDMwLT2017_1",
    "byVVTightIsolationMVArun2017v2DBoldDMwLT2017_1",
    "byIsolationMVArun2017v1DBoldDMwLTraw2017_1",
    "byVVLooseIsolationMVArun2017v1DBoldDMwLT2017_1",
    "byVLooseIsolationMVArun2017v1DBoldDMwLT2017_1",
    "byLooseIsolationMVArun2017v1DBoldDMwLT2017_1",
    "byMediumIsolationMVArun2017v1DBoldDMwLT2017_1",
    "byTightIsolationMVArun2017v1DBoldDMwLT2017_1",
    "byVTightIsolationMVArun2017v1DBoldDMwLT2017_1",
    "byVVTightIsolationMVArun2017v1DBoldDMwLT2017_1",
    "chargedIsoPtSum_1",
    "decayModeFinding_1",
    "decayModeFindingNewDMs_1",
    "neutralIsoPtSum_1",
    "puCorrPtSum_1",
    "footprintCorrection_1",
    "photonPtSumOutsideSignalCone_1",
    "decayDistX_1",
    "decayDistY_1",
    "decayDistZ_1",
    "decayDistM_1",
    "nPhoton_1",
    "ptWeightedDetaStrip_1",
    "ptWeightedDphiStrip_1",
    "ptWeightedDrSignal_1",
    "ptWeightedDrIsolation_1",
    "leadingTrackChi2_1",
    "eRatio_1",

    "byCombinedIsolationDeltaBetaCorrRaw3Hits_2",
    "byLooseCombinedIsolationDeltaBetaCorr3Hits_2",
    "byMediumCombinedIsolationDeltaBetaCorr3Hits_2",
    "byTightCombinedIsolationDeltaBetaCorr3Hits_2",
    "againstElectronLooseMVA6_2",
    "againstElectronMediumMVA6_2",
    "againstElectronTightMVA6_2",
    "againstElectronVLooseMVA6_2",
    "againstElectronVTightMVA6_2",
    "againstMuonLoose3_2",
    "againstMuonTight3_2",
    "byIsolationMVArun2v1DBoldDMwLTraw_2",
    "byVLooseIsolationMVArun2v1DBoldDMwLT_2",
    "byLooseIsolationMVArun2v1DBoldDMwLT_2",
    "byMediumIsolationMVArun2v1DBoldDMwLT_2",
    "byTightIsolationMVArun2v1DBoldDMwLT_2",
    "byVTightIsolationMVArun2v1DBoldDMwLT_2",
    "byVVTightIsolationMVArun2v1DBoldDMwLT_2",
    "byIsolationMVArun2017v2DBoldDMwLTraw2017_2",
    "byVVLooseIsolationMVArun2017v2DBoldDMwLT2017_2",
    "byVLooseIsolationMVArun2017v2DBoldDMwLT2017_2",
    "byLooseIsolationMVArun2017v2DBoldDMwLT2017_2",
    "byMediumIsolationMVArun2017v2DBoldDMwLT2017_2",
    "byTightIsolationMVArun2017v2DBoldDMwLT2017_2",
    "byVTightIsolationMVArun2017v2DBoldDMwLT2017_2",
    "byVVTightIsolationMVArun2017v2DBoldDMwLT2017_2",
    "byIsolationMVArun2017v1DBoldDMwLTraw2017_2",
    "byVVLooseIsolationMVArun2017v1DBoldDMwLT2017_2",
    "byVLooseIsolationMVArun2017v1DBoldDMwLT2017_2",
    "byLooseIsolationMVArun2017v1DBoldDMwLT2017_2",
    "byMediumIsolationMVArun2017v1DBoldDMwLT2017_2",
    "byTightIsolationMVArun2017v1DBoldDMwLT2017_2",
    "byVTightIsolationMVArun2017v1DBoldDMwLT2017_2",
    "byVVTightIsolationMVArun2017v1DBoldDMwLT2017_2",
    "chargedIsoPtSum_2",
    "decayModeFinding_2",
    "decayModeFindingNewDMs_2",
    "neutralIsoPtSum_2",
    "puCorrPtSum_2",
    "footprintCorrection_2",
    "photonPtSumOutsideSignalCone_2",
    "decayDistX_2",
    "decayDistY_2",
    "decayDistZ_2",
    "decayDistM_2",
    "nPhoton_2",
    "ptWeightedDetaStrip_2",
    "ptWeightedDphiStrip_2",
    "ptWeightedDrSignal_2",
    "ptWeightedDrIsolation_2",
    "leadingTrackChi2_2",
    "eRatio_2",

    "isFake",
    "NUP",
    "id_m_loose_1",
    "id_m_medium_1",
    "id_m_tight_1",
    "id_m_highpt_1",
    "id_e_mva_nt_loose_1",
    "id_e_cut_veto_1",
    "id_e_cut_loose_1",
    "id_e_cut_medium_1",
    "id_e_cut_tight_1",
    "pt_tt",
    "dilepton_veto",
    "extraelec_veto",
    "extramuon_veto",
    "gen_match_1",
    "gen_match_2",
    "decayMode_1",
    "decayMode_2",
    "npartons",
    "genbosonmass",
    "genbosonpt",
    "genbosoneta",
    "genbosonphi",

    "trg_singlemuon_24",
    "trg_singlemuon_27",
    "trg_crossmuon_mu20tau27",
    "trg_singleelectron_27",
    "trg_singleelectron_32",
    "trg_singleelectron_32_fallback",
    "trg_singleelectron_35",
    "trg_crossele_ele24tau30",
    "trg_doubletau_35_tightiso_tightid",
    "trg_doubletau_40_mediso_tightid",
    "trg_doubletau_40_tightiso",
    "trg_muonelectron_mu12ele23",
    "trg_muonelectron_mu23ele12",
    "trg_muonelectron_mu8ele23",
    "trg_singletau_leading",
    "trg_singletau_trailing",

    "isSingleMuon",
    "isSingleElectron",
    "isTau",
    "isMuonEG",
    "isDoubleEG",
    "isDoubleMuon",
    "isMC",
    "isEmbedded",

    "ggh_t_weight",
    "ggh_b_weight",
    "ggh_i_weight",
    "ggH_t_weight",
    "ggH_b_weight",
    "ggH_i_weight",
    "ggA_t_weight",
    "ggA_b_weight",
    "ggA_i_weight",
  ]
  '''
    "#mcweight",
    "#idweight_1",
    "#idweight_2",
    "#isoweight_1",
    "#isoweight_2",
    "#effweight",
    "#embeddedWeight",
    "#m_sv",
    "#mt_sv",
    "#pt_sv",
    "#eta_sv",
    "#phi_sv",
    "#met_sv",
    "#m_sv_Up",
    "#m_sv_Down",
    "#mva_1",
    "#passid_1",
    "#passiso_1",
    "#mva_2",
    "#passid_2",
    "#passiso_2",
    "#l1met",
    "#l1metphi",
    "#l1metcorr",
    "#calomet",
    "#calometphi",
    "#calometcorr",
    "#calometphicorr",
    "#mva_gf",
    "#mva_vbf",
    "#uncorrmet",
    "#genpX",
    "#genpY",
    "#vispX",
    "#vispY",
    "#TTbarGenDecayMode"
  '''
  
  return quantities_list
