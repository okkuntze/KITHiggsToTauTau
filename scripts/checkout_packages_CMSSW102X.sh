#!/bin/bash

if [ "$1" == "" ]; then
  echo "$0: Please provide the analysis branch you want to use"
  exit 1
fi
BRANCH=$1

CORES=`grep -c ^processor /proc/cpuinfo`
if [ ! "$2" == "" ]; then
  CORES=$2
fi

export SCRAM_ARCH=slc6_amd64_gcc700
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# set up CMSSW release area
scramv1 project CMSSW_10_2_13; pushd CMSSW_10_2_13/src
eval `scramv1 runtime -sh`

# JEC
git cms-addpkg CondFormats/JetMETObjects

# From Kappa, only the DataFormats are needed
# Mind that for certain skims, you need exactly the Kappa git tag that has been used for the production
git clone https://github.com/KIT-CMS/Kappa.git -b dictchanges_10_2
pushd Kappa
echo docs/ >> .git/info/sparse-checkout
echo DataFormats/ >> .git/info/sparse-checkout
echo Skimming/ >> .git/info/sparse-checkout
git config core.sparsecheckout true
git read-tree -mu HEAD
popd

git clone https://github.com/KIT-CMS/KappaTools.git -b master

git clone https://github.com/KIT-CMS/Artus.git -b reduced_trigger_objects

# checkout KITHiggsToTauTau CMSSW analysis package
git clone https://github.com/KIT-CMS/KITHiggsToTauTau HiggsAnalysis/KITHiggsToTauTau -b reduced_trigger_objects

# quantile mapping package
git clone https://github.com/KIT-CMS/quantile_mapping

# Svfit
git clone https://github.com/svfit/ClassicSVfit TauAnalysis/ClassicSVfit
cd TauAnalysis/ClassicSVfit
git checkout c78af4dc0f54cdc1c0d4b4fc4879918cfa2527c9
cd -
git clone https://github.com/svfit/SVfitTF TauAnalysis/SVfitTF

# Jet2Tau Fakes
git clone https://github.com/CMS-HTT/Jet2TauFakes.git HTTutilities/Jet2TauFakes

# EmuQCD Method
git clone https://github.com/CMS-HTT/QCDModelingEMu.git HTT-utilities/QCDModelingEMu

sed '/CombineHarvester/d' ${CMSSW_BASE}/src/HiggsAnalysis/KITHiggsToTauTau/BuildFile.xml -i

# TauTriggerSFs2017 tool
git clone https://github.com/truggles/TauTriggerSFs2017.git  TauAnalysisTools/TauTriggerSFs -b final_2017_MCv2

# Grid-Control
git clone https://github.com/janekbechtel/grid-control.git

# source ini script, needs to be done in every new shell
source HiggsAnalysis/KITHiggsToTauTau/scripts/ini_KITHiggsToTauTauAnalysis.sh

# compile everything
scram b -j $CORES
popd
