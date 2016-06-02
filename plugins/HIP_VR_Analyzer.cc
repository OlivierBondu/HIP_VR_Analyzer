// -*- C++ -*-
//
// Package:    RecoLocalTracker/HIP_VR_Analyzer
// Class:      HIP_VR_Analyzer
// 
/**\class HIP_VR_Analyzer HIP_VR_Analyzer.cc RecoLocalTracker/HIP_VR_Analyzer/plugins/HIP_VR_Analyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Olivier Bondu
//         Created:  Tue, 24 May 2016 09:57:58 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// DataFormats
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/SiStripDigi/interface/SiStripRawDigi.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"

// Utilities
#include <RecoLocalTracker/TreeWrapper/interface/TreeWrapper.h>
#define BRANCH(NAME, ...) __VA_ARGS__& NAME = tree[#NAME].write<__VA_ARGS__>()

// ROOT includes
#include "TTree.h"
#include "TFile.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class HIP_VR_Analyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
    public:
        explicit HIP_VR_Analyzer(const edm::ParameterSet&);
        ~HIP_VR_Analyzer();

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


    private:
        virtual void beginJob() override;
        virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
        virtual void endJob() override;

        // ----------member data ---------------------------
        std::string m_output_filename;
        std::unique_ptr<TFile> m_output;
        TTree *tree_;
        ROOT::TreeWrapper tree;
        unsigned int nHIPs;

        // event info
        BRANCH(run, unsigned int);
        BRANCH(lumi, unsigned int);
        BRANCH(event, unsigned int);
        BRANCH(bx, unsigned int);
        BRANCH(orbit, unsigned int);
        // subdet info
        BRANCH(detid, unsigned int);
        BRANCH(subDetector, unsigned int);
        BRANCH(napv, unsigned int);
        BRANCH(adc, std::vector<unsigned int>);
        BRANCH(strip, std::vector<unsigned int>);
        BRANCH(baseline, std::vector<unsigned int>);
        BRANCH(clusteredstrip, std::vector<unsigned int>);
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//

HIP_VR_Analyzer::HIP_VR_Analyzer(const edm::ParameterSet& iConfig):
    m_output_filename(iConfig.getParameter<std::string>("output"))
{
   //now do what ever initialization is needed
//   usesResource("TFileService");
    consumes< edm::DetSetVector<SiStripRawDigi> >(edm::InputTag("siStripDigis", "VirginRaw"));
    consumes< edmNew::DetSetVector<SiStripCluster> >(edm::InputTag("siStripClusters", ""));
    m_output.reset(TFile::Open(m_output_filename.c_str(), "recreate"));
}


HIP_VR_Analyzer::~HIP_VR_Analyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
    m_output->Close();
}


//
// member functions
//

// ------------ method called for each event  ------------
void
HIP_VR_Analyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;

    edm::Handle< edm::DetSetVector<SiStripRawDigi> > vecSiStripDigi;
    iEvent.getByLabel("siStripDigis", "VirginRaw", vecSiStripDigi);

    edm::Handle< edmNew::DetSetVector<SiStripCluster> > vecSiStripCluster;
    iEvent.getByLabel("siStripClusters", "", vecSiStripCluster);

    std::map<unsigned int, unsigned int> detid_apv_blacklist;
/*
    detid_apv_blacklist[369158268] = 0;
    detid_apv_blacklist[369158276] = 0;
    detid_apv_blacklist[369158280] = 0;
    detid_apv_blacklist[369158284] = 0;
    detid_apv_blacklist[436295012] = 0;
*/
    // One entry per apv for a given detid
    for (auto it_vecSiStripDigi = vecSiStripDigi->begin(); it_vecSiStripDigi != vecSiStripDigi->end(); ++it_vecSiStripDigi)
    { // loop over detid
        bool hasAHIP = false;
        run = iEvent.id().run();
        lumi = iEvent.id().luminosityBlock();
        event = iEvent.id().event();
        orbit = iEvent.orbitNumber();
        bx = iEvent.bunchCrossing();
        detid = it_vecSiStripDigi->detId();
        napv = it_vecSiStripDigi->size() / 128;
        std::vector<int> adc_sorted;
        unsigned int istrip = 0;
        unsigned int iapv = 0;
        adc.clear();
        baseline.clear();
        strip.clear();
        for (auto it_SiStripDigi = it_vecSiStripDigi->begin(); it_SiStripDigi != it_vecSiStripDigi->end(); ++it_SiStripDigi, ++istrip)
        { // loop over strips (gotta figure the number of apv on your own)
            iapv = istrip / 128;
            adc.push_back(it_SiStripDigi->adc());
            strip.push_back(istrip);
            clusteredstrip.push_back(0); // We will fill this later when looping over the clusters, but we can initialize this now.
            adc_sorted.push_back(it_SiStripDigi->adc());
            if (istrip % 128 == 127)
            { // last strip for the apv, store the adc vector for sorting and prepare a new empty one
                std::sort(adc_sorted.begin(), adc_sorted.end());
                unsigned int base = adc_sorted[64];
                for (unsigned int i = 0; i < 128; i++)
                {
                    baseline.push_back(base);
                }
                unsigned int maxadc = adc_sorted[127];
                if (
                    ((detid_apv_blacklist.find(detid) == detid_apv_blacklist.end())
                    || (detid_apv_blacklist[detid] != iapv))
                    && (base < 75 && maxadc > 0 && maxadc > 200)
                    )
                {
                    nHIPs++;
                    hasAHIP = true;
/*
                    std::cout << "New HIP candidate"
//                        << "\tnHIPs= " << nHIPs
                        << "\torbit= " << orbit
                        << "\tbx= " << bx
                        << "\tevent= " << event
                        << "\tdetid= " << detid
                        << "\tiapv= " << iapv
                        << "\tbaseline= " << adc_sorted[64] 
                        << "\tfirstAmplitude= " << adc_sorted[0]
                        << "\tlastAmplitude= " << adc_sorted[127]
                        << std::endl;
*/
                }
                adc_sorted.clear();
            } // end of if strip is the last of the apv
        } // end of loop over all the strips in the module
        if (hasAHIP)
        { // if there is a HIP from the strip data, then find the cluster informations
            std::cout << "There is a HIP, saving the module data" << std::endl;
            for (auto it_vecSiStripCluster = vecSiStripCluster->begin(); it_vecSiStripCluster != vecSiStripCluster->end(); ++it_vecSiStripCluster)
            { // loop over detid
                if (detid != it_vecSiStripCluster->detId())
                    continue;
                for (auto it_SiStripCluster = it_vecSiStripCluster->begin(); it_SiStripCluster != it_vecSiStripCluster->end(); ++it_SiStripCluster)
                { // loop over cluster
                    std::cout
                        << "\tcharge= " << it_SiStripCluster->charge()
                        << "\tfirstStrip= " << it_SiStripCluster->firstStrip()
                        << std::endl;
                    for (auto it_amplitudes = (it_SiStripCluster->amplitudes()).begin(); it_amplitudes != (it_SiStripCluster->amplitudes()).end(); ++it_amplitudes)
                    { // Loop over amplitudes
                        std::cout
                            << "\t\tadc= " << *it_amplitudes
                            << std::endl;
                    } // end of loop over cluster amplitudes
                } // end of loop over module clusters
            } // end of loop over detid
            tree.fill();
        }
        adc.clear();
    } // end of loop over modules
} // end of analyse


// ------------ method called once each job just before starting event loop  ------------
void 
HIP_VR_Analyzer::beginJob()
{
    nHIPs = 0;
    tree_ = new TTree("tree", "tree");
    tree.init(tree_);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HIP_VR_Analyzer::endJob() 
{
    m_output->Write();
    std::cout << "Total number of HIP candidates in this job: " << nHIPs << std::endl;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HIP_VR_Analyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HIP_VR_Analyzer);
