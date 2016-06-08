import FWCore.ParameterSet.Config as cms

process = cms.Process("HIPVRAnalyzer")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
    ignoreTotal = cms.untracked.int32(1),
    monitorPssAndPrivate = cms.untracked.bool(False)
    )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/test/output_VR_LS51_2000.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/test/output_VR_LS50-55.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_LS50-55.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_LS51.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_LS53.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_LS54-55.root',
        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output_VR_TEST.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/SiStripZeroSuppression/output_VR0.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/SiStripZeroSuppression/output_VR1.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/SiStripZeroSuppression/output_VR2.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/SiStripZeroSuppression/output_VR3.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/SiStripZeroSuppression/output_VR4.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/SiStripZeroSuppression/output_VR5.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/SiStripZeroSuppression/output_VR6.root',
#        'file:/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/SiStripZeroSuppression/output_VR7.root',
#        'file:/home/fynu/simon/TrackerDPG/CMSSW_8_0_7_patch1/src/HipAnalyzer/RunTheMacros/step3.root'
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
