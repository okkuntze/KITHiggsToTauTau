#!/usr/bin/env python

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import json
import HiggsAnalysis.KITHiggsToTauTau.plotting.higgsplot as higgsplot

import HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plot_classes as pltcl
from HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plotline_bib import *


def plot_root_variable(channel=['mt'],
                       variable='pt_1',
                       x_bins="30,0,120",
                       xlabel='',
                       legend=1):

    # 2017 Configs
    stitching_weight = "(((genbosonmass >= 50.0 && (npartons == 0 || npartons >= 4))*5.75970078e-5) + ((genbosonmass >= 50.0 && npartons == 1)*1.36277241e-5) + ((genbosonmass >= 50.0 && npartons == 2)*7.42888435e-6) + ((genbosonmass >= 50.0 && npartons == 3)*1.62808443e-5) + ((genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight))"
    selection_weight_mt = "(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)"
    genmatching_weight_mt = "(gen_match_2==5)*((gen_match_2 == 5)*0.95 + (gen_match_2 != 5))"
    generator_weight_mt = "generatorWeight*(generatorWeight<=1.0)*idisoweight_1*muonEffEmbeddedIDWeight_1*muonEffEmbeddedIDWeight_2*muonEffTrgWeight_1*muonEffVVLIsoWeight_1*muonEffVVLIsoWeight_2*triggerweight_1"
    ttbar_weight_mt = "generatorWeight*(generatorWeight<=1.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight*0.5*topPtReweightWeight*((gen_match_2 == 5)*0.95 + (gen_match_2 != 5))*puweight"
    stitching_weight_fall_17 = "(((genbosonmass >= 50.0 && (npartons == 0 || npartons >= 4))*2.455936181) + ((genbosonmass >= 50.0 && npartons == 1)*0.5608870881) + ((genbosonmass >= 50.0 && npartons == 2)*0.5745263806) + ((genbosonmass >= 50.0 && npartons == 3)*0.617450628))"
    # Define Legend Positions
    if legend == 1:  # top right
        legend_pos = [0.55, 0.62, 0.93, 0.82]
    elif legend == 2:
        # top left
        legend_pos = [0.20, 0.62, 0.58, 0.82]
    elif legend == 3:  # bottom middle
        legend_pos = [0.34, 0.08, 0.74, 0.28]
    elif legend == 4:  # top middle
        legend_pos = [0.34, 0.64, 0.74, 0.84]

    # default = pltcl.single_plot(
    #     x_expression=variable,
    #     normalized_by_binwidth=True,
    #     x_bins=x_bins,
    #     x_label=xlabel,
    #     y_label="Events per binwidth",
    #     plot_type="absolute",
    #     legend=legend_pos,
    #     horizontal_subplot_lines=[0.8, 1, 1.2],
    #     y_subplot_lims=[0.6, 1.4],
    #     y_subplot_label="Ratio",
    #     print_infos=True,
    #     y_log=False)
    # visibleMassMuTau = default.clone(
    #     name="mt",
    #     title="#mu#tau_{h}",
    #     normalized_to_hist1=False,
    #     weight=[
    #         "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
    #         #"(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
    #         #"(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
    #         "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1 == 4)*generatorWeight*muonEffTrgWeight",
    #         "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)"
    #     ],
    #     subplot_denominator=0,
    #     #subplot_numerators=[0, 1, 2, 3],
    #     subplot_numerators=[0, 1],
    #     output_dir=output_dir + '/mt/',
    #     y_subplot_lims=[0.6, 1.4],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
    #     plotlines=[
    #         DYFileWinter17_mt,
    #         #DYFileWinter17_mt_shift_up,
    #         #DYFileWinter17_mt_shift_down,
    #         DYFileWinter17_emb_mt,
    #         DYFileWinter17_mt_copy
    #     ])

    # visibleMassMuTau_fsr = default.clone(
    #     name="mt",
    #     title="#mu#tau_{h}",
    #     normalized_to_hist1=True,
    #     weight=[
    #         "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
    #         "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
    #         "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)*generatorWeight",
    #         "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)*generatorWeight",
    #     ],
    #     subplot_denominator=1,
    #     #subplot_numerators=[0, 1, 2, 3],
    #     subplot_numerators=[0, 2, 3],
    #     output_dir=output_dir + '/mt_fsr/',
    #     y_subplot_lims=[0.6, 1.4],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
    #     plotlines=[
    #         DYFileWinter17_mt_copy,
    #         DYFileWinter17_mt,
    #         DYFileWinter17_emb_mt,
    #         DYFileWinter17_emb_mt_no_fsr

    #     ])

    # visibleMassFall17_with_tt = default.clone(
    #     normalized_to_hist1=False,
    #     subplot_denominator=1,
    #     subplot_numerators=[2],
    #     y_label="Events per binwidth",
    #     y_subplot_lims=[0.6, 1.4],
    #     add_nicks=[0, 1],
    #     add_result_nicks=1,
    #     add_scale_factors=[1, 1],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}"
    # )
    # visibleMassMuTau_Fall17_with_tt = visibleMassFall17_with_tt.clone(
    #     name="mt",
    #     title="#mu#tau_{h}",
    #     weight=[
    #         stitching_weight_fall_17 +
    #         "*(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(mt_1<50)*(trg_singlemuon==1)*(gen_match_2==5)*(eleTauFakeRateWeight*muTauFakeRateWeight*isoWeight_1*idWeight_1*trackWeight_1*(singleTriggerMCEfficiencyWeightKIT_1>0.01*(singleTriggerDataEfficiencyWeightKIT_1/singleTriggerMCEfficiencyWeightKIT_1)+singleTriggerMCEfficiencyWeightKIT_1<0.01))",
    #         "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(mt_1<50)*(trg_singlemuon==1)*(gen_match_2 == 5)*(gen_match_1 == 4)*topPtReweightWeight*puweight",
    #         "(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(mt_1<50)*(trg_singlemuon==1)*(gen_match_2==5)*generatorWeight*muonEffTrgWeight*(idWeight_1*triggerWeight_1*isoWeight_1)"
    #     ],
    #     output_dir=output_dir + '/mt_fall17_with_tt/',
    #     plotlines=[DYFall17_mt, TTFall17_mt, Embedding17_mt])

    # visibleMassMuTau_Fall17 = default.clone(
    #     name="mt",
    #     title="#mu#tau_{h}",
    #     normalized_to_hist1=False,
    #     weight=[
    #         "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)*(gen_match_2==5)",
    #         "(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(trg_singlemuon==1)*(gen_match_2==5)*generatorWeight*muonEffTrgWeight"
    #     ],
    #     subplot_denominator=0,
    #     #subplot_numerators=[0, 1, 2, 3],
    #     subplot_numerators=[0, 1],
    #     y_label="Events per binwidth",
    #     output_dir=output_dir + '/mt_fall17/',
    #     y_subplot_lims=[0.6, 1.4],
    #     add_scale_factors=[1, 1],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
    #     plotlines=[DYFall17_mt, Embedding17_mt])

    # visibleMassMuMu = default.clone(
    #     name="mm",
    #     title="#mu#mu",
    #     normalized_to_hist1=False,
    #     weight=[
    #         "(pt_1>20 && pt_2>10)", "(pt_1>20 && pt_2>10)",
    #         "(pt_1>20 && pt_2>10)"
    #     ],
    #     subplot_denominator=0,
    #     subplot_numerators=[0, 1],
    #     output_dir=output_dir + '/mm_corr/',
    #     y_subplot_lims=[0.8, 1.2],
    #     horizontal_subplot_lines=[0.9, 1.0, 1.1],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#mu#mu simulation}}",
    #     plotlines=[
    #         DYFileWinter17_mm, DYFileWinter17_emb_mm, DYFileWinter17_mm_copy
    #     ])

    # visibleMassMuMu_fsr = default.clone(
    #     name="mm",
    #     title="#mu#mu",
    #     normalized_to_hist1=True,
    #     weight=[
    #         "(pt_1>20 && pt_2>10)",
    #         "(pt_1>20 && pt_2>10)",
    #         "(pt_1>20 && pt_2>10)",
    #         "(pt_1>20 && pt_2>10)"
    #     ],
    #     subplot_denominator=1,
    #     subplot_numerators=[0, 2, 3],
    #     output_dir=output_dir + '/mm_fsr/',
    #     y_subplot_lims=[0.8, 1.2],
    #     horizontal_subplot_lines=[0.9, 1.0, 1.1],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#mu#mu simulation}}",
    #     plotlines=[
    #         DYFileWinter17_mm_copy,
    #         DYFileWinter17_mm,
    #         DYFileWinter17_emb_mm,
    #         DYFileWinter17_emb_mm_no_fsr
    #     ])

    # visibleMassMuMu_fsr_matched = default.clone(
    #     name="mm",
    #     title="#mu#mu",
    #     normalized_to_hist1=True,
    #     weight=[
    #         "(pt_1>20 && pt_2>10)","(pt_1>20 && pt_2>10)","(pt_1>20 && pt_2>10)"],
    #     subplot_denominator=0,
    #     subplot_numerators=[0, 1],
    #     output_dir=output_dir + '/mm_fsr_vs_dy_event_matched/',
    #     y_subplot_lims=[0.8, 1.2],
    #     horizontal_subplot_lines=[0.9, 1.0, 1.1],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#mu#mu simulation}}",
    #     plotlines=[
    #         DYFileWinter17_mm_matched, DYFileWinter17_emb_mm_no_fsr_matched, DYFileWinter17_mm_matched_copy
    #     ])

    # visibleMassMuMu_PF = default.clone(
    #     name="mm",
    #     title="#mu#mu, p_{t} > 0.5 GeV, event Matched",
    #     normalized_to_hist1=False,
    #     weight=["1", "1", "1"],
    #     subplot_denominator=0,
    #     subplot_numerators=[0, 1],
    #     output_dir=output_dir + '/mm_pf/',
    #     y_subplot_lims=[0.8, 1.2],
    #     horizontal_subplot_lines=[0.9, 1.0, 1.1],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#mu#mu simulation}}",
    #     plotlines=[
    #         DYFileWinter17_mm_pf, DYFileWinter17_emb_mm_pf,
    #         DYFileWinter17_mm_pf_copy
    #     ])

    # visibleMassEE = pltcl.single_plot(
    #     name="ee",
    #     title="ee",
    #     x_expression=variable,
    #     normalized_to_hist1=True,
    #     x_bins=x_bins,
    #     #~ normalized_by_binwidth = True,
    #     x_label=xlabel,
    #     #weight = "generatorWeight*(generatorWeight<=1)*((iso_1<0.15) && (iso_2<0.15) && (q_1*q_2)<0 && pt_1>17 && pt_2>8)",
    #     weight=
    #     "generatorWeight*(generatorWeight<=1)*((iso_1<0.1) && (iso_2<0.1) && (q_1*q_2)<0 && pt_1>20 && pt_2>13)",
    #     y_label="Events",
    #     #y_lims = [0,0.058],
    #     plot_type="absolute",
    #     legend=[0.62, 0.74, 0.92, 0.84],
    #     subplot_denominator=0,
    #     subplot_numerators=[1],
    #     output_dir=output_dir + '/ee/',
    #     y_subplot_lims=[0.6, 1.4],
    #     y_subplot_label="Ratio",
    #     print_infos=True,
    #     y_log=False,
    #     plotlines=[DYFileEE_17, EmbFileEE_17])

    # visibleMassElTau = default.clone(
    #     name="ElTau",
    #     title="e#tau_{h}",
    #     normalized_to_hist1=False,
    #     weight=[
    #         "(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)",
    #         #"(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)",
    #         #"(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)",
    #         "(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*generatorWeight*(eta_1 < 2.2 && eta_2 < 2.4)*muonEffTrgWeight",
    #         "(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)"
    #     ],
    #     subplot_denominator=0,
    #     #subplot_numerators=[0, 1, 2, 3],
    #     subplot_numerators=[0, 1],
    #     output_dir=output_dir + '/et/',
    #     y_subplot_lims=[0.6, 1.4],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
    #     plotlines=[
    #         DYFileWinter17_et,
    #         #DYFileWinter17_et_shift_up,
    #         #DYFileWinter17_et_shift_down,
    #         DYFileWinter17_emb_et,
    #         DYFileWinter17_et_copy
    #     ])

    # visibleMassElTau_Fall17_with_tt = visibleMassFall17_with_tt.clone(
    #     name="et",
    #     title="e#tau_{h}",
    #     weight=[
    #         stitching_weight_fall_17 +
    #         "*(pt_1>37)*(pt_2>30)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronTightMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(iso_1<0.1)*(q_1*q_2<0)*(mt_1<50)*(trg_singleelectron==1)*(gen_match_2==5)*(eleTauFakeRateWeight*muTauFakeRateWeight*isoWeight_1*idWeight_1*trackWeight_1*(singleTriggerMCEfficiencyWeightKIT_1>0.01*(singleTriggerDataEfficiencyWeightKIT_1/singleTriggerMCEfficiencyWeightKIT_1)+singleTriggerMCEfficiencyWeightKIT_1<0.01))",
    #         "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>37)*(pt_2>30)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronTightMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(iso_1<0.1)*(q_1*q_2<0)*(mt_1<50)*(trg_singleelectron==1)*(gen_match_2 == 5)*(gen_match_1==3)*topPtReweightWeight*puweight",
    #         "(pt_1>37)*(pt_2>30)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronTightMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(iso_1<0.1)*(q_1*q_2<0)*(mt_1<50)*(trg_singleelectron==1)*(gen_match_2==5)*generatorWeight*muonEffTrgWeight*idWeight_1*isoWeight_1*triggerWeight_1"
    #     ],
    #     output_dir=output_dir + '/et_fall17_with_tt/',
    #     plotlines=[DYFall17_et, TTFall17_et, Embedding17_et])

    # visibleMassElMu = default.clone(
    #     name="ElMu",
    #     title="e#mu",
    #     normalized_to_hist1=False,
    #     weight=[
    #         "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)",
    #         # "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)",
    #         # "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)",
    #         "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)*generatorWeight*muonEffTrgWeight",
    #         "(pt_1>20 && pt_2>20)*(gen_match_1 == 3 && gen_match_2 == 4)"
    #     ],
    #     subplot_denominator=0,
    #     #subplot_numerators=[0, 1, 2, 3],
    #     subplot_numerators=[0, 1],
    #     output_dir=output_dir + '/em/',
    #     y_subplot_lims=[0.6, 1.4],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
    #     plotlines=[
    #         DYFileWinter17_em,
    #         #DYFileWinter17_em_shift_up,
    #         #DYFileWinter17_em_shift_down,
    #         DYFileWinter17_emb_em,
    #         DYFileWinter17_em_copy
    #     ])

    # visibleMassElMu_Fall17_with_tt = visibleMassFall17_with_tt.clone(
    #     name="em",
    #     title="e#mu",
    #     weight=[
    #         stitching_weight_fall_17 +
    #         "*(pt_1>20 && pt_2>20)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(iso_1<0.15)*(iso_2<0.2)*(q_1*q_2<0)*(idisoweight_1*idisoweight_2)*(trg_muonelectron_lowptmu == 1 ||trg_muonelectron_lowpte == 1)*(pZetaMissVis > -50)* (eleTauFakeRateWeight*muTauFakeRateWeight*isoWeight_1*idWeight_1*trackWeight_1*(singleTriggerMCEfficiencyWeightKIT_1>0.01*(singleTriggerDataEfficiencyWeightKIT_1/singleTriggerMCEfficiencyWeightKIT_1)+singleTriggerMCEfficiencyWeightKIT_1<0.01))",
    #         "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>20 && pt_2>20)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(iso_1<0.15)*(iso_2<0.2)*(q_1*q_2<0)*(gen_match_1 == 3 && gen_match_2 == 4)*(trg_muonelectron_lowptmu == 1 ||trg_muonelectron_lowpte == 1)*(pZetaMissVis > -50)*topPtReweightWeight*puweight",
    #         "(pt_1>20 && pt_2>20)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(iso_1<0.15)*(iso_2<0.2)*(q_1*q_2<0)*generatorWeight*muonEffTrgWeight*(idWeight_1*isoWeight_1*idWeight_2*isoWeight_2)*(trg_muonelectron_lowptmu == 1 ||trg_muonelectron_lowpte == 1)*(pZetaMissVis > -50)"
    #     ],
    #     output_dir=output_dir + '/em_fall17_with_tt/',
    #     plotlines=[DYFall17_em, TTFall17_em, Embedding17_em])

    # visibleMassTauTau_Fall17_with_tt = visibleMassFall17_with_tt.clone(
    #     name="tt",
    #     title="#tau_{h}#tau_{h}",
    #     weight=[
    #         stitching_weight_fall_17 +
    #         "*(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2==5)*(gen_match_1==5)* (eleTauFakeRateWeight*muTauFakeRateWeight*isoWeight_1*idWeight_1*trackWeight_1*(crossTriggerMCEfficiencyWeight_1>0.01*(crossTriggerDataEfficiencyWeight_1/crossTriggerMCEfficiencyWeight_1)+crossTriggerMCEfficiencyWeight_1<0.01)*(crossTriggerMCEfficiencyWeight_2>0.01*(crossTriggerDataEfficiencyWeight_2/crossTriggerMCEfficiencyWeight_2)+crossTriggerMCEfficiencyWeight_2<0.01))*(trg_doubletau==1)",
    #         "numberGeneratedEventsWeight*crossSectionPerEventWeight*41.29*1000*(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2 == 5)*(gen_match_1==5)*topPtReweightWeight*puweight*(trg_doubletau==1)",
    #         "(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2==5)*(gen_match_1==5)*generatorWeight*muonEffTrgWeight*crossTriggerDataEfficiencyWeight_1*crossTriggerDataEfficiencyWeight_2"
    #     ],
    #     # weight = [
    #     #     stitching_weight_fall_17 + '*(pt_1 > 50 && pt_2 > 40) * (nbtag == 0) * (njets >= 1) * ((eta_1 - eta_2) < 1 || (eta_1 - eta_2) < -1) * (m_vis < 100) * (pzetavis > 60) * (gen_match_2==5)*(gen_match_1==5)*(trg_doubletau == 1)',
    #     #     '(pt_1 > 50 && pt_2 > 40) * (nbtag == 0) * (njets >= 1) * ((eta_1 - eta_2) < 1 || (eta_1 - eta_2) < -1) * (m_vis < 100) * (pzetavis > 60) * (gen_match_2==5) * (gen_match_1==5) * (trg_doubletau == 1) * numberGeneratedEventsWeight * crossSectionPerEventWeight * 41.29 * 1000 * topPtReweightWeight * puweight',
    #     #     '(pt_1 > 50 && pt_2 > 40) * (nbtag == 0) * (njets >= 1) * ((eta_1 - eta_2) < 1 || (eta_1 - eta_2) < -1) * (m_vis < 100) * (pzetavis > 60) * (gen_match_2==5) * (gen_match_1==5) * generatorWeight * muonEffTrgWeight * (idweight_1 * isoweight_1 * idweight_2 * isoweight_2 * (triggerweight_1 * (triggerweight_1 <= 1.8) + (triggerweight_1 > 1.8)) * (triggerweight_2 * (triggerweight_2 <= 1.8) +(triggerweight_2 > 1.8))) * 0.50971080328'],
    #     output_dir=output_dir + '/tt_fall17_with_tt/',
    #     plotlines=[DYFall17_tt, TTFall17_tt, Embedding17_tt])
    # visibleMassTauTau = default.clone(
    #     name="TauTau",
    #     title="#tau_{h}#tau_{h}",
    #     normalized_to_hist1=False,
    #     weight=[
    #         "(pt_1>42 && pt_2>42)*(gen_match_1 == 5 && gen_match_2 == 5)",
    #         #"(pt_1>42 && pt_2>42)*(gen_match_1 == 5 && gen_match_2 == 5)",
    #         "(pt_1>42 && pt_2>42)*(gen_match_1 == 5 && gen_match_2 == 5)*generatorWeight*muonEffTrgWeight",
    #         "(pt_1>42 && pt_2>42)*(gen_match_1 == 5 && gen_match_2 == 5)"
    #     ],
    #     subplot_denominator=0,
    #     #subplot_numerators=[0, 1, 2, 3],
    #     subplot_numerators=[0, 1],
    #     output_dir=output_dir + '/tt/',
    #     y_subplot_lims=[0.6, 1.4],
    #     y_subplot_label=
    #     "#frac{#scale[0.5]{embedded}}{#scale[0.5]{Z#rightarrow#tau#tau simulation}}",
    #     plotlines=[
    #         DYFileWinter17_tt,
    #         #DYFileWinter17_tt_shift_up,
    #         #DYFileWinter17_tt_shift_down,
    #         DYFileWinter17_emb_tt,
    #         DYFileWinter17_tt_copy
    #     ])

    # if 'et' in channel:
    #     # configs.extend(
    #     #     visibleMassElTau.return_json_with_changed_x_and_weight(
    #     #         x_expressions=[variable]))
    #     configs.extend(
    #         visibleMassElTau_Fall17_with_tt.
    #         return_json_with_changed_x_and_weight(x_expressions=[variable]))
    # if 'tt' in channel:
    #     # configs.extend(
    #     #     visibleMassTauTau.return_json_with_changed_x_and_weight(
    #     #         x_expressions=[variable]))
    #     configs.extend(
    #         visibleMassTauTau_Fall17_with_tt.
    #         return_json_with_changed_x_and_weight(x_expressions=[variable]))
    # if 'mm' in channel:
    #     configs.extend(
    #         visibleMassMuMu_fsr.return_json_with_changed_x_and_weight(
    #             x_expressions=[variable]))

    # if 'ee' in channel:
    #     configs.extend(
    #         visibleMassEE.return_json_with_changed_x_and_weight(
    #             x_expressions=[variable]))
    # if 'mt' in channel:
    #     # configs.extend(
    #     #     visibleMassMuTau.return_json_with_changed_x_and_weight(
    #     #         x_expressions=[variable]))y
    #     configs.extend(
    #         visibleMassMuTau_fsr.
    #         return_json_with_changed_x_and_weight(x_expressions=[variable]))
    # if 'em' in channel:
    #     # configs.extend(
    #     #     visibleMassElMu.return_json_with_changed_x_and_weight(
    #     #         x_expressions=[variable]))
    #     configs.extend(
    #         visibleMassElMu_Fall17_with_tt.
    #         return_json_with_changed_x_and_weight(x_expressions=[variable]))

    ###############################
    # Paper Plots
    ###############################
    default = pltcl.single_plot(
        x_expression=variable,
        normalized_by_binwidth=True,
        x_bins=x_bins,
        x_label=xlabel,
        plot_type="absolute",
        legend=legend_pos,
        horizontal_subplot_lines=[0.8, 1, 1.2],
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label="Ratio",
        print_infos=True,
        y_log=False)

    visibleMassFall17_with_tt = default.clone(
        normalized_to_hist1=False,
        subplot_denominator=1,
        subplot_numerators=[2],
        y_label="N_{ets} \ bin width",
        y_subplot_lims=[0.6, 1.4],
        add_nicks=[0, 1],
        add_result_nicks=1,
        add_scale_factors=[1, 1],
        y_subplot_label="Ratio to sim.")
    weightscale_mm = "1"
    y_label = "N_{evts} / bin width"
    # if any(string == variable for string in [
    #         "pt_1", "pt_2", "rho", "jpt_1", "jpt_2", "jphi_2", "npv", "met",
    #         "mjj", "mt_1", "mt_2", "mt_tot", "metcov00", "metcov01",
    #         "metcov10", "metcov11"
    # ]):
    #     weightscale_mm = "1/1e3"
    #     y_label = "10^{-3} x N_{evts} / bin width"
    # if any(string == variable for string in [
    #         "eta_1", "eta_2", "jeta_1", "jeta_2", "jeta", "jeta_1", "jeta_2"
    #         "jphi_1", "jpt", "metphi", "m_vis", "phi_1", "phi_2"
    # ]):
    #     weightscale_mm = "1/1e6"
    #     y_label = "10^{-6} #times N_{evts} / bin width"
    # if any(string == variable for string in ["m_1", "m_2"]):
    #     weightscale_mm = "1/1e9"
    #     y_label = "10^{-9} x N_{evts} / bin width"
    if any(string == variable for string in ["met"]):
        subplot_ratio = [0.9, 1.1]
        subplot_ticks = [0.95, 1.0, 1.05]
    if any(string == variable for string in ["iso_p", "iso_t", "iso_1", "iso_2", "mt_tot", "m_vis", "nbtag", "pt_t", "pt_p"]):
        subplot_ratio = [0.8, 1.2]
        subplot_ticks = [0.9, 1.0, 1.1]
    else:
        subplot_ratio = [0.95, 1.05]
        subplot_ticks = [0.97, 1.0, 1.03]
    visibleMassMuMu = default.clone(
        name="mm",
        title="#mu#mu",
        normalized_to_hist1=False,
        weight=[
            weightscale_mm + "*(pt_1>20 && pt_2>10)",
            weightscale_mm + "*(pt_1>20 && pt_2>10)",
            weightscale_mm + "*(pt_1>20 && pt_2>10)"
        ],
        y_label=y_label,
        subplot_denominator=0,
        subplot_numerators=[1, 2],
        output_dir=output_dir + '/mm/',
        y_subplot_lims=subplot_ratio,
        horizontal_subplot_lines=subplot_ticks,
        y_subplot_label="Ratio to sim.",
        plotlines=[
            DYFileWinter17_mm, DYFileWinter17_mm_copy, DYFileWinter17_emb_mm
        ])

    visibleMassMuTau = default.clone(
        name="mt",
        title="#mu#tau_{h}",
        normalized_to_hist1=False,
        weight=[
            "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)",
            "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1 == 4)",
            "(pt_1>20 && pt_2>20)*(gen_match_2==5)*(gen_match_1==4)*generatorWeight*muonEffTrgWeight"
        ],
        subplot_denominator=0,
        y_label=y_label,
        subplot_numerators=[1, 2],
        output_dir=output_dir + '/mt/',
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label="Ratio to sim.",
        plotlines=[
            DYFileWinter17_mt,
            DYFileWinter17_mt_copy,
            DYFileWinter17_emb_mt
        ])

    visibleMassElTau = default.clone(
        name="et",
        title="e#tau_{h}",
        normalized_to_hist1=False,
        weight=[
            "(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)",
            "(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*(eta_1 < 2.2 && eta_2 < 2.4)",
            "(pt_1>25 && pt_2>20)*(gen_match_2==5)*(gen_match_1==3)*generatorWeight*(eta_1 < 2.2 && eta_2 < 2.4)*muonEffTrgWeight",

        ],
        y_label=y_label,
        subplot_denominator=0,
        subplot_numerators=[1, 2],
        output_dir=output_dir + '/et/',
        y_subplot_lims=[0.6, 1.4],
        y_subplot_label="Ratio to sim.",
        plotlines=[
            DYFileWinter17_et,
            DYFileWinter17_et_copy,
            DYFileWinter17_emb_et
        ])
    stitching_weight_fall_17_b = "(((genbosonmass >= 50.0 && (npartons == 0 || npartons >= 4))*0.2868728554) + ((genbosonmass >= 50.0 && npartons == 1)*0.0655160675) + ((genbosonmass >= 50.0 && npartons == 2)*0.0671092452) + ((genbosonmass >= 50.0 && npartons == 3)*0.0721231383))"
    
    
    visibleMassTauTau = default.clone(
        name="TauTau",
        title="#tau_{h}#tau_{h} with Crosstrigger",
        normalized_to_hist1=False,
        weight=[
            stitching_weight_fall_17_b +
            "*(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2==5)*(gen_match_1==5)* (eleTauFakeRateWeight*muTauFakeRateWeight*isoWeight_1*idWeight_1*trackWeight_1*(crossTriggerMCEfficiencyWeight_1>0.01*(crossTriggerDataEfficiencyWeight_1/crossTriggerMCEfficiencyWeight_1)+crossTriggerMCEfficiencyWeight_1<0.01)*(crossTriggerMCEfficiencyWeight_2>0.01*(crossTriggerDataEfficiencyWeight_2/crossTriggerMCEfficiencyWeight_2)+crossTriggerMCEfficiencyWeight_2<0.01))*(trg_doubletau==1)",

            "numberGeneratedEventsWeight*crossSectionPerEventWeight*4.823*1000*(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2 == 5)*(gen_match_1==5)*topPtReweightWeight*puweight*(trg_doubletau==1)",

            "(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2==5)*(gen_match_1==5)*generatorWeight*muonEffTrgWeight*(trg_doubletau==1)",

            "(pt_1>50 && pt_2>40)*(extraelec_veto<0.5)*(extramuon_veto<0.5)*(dilepton_veto<0.5)*(againstMuonLoose3_2>0.5)*(againstElectronVLooseMVA6_2>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_1>0.5)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(q_1*q_2<0)*(pt_tt>50)*(gen_match_2==5)*(gen_match_1==5)*generatorWeight*muonEffTrgWeight*(trg_doubletau==1)",
        ],
        y_label=y_label,
        subplot_denominator=1,
        subplot_numerators=[2,3],
        y_subplot_lims=[0.6, 1.4],
        add_nicks=[0, 1],
        add_result_nicks=1,
        add_scale_factors=[1, 1],
        output_dir=output_dir + '/tt_newer_with_trigger/',
        y_subplot_label="Ratio to sim.",
        plotlines=[
            DYFall17_tt, 
            TTFall17_tt,
            Embedded_trigger_old_tt,
            Embedded_trigger_new_v2_tt
        ])

    visibleMassMuTau =  default.clone(
        name="MuTau",
        title="#mu#tau_{h} with MuTau Crosstrigger",
        normalized_to_hist1=False,
        weight=[
            stitching_weight_fall_17_b +
            "*(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(mt_1<50)*(trg_muontau_lowptmu==1)*(gen_match_2==5)*(eleTauFakeRateWeight*muTauFakeRateWeight*isoWeight_1*idWeight_1*trackWeight_1*(crossTriggerMCEfficiencyWeight_1>0.01*(crossTriggerDataEfficiencyWeight_1/crossTriggerMCEfficiencyWeight_1)+crossTriggerMCEfficiencyWeight_1<0.01)*(crossTriggerMCEfficiencyWeight_2>0.01*(crossTriggerDataEfficiencyWeight_2/crossTriggerMCEfficiencyWeight_2)+crossTriggerMCEfficiencyWeight_2<0.01))",

            "numberGeneratedEventsWeight*crossSectionPerEventWeight*4.823*1000*(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(mt_1<50)*(trg_muontau_lowptmu==1)*(gen_match_2 == 5)*(gen_match_1 == 4)*topPtReweightWeight*puweight",

            "(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(mt_1<50)*(trg_muontau_lowptmu==1)*(gen_match_2==5)*generatorWeight*muonEffTrgWeight",

            "(pt_1>29)*(pt_2>30)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(dilepton_veto < 0.5)*(iso_1 < 0.15)*(byTightIsolationMVArun2v1DBoldDMwLT_2>0.5)*(mt_1<50)*(trg_muontau_lowptmu==1)*(gen_match_2==5)*generatorWeight*muonEffTrgWeight"
        ],
        y_label=y_label,
        subplot_denominator=1,
        subplot_numerators=[2,3],
        y_subplot_lims=[0.6, 1.4],
        add_nicks=[0, 1],
        add_result_nicks=1,
        add_scale_factors=[1, 1],
        output_dir=output_dir + '/crosstrigger_mt/',
        y_subplot_label="Ratio to sim.",
        plotlines=[
            DYFall17_mt, 
            TTFall17_mt,
            Embedded_trigger_old_mt,
            Embedded_trigger_new_mt
        ])

    visibleMassMuMu_cleaning = default.clone(
        name="mm",
        title="#mu#mu",
        normalized_to_hist1=True,
        weight=[
            weightscale_mm + "*(pt_1>20 && pt_2>10)",
            weightscale_mm + "*(pt_1>20 && pt_2>10)",
            weightscale_mm + "*(pt_1>20 && pt_2>10)"
        ],
        y_label=y_label,
        subplot_denominator=0,
        subplot_numerators=[1,2],
        output_dir=output_dir + '/mm_cleaning/',
        y_subplot_lims=subplot_ratio,
        horizontal_subplot_lines=subplot_ticks,
        y_subplot_label="Ratio to sim.",
        plotlines=[
             MuMu_Embedding_dy_comparison, 
             MuMu_Embedding_old_cleaning,
             MuMu_Embedding_new_cleaning
        ])
    
    visibleMassMuMu_cleaning_pfc = default.clone(
        name="mm",
        title="#mu#mu",
        normalized_to_hist1=False,
        y_label=y_label,
        subplot_denominator=0,
        subplot_numerators=[1,2],
        output_dir=output_dir + '/mm_cleaning_pfc/',
        y_subplot_lims=subplot_ratio,
        horizontal_subplot_lines=subplot_ticks,
        y_subplot_label="Ratio to sim.",
        plotlines=[
             MuMu_Embedding_dy_comparison_pfc, 
             MuMu_Embedding_old_cleaning_pfc, 
             MuMu_Embedding_new_cleaning_pfc
        ])

    visibleMassEE = default.clone(
        name="ee",
        title="ee ",
        x_expression=variable,
        normalized_to_hist1=True,       
        y_label=y_label,
        # weight=[
        #     "(eta_t < 1.479)",
        #     "(eta_t < 1.479)",
        #     "(eta_t < 1.479)",
        # ],
        # weight = 
        # [
        #      "pt_p > 15",
        #      "pt_p > 15",
        #      "pt_p > 15"   
        # ],
        subplot_denominator=0,
        subplot_numerators=[1,2],
        output_dir=output_dir + '/variables/',
        #vertical_lines=[0.00632],
        #vertical_lines=[0.0032],
        y_subplot_lims=subplot_ratio,
        horizontal_subplot_lines=subplot_ticks,
        y_subplot_label="Ratio to sim.",
        plotlines=[
            data_ee,
            embedded_ee,
            dy_ee
            
        ])

    if 'et' in channel:
        configs.extend(
            visibleMassElTau.
            return_json_with_changed_x_and_weight(x_expressions=[variable]))
    if "ee" in channel:
         configs.extend(
            visibleMassEE.
            return_json_with_changed_x_and_weight(x_expressions=[variable]))
    if 'mm' in channel:
        configs.extend(
            visibleMassMuMu_cleaning_pfc.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
    if 'mt' in channel:
        configs.extend(
            visibleMassMuTau.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
    if 'tt' in channel:
            configs.extend(
            visibleMassTauTau.return_json_with_changed_x_and_weight(
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
        help=
        "Specify what Binning should be used, Default: 'default', other options are 'analysis' "
    )

    args = parser.parse_args()
    logger.initLogger(args)
    configs = []
    output_dir = args.output_dir
    input_dir = args.input_dir
    data = json.load(open('scripts/variables.json'))
    print args.channel
    for channel in args.channel:
        try:
            variables_to_plot = data["preset"][args.preset]
        except KeyError:
            pass
        if args.quantities is not None:
            variables_to_plot = args.quantities
        for v in variables_to_plot:
            #read legend position
            try:
                legend_pos = legend = data[args.mode + "_plotting_dict"][v][
                    channel]["legend_position"]
            except KeyError:
                try:
                    legend_pos = legend = data["default_plotting_dict"][v][
                        channel]["legend_position"]
                except KeyError:
                    try:
                        legend_pos = legend = data["default_plotting_dict"][v][
                            "default"]["legend_position"]
                    except KeyError:
                        legend_pos = 1
            try:
                plot_root_variable(
                    variable=v,
                    xlabel=data[args.mode
                                + "_plotting_dict"][v][channel]["x_label"],
                    x_bins=data[args.mode
                                + "_plotting_dict"][v][channel]["x_bins"],
                    legend=legend_pos,
                    channel=args.channel)
            except KeyError:
                try:
                    plot_root_variable(
                        variable=v,
                        xlabel=data["default_plotting_dict"][v][channel][
                            "x_label"],
                        x_bins=data["default_plotting_dict"][v][channel][
                            "x_bins"],
                        legend=legend_pos,
                        channel=args.channel)
                except KeyError:
                    try:
                        plot_root_variable(
                            variable=v,
                            xlabel=data["default_plotting_dict"][v]["default"][
                                "x_label"],
                            x_bins=data["default_plotting_dict"][v]["default"][
                                "x_bins"],
                            legend=legend_pos,
                            channel=args.channel)
                    except KeyError:
                        plot_root_variable(
                            variable=v,
                            xlabel=v,
                            x_bins=data["default_plotting_dict"]["not_listed"][
                                "default"]["x_bins"],
                            legend=legend_pos,
                            channel=args.channel)

        print "Plotting..."
        higgs_plotter = higgsplot.HiggsPlotter(
            list_of_config_dicts=configs,
            list_of_args_strings=[""],
            n_processes=args.n_processes)
