# HIP VirginRaw data analyzer

## First time setup

```c++
export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSSW_8_0_7_patch1
cd CMSSW_8_0_7_patch1/src
cmsenv
git cms-init
cd ${CMSSW_BASE}/src 
git clone -o upstream git@github.com:blinkseb/TreeWrapper.git CalibTracker/TreeWrapper
git clone -o upstream git@github.com:OlivierBondu/HIP_VR_Analyzer.git RecoLocalTracker/HIP_VR_Analyzer
cd ${CMSSW_BASE}/src/
scram b -j 4
```
