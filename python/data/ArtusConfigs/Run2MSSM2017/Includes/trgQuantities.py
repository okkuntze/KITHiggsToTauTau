#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)


def build_list(**kwargs):
    minimal_setup = True if "minimal_setup" in kwargs and kwargs["minimal_setup"] else False

    # triggers flags that are needed to run the analysis
    quantities = [
        "trg_crossele_ele24tau30",
        "trg_crossmuon_mu20tau27",
        "trg_doubletau_35_tightiso_tightid",
        "trg_doubletau_40_mediso_tightid",
        "trg_doubletau_40_tightiso",
        "trg_muonelectron_mu23ele12",
        "trg_muonelectron_mu8ele23",
        "trg_singleelectron_27",
        "trg_singleelectron_32",
        "trg_singleelectron_35",
        "trg_singlemuon_24",
        "trg_singlemuon_27",
    ]

    if not minimal_setup:
        quantities.extend([
            "trg_singleelectron_32_fallback",
            "trg_singletau_leading",
            "trg_singletau_trailing",
        ])

    return list(set(quantities))
