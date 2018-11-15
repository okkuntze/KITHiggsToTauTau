#!/usr/bin/env python

import HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plot_classes as pltcl
 
# Embedding17_em = pltcl.single_plotline(
# 	name = "Embedding17_em",
# 	num_file = "/storage/9/sbrommer/artus_outputs/shape_comparison/2018-06-01/ElMuEmbedding2017.root",
# 	num_folder = "em_nominal",
# 	den_folder = "em_nominal",
# 	num_tree = "ntuple",
# 	label = "#mu#rightarrow#tau embedded Run 2017"
# )

muon_data = pltcl.single_plotline(
	name = "Data",
	num_file = "/storage/9/sbrommer/artus_outputs/TagAndProbe/2018-11-09/output/ZmmTP_Data_merge.root",
	num_folder = "",
	den_folder = "",
	num_tree = "",
	marker = "LINE",
	color = "kRed kWhite",
	label = "Data Muon"
)

singlemuon_data = pltcl.single_plotline(
	name = "Data",
	num_file = "/storage/9/sbrommer/artus_outputs/TagAndProbe/2018-11-09/output/ZmmTP_Data_sm_merge.root",
	num_folder = "",
	den_folder = "",
	num_tree = "",
	marker = "LINE",
	color = "kRed kWhite",
	label = "Data SingleMuon"
)

muon_dy = pltcl.single_plotline(
	name = "Data",
	num_file = "/storage/9/sbrommer/artus_outputs/TagAndProbe/2018-11-09/output/ZmmTP_DY_merge.root",
	num_folder = "",
	den_folder = "",
	num_tree = "",
	marker = "LINE",
	color = "kBlue kWhite",
	label = "Z #rightarrow #mu#mu (simulation)"
)

muon_emb = pltcl.single_plotline(
	name = "Data",
	num_file = "/storage/9/sbrommer/artus_outputs/TagAndProbe/2018-11-09/output/ZmmTP_Embedding_merge.root",
	num_folder = "",
	den_folder = "",
	num_tree = "",
	marker = "LINE",
	color = "kGreen kWhite",
	label = "Z #rightarrow #mu#mu (embedded)"
)
ele_data = pltcl.single_plotline(
	name = "Data",
	num_file = "/storage/9/sbrommer/artus_outputs/TagAndProbe/2018-11-09/output/ZeeTP_Data_merge.root",
	num_folder = "",
	den_folder = "",
	num_tree = "",
	marker = "LINE",
	color = "kRed kWhite",
	label = "Data"
)

ele_dy = pltcl.single_plotline(
	name = "Data",
	num_file = "/storage/9/sbrommer/artus_outputs/TagAndProbe/2018-11-09/output/ZeeTP_DY_merge.root ",
	num_folder = "",
	den_folder = "",
	num_tree = "",
	marker = "LINE",
	color = "kBlue kWhite",
	label = "Z #rightarrow ee (simulation)"
)

ele_emb = pltcl.single_plotline(
	name = "Data",
	num_file = "/storage/9/sbrommer/artus_outputs/TagAndProbe/2018-11-09/output/ZeeTP_Embedding_merge.root",
	num_folder = "",
	den_folder = "",
	num_tree = "",
	marker = "LINE",
	color = "kGreen kWhite",
	label = "Z #rightarrow ee (embedded)"
)
