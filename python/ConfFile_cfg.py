import FWCore.ParameterSet.Config as cms

process = cms.Process("HIPVRAnalyzer")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#    ignoreTotal = cms.untracked.int32(1),
#    monitorPssAndPrivate = cms.untracked.bool(False)
#    )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/test/output_VR_LS51_2000.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/test/output_VR_LS50-55.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_LS50-55.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_LS51.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_LS53.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_LS54-55.root',
##        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_TEST.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_1.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_10.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_11.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_12.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_13.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_14.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_15.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_16.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_17.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_18.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_19.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_2.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_20.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_21.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_22.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_23.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_24.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_25.root',
    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_26.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_28.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_3.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_30.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_31.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_32.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_33.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_35.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_36.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_39.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_4.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_40.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_41.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_43.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_46.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_47.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_49.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_5.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_50.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_51.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_52.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_53.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_54.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_56.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_57.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_58.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_6.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_60.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_61.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_63.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_65.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_66.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_67.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_68.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_69.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_7.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_71.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_72.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_73.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_76.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_77.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_78.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_8.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_80.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_81.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_82.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_83.root',
#    'file:/storage/data/cms/store/user/obondu/VRRandom0/VRRandom0_Run2016B-v2/160608_161027/0000/output_VR_DIGIRECO_9.root',
    )
)

process.TkDetMap = cms.Service("TkDetMap")
process.SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")

process.hip_vr_analyzer = cms.EDAnalyzer('HIP_VR_Analyzer',
    debug = cms.bool(False),
    lowbaseline_adc_threshold = cms.uint32(75), # default: 75
    hip_adc_threshold = cms.uint32(200), # default: 200
    output = cms.string('output.root'),
)


process.p = cms.Path(process.hip_vr_analyzer)
