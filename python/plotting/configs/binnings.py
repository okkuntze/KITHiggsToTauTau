
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import Artus.HarryPlotter.utility.binnings as binnings


class BinningsDict(binnings.BinningsDict):
	def __init__(self, additional_binnings=None):
		super(BinningsDict, self).__init__(additional_binnings=additional_binnings)
		
		self.binnings_dict["diLepMass"] = "50,0,250"
		self.binnings_dict["svfitMass"] = "50,0,250"
		
		self.binnings_dict["tt_decayMode_1"] = "11,0.0,11.0"
		self.binnings_dict["tt_decayMode_2"] = "11,0.0,11.0"
		self.binnings_dict["tt_eta_1"] = "30,-3.0,3.0"
		self.binnings_dict["tt_eta_2"] = "30,-3.0,3.0"
		self.binnings_dict["tt_eta_ll"] = "25,-5.0,5.0"
		self.binnings_dict["tt_eta_llmet"] = "25,-5.0,5.0"
		self.binnings_dict["tt_eta_sv"] = "25,-5.0,5.0"
		self.binnings_dict["tt_inclusive"] = "1,0.0,1.0"
		self.binnings_dict["tt_iso_1"] = "25,0.0,2.0"
		self.binnings_dict["tt_iso_2"] = "25,0.0,2.0"
		self.binnings_dict["tt_jdeta"] = "25,0.0,10.0"
		self.binnings_dict["tt_jeta_1"] = "30,-5.0,5.0"
		self.binnings_dict["tt_jeta_2"] = "30,-5.0,5.0"
		self.binnings_dict["tt_jphi_1"] = "32,-3.2,3.2"
		self.binnings_dict["tt_jphi_2"] = "32,-3.2,3.2"
		self.binnings_dict["tt_jpt_1"] = "25,0.0,250.0"
		self.binnings_dict["tt_jpt_2"] = "25,0.0,500.0"
		self.binnings_dict["tt_m_1"] = "20,-0.2,0.2"
		self.binnings_dict["tt_m_2"] = "25,0.0,2.5"
		self.binnings_dict["tt_m_ll"] = "60,0.0,300"
		self.binnings_dict["tt_m_llmet"] = "60,0.0,400"
		self.binnings_dict["tt_m_sv"] = "25,0.0,250"
		self.binnings_dict["tt_met"] = "40,0.0,200.0"
		self.binnings_dict["tt_metcov00"] = "25,0.0,1000.0"
		self.binnings_dict["tt_metcov01"] = "25,-500.0,500.0"
		self.binnings_dict["tt_metcov10"] = "25,-500.0,500.0"
		self.binnings_dict["tt_metcov11"] = "25,0.0,1000.0"
		self.binnings_dict["tt_metphi"] = "32,-3.2,3.2"
		self.binnings_dict["tt_mjj"] = "30,0.0,3000.0"
		self.binnings_dict["tt_mt_1"] = "30,0.0,150"
		self.binnings_dict["tt_mt_lep1met"] = "30,0.0,300"
		self.binnings_dict["tt_mt_ll"] = "25,75.0,300"
		self.binnings_dict["tt_mt_llmet"] = "40,0.0,400"
		self.binnings_dict["tt_mvacov00"] = "25,0.0,1000.0"
		self.binnings_dict["tt_mvacov01"] = "25,-500.0,500.0"
		self.binnings_dict["tt_mvacov10"] = "25,-500.0,500.0"
		self.binnings_dict["tt_mvacov11"] = "25,0.0,1000.0"
		self.binnings_dict["tt_mvamet"] = "40,0.0,200.0"
		self.binnings_dict["tt_mvametcov00"] = "25,0.0,1000.0"
		self.binnings_dict["tt_mvametcov01"] = "25,-500.0,500.0"
		self.binnings_dict["tt_mvametcov10"] = "25,-500.0,500.0"
		self.binnings_dict["tt_mvametcov11"] = "25,0.0,1000.0"
		self.binnings_dict["tt_mvametphi"] = "32,-3.2,3.2"
		self.binnings_dict["tt_m_vis"] = "35,0.0,350.0"
		self.binnings_dict["tt_nJets30"] = "6,-0.5,5.5"
		self.binnings_dict["tt_njets"] = "10,0.0,10.0"
		self.binnings_dict["tt_npu"] = "30,0.0,60.0"
		self.binnings_dict["tt_npv"] = "30,0.0,60.0"
		self.binnings_dict["tt_phi_1"] = "32,-3.2,3.2"
		self.binnings_dict["tt_phi_2"] = "32,-3.2,3.2"
		self.binnings_dict["tt_phi_ll"] = "32,-3.2,3.2"
		self.binnings_dict["tt_phi_llmet"] = "32,-3.2,3.2"
		self.binnings_dict["tt_phi_sv"] = "32,-3.2,3.2"
		self.binnings_dict["tt_pt_1"] = "25,0.0,250.0"
		self.binnings_dict["tt_pt_2"] = "25,0.0,250.0"
		self.binnings_dict["tt_pt_ll"] = "25,0.0,250"
		self.binnings_dict["tt_pt_llmet"] = "25,0.0,250"
		self.binnings_dict["tt_pt_sv"] = "25,0.0,250"
		self.binnings_dict["tt_pt_tt"] = "20,0.0,200"
		self.binnings_dict["tt_puweight"] = "20,0.0,2.0"
		self.binnings_dict["tt_rho"] = "25,0.0,50.0"
		self.binnings_dict["tt_svfitMass"] = "25,0.0,250"
		self.binnings_dict["tt_trigweight_1"] = "20,0.5,1.5"
		self.binnings_dict["tt_trigweight_2"] = "20,0.5,1.5"
		self.binnings_dict["mt_decayMode_2"] = "11,0.0,11.0"
		self.binnings_dict["mt_eta_1"] = "30,-3.0,3.0"
		self.binnings_dict["mt_eta_2"] = "30,-3.0,3.0"
		self.binnings_dict["mt_eta_ll"] = "25,-5.0,5.0"
		self.binnings_dict["mt_eta_llmet"] = "25,-5.0,5.0"
		self.binnings_dict["mt_eta_sv"] = "25,-5.0,5.0"
		self.binnings_dict["mt_inclusive"] = "1,0.0,1.0"
		self.binnings_dict["mt_iso_1"] = "25,0.0,0.1"
		self.binnings_dict["mt_iso_2"] = "25,0.0,2.0"
		self.binnings_dict["mt_jdeta"] = "25,0.0,10.0"
		self.binnings_dict["mt_jeta_1"] = "30,-5.0,5.0"
		self.binnings_dict["mt_jeta_2"] = "30,-5.0,5.0"
		self.binnings_dict["mt_jphi_1"] = "32,-3.2,3.2"
		self.binnings_dict["mt_jphi_2"] = "32,-3.2,3.2"
		self.binnings_dict["mt_jpt_1"] = "25,0.0,250.0"
		self.binnings_dict["mt_jpt_2"] = "25,0.0,500.0"
		self.binnings_dict["mt_m_1"] = "20,-0.2,0.2"
		self.binnings_dict["mt_m_2"] = "25,0.0,2.5"
		self.binnings_dict["mt_m_ll"] = "60,0.0,300"
		self.binnings_dict["mt_m_llmet"] = "60,0.0,400"
		self.binnings_dict["mt_m_sv"] = "25,0.0,250"
		self.binnings_dict["mt_met"] = "40,0.0,200.0"
		self.binnings_dict["mt_metcov00"] = "25,0.0,1000.0"
		self.binnings_dict["mt_metcov01"] = "25,-500.0,500.0"
		self.binnings_dict["mt_metcov10"] = "25,-500.0,500.0"
		self.binnings_dict["mt_metcov11"] = "25,0.0,1000.0"
		self.binnings_dict["mt_metphi"] = "32,-3.2,3.2"
		self.binnings_dict["mt_metProjection"] = "25,-50,50"
		self.binnings_dict["mt_mjj"] = "30,0.0,3000.0"
		self.binnings_dict["mt_mt_1"] = "30,0.0,150"
		self.binnings_dict["mt_mt_lep1met"] = "30,0.0,300"
		self.binnings_dict["mt_mt_ll"] = "25,75.0,300"
		self.binnings_dict["mt_mt_llmet"] = "40,0.0,400"
		self.binnings_dict["mt_mvacov00"] = "25,0.0,1000.0"
		self.binnings_dict["mt_mvacov01"] = "25,-500.0,500.0"
		self.binnings_dict["mt_mvacov10"] = "25,-500.0,500.0"
		self.binnings_dict["mt_mvacov11"] = "25,0.0,1000.0"
		self.binnings_dict["mt_mvamet"] = "40,0.0,200.0"
		self.binnings_dict["mt_mvametcov00"] = "25,0.0,1000.0"
		self.binnings_dict["mt_mvametcov01"] = "25,-500.0,500.0"
		self.binnings_dict["mt_mvametcov10"] = "25,-500.0,500.0"
		self.binnings_dict["mt_mvametcov11"] = "25,0.0,1000.0"
		self.binnings_dict["mt_mvametphi"] = "32,-3.2,3.2"
		self.binnings_dict["mt_m_vis"] = "35,0.0,350.0"
		self.binnings_dict["mt_nJets30"] = "6,-0.5,5.5"
		self.binnings_dict["mt_njets"] = "10,0.0,10.0"
		self.binnings_dict["mt_npu"] = "30,0.0,60.0"
		self.binnings_dict["mt_npv"] = "30,0.0,60.0"
		self.binnings_dict["mt_phi_1"] = "32,-3.2,3.2"
		self.binnings_dict["mt_phi_2"] = "32,-3.2,3.2"
		self.binnings_dict["mt_phi_ll"] = "32,-3.2,3.2"
		self.binnings_dict["mt_phi_llmet"] = "32,-3.2,3.2"
		self.binnings_dict["mt_phi_sv"] = "32,-3.2,3.2"
		self.binnings_dict["mt_pt_1"] = "25,0.0,100.0"
		self.binnings_dict["mt_pt_2"] = "25,0.0,100.0"
		self.binnings_dict["mt_pt_ll"] = "25,0.0,250"
		self.binnings_dict["mt_pt_llmet"] = "25,0.0,250"
		self.binnings_dict["mt_pt_sv"] = "25,0.0,250"
		self.binnings_dict["mt_pt_tt"] = "20,0.0,200"
		self.binnings_dict["mt_puweight"] = "20,0.0,2.0"
		self.binnings_dict["mt_rho"] = "25,0.0,50.0"
		self.binnings_dict["mt_svfitMass"] = "25,0.0,250"
		self.binnings_dict["mt_trigweight_1"] = "20,0.5,1.5"
		self.binnings_dict["mt_trigweight_2"] = "20,0.5,1.5"
		self.binnings_dict["mt_pzetamiss"] = "20,0.0,100.0"
		self.binnings_dict["mt_pzetavis"] = "20,0.0,100.0"
		self.binnings_dict["et_decayMode_2"] = "11,0.0,11.0"
		self.binnings_dict["et_eta_1"] = "30,-3.0,3.0"
		self.binnings_dict["et_eta_2"] = "30,-3.0,3.0"
		self.binnings_dict["et_eta_ll"] = "25,-5.0,5.0"
		self.binnings_dict["et_eta_llmet"] = "25,-5.0,5.0"
		self.binnings_dict["et_eta_sv"] = "25,-5.0,5.0"
		self.binnings_dict["et_inclusive"] = "1,0.0,1.0"
		self.binnings_dict["et_iso_1"] = "25,0.0,0.1"
		self.binnings_dict["et_iso_2"] = "25,0.0,2.0"
		self.binnings_dict["et_jdeta"] = "25,0.0,10.0"
		self.binnings_dict["et_jeta_1"] = "30,-5.0,5.0"
		self.binnings_dict["et_jeta_2"] = "30,-5.0,5.0"
		self.binnings_dict["et_jphi_1"] = "32,-3.2,3.2"
		self.binnings_dict["et_jphi_2"] = "32,-3.2,3.2"
		self.binnings_dict["et_jpt_1"] = "25,0.0,250.0"
		self.binnings_dict["et_jpt_2"] = "25,0.0,500.0"
		self.binnings_dict["et_m_1"] = "20,-0.2,0.2"
		self.binnings_dict["et_m_2"] = "25,0.0,2.5"
		self.binnings_dict["et_m_ll"] = "60,0.0,300"
		self.binnings_dict["et_m_llmet"] = "60,0.0,400"
		self.binnings_dict["et_m_sv"] = "25,0.0,250"
		self.binnings_dict["et_met"] = "40,0.0,200.0"
		self.binnings_dict["et_metcov00"] = "25,0.0,1000.0"
		self.binnings_dict["et_metcov01"] = "25,-500.0,500.0"
		self.binnings_dict["et_metcov10"] = "25,-500.0,500.0"
		self.binnings_dict["et_metcov11"] = "25,0.0,1000.0"
		self.binnings_dict["et_metphi"] = "32,-3.2,3.2"
		self.binnings_dict["et_metProjection"] = "25,-50,50"
		self.binnings_dict["et_mt_1"] = "30,0.0,150"
		self.binnings_dict["et_mjj"] = "30,0.0,3000.0"
		self.binnings_dict["et_mt_lep1met"] = "30,0.0,300"
		self.binnings_dict["et_mt_ll"] = "25,75.0,300"
		self.binnings_dict["et_mt_llmet"] = "40,0.0,400"
		self.binnings_dict["et_mvacov00"] = "25,0.0,1000.0"
		self.binnings_dict["et_mvacov01"] = "25,-500.0,500.0"
		self.binnings_dict["et_mvacov10"] = "25,-500.0,500.0"
		self.binnings_dict["et_mvacov11"] = "25,0.0,1000.0"
		self.binnings_dict["et_mvamet"] = "40,0.0,200.0"
		self.binnings_dict["et_mvametcov00"] = "25,0.0,1000.0"
		self.binnings_dict["et_mvametcov01"] = "25,-500.0,500.0"
		self.binnings_dict["et_mvametcov10"] = "25,-500.0,500.0"
		self.binnings_dict["et_mvametcov11"] = "25,0.0,1000.0"
		self.binnings_dict["et_mvametphi"] = "32,-3.2,3.2"
		self.binnings_dict["et_m_vis"] = "35,0.0,350.0"
		self.binnings_dict["et_nJets30"] = "6,-0.5,5.5"
		self.binnings_dict["et_njets"] = "10,0.0,10.0"
		self.binnings_dict["et_npu"] = "30,0.0,60.0"
		self.binnings_dict["et_npv"] = "30,0.0,60.0"
		self.binnings_dict["et_phi_1"] = "32,-3.2,3.2"
		self.binnings_dict["et_phi_2"] = "32,-3.2,3.2"
		self.binnings_dict["et_phi_ll"] = "32,-3.2,3.2"
		self.binnings_dict["et_phi_llmet"] = "32,-3.2,3.2"
		self.binnings_dict["et_phi_sv"] = "32,-3.2,3.2"
		self.binnings_dict["et_pt_1"] = "25,0.0,100.0"
		self.binnings_dict["et_pt_2"] = "25,0.0,100.0"
		self.binnings_dict["et_pt_ll"] = "25,0.0,250"
		self.binnings_dict["et_pt_llmet"] = "25,0.0,250"
		self.binnings_dict["et_pt_sv"] = "25,0.0,250"
		self.binnings_dict["et_pt_tt"] = "20,0.0,200"
		self.binnings_dict["et_puweight"] = "20,0.0,2.0"
		self.binnings_dict["et_rho"] = "25,0.0,50.0"
		self.binnings_dict["et_svfitMass"] = "25,0.0,250"
		self.binnings_dict["et_trigweight_1"] = "20,0.5,1.5"
		self.binnings_dict["et_trigweight_2"] = "20,0.5,1.5"
		self.binnings_dict["et_pzetamiss"] = "20,0.0,100.0"
		self.binnings_dict["et_pzetavis"] = "20,0.0,100.0"
		self.binnings_dict["em_eta_1"] = "30,-3.0,3.0"
		self.binnings_dict["em_eta_2"] = "30,-3.0,3.0"
		self.binnings_dict["em_eta_ll"] = "25,-5.0,5.0"
		self.binnings_dict["em_eta_llmet"] = "25,-5.0,5.0"
		self.binnings_dict["em_eta_sv"] = "25,-5.0,5.0"
		self.binnings_dict["em_inclusive"] = "1,0.0,1.0"
		self.binnings_dict["em_iso_1"] = "25,0.0,0.1"
		self.binnings_dict["em_iso_2"] = "25,0.0,0.1"
		self.binnings_dict["em_jdeta"] = "25,0.0,10.0"
		self.binnings_dict["em_jeta_1"] = "30,-5.0,5.0"
		self.binnings_dict["em_jeta_2"] = "30,-5.0,5.0"
		self.binnings_dict["em_jphi_1"] = "32,-3.2,3.2"
		self.binnings_dict["em_jphi_2"] = "32,-3.2,3.2"
		self.binnings_dict["em_jpt_1"] = "25,0.0,250.0"
		self.binnings_dict["em_jpt_2"] = "25,0.0,250.0"
		self.binnings_dict["em_m_1"] = "20,-0.2,0.2"
		self.binnings_dict["em_m_2"] = "25,0.0,2.5"
		self.binnings_dict["em_m_ll"] = "60,0.0,300"
		self.binnings_dict["em_m_llmet"] = "60,0.0,400"
		self.binnings_dict["em_m_sv"] = "25,0.0,250"
		self.binnings_dict["em_met"] = "40,0.0,200.0"
		self.binnings_dict["em_metcov00"] = "25,0.0,1000.0"
		self.binnings_dict["em_metcov01"] = "25,-500.0,500.0"
		self.binnings_dict["em_metcov10"] = "25,-500.0,500.0"
		self.binnings_dict["em_metcov11"] = "25,0.0,1000.0"
		self.binnings_dict["em_metphi"] = "32,-3.2,3.2"
		self.binnings_dict["em_metProjection"] = "25,-50,50"
		self.binnings_dict["em_mjj"] = "30,0.0,3000.0"
		self.binnings_dict["em_mt_1"] = "30,0.0,150"
		self.binnings_dict["em_mt_lep1met"] = "30,0.0,300"
		self.binnings_dict["em_mt_ll"] = "25,75.0,300"
		self.binnings_dict["em_mt_llmet"] = "40,0.0,400"
		self.binnings_dict["em_mvacov00"] = "25,0.0,1000.0"
		self.binnings_dict["em_mvacov01"] = "25,-500.0,500.0"
		self.binnings_dict["em_mvacov10"] = "25,-500.0,500.0"
		self.binnings_dict["em_mvacov11"] = "25,0.0,1000.0"
		self.binnings_dict["em_mvamet"] = "40,0.0,200.0"
		self.binnings_dict["em_mvametcov00"] = "25,0.0,1000.0"
		self.binnings_dict["em_mvametcov01"] = "25,-500.0,500.0"
		self.binnings_dict["em_mvametcov10"] = "25,-500.0,500.0"
		self.binnings_dict["em_mvametcov11"] = "25,0.0,1000.0"
		self.binnings_dict["em_mvametphi"] = "32,-3.2,3.2"
		self.binnings_dict["em_m_vis"] = "35,0.0,350.0"
		self.binnings_dict["em_nJets30"] = "6,-0.5,5.5"
		self.binnings_dict["em_njets"] = "10,0.0,10.0"
		self.binnings_dict["em_npu"] = "30,0.0,60.0"
		self.binnings_dict["em_npv"] = "30,0.0,60.0"
		self.binnings_dict["em_phi_1"] = "32,-3.2,3.2"
		self.binnings_dict["em_phi_2"] = "32,-3.2,3.2"
		self.binnings_dict["em_phi_ll"] = "32,-3.2,3.2"
		self.binnings_dict["em_phi_llmet"] = "32,-3.2,3.2"
		self.binnings_dict["em_phi_sv"] = "32,-3.2,3.2"
		self.binnings_dict["em_pt_1"] = "25,0.0,100.0"
		self.binnings_dict["em_pt_2"] = "25,0.0,100.0"
		self.binnings_dict["em_pt_ll"] = "25,0.0,250"
		self.binnings_dict["em_pt_llmet"] = "25,0.0,250"
		self.binnings_dict["em_pt_sv"] = "25,0.0,250"
		self.binnings_dict["em_pt_tt"] = "20,0.0,200"
		self.binnings_dict["em_puweight"] = "20,0.0,2.0"
		self.binnings_dict["em_rho"] = "25,0.0,50.0"
		self.binnings_dict["em_svfitMass"] = "25,0.0,250"
		self.binnings_dict["em_trigweight_1"] = "20,0.5,1.5"
		self.binnings_dict["em_trigweight_2"] = "20,0.5,1.5"
		self.binnings_dict["em_pzetamiss"] = "20,0.0,100.0"
		self.binnings_dict["em_pzetavis"] = "20,0.0,100.0"
		self.binnings_dict["mm_eta_1"] = "30,-3.0,3.0"
		self.binnings_dict["mm_eta_2"] = "30,-3.0,3.0"
		self.binnings_dict["mm_eta_ll"] = "25,-5.0,5.0"
		self.binnings_dict["mm_eta_llmet"] = "25,-5.0,5.0"
		self.binnings_dict["mm_eta_sv"] = "25,-5.0,5.0"
		self.binnings_dict["mm_inclusive"] = "1,0.0,1.0"
		self.binnings_dict["mm_iso_1"] = "25,0.0,0.1"
		self.binnings_dict["mm_iso_2"] = "25,0.0,0.1"
		self.binnings_dict["mm_jdeta"] = "25,0.0,10.0"
		self.binnings_dict["mm_jeta_1"] = "30,-5.0,5.0"
		self.binnings_dict["mm_jeta_2"] = "30,-5.0,5.0"
		self.binnings_dict["mm_jphi_1"] = "32,-3.2,3.2"
		self.binnings_dict["mm_jphi_2"] = "32,-3.2,3.2"
		self.binnings_dict["mm_jpt_1"] = "25,0.0,250.0"
		self.binnings_dict["mm_jpt_2"] = "25,0.0,500.0"
		self.binnings_dict["mm_m_1"] = "20,-0.2,0.2"
		self.binnings_dict["mm_m_2"] = "25,0.0,2.5"
		self.binnings_dict["mm_m_ll"] = "60,0.0,300"
		self.binnings_dict["mm_m_llmet"] = "60,0.0,400"
		self.binnings_dict["mm_m_sv"] = "25,0.0,250"
		self.binnings_dict["mm_met"] = "40,0.0,200.0"
		self.binnings_dict["mm_metcov00"] = "25,0.0,1000.0"
		self.binnings_dict["mm_metcov01"] = "25,-500.0,500.0"
		self.binnings_dict["mm_metcov10"] = "25,-500.0,500.0"
		self.binnings_dict["mm_metcov11"] = "25,0.0,1000.0"
		self.binnings_dict["mm_metphi"] = "32,-3.2,3.2"
		self.binnings_dict["mm_mjj"] = "30,0.0,3000.0"
		self.binnings_dict["mm_mt_1"] = "30,0.0,150"
		self.binnings_dict["mm_mt_lep1met"] = "30,0.0,300"
		self.binnings_dict["mm_mt_ll"] = "25,75.0,300"
		self.binnings_dict["mm_mt_llmet"] = "40,0.0,400"
		self.binnings_dict["mm_mvacov00"] = "25,0.0,1000.0"
		self.binnings_dict["mm_mvacov01"] = "25,-500.0,500.0"
		self.binnings_dict["mm_mvacov10"] = "25,-500.0,500.0"
		self.binnings_dict["mm_mvacov11"] = "25,0.0,1000.0"
		self.binnings_dict["mm_mvamet"] = "40,0.0,200.0"
		self.binnings_dict["mm_mvametcov00"] = "25,0.0,1000.0"
		self.binnings_dict["mm_mvametcov01"] = "25,-500.0,500.0"
		self.binnings_dict["mm_mvametcov10"] = "25,-500.0,500.0"
		self.binnings_dict["mm_mvametcov11"] = "25,0.0,1000.0"
		self.binnings_dict["mm_mvametphi"] = "32,-3.2,3.2"
		self.binnings_dict["mm_m_vis"] = "35,0.0,350.0"
		self.binnings_dict["mm_nJets30"] = "6,-0.5,5.5"
		self.binnings_dict["mm_njets"] = "10,0.0,10.0"
		self.binnings_dict["mm_npu"] = "30,0.0,60.0"
		self.binnings_dict["mm_npv"] = "30,0.0,60.0"
		self.binnings_dict["mm_phi_1"] = "32,-3.2,3.2"
		self.binnings_dict["mm_phi_2"] = "32,-3.2,3.2"
		self.binnings_dict["mm_phi_ll"] = "32,-3.2,3.2"
		self.binnings_dict["mm_phi_llmet"] = "32,-3.2,3.2"
		self.binnings_dict["mm_phi_sv"] = "32,-3.2,3.2"
		self.binnings_dict["mm_pt_1"] = "25,0.0,250.0"
		self.binnings_dict["mm_pt_2"] = "25,0.0,250.0"
		self.binnings_dict["mm_pt_ll"] = "25,0.0,250"
		self.binnings_dict["mm_pt_llmet"] = "25,0.0,250"
		self.binnings_dict["mm_pt_sv"] = "25,0.0,250"
		self.binnings_dict["mm_pt_tt"] = "20,0.0,200"
		self.binnings_dict["mm_puweight"] = "20,0.0,2.0"
		self.binnings_dict["mm_rho"] = "25,0.0,50.0"
		self.binnings_dict["mm_svfitMass"] = "25,0.0,250"
		self.binnings_dict["mm_trigweight_1"] = "20,0.5,1.5"
		self.binnings_dict["mm_trigweight_2"] = "20,0.5,1.5"
		self.binnings_dict["ee_eta_1"] = "30,-3.0,3.0"
		self.binnings_dict["ee_eta_2"] = "30,-3.0,3.0"
		self.binnings_dict["ee_eta_ll"] = "25,-5.0,5.0"
		self.binnings_dict["ee_eta_llmet"] = "25,-5.0,5.0"
		self.binnings_dict["ee_eta_sv"] = "25,-5.0,5.0"
		self.binnings_dict["ee_inclusive"] = "1,0.0,1.0"
		self.binnings_dict["ee_iso_1"] = "25,0.0,0.1"
		self.binnings_dict["ee_iso_2"] = "25,0.0,0.1"
		self.binnings_dict["ee_jdeta"] = "25,0.0,10.0"
		self.binnings_dict["ee_jeta_1"] = "30,-5.0,5.0"
		self.binnings_dict["ee_jeta_2"] = "30,-5.0,5.0"
		self.binnings_dict["ee_jphi_1"] = "32,-3.2,3.2"
		self.binnings_dict["ee_jphi_2"] = "32,-3.2,3.2"
		self.binnings_dict["ee_jpt_1"] = "25,0.0,250.0"
		self.binnings_dict["ee_jpt_2"] = "25,0.0,500.0"
		self.binnings_dict["ee_m_1"] = "20,-0.2,0.2"
		self.binnings_dict["ee_m_2"] = "25,0.0,2.5"
		self.binnings_dict["ee_m_ll"] = "60,0.0,300"
		self.binnings_dict["ee_m_llmet"] = "60,0.0,400"
		self.binnings_dict["ee_m_sv"] = "25,0.0,250"
		self.binnings_dict["ee_met"] = "40,0.0,200.0"
		self.binnings_dict["ee_metcov00"] = "25,0.0,1000.0"
		self.binnings_dict["ee_metcov01"] = "25,-500.0,500.0"
		self.binnings_dict["ee_metcov10"] = "25,-500.0,500.0"
		self.binnings_dict["ee_metcov11"] = "25,0.0,1000.0"
		self.binnings_dict["ee_metphi"] = "32,-3.2,3.2"
		self.binnings_dict["ee_mjj"] = "30,0.0,3000.0"
		self.binnings_dict["ee_mt_1"] = "30,0.0,150"
		self.binnings_dict["ee_mt_lep1met"] = "30,0.0,300"
		self.binnings_dict["ee_mt_ll"] = "25,75.0,300"
		self.binnings_dict["ee_mt_llmet"] = "40,0.0,400"
		self.binnings_dict["ee_mvacov00"] = "25,0.0,1000.0"
		self.binnings_dict["ee_mvacov01"] = "25,-500.0,500.0"
		self.binnings_dict["ee_mvacov10"] = "25,-500.0,500.0"
		self.binnings_dict["ee_mvacov11"] = "25,0.0,1000.0"
		self.binnings_dict["ee_mvamet"] = "40,0.0,200.0"
		self.binnings_dict["ee_mvametcov00"] = "25,0.0,1000.0"
		self.binnings_dict["ee_mvametcov01"] = "25,-500.0,500.0"
		self.binnings_dict["ee_mvametcov10"] = "25,-500.0,500.0"
		self.binnings_dict["ee_mvametcov11"] = "25,0.0,1000.0"
		self.binnings_dict["ee_mvametphi"] = "32,-3.2,3.2"
		self.binnings_dict["ee_m_vis"] = "35,0.0,350.0"
		self.binnings_dict["ee_nJets30"] = "6,-0.5,5.5"
		self.binnings_dict["ee_njets"] = "10,0.0,10.0"
		self.binnings_dict["ee_npu"] = "30,0.0,60.0"
		self.binnings_dict["ee_npv"] = "30,0.0,60.0"
		self.binnings_dict["ee_phi_1"] = "32,-3.2,3.2"
		self.binnings_dict["ee_phi_2"] = "32,-3.2,3.2"
		self.binnings_dict["ee_phi_ll"] = "32,-3.2,3.2"
		self.binnings_dict["ee_phi_llmet"] = "32,-3.2,3.2"
		self.binnings_dict["ee_phi_sv"] = "32,-3.2,3.2"
		self.binnings_dict["ee_pt_1"] = "25,0.0,250.0"
		self.binnings_dict["ee_pt_2"] = "25,0.0,250.0"
		self.binnings_dict["ee_pt_ll"] = "25,0.0,250"
		self.binnings_dict["ee_pt_llmet"] = "25,0.0,250"
		self.binnings_dict["ee_pt_sv"] = "25,0.0,250"
		self.binnings_dict["ee_pt_tt"] = "20,0.0,200"
		self.binnings_dict["ee_puweight"] = "20,0.0,2.0"
		self.binnings_dict["ee_rho"] = "25,0.0,50.0"
		self.binnings_dict["ee_svfitMass"] = "25,0.0,250"
		self.binnings_dict["ee_trigweight_1"] = "20,0.5,1.5"
		self.binnings_dict["ee_trigweight_2"] = "20,0.5,1.5"

