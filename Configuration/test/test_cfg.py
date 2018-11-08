import FWCore.ParameterSet.Config as cms

########################################
# Command line argument parsing
########################################
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.register ('crab',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Set to 1 to run on CRAB.")
options.register ('data',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Set to 1 for data.")
sample_options = ['signal', 'background', 'wjet', 'gjet'] # Valid options for sample
options.register ('sample',
                  'signal', # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Specify type of sample. Valid values: %s" % sample_options)
steps_options = ['skim', 'analyze'] # Valid options for steps
options.register ('steps',
                  [],
                  VarParsing.VarParsing.multiplicity.list, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Steps to execute. Possible values: skim, analyze.")
options.steps = ['skim', 'analyze'] # default value
options.register ('doHLT',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Set to 1 to turn on HLT selection for skim step.")
options.register ('doJetFilter',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Set to 1 to turn on JetFilter for skim step.")
# options.register ('ntupleFile',
#                   'ntuple.root', # default value
#                   VarParsing.VarParsing.multiplicity.singleton, # singleton or list
#                   VarParsing.VarParsing.varType.string,          # string, int, or float
#                   "Specify plain root output file created by TFileService")
options.register ('outputLabel',
                  '', # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Specify label for both PoolOutputModule and TFileService output files.")
# Get and parse the command line arguments
options.parseArguments()
print ''
print 'Printing options:'
print options
print 'Only the following options are used: crab, data, sample, steps, doHLT, doJetFilter'
print ''

# Check validity of command line arguments
if options.sample not in sample_options:
    print 'Invalid sample type. Setting to sample type to signal.'
    options.sample = 'signal'
for step in options.steps:
    if step not in steps_options:
        print "Skipping invalid steps: %s" % step
        options.steps.remove(step)

print options.steps

from EmergingJetAnalysis.Configuration.emjetTools import *

process = cms.Process('TEST')
if 'skim' in options.steps and len(options.steps)==1:
    # If only running skim, change process name
    process.setName_('SKIM')

########################################
# Stable configuration
########################################
# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')


## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

## Options and Output Report
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False),
        # SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Unscheduled execution
#process.options.allowUnscheduled = cms.untracked.bool(False)
process.options.allowUnscheduled = cms.untracked.bool(True)

########################################
# Skim
########################################
import os
cmssw_version = os.environ['CMSSW_VERSION']
skimStep = cms.Sequence()
if 'skim' in options.steps:
    print ''
    print '####################'
    print 'Adding Skim step'
    print '####################'
    print ''
    if options.sample=='wjet':
        skimStep = addWJetSkim(process, options.data)
        if 'CMSSW_7_4_12' in cmssw_version:
            process.wJetFilter.electronID = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-medium')
        elif 'CMSSW_7_4_1_patch4' in cmssw_version:
            process.wJetFilter.electronID = cms.string('cutBasedElectronID-CSA14-50ns-V1-standalone-medium')
    elif options.sample=='gjet':
        skimStep = addGJetSkim(process, isData=options.data)
    else:
        skimStep = addSkim(process, isData=options.data, doJetFilter=options.doJetFilter, doHLT=options.doHLT)

########################################
# Analyze
########################################
analyzeStep = cms.Sequence()
if 'analyze' in options.steps:
    print ''
    print '####################'
    print 'Adding Analyze step'
    print '####################'
    print ''
    analyzeStep = addAnalyze(process, options.data, options.sample)

if options.sample=='gjet':
    phoSrc = cms.InputTag("gedPhotons")
    process.egmPhotonIDs.physicsObjectSrc = phoSrc
    process.photonIDValueMapProducer.src = phoSrc

########################################
# Testing step
########################################
testing = 0
testingStep = cms.Sequence()
if testing:
    testingStep = addTesting(process, options.data, options.sample)

##testMetFilters = 0
##if testMetFilters:
##    process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
##    #process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")#miniAOD
##    process.BadPFMuonFilter.muons = cms.InputTag("muons")
##    process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
##    process.BadPFMuonFilter.taggingMode = cms.bool(True)
##    process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
##    #process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")#miniAOD
##    process.BadChargedCandidateFilter.muons = cms.InputTag("muons")
##    process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
##    process.BadChargedCandidateFilter.taggingMode = cms.bool(True)
##    process.emJetAnalyzer.BadChargedCandidateFilter = cms.InputTag("BadChargedCandidateFilter")
##    process.emJetAnalyzer.BadPFMuonFilter = cms.InputTag("BadPFMuonFilter")
##    testMetFilterStep = cms.Sequence(process.BadPFMuonFilter * process.BadChargedCandidateFilter)

process.p = cms.Path( skimStep * testingStep * analyzeStep )
##if testMetFilters: process.p = cms.Path( testMetFilterStep * skimStep * testingStep * analyzeStep )


# MET Uncertainties
# from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
# runMetCorAndUncFromMiniAOD(process,
# 		isData=True,
# )

########################################
# Configure EDM Output
########################################
if 'skim' in options.steps and len(options.steps)==1:
    # If only running skim, add AOD/AODSIM and jetFilter/wJetFilter to output
    print ''
    print '####################'
    print 'Adding EDM output'
    print '####################'
    print ''
    addEdmOutput(process, options.data, options.sample)
else:
    # Otherwise only save EDM output of jetFilter and wJetFilter
    process.out = cms.OutputModule("PoolOutputModule",
        fileName = cms.untracked.string('output.root'),
        outputCommands = cms.untracked.vstring('drop *'),
        SelectEvents = cms.untracked.PSet( 
                       SelectEvents = cms.vstring("p")
        )
    )
##    if testMetFilters:
##       process.out.outputCommands.extend(cms.untracked.vstring('keep *_BadPFMuonFilter_*_*',))
##       process.out.outputCommands.extend(cms.untracked.vstring('keep *_BadChargedCandidateFilter_*_*',))

##    if options.sample=='wjet'  : process.out.outputCommands.extend(cms.untracked.vstring('keep *_wJetFilter_*_*',))
##    elif options.sample=='gjet': process.out.outputCommands.extend(cms.untracked.vstring('keep *_gJetFilter_*_*',))
##    else                       : process.out.outputCommands.extend(cms.untracked.vstring('keep *_jetFilter_*_*',))

testMETUnc = 0
process.emJetAnalyzer.doPATMET = cms.untracked.bool( False )
if testMETUnc:
    process.emJetAnalyzer.doPATMET = cms.untracked.bool( True )
    process.out = cms.OutputModule("PoolOutputModule",
        compressionLevel = cms.untracked.int32(4),
        compressionAlgorithm = cms.untracked.string('LZMA'),
        eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
        outputCommands = cms.untracked.vstring( "keep *_slimmedMETs_*_*",
                                                "keep *_slimmedMETsNoHF_*_*",
                                                "keep *_patPFMet_*_*",
                                                "keep *_patPFMetT1_*_*",
                                                "keep *_patPFMetT1JetResDown_*_*",
                                                "keep *_patPFMetT1JetResUp_*_*",
                                                "keep *_patPFMetT1Smear_*_*",
                                                "keep *_patPFMetT1SmearJetResDown_*_*",
                                                "keep *_patPFMetT1SmearJetResUp_*_*",
                                                "keep *_patPFMetT1Puppi_*_*",
                                                "keep *_slimmedMETsPuppi_*_*",
                                                ),
        fileName = cms.untracked.string('corMETMiniAOD.root'),
        dataset = cms.untracked.PSet(
            filterName = cms.untracked.string(''),
            dataTier = cms.untracked.string('')
        ),
        dropMetaData = cms.untracked.string('ALL'),
        fastCloning = cms.untracked.bool(False),
        overrideInputFileSplitLevels = cms.untracked.bool(True)
    )


########################################
# Generic configuration
########################################
if 'CMSSW_7_4_12' in cmssw_version:
    globalTags=['74X_mcRun2_design_v2','74X_dataRun2_Prompt_v3']
elif 'CMSSW_7_4_1_patch4' in cmssw_version:
    globalTags=['MCRUN2_74_V9','74X_dataRun2_Prompt_v0']
elif 'CMSSW_7_6_3' in cmssw_version:
    globalTags=['76X_mcRun2_asymptotic_RunIIFall15DR76_v1','76X_dataRun2_16Dec2015_v0']
elif 'CMSSW_8_0_26_patch1' in cmssw_version:
    # globalTags=['80X_mcRun2_asymptotic_2016_miniAODv2_v1','80X_dataRun2_2016SeptRepro_v7']
    globalTags=['80X_mcRun2_asymptotic_2016_TrancheIV_v8','80X_dataRun2_2016SeptRepro_v7']
elif 'CMSSW_9_4_10' in cmssw_version:
    #globalTags=['80X_mcRun2_asymptotic_2016_TrancheIV_v8','94X_dataRun2_v6']#2016 signal
    globalTags=['94X_mc2017_realistic_v14','94X_dataRun2_ReReco_EOY17_v6']
else: print 'No global tag specified for CMSSW_VERSION: %s' % cmssw_version
print 'CMSSW_VERSION is %s' % cmssw_version
print 'Using the following global tags [MC, DATA]:'
print globalTags
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, globalTags[options.data], '')

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)
##process.MessageLogger.threshold = cms.untracked.string('DEBUG')
process.MessageLogger.cerr.FwkReport.limit = 20
process.MessageLogger.cerr.default.limit = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.source = cms.Source("PoolSource",
    # eventsToProcess = cms.untracked.VEventRange("1:36:3523-1:36:3523"),
    # eventsToProcess = cms.untracked.VEventRange("281976:2166:min-281976:2166:max"),
    # eventsToProcess = cms.untracked.VEventRange("281976:2166:3740421624-281976:2166:max"),
    # eventsToProcess = cms.untracked.VEventRange("281976:2166:3739658361-281976:2166:3739658361"),
    fileNames = cms.untracked.vstring(
        # Signal samples
        # 2016 EmergingJet Official MC
        # modelA
        #'/store/mc/RunIISummer16DR80/EmergingJets_mX-1000-m_dpi-5-tau_dpi-150_TuneCUETP8M1_13TeV_pythia8_v2/AODSIM/FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/E8524A42-D992-E811-B912-FA163EBE0C61.root'
        #'file:/data/users/jengbou/EmJetMC/Tests/2017/E8524A42-D992-E811-B912-FA163EBE0C61.root'
        #'file:/home/jengbou/workspace/CMSSW_9_4_10/src/EmergingJetAnalysis/Configuration/test/output.root'# skim output
        #'/store/mc/RunIISummer16DR80/EmergingJets_mX-1000-m_dpi-5-tau_dpi-150_TuneCUETP8M1_13TeV_pythia8_v2/AODSIM/FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/D254A5FE-8592-E811-8345-A0369FD0B266.root'
        # modelB
        #'/store/mc/RunIISummer16DR80/EmergingJets_mX-1000-m_dpi-2-tau_dpi-5_TuneCUETP8M1_13TeV_pythia8_v2/AODSIM/FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/6247EBBD-B891-E811-93E2-FA163E1199C7.root'

        # 2017 QCD
        #'/store/mc/RunIIFall17DRPremix/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/0AC96F0B-CD59-E811-8B9F-0CC47A4D76D2.root'
        #'/store/mc/RunIIFall17DRPremix/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/10000/00B3E0FF-70F8-E711-9F37-0025905A6126.root'

        #'/store/mc/RunIIFall17DRPremix/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/64F7B641-25E8-E711-B504-FA163E5F2E72.root'
        #'/store/mc/RunIIFall17DRPremix/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/1010000/FE7566F2-9A62-E811-974F-FA163EE6807E.root'
        # 2017 data C JetHT
        #'/store/data/Run2017C/JetHT/AOD/17Nov2017-v1/70000/744DA565-A1DA-E711-AFDB-001E6739730A.root'
        #'file:/data/users/jengbou/EmJet/Tests/2017/744DA565-A1DA-E711-AFDB-001E6739730A.root'
        # SinglePhoton
        #'/store/data/Run2017B/SinglePhoton/AOD/17Nov2017-v1/20000/58EF0879-65D3-E711-AE06-7CD30ACE0FE7.root'
        'file:/data/users/jengbou/EmJet/Tests/2017/SinglePhoton/58EF0879-65D3-E711-AE06-7CD30ACE0FE7.root'
        #"/store/mc/RunIIFall17DRPremix/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/010000/1CF5277A-B679-E811-A138-F01FAFE15CBD.root"
        #"/store/mc/RunIIFall17DRPremix/GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/90000/8E035DB1-1150-E811-9AA4-24BE05C38CA1.root"
        #"/store/mc/RunIIFall17DRPremix/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/10000/D48E5941-CBB0-E811-8C56-AC1F6B0DE140.root"
        #'/store/mc/RunIIFall17DRPremix/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B6B3AB6C-CB3B-E811-8D3C-F01FAFD8F9BA.root'
        #'/store/mc/RunIIFall17DRPremix/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/30000/30B22337-02D7-E711-A2FE-0CC47A5FC619.root'
        #'file:/data/users/jengbou/EmJetMC/Tests/2017/D48E5941-CBB0-E811-8C56-AC1F6B0DE140.root'
        #"/store/mc/RunIIFall17DRPremix/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/2AFFA030-37AC-E811-843A-A0369FD0B130.root"
    ),
)

producePdfWeights = 0
if producePdfWeights:
# if options.data==0:
    # Produce PDF weights (maximum is 3)
    process.pdfWeights = cms.EDProducer("PdfWeightProducer",
        # Fix POWHEG if buggy (this PDF set will also appear on output,
        # so only two more PDF sets can be added in PdfSetNames if not "")
        #FixPOWHEG = cms.untracked.string("cteq66.LHgrid"),
        #GenTag = cms.untracked.InputTag("genParticles"),
        PdfInfoTag = cms.untracked.InputTag("generator"),
        PdfSetNames = cms.untracked.vstring(
                "CT14nlo.LHgrid",
                "NNPDF30_nlo_as_0118.LHgrid",
                "NNPDF23_lo_as_0130_qed.LHgrid",
                # , "MRST2006nnlo.LHgrid"
                # , "NNPDF10_100.LHgrid"
        )
    )


process.TFileService = cms.Service("TFileService", fileName = cms.string('ntuple_20181018.root') )

testVertexReco = 0
if testVertexReco:
    # addEdmOutput(process, options.data, options.sample)
    # Keep all objects created by emJetAnalyzer
    process.out.outputCommands.extend(cms.untracked.vstring('keep *_emJetAnalyzer_*_*',))
    # Keep genParticles
    process.out.outputCommands.extend(cms.untracked.vstring('keep *_genParticles_*_*',))

if options.outputLabel:
    process.out.fileName = cms.untracked.string('output-%s.root' % options.outputLabel)
    process.TFileService.fileName = cms.string('ntuple-%s.root' % options.outputLabel)

# storage
process.outpath = cms.EndPath(process.out)

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
# # Needed for GetTrackTrajInfo
# process.load("RecoTracker.Configuration.RecoTracker_cff")

# process.load('Configuration.StandardSequences.Reconstruction_cff') #new for navigation
# process.load('Configuration.StandardSequences.GeometryExtended_cff') #new for navigation
# # process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff') #new for navigation
# # process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
# # process.load('JetMETCorrections.Configuration.CorrectedJetProducers_cff')
# # # #get the jet energy corrections from the db file
# # process.load("CondCore.CondDB.CondDB_cfi")

# process.out.outputCommands = cms.untracked.vstring('drop *')

