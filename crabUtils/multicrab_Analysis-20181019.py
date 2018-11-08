"""MultiCRAB script template for EmergingJet analysis"""
MC=0
DATA=1

jobname = 'Analysis-20181019'        # Jobname
psetname = 'Configuration/test/test_cfg.py'      # Path to pset
postfix = 'v1'                # Postfix to job, increment for each major version
dryrun = 0


from datasets import dataset, load_datasets
from wrappers import submit, submit_newthread

# Import short name for datasets
#from datasets_AODSIM_2018_10_18 import *

## private
##ModelA           = "/EmergingJets_mass_X_d_1000_mass_pi_d_5_tau_pi_d_150_TuneCUETP8M1_13TeV_pythia8Mod/yoshin-RunIISummer16DR80Premix_private-AODSIM-v2017-05-02-9b8a2f7f8fb796283f35935e0ffa8bb2/USER"
##ModelB           = "/EmergingJets_mass_X_d_1000_mass_pi_d_2_tau_pi_d_5_TuneCUETP8M1_13TeV_pythia8Mod/yoshin-RunIISummer16DR80Premix_private-AODSIM-v2017-05-02-9b8a2f7f8fb796283f35935e0ffa8bb2/USER"

## official MC
ModelA           = "/EmergingJets_mX-1000-m_dpi-5-tau_dpi-150_TuneCUETP8M1_13TeV_pythia8_v2/RunIISummer16DR80-FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/AODSIM"
ModelB           = "/EmergingJets_mX-1000-m_dpi-2-tau_dpi-5_TuneCUETP8M1_13TeV_pythia8_v2/RunIISummer16DR80-FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/AODSIM"

## 2016
QCD_HT50to100    = "/QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
QCD_HT100to200   = "/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
QCD_HT200to300   = "/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
QCD_HT300to500   = "/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
QCD_HT500to700   = "/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
QCD_HT700to1000  = "/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
QCD_HT1000to1500 = "/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
QCD_HT1500to2000 = "/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
QCD_HT2000toInf  = "/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"

QCD_HT700to1000x = "/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/AODSIM"
QCD_HT1000to1500x= "/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/AODSIM"
QCD_HT1500to2000x= "/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/AODSIM"
QCD_HT2000toInfx = "/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/AODSIM"

TTbar            = "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"
WJet             = "/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM"

# Data 2016
JetHT_B1         = "/JetHT/Run2016B-23Sep2016-v1/AOD"
JetHT_B3         = "/JetHT/Run2016B-23Sep2016-v3/AOD"
JetHT_C1         = "/JetHT/Run2016C-23Sep2016-v1/AOD"
JetHT_D1         = "/JetHT/Run2016D-23Sep2016-v1/AOD"
JetHT_E1         = "/JetHT/Run2016E-23Sep2016-v1/AOD"
JetHT_F1         = "/JetHT/Run2016F-23Sep2016-v1/AOD"
JetHT_G1         = "/JetHT/Run2016G-23Sep2016-v1/AOD"
JetHT_H1         = "/JetHT/Run2016H-PromptReco-v1/AOD"
JetHT_H2         = "/JetHT/Run2016H-PromptReco-v2/AOD"
JetHT_H3         = "/JetHT/Run2016H-PromptReco-v3/AOD"

SingleMuon_B1    = "/SingleMuon/Run2016B-23Sep2016-v1/AOD"
SingleMuon_B3    = "/SingleMuon/Run2016B-23Sep2016-v3/AOD"
SingleMuon_C1    = "/SingleMuon/Run2016C-23Sep2016-v1/AOD"
SingleMuon_D1    = "/SingleMuon/Run2016D-23Sep2016-v1/AOD"
SingleMuon_E1    = "/SingleMuon/Run2016E-23Sep2016-v1/AOD"
SingleMuon_F1    = "/SingleMuon/Run2016F-23Sep2016-v1/AOD"
SingleMuon_G1    = "/SingleMuon/Run2016G-23Sep2016-v1/AOD"
SingleMuon_H1    = "/SingleMuon/Run2016H-PromptReco-v1/AOD"
SingleMuon_H2    = "/SingleMuon/Run2016H-PromptReco-v2/AOD"
SingleMuon_H3    = "/SingleMuon/Run2016H-PromptReco-v3/AOD"

# Data 2017
JetHT17_B        = "/JetHT/Run2017B-17Nov2017-v1/AOD"
JetHT17_C        = "/JetHT/Run2017C-17Nov2017-v1/AOD"
JetHT17_D        = "/JetHT/Run2017D-17Nov2017-v1/AOD"
JetHT17_E        = "/JetHT/Run2017E-17Nov2017-v1/AOD"
JetHT17_F        = "/JetHT/Run2017F-17Nov2017-v1/AOD"

GJet17_B         = "/SinglePhoton/Run2017B-17Nov2017-v1/AOD"
GJet17_C         = "/SinglePhoton/Run2017C-17Nov2017-v1/AOD"
GJet17_D         = "/SinglePhoton/Run2017D-17Nov2017-v1/AOD"
GJet17_E         = "/SinglePhoton/Run2017E-17Nov2017-v1/AOD"
GJet17_F         = "/SinglePhoton/Run2017F-17Nov2017-v1/AOD"


datasets = [
    ## 2016 Official MC 80X (8_0_29)
##    dataset(alias="ModelA",
##            fullpath="/EmergingJets_mX-1000-m_dpi-5-tau_dpi-150_TuneCUETP8M1_13TeV_pythia8_v2/RunIISummer16DR80-FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/AODSIM", isData=False, unitsPerJob=1, totalUnits=1000000, splitting="FileBased", priority=99, label="signal"),

##    dataset(alias="ModelB",
##            fullpath="/EmergingJets_mX-1000-m_dpi-2-tau_dpi-5_TuneCUETP8M1_13TeV_pythia8_v2/RunIISummer16DR80-FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/AODSIM", isData=False, unitsPerJob=1, totalUnits=1000000, splitting="FileBased", priority=99, label="signal"),

    ## 2017 QCD 94X
##    dataset(alias="QCD_HT200to300",
##            fullpath="/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT300to500",
##            fullpath="/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT500to700",
##            fullpath="/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT700to1000",
##            fullpath="/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT1000to1500",
##            fullpath="/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_new_pmx_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=2, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT1500to2000",
##            fullpath="/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM", isData=False, unitsPerJob=2, totalUnits=10000, splitting="FileBased", priority=99, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT1500to2000",
##            fullpath="/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM", isData=False, unitsPerJob=2, totalUnits=10000, splitting="FileBased", priority=99, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT2000toInf",
##            fullpath="/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="background", doHLT=0, doJetFilter=1),

    ## GJets MC
##    dataset(alias="GJets_HT100to200",
##            fullpath="/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_4cores5k_94X_mc2017_realistic_v11-v3/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),
##    dataset(alias="GJets_HT200to400",
##            fullpath="/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),
##    dataset(alias="GJets_HT400to600",
##            fullpath="/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),

    dataset(alias="GJets_HT600toInf",
            fullpath="/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),

    ## v10-v1
##    dataset(alias="GJets_HT600toInf_v10-v1",
##            fullpath="/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),

##    dataset(alias="GJets_DR-0p4_HT100to200",
##            fullpath="/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),
##    dataset(alias="GJets_DR-0p4_HT200to400",
##            fullpath="/GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),
##    dataset(alias="GJets_DR-0p4_HT400to600",
##            fullpath="/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),
##    dataset(alias="GJets_DR-0p4_HT600toInf",
##            fullpath="/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM", isData=False, unitsPerJob=1, totalUnits=10000, splitting="FileBased", priority=99, label="gjet", doHLT=0, doJetFilter=0),

    ## 2017 Data
##    dataset( "JetHT17_B"    , JetHT17_B    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='signal' , doHLT=1, doJetFilter=1 )  ,
##    dataset( "JetHT17_C"    , JetHT17_C    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='signal' , doHLT=1, doJetFilter=1 )  ,
##    dataset( "JetHT17_D"    , JetHT17_D    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='signal' , doHLT=1, doJetFilter=1 )  ,
##    dataset( "JetHT17_E"    , JetHT17_E    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='signal' , doHLT=1, doJetFilter=1 )  ,
##    dataset( "JetHT17_F"    , JetHT17_F    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='signal' , doHLT=1, doJetFilter=1 )  ,

    ## 2017 Data for photon+jets skim (GJetFilter; doHLT and doJetFilter are dummy options here)
##    dataset( "GJet17_B"    , GJet17_B    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='gjet' , doHLT=0, doJetFilter=0 )  ,
##    dataset( "GJet17_C"    , GJet17_C    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='gjet' , doHLT=0, doJetFilter=0 )  ,
##    dataset( "GJet17_D"    , GJet17_D    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='gjet' , doHLT=0, doJetFilter=0 )  ,
##    dataset( "GJet17_E"    , GJet17_E    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='gjet' , doHLT=0, doJetFilter=0 )  ,
##    dataset( "GJet17_F"    , GJet17_F    , DATA , 20  , 100000000 , splitting='LumiBased' , priority=199 , label='gjet' , doHLT=0, doJetFilter=0 )  ,

]

datasets_part2 = [
#     # def __init__(self, alias, fullpath, isData, unitsPerJob=1, totalUnits=1, splitting='FileBased', priority=1, inputDBS='global', label='', doHLT=1, doJetFilter=0):
#     # dataset( "Dummy" , Dummy , MC , 1 , 10000 , splitting='FileBased' , priority=99 , label='signal' ) ,
    # dataset( "mass_X_d_1000_mass_pi_d_1_tau_pi_d_0p001"  , mass_X_d_1000_mass_pi_d_1_tau_pi_d_0p001  , MC , 1 , 10000 , splitting='FileBased' , priority=99 , inputDBS='phys03' , label='signal' , doHLT=0 ) ,
]

#template = dataset( "ALIAS"  , "/FULL/PATH-TO/DATSET"  , MC , 1 , 1000000 , splitting='FileBased' , priority=99 , inputDBS='phys03' , label='signal' , doHLT=0 )
template = dataset( "ALIAS"  , "/FULL/PATH-TO/DATSET"  , MC , 1 , 1000000 , splitting='FileBased' , priority=99 , inputDBS='global' , label='signal' , doHLT=0 )
#dataset_list = load_datasets('crabUtils/dataset_lists/list_RunIISummer16DR80Premix_private-AODSIM-v2017-09-11-longlifetime.txt', template)
#dataset_list = load_datasets('crabUtils/dataset_lists/list_RunIISummer16DR80_official-AODSIM-v2018-10-18.txt', template)
##print 'dataset_list'
##for i in dataset_list:
##    print i.alias, i.fullpath
##datasets = dataset_list
# datasets.extend(datasets_part2)

#exit()

import os
crabTaskDir = 'crabTasks'
if not os.path.exists(crabTaskDir):
    os.makedirs(crabTaskDir)

if __name__ == '__main__':

    ############################################################
    ## Common settings
    ############################################################
    from CRABClient.UserUtilities import config
    config = config()
    import time

    config.General.workArea = crabTaskDir + '/' + 'crab_' + jobname + '-' + postfix + time.strftime("-%Y-%m%d")
    tasklistFileName = config.General.workArea + '.txt'
    if not dryrun: tasklistFile = open(tasklistFileName, 'a')

    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = psetname
    # config.JobType.scriptExe = 'crab_script.sh'                                # Script to run instead of cmsRun
    # config.JobType.inputFiles = ['emjet-basicJetAnalyzer.py','crab_script.py'] # Additional input files
    # config.JobType.outputFiles = ['histo.root']                                # Collect non-EDM outputs if any

    config.Data.splitting = 'FileBased'
    config.Data.publication = False
    config.Data.outputDatasetTag = jobname + '-' + postfix
    config.Data.ignoreLocality = True

    config.Site.storageSite = "T3_US_UMD"
    #config.Site.blacklist = ['T3_US_UCR']
    #config.Site.whitelist = ['T1_US_FNAL','T2_US_*','T2_CH_*']
    #config.Site.whitelist = ['T1_UK_RAL'] # for QCD_HT1500to2000_v11-v2 and SinglePhoton GJet17_D
    #config.Site.whitelist = ['T1_DE_KIT', 'T1_UK_RAL'] # for SinglePhoton GJet17_E
    #config.Site.whitelist = ['T2_CH_CERN', 'T2_CH_CSCS', 'T2_IT_Legnaro'] # for GJet17_F
    #config.Site.whitelist = ['T1_US_FNAL', 'T1_UK_RAL', 'T2_US_MIT', 'T2_US_Purdue', 'T2_US_Nebraska', 'T2_US_UCSD', 'T2_US_Wisconsin', 'T2_US_Vanderbilt', 'T2_US_Caltech', 'T2_US_Florida', 'T2_CH_CERN']
    #config.Site.whitelist = ['T1_US_FNAL', 'T2_BR_SPRACE', 'T2_US_MIT', 'T2_US_Purdue', 'T2_US_Nebraska', 'T2_US_UCSD', 'T2_US_Wisconsin', 'T2_US_Vanderbilt', 'T2_US_Caltech', 'T2_US_Florida', 'T2_CH_CERN']
    #config.Site.whitelist = ['T1_US_FNAL', 'T2_BE_UCL', 'T2_US_MIT', 'T2_US_Purdue', 'T2_US_Nebraska', 'T2_US_UCSD', 'T2_US_Wisconsin', 'T2_US_Vanderbilt', 'T2_US_Caltech', 'T2_US_Florida']#2017 data C
    #config.Site.whitelist = ['T2_CH_CERN', 'T1_RU_JINR']#2017 SinglePhoton GJet17 B
    #config.Site.whitelist = ['T2_CH_CERN', 'T2_US_Caltech']#2017 SinglePhoton GJet17 C
    #config.Site.whitelist = ['T1_RU_JINR', 'T1_UK_RAL'] # JetHT17_D
    #config.Site.whitelist = ['T1_DE_KIT'] # JetHT17_E
    #config.Site.whitelist = ['T3_US_FNALLPC', 'T1_US_FNAL', 'T1_DE_KIT'] # JetHT17_F
    #config.Site.whitelist = ['T1_US_FNAL', 'T2_CH_CERN', 'T1_DE_KIT', 'T2_US_Caltech', 'T1_ES_PIC', 'T1_FR_CCIN2P3', 'T2_HU_Budapest']#2017 GJets MC
    config.Site.whitelist = ['T2_EE_Estonia', 'T2_CH_CERN', 'T2_US_MIT', 'T2_US_Purdue', 'T2_US_Nebraska', 'T2_US_UCSD', 'T2_US_Wisconsin', 'T2_US_Vanderbilt', 'T2_US_Caltech', 'T2_US_Florida']
    # config.Site.ignoreGlobalBlacklist = True

    ############################################################
    ## Dataset specific settings
    ############################################################
    for dataset in datasets:
        alias = dataset.alias
        pyCfgParams = ['crab=1'] # Temporary list, must be written to config.JobType.pyCfgParams before submitting
        config.General.requestName   = ('%s-%s-%s' + time.strftime("-%Y-%m%d-%H%M%S")) % (jobname, postfix, alias)
        config.Data.outLFNDirBase = '/store/user/jengbou/EmJet/ntuple/%s-%s/%s/' % (jobname, postfix, alias)
        config.Data.inputDataset = dataset.fullpath
        config.Data.unitsPerJob  = dataset.unitsPerJob
        config.Data.totalUnits   = dataset.totalUnits
        isData                   = dataset.isData
        config.Data.splitting    = dataset.splitting
        config.JobType.priority  = dataset.priority
        config.Data.inputDBS     = dataset.inputDBS
        label                    = dataset.label
        doHLT                    = dataset.doHLT
        doJetFilter              = dataset.doJetFilter
        # MC specific settings:
        if not isData:
            pyCfgParams.append('data=0')
        # Data specific settings:
        if isData:
            pyCfgParams.append('data=1')
            ## 2016
            #config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
            ## 2017
            config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
        pyCfgParams.append('steps=skim,analyze')
        # Label specific settings
        pyCfgParams.append('sample='+label)
        pyCfgParams.append('doHLT=%d' % doHLT)
        pyCfgParams.append('doJetFilter=%d' % doJetFilter)
        config.JobType.pyCfgParams = pyCfgParams

        res = submit_newthread(config, dryrun)
        if not dryrun:
            #res = submit_newthread(config, dryrun=dryrun)
            taskId = res['uniquerequestname'].split(':')[0]
            filePath = '%s%s/%s/%s/' % ( config.Data.outLFNDirBase, config.Data.inputDataset.split('/')[1], config.Data.outputDatasetTag, taskId )
            print 'filePath:'
            print filePath
            tasklistFile.write(filePath)
            tasklistFile.write('\n')

    if not dryrun: tasklistFile.close()

