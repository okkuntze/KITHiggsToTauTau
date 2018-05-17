#!/usr/bin/env python

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import json
import HiggsAnalysis.KITHiggsToTauTau.plotting.higgsplot as higgsplot

import HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plot_classes as pltcl
from HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plotline_bib import *


def embedding_stitchingweight(channel):

    if channel == 'mt':
        comp_eff_B = "(1.0/0.899)"
        comp_eff_C = "(1.0/0.881)"
        comp_eff_D = "(1.0/0.877)"
        comp_eff_E = "(1.0/0.939)"
        comp_eff_F = "(1.0/0.936)"
        comp_eff_G = "(1.0/0.908)"
        comp_eff_H = "(1.0/0.962)"
        runB = "((run >= 272007) && (run < 275657))*" + comp_eff_B
        runC = "+((run >= 275657) && (run < 276315))*" + comp_eff_C
        runD = "+((run >= 276315) && (run < 276831))*" + comp_eff_D
        runE = "+((run >= 276831) && (run < 277772))*" + comp_eff_E
        runF = "+((run >= 277772) && (run < 278820))*" + comp_eff_F
        runG = "+((run >= 278820) && (run < 280919))*" + comp_eff_G
        runH = "+((run >= 280919) && (run < 284045))*" + comp_eff_H
        return "(" + runB + runC + runD + runE + runF + runG + runH + ")"
    elif channel == 'et':
        comp_eff_B = "(1.0/0.902)"
        comp_eff_C = "(1.0/0.910)"
        comp_eff_D = "(1.0/0.945)"
        comp_eff_E = "(1.0/0.945)"
        comp_eff_F = "(1.0/0.915)"
        comp_eff_G = "(1.0/0.903)"
        comp_eff_H = "(1.0/0.933)"
        runB = "((run >= 272007) && (run < 275657))*" + comp_eff_B
        runC = "+((run >= 275657) && (run < 276315))*" + comp_eff_C
        runD = "+((run >= 276315) && (run < 276831))*" + comp_eff_D
        runE = "+((run >= 276831) && (run < 277772))*" + comp_eff_E
        runF = "+((run >= 277772) && (run < 278820))*" + comp_eff_F
        runG = "+((run >= 278820) && (run < 280919))*" + comp_eff_G
        runH = "+((run >= 280919) && (run < 284045))*" + comp_eff_H
        return "(" + runB + runC + runD + runE + runF + runG + runH + ")"
    elif channel == 'tt':
        comp_eff_B = "(1.0/0.897)"
        comp_eff_C = "(1.0/0.908)"
        comp_eff_D = "(1.0/0.950)"
        comp_eff_E = "(1.0/0.861)"
        comp_eff_F = "(1.0/0.941)"
        comp_eff_G = "(1.0/0.908)"
        comp_eff_H = "(1.0/0.949)"
        runB = "((run >= 272007) && (run < 275657))*" + comp_eff_B
        runC = "+((run >= 275657) && (run < 276315))*" + comp_eff_C
        runD = "+((run >= 276315) && (run < 276831))*" + comp_eff_D
        runE = "+((run >= 276831) && (run < 277772))*" + comp_eff_E
        runF = "+((run >= 277772) && (run < 278820))*" + comp_eff_F
        runG = "+((run >= 278820) && (run < 280919))*" + comp_eff_G
        runH = "+((run >= 280919) && (run < 284045))*" + comp_eff_H
        return "(" + runB + runC + runD + runE + runF + runG + runH + ")"
    elif channel == 'em':
        comp_eff_B = "(1.0/0.891)"
        comp_eff_C = "(1.0/0.910)"
        comp_eff_D = "(1.0/0.953)"
        comp_eff_E = "(1.0/0.947)"
        comp_eff_F = "(1.0/0.942)"
        comp_eff_G = "(1.0/0.906)"
        comp_eff_H = "(1.0/0.950)"
        runB = "((run >= 272007) && (run < 275657))*" + comp_eff_B
        runC = "+((run >= 275657) && (run < 276315))*" + comp_eff_C
        runD = "+((run >= 276315) && (run < 276831))*" + comp_eff_D
        runE = "+((run >= 276831) && (run < 277772))*" + comp_eff_E
        runF = "+((run >= 277772) && (run < 278820))*" + comp_eff_F
        runG = "+((run >= 278820) && (run < 280919))*" + comp_eff_G
        runH = "+((run >= 280919) && (run < 284045))*" + comp_eff_H
        return "(" + runB + runC + runD + runE + runF + runG + runH + ")"
    else:
        log.error("Embedding currently not implemented for channel \"%s\"!" %
                  channel)


def plot_root_variable(channel=['mt'],
                       variable='pt_1',
                       x_bins="30,0,120",
                       xlabel='',
                       legend=1):
    #2016 Configs
    #selection_weight_mt = "(pt_1>23)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*((q_1*q_2)<0.0)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)"#*(trg_singlemuon==1)"
    #stitching_weight = "(((genbosonmass >= 150.0 && (npartons == 0 || npartons >= 5))*1.25449124172134e-6) + ((genbosonmass >= 150.0 && npartons == 1)*1.17272893569016e-6) + ((genbosonmass >= 150.0 && npartons == 2)*1.17926755938344e-6) + ((genbosonmass >= 150.0 && npartons == 3)*1.18242445124698e-6) + ((genbosonmass >= 150.0 && npartons == 4)*1.16077776187804e-6)+((genbosonmass >= 50.0 && genbosonmass < 150.0 && (npartons == 0 || npartons >= 5))*1.15592e-4) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 1)*1.5569730365e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 2)*1.68069486078868e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 3)*1.74717616341537e-5) + ((genbosonmass >= 50.0 && genbosonmass < 150.0 && npartons == 4)*1.3697397756176e-5)+((genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight))/(numberGeneratedEventsWeight*crossSectionPerEventWeight*sampleStitchingWeight)*"
    selection_weight_et = "(pt_1>26)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(againstMuonLoose3_2 > 0.5)*(dilepton_veto < 0.5)*(againstElectronTightMVA6_2 > 0.5)*(mt_1<40.0)*(iso_1 < 0.1)*((q_1*q_2)<0.0)"
    selection_weight_tt = "(pt_1 > 42.0 && pt_2 > 42.0)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(againstMuonLoose3_1 > 0.5)*(againstMuonLoose3_2 > 0.5)*(againstElectronVLooseMVA6_1 > 0.5)*(againstElectronVLooseMVA6_2 > 0.5)*((q_1*q_2)<0.0)*(trg_doubletau==1)"
    selection_weight_em = "(pt_1 > 24.0 && pt_2 > 24.0)*(pZetaMissVis > -20.0)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(iso_1 < 0.15)*(iso_2 < 0.2)*((q_1*q_2)<0.0)"
    selection_weight_em = "(pt_1 > 24.0 && pt_2 > 24.0)*(pZetaMissVis > -20.0)*(iso_1 < 0.15)*(iso_2 < 0.2)*((q_1*q_2)<0.0)"
    genmatching_weight_xt = "(gen_match_2 == 5)"
    genmatching_weight_tt = "(gen_match_1 == 5 && gen_match_2 == 5)"
    genmatching_weight_em = "(gen_match_1 > 2 && gen_match_2 > 3)"
    selection_weight_mt = "(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonTight3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(iso_1<0.15)*(q_1*q_2<0)*(mt_1<50)*(pt_1>30 && pt_2>30)"
    selection_weight_16_mt = "(pt_1>23)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*((q_1*q_2)<0.0)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)"  #*(trg_singlemuon==1)"
    generator_weight_16_mt = "idWeight_1*(idWeight_1<2.0)*trgWeight_1*(trgWeight_1<2.0)*isoWeight_1*(isoWeight_1<2.0)*muonEffEmbeddedIDWeight_1*muonEffEmbeddedIDWeight_2*muonEffVVLIsoWeight_1*muonEffVVLIsoWeight_2*(((eta_1<=1.2)*(eta_1>=-1.2))*1.128668+((eta_1>1.2)||(eta_1<-1.2))*1.199)"

    #2017 Configs
    stitching_weight = "(((genbosonmass >= 50.0 && (npartons == 0 || npartons >= 4))*5.75970078e-5) + ((genbosonmass >= 50.0 && npartons == 1)*1.36277241e-5) + ((genbosonmass >= 50.0 && npartons == 2)*7.42888435e-6) + ((genbosonmass >= 50.0 && npartons == 3)*1.62808443e-5) + ((genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight))"
    selection_weight_mt = "(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)"
    genmatching_weight_mt = "(gen_match_2==5)*((gen_match_2 == 5)*0.95 + (gen_match_2 != 5))"
    generator_weight_mt = "generatorWeight*(generatorWeight<=1.0)*idisoweight_1*muonEffEmbeddedIDWeight_1*muonEffEmbeddedIDWeight_2*muonEffTrgWeight_1*muonEffVVLIsoWeight_1*muonEffVVLIsoWeight_2*triggerweight_1"
    ttbar_weight_mt = "generatorWeight*(generatorWeight<=1.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight*0.5*topPtReweightWeight*((gen_match_2 == 5)*0.95 + (gen_match_2 != 5))*puweight"
    stitching_weight_fall_17 = "(((genbosonmass >= 50.0 && (npartons == 0 || npartons >= 4))*2.455936181) + ((genbosonmass >= 50.0 && npartons == 1)*0.5608870881) + ((genbosonmass >= 50.0 && npartons == 2)*0.5745263806) + ((genbosonmass >= 50.0 && npartons == 3)*0.617450628))"
    ## Define Legend Positions
    if legend == 1: #top right
        legend_pos = [0.55, 0.62, 0.93, 0.82]
    elif legend == 2: #top left
        legend_pos = [0.20, 0.62, 0.58, 0.82]
    elif legend == 3: #bottom middle
        legend_pos = [0.34, 0.08, 0.74, 0.28]
    elif legend == 4: #top middle
        legend_pos = [0.34, 0.64, 0.74, 0.84]
    
    default = pltcl.single_plot(
        x_expression=variable,
        normalized_by_binwidth = True,
        x_bins=x_bins,
        x_label=xlabel,
        y_label="Events per binwidth",
        plot_type="absolute",
        legend = legend_pos,
        horizontal_subplot_lines=[0.8, 1, 1.2],
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label="Ratio",
        print_infos=True,
        y_log=False
    )
    visibleMassMuTau = default.clone(
        name="mt",
        title="#mu#tau_{h}",
        normalized_to_hist1=False,
        weight=["(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
                #"(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
                #"(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
                "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1 == 4)*generatorWeight*muonEffTrgWeight",
                "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)"],
	    subplot_denominator=0,
        #subplot_numerators=[0, 1, 2, 3],
        subplot_numerators=[0,1],
        output_dir=output_dir + '/mt/',
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label=
        "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
        plotlines=[DYFileWinter17_mt, 
        #DYFileWinter17_mt_shift_up, 
        #DYFileWinter17_mt_shift_down, 
        DYFileWinter17_emb_mt,
        DYFileWinter17_mt_copy])

    visibleMassFall17_with_tt = default.clone(
        normalized_to_hist1=False,
	    subplot_denominator=1,
        subplot_numerators=[2],
        y_label="Events per binwidth",
        y_subplot_lims=[0.6, 1.4],
        add_nicks=[0,1],
        add_result_nicks=1,
        add_scale_factors=[1,1],
        y_subplot_label=
        "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}"
    )
    visibleMassMuTau_Fall17_with_tt = visibleMassFall17_with_tt.clone(
        name="mt",
        title="#mu#tau_{h}",
        weight=[
                stitching_weight_fall_17 + "*(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)*(gen_match_2==5)*(idisoweight_1*triggerweight_1)",

                "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)*(gen_match_2 == 5)*(gen_match_1 == 4)*topPtReweightWeight*puweight",

                "(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)*(gen_match_2==5)*generatorWeight*muonEffTrgWeight*(idweight_1*triggerweight_1*isoweight_1)"
                ],
        output_dir=output_dir + '/mt_fall17_with_tt/',
        plotlines=[DYFall17_mt, TTFall17_mt, Embedding17_mt])

    visibleMassMuTau_Fall17 = default.clone(
        name="mt",
        title="#mu#tau_{h}",
        normalized_to_hist1=False,
        weight=[
                "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)*(gen_match_2==5)",

                "(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)*(gen_match_2==5)*generatorWeight*muonEffTrgWeight"
                ],
	    subplot_denominator=0,
        #subplot_numerators=[0, 1, 2, 3],
        subplot_numerators=[0, 1],
        y_label="Events per binwidth",
        output_dir=output_dir + '/mt_fall17/',
        y_subplot_lims=[0.6, 1.4],
        add_scale_factors=[1,1],
        y_subplot_label=
        "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
        plotlines=[DYFall17_mt, Embedding17_mt])

    visibleMassMuMu =default.clone(
        name="mm",
        title="#mu#mu",
        normalized_to_hist1=False,
        weight=["(pt_1>20 && pt_2>10)",
                "(pt_1>20 && pt_2>10)",
                "(pt_1>20 && pt_2>10)"],
        subplot_denominator=0,
        subplot_numerators=[0, 1],
        output_dir=output_dir + '/mm_corr/',
        y_subplot_lims=[0.8, 1.2],
        horizontal_subplot_lines = [0.9, 1.0, 1.1],
        y_subplot_label=
        "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#mu#mu simulation}}",
        plotlines=[DYFileWinter17_mm,
                   DYFileWinter17_emb_mm,
                   DYFileWinter17_mm_copy])

    visibleMassMuMu_PF =default.clone(
        name="mm",
        title="#mu#mu",
        normalized_to_hist1=False,
        weight=["1",
                "muonEffTrgWeight*generatorWeight",
                "1"],
        subplot_denominator=0,
        subplot_numerators=[0, 1],
        output_dir=output_dir + '/mm_pf/',
        y_subplot_lims=[0.8, 1.2],
        horizontal_subplot_lines = [0.9, 1.0, 1.1],
        y_subplot_label=
        "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#mu#mu simulation}}",
        plotlines=[DYFileWinter17_mm_pf,
                   DYFileWinter17_emb_mm_pf,
                   DYFileWinter17_mm_pf_copy])

    visibleMassEE = pltcl.single_plot(
        name="ee",
        title="ee",
        x_expression=variable,
        normalized_to_hist1=True,
        x_bins=x_bins,
        #~ normalized_by_binwidth = True,
        x_label=xlabel,
        #weight = "generatorWeight*(generatorWeight<=1)*((iso_1<0.15) && (iso_2<0.15) && (q_1*q_2)<0 && pt_1>17 && pt_2>8)",
        weight=
        "generatorWeight*(generatorWeight<=1)*((iso_1<0.1) && (iso_2<0.1) && (q_1*q_2)<0 && pt_1>20 && pt_2>13)",
        y_label="Events",
        #y_lims = [0,0.058],
        plot_type="absolute",
        legend=[0.62, 0.74, 0.92, 0.84],
        subplot_denominator=0,
        subplot_numerators=[1],
        output_dir=output_dir + '/ee/',
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label="Ratio",
        print_infos=True,
        y_log=False,
        plotlines=[DYFileEE_17, EmbFileEE_17])

    visibleMassElTau = default.clone(
        name="ElTau",
        title="e#tau_{h}",
        normalized_to_hist1=False,
        weight=["(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)",
                #"(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)",
                #"(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)",
		        "(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*generatorWeight*(eta_1 < 2.2 && eta_2 < 2.4)*muonEffTrgWeight",
                "(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)"],
        subplot_denominator=0,
        #subplot_numerators=[0, 1, 2, 3],
        subplot_numerators=[0,1],
        output_dir=output_dir + '/et/', 
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label=
        "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",       
        plotlines=[DYFileWinter17_et,
        #DYFileWinter17_et_shift_up,
        #DYFileWinter17_et_shift_down,
        DYFileWinter17_emb_et,
        DYFileWinter17_et_copy])
    
    visibleMassElTau_Fall17_with_tt = visibleMassFall17_with_tt.clone(
        name="et",
        title="e#tau_{h}",
        weight=[
                stitching_weight_fall_17 + "*(pt_1>37)*(pt_2>30)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronTightMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(iso_1<0.1)*(q_1*q_2<0)*(mt_1<50)*(trg_singleelectron==1)*(gen_match_2==5)*idisoweight_1*triggerweight_1",

                "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>37)*(pt_2>30)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronTightMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(iso_1<0.1)*(q_1*q_2<0)*(mt_1<50)*(trg_singleelectron==1)*(gen_match_2 == 5)*(gen_match_1==3)*topPtReweightWeight*puweight",

                "(pt_1>37)*(pt_2>30)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronTightMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(iso_1<0.1)*(q_1*q_2<0)*(mt_1<50)*(trg_singleelectron==1)*(gen_match_2==5)*generatorWeight*muonEffTrgWeight*idweight_1*isoweight_1*triggerweight_1"
                ],
        output_dir=output_dir + '/et_fall17_with_tt/',
        plotlines=[DYFall17_et, TTFall17_et, Embedding17_et])


    visibleMassElMu = default.clone(
        name="ElMu",
        title="e#mu",
        normalized_to_hist1=False,
        weight=["(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)",
               # "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)",
               # "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)",
		        "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)*generatorWeight*muonEffTrgWeight",
                "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)"],
        subplot_denominator=0,
        #subplot_numerators=[0, 1, 2, 3],
        subplot_numerators=[0,1],
        output_dir=output_dir + '/em/',
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label=
        "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
        plotlines=[DYFileWinter17_em,
                #DYFileWinter17_em_shift_up, 
                #DYFileWinter17_em_shift_down,  
                DYFileWinter17_emb_em,
                DYFileWinter17_em_copy])
    

    visibleMassElMu_Fall17_with_tt = visibleMassFall17_with_tt.clone(
        name="em",
        title="e#mu",
        weight=[
                stitching_weight_fall_17 + "*(pt_1>20 && pt_2>20)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(iso_1<0.15)*(iso_2<0.2)*(q_1*q_2<0)*(idisoweight_1*idisoweight_2)*(trg_muonelectron_lowptmu == 1)",

                "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>20 && pt_2>20)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(iso_1<0.15)*(iso_2<0.2)*(q_1*q_2<0)*(gen_match_1 == 3 && gen_match_2 == 4)*topPtReweightWeight*puweight",

                "(pt_1>20 && pt_2>20)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(iso_1<0.15)*(iso_2<0.2)*(q_1*q_2<0)*generatorWeight*muonEffTrgWeight*(idweight_1*isoweight_1*idweight_2*isoweight_2)*(trg_muonelectron_lowptmu == 1)"
                ],
        output_dir=output_dir + '/em_fall17_with_tt/',
        plotlines=[DYFall17_em, TTFall17_em, Embedding17_em])

    visibleMassTauTau_Fall17_with_tt = visibleMassFall17_with_tt.clone(
        name="tt",
        title="#tau_{h}#tau_{h}",
        weight=[
                stitching_weight_fall_17 + "*(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2==5)*(gen_match_1==5)",

                "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2 == 5)*(gen_match_1==5)*topPtReweightWeight*puweight",

                "(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2==5)*(gen_match_1==5)*generatorWeight*muonEffTrgWeight*(idweight_1*isoweight_1*idweight_2*isoweight_2*(triggerweight_1*(triggerweight_1<=1.8)+(triggerweight_1>1.8))*(triggerweight_2*(triggerweight_2<=1.8)+(triggerweight_2>1.8)))"
                ],
        output_dir=output_dir + '/tt_fall17_with_tt/',
        plotlines=[DYFall17_tt, TTFall17_tt, Embedding17_tt])
    visibleMassTauTau = default.clone(
        name="TauTau",
        title="#tau_{h}#tau_{h}",
        normalized_to_hist1=False,
        weight=["(pt_1>42 && pt_2>42)*(gen_match_1 == 5 && gen_match_2 == 5)",
                #"(pt_1>42 && pt_2>42)*(gen_match_1 == 5 && gen_match_2 == 5)",
		        "(pt_1>42 && pt_2>42)*(gen_match_1 == 5 && gen_match_2 == 5)*generatorWeight*muonEffTrgWeight",
                "(pt_1>42 && pt_2>42)*(gen_match_1 == 5 && gen_match_2 == 5)"],
        subplot_denominator=0,
        #subplot_numerators=[0, 1, 2, 3],
        subplot_numerators=[0,1],
        output_dir=output_dir + '/tt/',
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label=
        "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
        plotlines=[DYFileWinter17_tt, 
                #DYFileWinter17_tt_shift_up,
                #DYFileWinter17_tt_shift_down,
                DYFileWinter17_emb_tt,
                DYFileWinter17_tt_copy])
                
                
                


    if 'et' in channel:
        # configs.extend(
        #     visibleMassElTau.return_json_with_changed_x_and_weight(
        #         x_expressions=[variable]))
        configs.extend(
            visibleMassElTau_Fall17_with_tt.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
    if 'tt' in channel:
        # configs.extend(
        #     visibleMassTauTau.return_json_with_changed_x_and_weight(
        #         x_expressions=[variable]))
        configs.extend(
            visibleMassTauTau_Fall17_with_tt.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
    if 'mm' in channel:
        configs.extend(
            visibleMassMuMu.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
        # configs.extend(
        #     visibleMassMuMu_PF.return_json_with_changed_x_and_weight(
        #         x_expressions=[variable]))

    if 'ee' in channel:
        configs.extend(
            visibleMassEE.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
    if 'mt' in channel:
        # configs.extend(
        #     visibleMassMuTau.return_json_with_changed_x_and_weight(
        #         x_expressions=[variable]))y
        configs.extend(
            visibleMassMuTau_Fall17_with_tt.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
    if 'em' in channel:
        # configs.extend(
        #     visibleMassElMu.return_json_with_changed_x_and_weight(
        #         x_expressions=[variable]))
        configs.extend(
            visibleMassElMu_Fall17_with_tt.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))


def default_plot_root_variable(channel=['mt'], variable='pt_1'):

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
        name=variable + "MuTau",
        title="#mu#tau_{h}",
        x_expression=variable,
        #~ normalized_to_hist1 = True,
        #~ x_bins = x_bins,
        #	x_bins = "1,0,13000",
        normalized_by_binwidth=True,
        #	normalized_by_binwidth = False,
        #~ x_label = xlabel,
        weight=[
            selection_weight_mt + "*" + genmatching_weight_xt +
            "*generatorWeight*(generatorWeight<=1)", selection_weight_mt +
            "*" + stitching_weight + genmatching_weight_xt + "*eventWeight",
            selection_weight_mt +
            "*((gen_match_1==4)&&(gen_match_2==5))*eventWeight"
        ],
        y_label="Events per bin width",
        #y_lims = [0,0.058],
        plot_type="absolute",
        legend=[0.53, 0.44, 0.92, 0.88],
        subplot_denominator=0,
        stacked=True,
        subplot_numerators=[1, 2],
        output_dir=output_dir + '/mt/',
        wwwfolder=None,
        y_subplot_lims=[0.5, 1.5],
        y_subplot_label="Ratio",
        print_infos=True,
        plotlines=[EmbeddingMuTauFileNominal_all, DYFileMuTauFile])
    if 'mt' in channel:
        configs.extend(
            visibleMassMuTau.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Make embedding plots.", parents=[logger.loggingParser])

    parser.add_argument(
        "-i",
        "--input-dir",
        required=False,
        default=".",
        help="Input directory [Default: %(default)s]")
    parser.add_argument(
        "-o",
        "--output-dir",
        required=False,
        default="plots",
        help="Output directory [Default: %(default)s]")
    parser.add_argument(
        "-c",
        "--channel",
        required=False,
        default=['mt', 'et'],
        nargs="*",
        help="Select decay channel. [Default: %(default)s]")
    parser.add_argument(
        "-n",
        "--n-processes",
        required=False,
        default=1,
        help="Number of parallel processes. [Default: %(default)s]")
    parser.add_argument(
        "-x",
        "--quantities",
        required=False,
        default=None,
        nargs="*",
        help="Select quantities to plot. [Default: %(default)s]")
    parser.add_argument(
        "-p",
        "--preset",
        required=False,
        default=False,
        help="Use a Quantities Preset listed in variables.json")
    parser.add_argument(
        "-m",
        "--mode",
        required=False,
        default="default",
        help="Specify what Binning should be used, Default: 'default', other options are 'analysis' ")

    args = parser.parse_args()
    logger.initLogger(args)
    configs = []
    output_dir = args.output_dir
    input_dir = args.input_dir
    data = json.load(open('scripts/variables.json'))
    print args.channel
    for channel in args.channel:

        # tau_iso_variables = [x for x in iso_variables if x[-2:] == "_2"]
        # plotting_dict = {}
        # #~ for v in default_variables:
        # for v in default_variables + selection_variables:
        #     plotting_dict.setdefault(v, [])
        #     plotting_dict[v] = {}
        #     plotting_dict[v].setdefault("x_label", channel + '_' + v)
        #     plotting_dict[v].setdefault("x_bins", channel + '_' + v)
        #     plotting_dict.setdefault(v, [])
        #     plotting_dict[v] = {}
        #     plotting_dict[v].setdefault("x_label", v)
        #     if 'eta' in v or 'Eta' in v:
        #         plotting_dict[v].setdefault("x_bins", "25,-2.5,2.5")
        #     if 'phi' in v or 'Phi' in v:
        #         plotting_dict[v].setdefault("x_bins", "30,-3.2,3.2")
        #     if 'njet' in v:
        #         plotting_dict[v].setdefault("x_bins", "7,0,7")
        #     if 'Weight' in v or 'weight' in v:
        #         plotting_dict[v].setdefault("x_bins", "24,0,1.2")
        #     if 'trg' in v or 'weight' in v:
        #         plotting_dict[v].setdefault("x_bins", "3,0,3")

        #     plotting_dict[v].setdefault("x_bins", "20,0,20")
        #if args.preset != None:
        try:
            variables_to_plot = data["preset"][args.preset]
        except KeyError:
            pass
	if args.quantities is not None:
            variables_to_plot = args.quantities
        for v in variables_to_plot:
            #read legend position
            try:
                legend_pos = legend=data[args.mode + "_plotting_dict"][v][channel]["legend_position"]
            except KeyError:
                try: 
                    legend_pos = legend=data["default_plotting_dict"][v][channel]["legend_position"]
                except KeyError:
                    try: 
                        legend_pos = legend=data["default_plotting_dict"][v]["default"]["legend_position"]
                    except KeyError:
                        legend_pos = 1
            try:
                plot_root_variable(
                    variable=v,
                    xlabel=data[args.mode + "_plotting_dict"][v][channel]["x_label"],
                    x_bins=data[args.mode + "_plotting_dict"][v][channel]["x_bins"],
                    legend=legend_pos,
                    channel=args.channel)
            except KeyError:
                try:
                    plot_root_variable(
                    variable=v,
                    xlabel=data["default_plotting_dict"][v][channel]["x_label"],
                    x_bins=data["default_plotting_dict"][v][channel]["x_bins"],
                    legend=legend_pos,
                    channel=args.channel)
                except KeyError:
                    try:
                        plot_root_variable(
                            variable=v,
                            xlabel=data["default_plotting_dict"][v]["default"]["x_label"],
                            x_bins=data["default_plotting_dict"][v]["default"]["x_bins"],
                            legend=legend_pos,
                            channel=args.channel)
                    except KeyError:
                        plot_root_variable(
                            variable=v,
                            xlabel=v,
                            x_bins=data["default_plotting_dict"]["not_listed"]["default"]["x_bins"],
                            legend=legend_pos,
                            channel=args.channel)

        print "Plotting..."
        higgs_plotter = higgsplot.HiggsPlotter(
            list_of_config_dicts=configs,
            list_of_args_strings=[""],
            n_processes=args.n_processes)
