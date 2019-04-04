#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)


def build_list(**kwargs):
    minimal_setup = True if "minimal_setup" in kwargs and kwargs["minimal_setup"] else False

    # quantities that are needed to run the analysis
    quantities = [
        "againstElectronVLooseMVA6_1",
        "againstElectronVLooseMVA6_2",
        "againstMuonLoose3_1",
        "againstMuonLoose3_2",
        "againstMuonTight3_2",

        "byLooseIsolationMVArun2v1DBoldDMwLT_1",
        "byTightIsolationMVArun2v1DBoldDMwLT_1",
        "byTightIsolationMVArun2v1DBoldDMwLT_2",
        "byVTightIsolationMVArun2v1DBoldDMwLT_2",

        "byMediumIsolationMVArun2017v2DBoldDMwLT2017_1",
        "byTightIsolationMVArun2017v2DBoldDMwLT2017_1",
        "byVLooseIsolationMVArun2017v2DBoldDMwLT2017_1",
        "byMediumIsolationMVArun2017v2DBoldDMwLT2017_2",
        "byTightIsolationMVArun2017v2DBoldDMwLT2017_2",
        "byVLooseIsolationMVArun2017v2DBoldDMwLT2017_2",
    ]

    if not minimal_setup:
        quantities.extend([
            # "ElectronMVAEstimatorRun2Fall17IsoV1Values_1",
            # "ElectronMVAEstimatorRun2Fall17IsoV1Values_2",
            # "ElectronMVAEstimatorRun2Fall17NoIsoV1Values_1",
            # "ElectronMVAEstimatorRun2Fall17NoIsoV1Values_2",

            # "ElectronMVAEstimatorRun2Fall17IsoV2Values_1",
            # "ElectronMVAEstimatorRun2Fall17IsoV2Values_2",
            # "ElectronMVAEstimatorRun2Fall17NoIsoV2Values_1",
            # "ElectronMVAEstimatorRun2Fall17NoIsoV2Values_2",

            "againstElectronVLooseMVA6_1",
            "againstElectronLooseMVA6_1",
            "againstElectronMediumMVA6_1",
            "againstElectronTightMVA6_1",
            "againstElectronVTightMVA6_1",

            "againstElectronVLooseMVA6_2",
            "againstElectronLooseMVA6_2",
            "againstElectronMediumMVA6_2",
            "againstElectronTightMVA6_2",
            "againstElectronVTightMVA6_2",

            "againstMuonLoose3_1",
            "againstMuonLoose3_2",
            "againstMuonTight3_1",
            "againstMuonTight3_2",

            "byCombinedIsolationDeltaBetaCorrRaw3Hits_1",
            "byCombinedIsolationDeltaBetaCorrRaw3Hits_2",
            "byLooseCombinedIsolationDeltaBetaCorr3Hits_1",
            "byLooseCombinedIsolationDeltaBetaCorr3Hits_2",
            "byMediumCombinedIsolationDeltaBetaCorr3Hits_1",
            "byMediumCombinedIsolationDeltaBetaCorr3Hits_2",
            "byTightCombinedIsolationDeltaBetaCorr3Hits_1",
            "byTightCombinedIsolationDeltaBetaCorr3Hits_2",

            "byIsolationMVArun2017v1DBoldDMwLTraw2017_1",
            "byIsolationMVArun2017v1DBoldDMwLTraw2017_2",
            "byVVLooseIsolationMVArun2017v1DBoldDMwLT2017_1",
            "byVVLooseIsolationMVArun2017v1DBoldDMwLT2017_2",
            "byVLooseIsolationMVArun2017v1DBoldDMwLT2017_1",
            "byVLooseIsolationMVArun2017v1DBoldDMwLT2017_2",
            "byLooseIsolationMVArun2017v1DBoldDMwLT2017_1",
            "byLooseIsolationMVArun2017v1DBoldDMwLT2017_2",
            "byMediumIsolationMVArun2017v1DBoldDMwLT2017_1",
            "byMediumIsolationMVArun2017v1DBoldDMwLT2017_2",
            "byTightIsolationMVArun2017v1DBoldDMwLT2017_1",
            "byTightIsolationMVArun2017v1DBoldDMwLT2017_2",
            "byVTightIsolationMVArun2017v1DBoldDMwLT2017_1",
            "byVTightIsolationMVArun2017v1DBoldDMwLT2017_2",
            "byVVTightIsolationMVArun2017v1DBoldDMwLT2017_1",
            "byVVTightIsolationMVArun2017v1DBoldDMwLT2017_2",

            "byIsolationMVArun2017v2DBoldDMwLTraw2017_1",
            "byIsolationMVArun2017v2DBoldDMwLTraw2017_2",
            "byVVLooseIsolationMVArun2017v2DBoldDMwLT2017_1",
            "byVVLooseIsolationMVArun2017v2DBoldDMwLT2017_2",
            "byVLooseIsolationMVArun2017v2DBoldDMwLT2017_1",
            "byVLooseIsolationMVArun2017v2DBoldDMwLT2017_2",
            "byLooseIsolationMVArun2017v2DBoldDMwLT2017_1",
            "byLooseIsolationMVArun2017v2DBoldDMwLT2017_2",
            "byMediumIsolationMVArun2017v2DBoldDMwLT2017_1",
            "byMediumIsolationMVArun2017v2DBoldDMwLT2017_2",
            "byTightIsolationMVArun2017v2DBoldDMwLT2017_1",
            "byTightIsolationMVArun2017v2DBoldDMwLT2017_2",
            "byVTightIsolationMVArun2017v2DBoldDMwLT2017_1",
            "byVTightIsolationMVArun2017v2DBoldDMwLT2017_2",
            "byVVTightIsolationMVArun2017v2DBoldDMwLT2017_1",
            "byVVTightIsolationMVArun2017v2DBoldDMwLT2017_2",

            "byIsolationMVArun2v1DBoldDMwLTraw_1",
            "byIsolationMVArun2v1DBoldDMwLTraw_2",
            "byVLooseIsolationMVArun2v1DBoldDMwLT_1",
            "byVLooseIsolationMVArun2v1DBoldDMwLT_2",
            "byLooseIsolationMVArun2v1DBoldDMwLT_1",
            "byLooseIsolationMVArun2v1DBoldDMwLT_2",
            "byMediumIsolationMVArun2v1DBoldDMwLT_1",
            "byMediumIsolationMVArun2v1DBoldDMwLT_2",
            "byTightIsolationMVArun2v1DBoldDMwLT_1",
            "byTightIsolationMVArun2v1DBoldDMwLT_2",
            "byVTightIsolationMVArun2v1DBoldDMwLT_1",
            "byVTightIsolationMVArun2v1DBoldDMwLT_2",
            "byVVTightIsolationMVArun2v1DBoldDMwLT_1",
            "byVVTightIsolationMVArun2v1DBoldDMwLT_2",

            "id_e_cut_loose_1",
            "id_e_cut_medium_1",
            "id_e_cut_tight_1",
            "id_e_cut_veto_1",
            "id_e_mva_nt_loose_1",
            "id_m_highpt_1",
            "id_m_loose_1",
            "id_m_medium_1",
            "id_m_tight_1",
        ])

    return list(set(quantities))
