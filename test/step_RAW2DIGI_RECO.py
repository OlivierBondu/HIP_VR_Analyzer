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
    input = cms.untracked.int32(-1)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.threshold  = cms.untracked.string('DEBUG')
#process.MessageLogger.debugModules = cms.untracked.vstring('*')

datasets = []
for i in range(0,1):
    datasets.append('/VRRandom%d/Run2016B-v2/RAW' % i)


def get_dataset_files(dataset):
    print 'get files for dataset %s' % dataset
    import subprocess, json
    j = subprocess.check_output(['das_client', '--format', 'json', '--query', 'file dataset=%s run=273162' % dataset])
    data = json.loads(j)
    files = []
    for d in data["data"]:
        for f in d['file']:
            if 'dataset' in f:
                o = subprocess.check_output(['edmFileUtil', '-f', str('root://xrootd.unl.edu//%s') % str(f['name']), '--eventsInLumis'])
                for line in o.split('\n'):
                    if '273162' in line:
                        print line
                        if 50 <= int(line.split()[1]) <= 55:
                            print '\tkeeping file %s' % f['name']
                            files.append(f['name'])
            
    return [str('root://xrootd.unl.edu//%s') % str(f) for f in files]

files = []
datasets = []
if len(datasets) > 0:
    for dataset in datasets:
        for f in get_dataset_files(dataset):
            files.append(f)
else:
    files = [
        '/store/data/Run2016B/VRRandom0/RAW/v2/000/273/162/00000/0062380D-2B18-E611-AB05-02163E0126C0.root', # 51, 434
#        '/store/data/Run2016B/VRRandom0/RAW/v2/000/273/162/00000/0493FB78-2B18-E611-80D7-02163E014701.root', # 53, 454
#        '/store/data/Run2016B/VRRandom0/RAW/v2/000/273/162/00000/16C0C21D-2B18-E611-9AF9-02163E0138AF.root', # 55, 439
#        '/store/data/Run2016B/VRRandom1/RAW/v2/000/273/162/00000/242C6308-2B18-E611-A475-02163E01377D.root', # 54, 451
        '/store/data/Run2016B/VRRandom2/RAW/v2/000/273/162/00000/0A931DBC-2918-E611-B1D4-02163E012899.root', # 51, 447
#        '/store/data/Run2016B/VRRandom2/RAW/v2/000/273/162/00000/1E69B4BD-2918-E611-9EA8-02163E011A27.root', # 54, 451
#        '/store/data/Run2016B/VRRandom3/RAW/v2/000/273/162/00000/0284A067-2B18-E611-BF5F-02163E011F40.root', # 55, 431
#        '/store/data/Run2016B/VRRandom4/RAW/v2/000/273/162/00000/227BF06F-2A18-E611-946F-02163E01216A.root', # 55, 454
#        '/store/data/Run2016B/VRRandom6/RAW/v2/000/273/162/00000/10E9CC5F-2A18-E611-A366-02163E012160.root', # 55, 445
#        '/store/data/Run2016B/VRRandom6/RAW/v2/000/273/162/00000/2CFBCB5A-2A18-E611-92A9-02163E011C19.root', # 53, 449
        '/store/data/Run2016B/VRRandom7/RAW/v2/000/273/162/00000/10BF9A5C-2A18-E611-9E25-02163E011DD6.root', # 51, 222
        ]
    files = [str('root://xrootd.unl.edu//%s') % str(f) for f in files]

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePythonTips#Running_on_more_than_255_files
            *tuple(files)
        ),
#    lumisToProcess = cms.untracked.VLuminosityBlockRange('273162:50-273162:55'),
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
    fileName = cms.untracked.string('output_VR_LS51_v2.root'),
#    outputCommands = process.RECOSIMEventContent.outputCommands,
    outputCommands = cms.untracked.vstring(
        'keep *',
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


