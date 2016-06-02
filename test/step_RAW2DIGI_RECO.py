# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: digireco -s RAW2DIGI,RECO --conditions 80X_dataRun2_v13 --filein file:/storage/data/cms/store/user/obondu/testFiles/VRZeroBias2_Run2016B-v2_RAW.root --fileout test_dr.root --data --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.threshold  = cms.untracked.string('DEBUG')
#process.MessageLogger.debugModules = cms.untracked.vstring('*')

datasets = []
for i in range(0,8):
    datasets.append('/VRRandom%d/Run2016B-v2/RAW' % i)


def get_dataset_files(dataset):
    import subprocess, json
    j = subprocess.check_output(['das_client', '--format', 'json', '--query', 'file dataset=%s' % dataset])
    data = json.loads(j)
    files = []
    for d in data["data"]:
        for f in d['file']:
            if 'dataset' in f:
                files.append(f['name'])
    return [str('root://xrootd.unl.edu//%s') % str(f) for f in files]

files = []
for dataset in datasets:
    for f in get_dataset_files(dataset):
        files.append(f)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePythonTips#Running_on_more_than_255_files
            *tuple(files)
        ),
    lumisToProcess = cms.untracked.VLuminosityBlockRange('273162:51-273162:51'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('digireco nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Turning on only strip digi
from Configuration.StandardSequences.RawToDigi_cff import *
process.RawToDigi = cms.Sequence(
#    siPixelDigis+
    siStripDigis
    )

# Turning on only tracker local reco
#from Configuration.StandardSequences.Reconstruction_cff import *
#process.reconstruction = cms.Sequence(bunchSpacingProducer*localreco*globalreco_tracking)
#from RecoLuminosity.LumiProducer.bunchSpacingProducer_cfi import *
from RecoLocalTracker.Configuration.RecoLocalTracker_cff import *
#clusterSummaryProducer.doPixel = cms.bool(False)
#clusterSummaryProducer.wantedSubDets = cms.vstring("TOB","TIB","TID","TEC","STRIP")
#print type(clusterSummaryProducer), clusterSummaryProducer, dir(clusterSummaryProducer)
#print clusterSummaryProducer
siStripZeroSuppression.doAPVRestore = cms.bool(False)
siStripZeroSuppression.PedestalSubtractionFedMode = cms.bool(True)
siStripZeroSuppression.CommonModeNoiseSubtractionMode = cms.string('Median')
#siStripZeroSuppression.produceBaselinePoints = cms.bool(True)
#siStripZeroSuppression.produceCalculatedBaseline = cms.bool(True)
#siStripZeroSuppression.mergeCollections = cms.bool(True)
#striptrackerlocalreco = cms.Sequence(siStripZeroSuppression*siStripClusters)#*siStripMatchedRecHits)
#localreco = cms.Sequence(striptrackerlocalreco) #*clusterSummaryProducer)
#from FWCore.Modules.logErrorHarvester_cfi import *
#process.reconstruction = cms.Sequence(bunchSpacingProducer*localreco*logErrorHarvester)
process.reconstruction_custom = cms.Sequence(siStripZeroSuppression * siStripClusters)
#print type(process.reconstruction), process.reconstruction
#from RecoLocalTracker.SiStripZeroSuppression.SiStripBaselineAnalyzer_cfi import *
#process.SiStripBaselineAnalyzer = SiStripBaselineAnalyzer


# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('output_VR_LS51_100.root'),
#    outputCommands = process.RECOSIMEventContent.outputCommands,
    outputCommands = cms.untracked.vstring(
        'keep *',
#        'drop *',
#        'keep *_siPixel*_*_*',
#        'keep *_siStrip*_*_*',
#        'keep ClusterSummary_clusterSummaryProducer_*_*',
#        'keep recoTracks_*_*_*',
#        'keep recoTrackExtras_*_*_*',
#        'keep TrackingRecHitsOwned_*_*_*',
#        'keep *_generalTracks_*_*',
#        'keep PileupSummaryInfos_*_*_*',
#        'keep int_*_bunchSpacing_*'
        ),
    splitLevel = cms.untracked.int32(0)
)

#print process.RECOSIMoutput.outputCommands

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_v13', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
#process.reconstruction_step = cms.Path(process.reconstruction)
#process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
process.reconstruction_step = cms.Path(process.reconstruction_custom)
#process.SiStripBaselineAnalyzer_step = cms.Path(process.SiStripBaselineAnalyzer)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(
    process.raw2digi_step,
    process.reconstruction_step,
#    process.SiStripBaselineAnalyzer_step,
#    process.endjob_step,
    process.RECOSIMoutput_step
    )


