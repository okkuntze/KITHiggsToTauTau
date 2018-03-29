#!/usr/bin/env python

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import HiggsAnalysis.KITHiggsToTauTau.plotting.higgsplot as higgsplot

import HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plot_classes as pltcl
from HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plotline_bib import *
def embedding_stitchingweight(channel):

	if channel=='mt':
		comp_eff_B="(1.0/0.899)"
		comp_eff_C="(1.0/0.881)"
		comp_eff_D="(1.0/0.877)"
		comp_eff_E="(1.0/0.939)"
		comp_eff_F="(1.0/0.936)"
		comp_eff_G="(1.0/0.908)"
		comp_eff_H="(1.0/0.962)"
		runB = "((run >= 272007) && (run < 275657))*"+comp_eff_B
		runC = "+((run >= 275657) && (run < 276315))*"+comp_eff_C
		runD = "+((run >= 276315) && (run < 276831))*"+comp_eff_D
		runE = "+((run >= 276831) && (run < 277772))*"+comp_eff_E
		runF = "+((run >= 277772) && (run < 278820))*"+comp_eff_F
		runG = "+((run >= 278820) && (run < 280919))*"+comp_eff_G
		runH = "+((run >= 280919) && (run < 284045))*"+comp_eff_H
		return "("+runB+runC+runD+runE+runF+runG+runH+")"
	elif channel=='et':
		comp_eff_B="(1.0/0.902)"
		comp_eff_C="(1.0/0.910)"
		comp_eff_D="(1.0/0.945)"
		comp_eff_E="(1.0/0.945)"
		comp_eff_F="(1.0/0.915)"
		comp_eff_G="(1.0/0.903)"
		comp_eff_H="(1.0/0.933)"
		runB = "((run >= 272007) && (run < 275657))*"+comp_eff_B
		runC = "+((run >= 275657) && (run < 276315))*"+comp_eff_C
		runD = "+((run >= 276315) && (run < 276831))*"+comp_eff_D
		runE = "+((run >= 276831) && (run < 277772))*"+comp_eff_E
		runF = "+((run >= 277772) && (run < 278820))*"+comp_eff_F
		runG = "+((run >= 278820) && (run < 280919))*"+comp_eff_G
		runH = "+((run >= 280919) && (run < 284045))*"+comp_eff_H
		return "("+runB+runC+runD+runE+runF+runG+runH+")"
	elif channel=='tt':
		comp_eff_B="(1.0/0.897)"
		comp_eff_C="(1.0/0.908)"
		comp_eff_D="(1.0/0.950)"
		comp_eff_E="(1.0/0.861)"
		comp_eff_F="(1.0/0.941)"
		comp_eff_G="(1.0/0.908)"
		comp_eff_H="(1.0/0.949)"
		runB = "((run >= 272007) && (run < 275657))*"+comp_eff_B
		runC = "+((run >= 275657) && (run < 276315))*"+comp_eff_C
		runD = "+((run >= 276315) && (run < 276831))*"+comp_eff_D
		runE = "+((run >= 276831) && (run < 277772))*"+comp_eff_E
		runF = "+((run >= 277772) && (run < 278820))*"+comp_eff_F
		runG = "+((run >= 278820) && (run < 280919))*"+comp_eff_G
		runH = "+((run >= 280919) && (run < 284045))*"+comp_eff_H
		return "("+runB+runC+runD+runE+runF+runG+runH+")"
	elif channel=='em':
		comp_eff_B="(1.0/0.891)"
		comp_eff_C="(1.0/0.910)"
		comp_eff_D="(1.0/0.953)"
		comp_eff_E="(1.0/0.947)"
		comp_eff_F="(1.0/0.942)"
		comp_eff_G="(1.0/0.906)"
		comp_eff_H="(1.0/0.950)"
		runB = "((run >= 272007) && (run < 275657))*"+comp_eff_B
		runC = "+((run >= 275657) && (run < 276315))*"+comp_eff_C
		runD = "+((run >= 276315) && (run < 276831))*"+comp_eff_D
		runE = "+((run >= 276831) && (run < 277772))*"+comp_eff_E
		runF = "+((run >= 277772) && (run < 278820))*"+comp_eff_F
		runG = "+((run >= 278820) && (run < 280919))*"+comp_eff_G
		runH = "+((run >= 280919) && (run < 284045))*"+comp_eff_H
		return "("+runB+runC+runD+runE+runF+runG+runH+")"
	else:
		log.error("Embedding currently not implemented for channel \"%s\"!" % channel)			
def plot_root_variable(channel=['mt'],variable='pt_1',x_bins = "30,0,120",xlabel=''):
	
	stitching_weight = "(((genbosonmass >= 150.0 && (npartons == 0 || npartons >= 5))*1.25449124172134e-6) + ((genbosonmass >= 150.0 && npartons == 1)*1.17272893569016e-6) + ((genbosonmass >= 150.0 && npartons == 2)*1.17926755938344e-6) + ((genbosonmass >= 150.0 && npartons == 3)*1.18242445124698e-6) + ((genbosonmass >= 150.0 && npartons == 4)*1.16077776187804e-6)+((genbosonmass >= 50.0 && genbosonmass < 150.0 && (npartons == 0 || npartons >= 5))*1.15592e-4) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 1)*1.5569730365e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 2)*1.68069486078868e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 3)*1.74717616341537e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 4)*1.3697397756176e-5)+((genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight))/(numberGeneratedEventsWeight*crossSectionPerEventWeight*sampleStitchingWeight)*"

	selection_weight_mt = "(pt_1>23)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*((q_1*q_2)<0.0)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)"#*(trg_singlemuon==1)"

	selection_weight_et = "(pt_1>26)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(againstMuonLoose3_2 > 0.5)*(dilepton_veto < 0.5)*(againstElectronTightMVA6_2 > 0.5)*(mt_1<40.0)*(iso_1 < 0.1)*((q_1*q_2)<0.0)"

	selection_weight_tt = "(pt_1 > 42.0 && pt_2 > 42.0)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(againstMuonLoose3_1 > 0.5)*(againstMuonLoose3_2 > 0.5)*(againstElectronVLooseMVA6_1 > 0.5)*(againstElectronVLooseMVA6_2 > 0.5)*((q_1*q_2)<0.0)*(trg_doubletau==1)"

	selection_weight_em = "(pt_1 > 24.0 && pt_2 > 24.0)*(pZetaMissVis > -20.0)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(iso_1 < 0.15)*(iso_2 < 0.2)*((q_1*q_2)<0.0)"
	selection_weight_em = "(pt_1 > 24.0 && pt_2 > 24.0)*(pZetaMissVis > -20.0)*(iso_1 < 0.15)*(iso_2 < 0.2)*((q_1*q_2)<0.0)"

	genmatching_weight_xt = "(gen_match_2 == 5)"
	genmatching_weight_tt = "(gen_match_1 == 5 && gen_match_2 == 5)"
	genmatching_weight_em = "(gen_match_1 > 2 && gen_match_2 > 3)"
	
	visibleMassMuTau = pltcl.single_plot(
		name = variable,
		title = "#mu#tau_{h}",
		x_expression = variable,
		normalized_to_hist1 = True,
		x_bins = x_bins,
		#~ normalized_by_binwidth = True,
		x_label = xlabel,
		weight = ["generatorWeight*(generatorWeight<=1)","generatorWeight*(generatorWeight<=1)"],

		y_label = "Events",
		#y_lims = [0,0.058],
		plot_type = "absolute",
		legend = [0.53,0.44,0.92,0.88],
		subplot_denominator = 0,
		subplot_numerators = [1],
		output_dir=output_dir+'/mt/',
		y_subplot_lims = [0.6,1.4],
		y_subplot_label = "Ratio",
		print_infos = True,
		y_log=False,
		plotlines = [EmbeddingMuTauFileNominal,  EmbeddingMuTauFileNominal2017]
	)
	if 'mt' in channel:
		configs.extend(visibleMassMuTau.return_json_with_changed_x_and_weight(x_expressions = [variable]))
	if variable=='pt_1':
		xlabel='Electron p_{T} / GeV'
	visibleMassElTau = visibleMassMuTau.clone(
		name = variable,
		x_label = xlabel,
		output_dir=output_dir+'/et/',
		horizontal_subplot_lines=[1.0,3,5,7,9],
		title = "e#tau_{h}",
		weight = [selection_weight_et+"*"+genmatching_weight_xt + "*idisoweight_1*(idisoweight_1<1.1)*triggerWeight_1*(triggerWeight_1<1.1)*generatorWeight*(generatorWeight<=1)",selection_weight_et+"*"+genmatching_weight_xt + "*generatorWeight*(generatorWeight<=1)"],
		plotlines = [EmbeddingElTauFileNominal,  EmbeddingElTauFileNominal]
	)
	if 'et' in channel:
		configs.extend(visibleMassElTau.return_json_with_changed_x_and_weight(x_expressions = [variable]))

	visibleMassTauTau = visibleMassMuTau.clone(
		name = variable,
		title = "#tau_{h}#tau_{h}",
		x_bins = x_bins,
		output_dir=output_dir+'/tt/',
		normalized_by_binwidth = True,
		weight = [selection_weight_tt+"*"+genmatching_weight_tt + "*2.2*generatorWeight*(generatorWeight<=1)",selection_weight_tt+"*"+stitching_weight+genmatching_weight_tt+"*eventWeight"],
		plotlines = [EmbeddingTauTauFileNominal, EmbeddingTauTauFileNominal]
	)
	if 'tt' in channel:
		configs.extend(visibleMassTauTau.return_json_with_changed_x_and_weight(x_expressions = [variable]))

	visibleMassElMu = visibleMassMuTau.clone(
		name = "visibleMassElMu",
		title = "e#mu",
		subplot_denominator = 0,
		normalized_by_binwidth = True,
		weight = [ genmatching_weight_xt + "*generatorWeight*(generatorWeight<=1)",stitching_weight + genmatching_weight_xt + "*generatorWeight*(generatorWeight<=1)"],
		plotlines = [EmbeddingElMuFileNominal,DYFileElMuFile]
	)

	#configs.extend(visibleMassElMu.return_json_with_changed_x_and_weight(x_expressions = ["m_vis"]))

def default_plot_root_variable(channel=['mt'],variable='pt_1'):
	
	stitching_weight = "(((genbosonmass >= 150.0 && (npartons == 0 || npartons >= 5))*1.25449124172134e-6) + ((genbosonmass >= 150.0 && npartons == 1)*1.17272893569016e-6) + ((genbosonmass >= 150.0 && npartons == 2)*1.17926755938344e-6) + ((genbosonmass >= 150.0 && npartons == 3)*1.18242445124698e-6) + ((genbosonmass >= 150.0 && npartons == 4)*1.16077776187804e-6)+((genbosonmass >= 50.0 && genbosonmass < 150.0 && (npartons == 0 || npartons >= 5))*1.15592e-4) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 1)*1.5569730365e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 2)*1.68069486078868e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 3)*1.74717616341537e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 4)*1.3697397756176e-5)+((genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight))/(numberGeneratedEventsWeight*crossSectionPerEventWeight*sampleStitchingWeight)*"
	#(againstMuonTight3_2 > 0.5)*(againstElectronVLooseMVA6_2 > 0.5)*
	#~ stitching_weight = "(1.0)"
	#(againstMuonTight3_2 > 0.5)*(againstElectronVLooseMVA6_2 > 0.5)*
	selection_weight_mt = "(pt_1>23)*(pt_2>30)*(mt_1<70.0)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*((q_1*q_2)<0.0)*(trg_singlemuon==1)"

	selection_weight_et = "(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(againstMuonLoose3_2 > 0.5)*(dilepton_veto < 0.5)*(againstElectronTightMVA6_2 > 0.5)*(mt_1<40.0)*(iso_1 < 0.1)*((q_1*q_2)<0.0)"

	selection_weight_tt = "(pt_1 > 42.0 && pt_2 > 42.0)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(againstMuonLoose3_1 > 0.5)*(againstMuonLoose3_2 > 0.5)*(againstElectronVLooseMVA6_1 > 0.5)*(againstElectronVLooseMVA6_2 > 0.5)*((q_1*q_2)<0.0)*(trg_doubletau==1)"

	#selection_weight_em = "(pt_1 > 24.0 && pt_2 > 24.0)*(pZetaMissVis > -20.0)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(iso_1 < 0.15)*(iso_2 < 0.2)*((q_1*q_2)<0.0)"
	selection_weight_em = "(pt_1 > 24.0 && pt_2 > 24.0)*(pZetaMissVis > -20.0)*(iso_1 < 0.15)*(iso_2 < 0.2)*((q_1*q_2)<0.0)"

	genmatching_weight_xt = "(gen_match_2 == 5)"
	genmatching_weight_tt = "(gen_match_1 == 5 && gen_match_2 == 5)"
	genmatching_weight_em = "(gen_match_1 > 2 && gen_match_2 > 3)"
	
	visibleMassMuTau = pltcl.single_plot(
		name = variable+"MuTau",
		title = "#mu#tau_{h}",
		x_expression = variable,
		#~ normalized_to_hist1 = True,
		#~ x_bins = x_bins,
	#	x_bins = "1,0,13000",
		normalized_by_binwidth = True,
	#	normalized_by_binwidth = False,
		#~ x_label = xlabel,
		weight = [selection_weight_mt+"*"+genmatching_weight_xt + "*generatorWeight*(generatorWeight<=1)",selection_weight_mt+"*"+stitching_weight + genmatching_weight_xt + "*eventWeight",selection_weight_mt+"*((gen_match_1==4)&&(gen_match_2==5))*eventWeight"],
		y_label = "Events per bin width",
		#y_lims = [0,0.058],
		plot_type = "absolute",
		legend = [0.53,0.44,0.92,0.88],
		subplot_denominator = 0,
		stacked=True,
		subplot_numerators = [1,2],
		output_dir=output_dir+'/mt/',
		wwwfolder = None,
		y_subplot_lims = [0.5,1.5],
		y_subplot_label = "Ratio",
		print_infos = True,
		plotlines = [EmbeddingMuTauFileNominal,  DYFileMuTauFile]
	)
	if 'mt' in channel:
		configs.extend(visibleMassMuTau.return_json_with_changed_x_and_weight(x_expressions = [variable]))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Make embedding plots.",
									 parents=[logger.loggingParser])

	parser.add_argument("-i", "--input-dir", required=False, default = ".",
						help="Input directory [Default: %(default)s]")
	parser.add_argument("-o", "--output-dir", required=False, default = "plots",
						help="Output directory [Default: %(default)s]")
	parser.add_argument("-c","--channel", required=False, default = ['mt','et'], nargs="*", help="Select decay channel. [Default: %(default)s]")
	parser.add_argument("-n","--n-processes",required=False, default=1, help="Number of parallel processes. [Default: %(default)s]")
	parser.add_argument("-x","--quantities", required=False, default = None, nargs="*", help="Select quantities to plot. [Default: %(default)s]")
	parser.add_argument("--default", required=False, action="store_true", default=False, help = "Set to let HiggsPlotter take care of binning and skip custom configs.")

	args = parser.parse_args()
	logger.initLogger(args)
	configs = []
	output_dir = args.output_dir
	input_dir = args.input_dir

	default_variables=[
			"integral",
			"pt_1", "eta_1", "phi_1", "m_1", "iso_1", "mt_1",
			"pt_2", "eta_2", "phi_2", "m_2", "iso_2", "mt_2",
			"pt_sv", "eta_sv", "phi_sv", "m_sv", "m_vis", "ptvis",
			"met", "metphi", "metcov00", "metcov01", "metcov10", "metcov11",
			"mvamet", "mvametphi", "mvacov00", "mvacov01", "mvacov10", "mvacov11",
			"pZetaMissVis", "pzetamiss", "pzetavis",
			"jpt_1", "jeta_1", "jphi_1", "m_sv",
			"jpt_2", "jeta_2", "jphi_2",
			"njetspt30", "mjj", "jdeta", "njetingap20", "njetingap",
			"trigweight_1", "trigweight_2", "puweight",
			"npv", "npu", "rho","nbtag",'genMatchedLep1LV.fCoordinates.fPt','genMatchedLep2LV.fCoordinates.fPt','genMatchedLep2LV.fCoordinates.fEta','genMatchedLep1LV.fCoordinates.fEta','genMatchedLep2LV.fCoordinates.fPhi','genMatchedLep1LV.fCoordinates.fPhi','triggerWeight_1','identificationWeight_1','jcsv_1','jcsv_2','jm_1','jmva_1','bpt_1','beta_1','beta_2','bphi_1', 'bphi_2', 'bcsv_1', 'bcsv_2', 'njets', 'nbtag', 'mt_1', 'ptvis', 'pt_tt', 'mjj', 'jdeta', 'm_vis', 'dijetphi', 'dijetpt', 'met', 'd0_1','bpt_1', 'bpt_2', 'beta_1','beta_2', 'bphi_1', 'bphi_2', 'bcsv_1', 'bcsv_2']
	for x in args.quantities:
		if x not in default_variables:
			default_variables.append(x)
	selection_variables=['trigweight_1','extraelec_veto','extramuon_vet','againstMuonLoose3_1','againstMuonLoose3_2','trg_doubletau','againstElectronVLooseMVA6_1','againstElectronVLooseMVA6_2','byMediumIsolationMVArun2v1DBoldDMwLT_2','byMediumIsolationMVArun2v1DBoldDMwLT_1']
	iso_variables = [
	"againstElectronLooseMVA6_1",
		"againstElectronLooseMVA6_2",

		"iso_1",
		"iso_2",
		"decayDistX_1",
		"decayDistX_2",
		"decayDistY_1",
		"decayDistY_2",
		"decayDistZ_1",
		"decayDistZ_2",
		"decayDistM_1",
		"decayDistM_2",
		"nPhoton_1",
		"nPhoton_2",
		"ptWeightedDetaStrip_1",
		"ptWeightedDetaStrip_2",
		"ptWeightedDphiStrip_1",
		"ptWeightedDphiStrip_2",
		"ptWeightedDrSignal_1",
		"ptWeightedDrSignal_2",
		"ptWeightedDrIsolation_1",
		"ptWeightedDrIsolation_2",
		"leadingTrackChi2_1",
		"leadingTrackChi2_2",
		"eRatio_1",
		"eRatio_2",
		"MVAdxy_sign_1",
		"MVAdxy_sign_2",
		"MVAdxy_abs_1",	 
		"MVAdxy_abs_2",
		"MVAdxy_signal_1",
		"MVAdxy_signal_2",
		"MVAdxy_ip3d_sign_1",
		"MVAdxy_ip3d_sign_2",
		"MVAdxy_ip3d_abs_1",
		"MVAdxy_ip3d_abs_2",
		"MVAdxy_ip3d_signal_1",
		"MVAdxy_ip3d_signal_2",
		"hasSecondaryVertex_1",
		"hasSecondaryVertex_2",
		"flightLengthSig_1",
		"flightLengthSig_2","byCombinedIsolationDeltaBetaCorrRaw3Hits_2","byCombinedIsolationDeltaBetaCorrRaw3Hits_2","photonPtSumOutsideSignalCone_2","chargedIsoPtSum_2","neutralIsoPtSum_2","footprintCorrection_2","puCorrPtSum_2"]
	for channel in args.channel:
		
		tau_iso_variables = [x for x in iso_variables if x[-2:]=="_2"]
		plotting_dict={}
		#~ for v in default_variables:
		for v in default_variables+selection_variables:
			plotting_dict.setdefault(v,[])
			plotting_dict[v]={}
			plotting_dict[v].setdefault("x_label",channel+'_'+v)
			plotting_dict[v].setdefault("x_bins",channel+'_'+v)
			plotting_dict.setdefault(v,[])
			plotting_dict[v]={}
			plotting_dict[v].setdefault("x_label",v)
			if 'eta' in v or 'Eta' in v:
				plotting_dict[v].setdefault("x_bins","25,-2.5,2.5")
			if 'phi' in v or 'Phi' in v:
				plotting_dict[v].setdefault("x_bins","30,-3.2,3.2")
			if 'njet' in v:
				plotting_dict[v].setdefault("x_bins","7,0,7")	
			if 'Weight' in v or 'weight' in v:
				plotting_dict[v].setdefault("x_bins","24,0,1.2")
			if 'trg' in v or 'weight' in v:
				plotting_dict[v].setdefault("x_bins","3,0,3")
			
			plotting_dict[v].setdefault("x_bins","20,0,20")
		plotting_dict['genMatchedLep1LV.fCoordinates.fPt']["x_bins"]="50,0,100"

		plotting_dict["integral"]["x_bins"]="1,0,1"
		plotting_dict["m_1"]["x_bins"]="10,0,0.5"
		plotting_dict["m_1"]["x_label"]="Muon Mass / GeV"
		plotting_dict["m_2"]["x_bins"]="30,0,1.5"
		plotting_dict["mt_1"]["x_bins"]="25,0,50"
		plotting_dict["m_vis"]["x_bins"]="25,20,120"
		plotting_dict["npu"]["x_bins"]="30,0,60"
		plotting_dict["npv"]["x_bins"]="30,0,60"
		plotting_dict["npv"]["x_bins"]="30,0,60"
		plotting_dict["iso_1"]["x_bins"]="25,0.,1."
		plotting_dict["nbtag"]["x_bins"]="5,0,5"

		plotting_dict["m_2"]["x_label"]="Tau Mass / GeV"
		plotting_dict["mt_1"]["x_label"]="m_{T} / GeV"
		plotting_dict["m_vis"]["x_label"]="m_{vis} / GeV"
		plotting_dict["npu"]["x_label"]="Number Pileup"
		plotting_dict["npv"]["x_label"]="NPV"
		plotting_dict["iso_1"]["x_label"]="Muon Isolation"
		plotting_dict["nbtag"]["x_label"]="Number of b-tags"
		plotting_dict["njetspt30"]["x_label"]="Number of Jets (p_{T} 30)"
		plotting_dict["pt_1"]["x_label"]="Muon p_{T} / GeV"
		plotting_dict["pt_2"]["x_label"]="Tau p_{T} / GeV"

		for v in iso_variables:
			plotting_dict.setdefault(v,[])
			plotting_dict[v]={}
			plotting_dict[v].setdefault("x_label",v)
			if "sign_" in v:
				plotting_dict[v].setdefault("x_bins","15,-1.5,1.5")
			elif "ptWeightedD" in v:
				plotting_dict[v].setdefault("x_bins","30,0,0.6")
			else:
				plotting_dict[v].setdefault("x_bins","20,0,10")
		plotting_dict["decayDistX_2"]["x_bins"]="20,-2,2"
		plotting_dict["decayDistY_2"]["x_bins"]="20,-2,2"
		plotting_dict["decayDistZ_2"]["x_bins"]="20,-2,2"
		plotting_dict["MVAdxy_abs_2"]["x_bins"]="30,0,0.3"
		plotting_dict["eRatio_2"]["x_bins"]="20,0,2"
		plotting_dict["hasSecondaryVertex_2"]["x_bins"]="10,-0.5,1.5"
		#plotting_dict["MVAdxy_abs_2"]["x_bins"]="30,0,0.3"
		#plotting_dict["MVAdxy_abs_2"]["x_bins"]="30,0,0.3"
		plotting_dict["againstElectronLooseMVA6_2"]["x_bins"]="2,-0.5,1.5"
		plotting_dict["MVAdxy_ip3d_abs_2"]["x_bins"]="30,0,0.3"
		plotting_dict["decayDistM_2"]["x_bins"]="15,0,3"
		plotting_dict["byCombinedIsolationDeltaBetaCorrRaw3Hits_2"]["x_bins"]="20,0,10"
		plotting_dict["photonPtSumOutsideSignalCone_2"]["x_bins"]="20,0,10"
		plotting_dict["chargedIsoPtSum_2"]["x_bins"]="20,0,1"
		plotting_dict["neutralIsoPtSum_2"]["x_bins"]="20,0,20"
		plotting_dict["footprintCorrection_2"]["x_bins"]="25,0,25"
		plotting_dict["puCorrPtSum_2"]["x_bins"]="20,0,80"
		plotting_dict["decayDistM_2"]["x_bins"]="20,0,1"
		plotting_dict["flightLengthSig_2"]["x_bins"]="24,-6,6"
		
		
		selection_variables=['trigweight_1','trigweight_2','extraelec_veto','extramuon_vet','againstMuonLoose3_1','againstMuonLoose3_2','trg_doubletau','againstElectronVLooseMVA6_1','againstElectronVLooseMVA6_2','byMediumIsolationMVArun2v1DBoldDMwLT_2','byMediumIsolationMVArun2v1DBoldDMwLT_1','iso_1','iso_2']
		#~ selection_variables=['extraelec_veto','idisoweight_1','trg_weight_1','extramuon_veto','againstMuonTight3_2','dilepton_veto','trg_singlemuon','againstElectronVLooseMVA6_2','byTightIsolationMVArun2v1DBoldDMwLT_2','iso_1','iso_2','zPtReweightWeight']
		'''
		plotting_dict={}

		for v in selection_variables:
			plotting_dict.setdefault(v,[])
			plotting_dict[v]={}
			plotting_dict[v].setdefault("x_label",v)
			plotting_dict[v].setdefault("x_bins","3,0,2")
			if "weight" in v or "solation" in v or "iso" in v:
				plotting_dict[v]["x_bins"]="60,0.9,1.2"
		plotting_dict["trigweight_1"]["x_bins"]="50,0.8,1.3"
		plotting_dict["trigweight_2"]["x_bins"]="50,0.8,1.3"
		'''
		#~ plotting_dict["iso_2"]["x_bins"]="50,0.5,1"

		#~ variables_to_plot = ["pt_1"]
		#variables_to_plot = tau_iso_variables
		#variables_to_plot = ["MVAdxy_abs_2","MVAdxy_ip3d_abs_2"]

	#	variables_to_plot=["flightLengthSig_2"]
		variables_to_plot=selection_variables
		if args.quantities is not None:
			variables_to_plot=args.quantities
		for v in variables_to_plot:
			if not args.default:						
				plot_root_variable(variable=v,xlabel=plotting_dict[v]["x_label"],x_bins=plotting_dict[v]["x_bins"],channel=args.channel)
			else:
				default_plot_root_variable(variable=v)
		print "Plotting..."
		higgs_plotter = higgsplot.HiggsPlotter(list_of_config_dicts=configs, list_of_args_strings=[""],n_processes=args.n_processes)
