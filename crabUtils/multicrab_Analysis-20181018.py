"""MultiCRAB script template for EmergingJet analysis"""
MC=0
DATA=1

jobname = 'Analysis-20181018'        # Jobname
psetname = 'Configuration/test/test_cfg.py'      # Path to pset
postfix = 'test1'                # Postfix to job, increment for each major version
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

# Data
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

datasets = [
    ## 2016 Official MC 80X
##    dataset(alias="ModelA",
##            fullpath="/EmergingJets_mX-1000-m_dpi-5-tau_dpi-150_TuneCUETP8M1_13TeV_pythia8_v2/RunIISummer16DR80-FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/AODSIM", isData=False, unitsPerJob=1, totalUnits=1000000, splitting="FileBased", priority=99, label="signal"),

##    dataset(alias="ModelB",
##            fullpath="/EmergingJets_mX-1000-m_dpi-2-tau_dpi-5_TuneCUETP8M1_13TeV_pythia8_v2/RunIISummer16DR80-FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/AODSIM", isData=False, unitsPerJob=1, totalUnits=1000000, splitting="FileBased", priority=99, label="signal"),

    ## 2017 QCD 94X
##    dataset(alias="QCD_HT200to300",
##            fullpath="/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=10, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT300to500",
##            fullpath="/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=10, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT500to700",
##            fullpath="/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM", isData=False, unitsPerJob=10, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT700to1000",
##            fullpath="/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=10, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT1000to1500",
##            fullpath="/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_new_pmx_94X_mc2017_realistic_v11-v1/AODSIM", isData=False, unitsPerJob=10, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
##    dataset(alias="QCD_HT1500to2000",
##            fullpath="/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM", isData=False, unitsPerJob=10, totalUnits=10000, splitting="FileBased", priority=25, label="background", doHLT=0, doJetFilter=1),
    dataset(alias="QCD_HT2000toInf",
            fullpath="/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM", isData=False, unitsPerJob=10, totalUnits=10000, splitting="FileBased", priority=99, label="background", doHLT=0, doJetFilter=1),

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

    config.General.workArea = crabTaskDir + '/' + 'crab_' + jobname + time.strftime("-%Y-%m%d") + '-' + postfix
    tasklistFileName = config.General.workArea + '.txt'
    if not dryrun: tasklistFile = open(tasklistFileName, 'a')

    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = psetname
    # config.JobType.scriptExe = 'crab_script.sh'                                # Script to run instead of cmsRun
    # config.JobType.inputFiles = ['emjet-basicJetAnalyzer.py','crab_script.py'] # Additional input files
    # config.JobType.outputFiles = ['histo.root']                                # Collect non-EDM outputs if any

    config.Data.splitting = 'FileBased'
    config.Data.publication = False
    config.Data.outputDatasetTag = jobname
    config.Data.ignoreLocality = True

    config.Site.storageSite = "T3_US_UMD"
    #config.Site.blacklist = ['T3_US_UCR']
    # config.Site.whitelist = ['T3_US_UMD']
    config.Site.whitelist = ['T2_US_MIT', 'T2_US_Purdue', 'T2_US_Nebraska', 'T2_US_Wisconsin']
    # config.Site.ignoreGlobalBlacklist = True

    ############################################################
    ## Dataset specific settings
    ############################################################
    for dataset in datasets:
        alias = dataset.alias
        pyCfgParams = ['crab=1'] # Temporary list, must be written to config.JobType.pyCfgParams before submitting
        config.General.requestName   = ('%s-%s' + time.strftime("-%Y-%m%d-%H%M%S")) % (jobname, alias)
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
            config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
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

