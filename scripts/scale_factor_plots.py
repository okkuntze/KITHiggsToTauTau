#!/usr/bin/env python

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import json
import HiggsAnalysis.KITHiggsToTauTau.plotting.higgsplot as higgsplot

import HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plot_classes as pltcl
from HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_scalefactor_bib import *

def plot_root_variable(channel=['m'],
                       variable='pt_1',
                       name = '',
                       title = '',
                       x_bins="30,0,120",
                       xlabel='',
                       y_subplot_lims=[],
                       y_lims=[],
                       horizontal_subplot_lines=[],
                       y_ticks=[],
                       legend=1):
    # Define Legend Positions
    if legend == 1: #top right
        legend_pos = [0.48, 0.52, 0.9, 0.82]
    elif legend == 2:
        # top left
        legend_pos = [0.20, 0.52, 0.58, 0.82]
    elif legend == 3:  # bottom middle
        legend_pos = [0.32, 0.08, 0.74, 0.38]
    elif legend == 4:  # top middle
        legend_pos = [0.32, 0.52, 0.74, 0.84]
    elif legend == 5: #top right
        legend_pos = [0.48, 0.08, 0.9, 0.38]
    elif legend == 6: # bottom right
        legend_pos = [0.55, 0.08, 0.93, 0.38]
    
    default = pltcl.single_plot(
        x_expression=variable,
        name=name,
        title=title,
        normalized_by_binwidth=False,
        x_bins=x_bins,
        x_label=xlabel,
        y_label="Efficiency",
        plot_type="absolute",
        legend=legend_pos,
        y_subplot_lims=y_subplot_lims,
        y_subplot_label="Ratio to data",
        y_lims=y_lims,
        y_ticks = y_ticks,
        horizontal_subplot_lines=horizontal_subplot_lines,
        print_infos=True,
        y_log=False)

    muon_scalefactors = default.clone(
        x_log = True,
        weight = ["1","1","1"],
        subplot_denominator=0,
        output_dir=output_dir + '/muon_scalefactor/',
        subplot_numerators=[1,2],
        plotlines = [
            muon_data,
            muon_dy,
            muon_emb
        ])
    singlemuon_scalefactors = muon_scalefactors.clone(
        output_dir=output_dir + '/singlemuon_scalefactor/',
        plotlines = [
            singlemuon_data,
            muon_dy,
            muon_emb
        ])
    electron_scalefactors = default.clone(
        x_log = True,
        weight = ["1","1","1"],
        subplot_denominator=0,
        output_dir=output_dir + '/electron_scalefactor/',
        subplot_numerators=[1,2],
        plotlines = [
            ele_data,
            ele_dy,
            ele_emb
        ]

    )
    if 'm' in channel:
        configs.extend(
            muon_scalefactors.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
    if 'e' in channel:
        configs.extend(
            electron_scalefactors.return_json_with_changed_x_and_weight(
                x_expressions=[variable]))
    if 'sm' in channel:
        configs.extend(
            singlemuon_scalefactors.return_json_with_changed_x_and_weight(
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
        default=['m', 'e','sm'],
        nargs="*",
        help="Select decay channel. [Default: %(default)s]")
    parser.add_argument(
        "-n",
        "--n-processes",
        required=False,
        default=1,
        help="Number of parallel processes. [Default: %(default)s]")

    args = parser.parse_args()
    logger.initLogger(args)
    configs = []
    output_dir = args.output_dir
    input_dir = args.input_dir
    data = json.load(open('scripts/scalefactors.json'))
    print args.channel
    for channel in args.channel:
        for variable in data[channel]:
            for i in xrange(1,len(data[channel][variable]["eta_bins"])):
                eta_ext = "_projx_" + str(i)
                title_ext = "[" + str(data[channel][variable]["eta_bins"][i-1]) + "," + str(data[channel][variable]["eta_bins"][i]) + "]"
                plot_root_variable(
                       channel=channel,
                       variable=variable + eta_ext,
                       name = data[channel][variable]["name"],
                       title = data[channel][variable]["title"] + title_ext,
                       x_bins=data[channel][variable]["x_bins"],
                       xlabel=data[channel][variable]["x_label"],
                       y_subplot_lims=data[channel][variable]["subplot_range"],
                       y_lims=data[channel][variable]["plot_range"],
                       horizontal_subplot_lines=data[channel][variable]["subplot_ticks"],
                       y_ticks=data[channel][variable]["plot_ticks"],
                       legend=data[channel][variable]["legend_position"])
        print "Plotting..."
        higgs_plotter = higgsplot.HiggsPlotter(
            list_of_config_dicts=configs,
            list_of_args_strings=[""],
            n_processes=args.n_processes)
