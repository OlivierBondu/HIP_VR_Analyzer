#!/bin/env python

#python imports
import itertools

# ROOT setup
import ROOT
from ROOT import TCanvas, TLatex, TChain, TH1I
ROOT.gROOT.Reset()
ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.ProcessLine(".x test/setTDRStyle.C")
ROOT.TGaxis.SetMaxDigits(3)

c1 = TCanvas()
chain = TChain('tree')
chain.Add('/home/fynu/obondu/TRK/CMSSW_8_0_7_patch1/src/RecoLocalTracker/HIP_VR_Analyzer/output.root')
nEntries = chain.GetEntries()
nEntries = 10
print 'nEntries= ', nEntries


for i in xrange(nEntries):
    chain.GetEntry(i)
    h_adc = TH1I('adc_%i' % i, 'adc_%i' % i, 800, 0, 800)
    h_baseline = TH1I('baseline_%i' % i, 'baseline_%i' % i, 800, 0, 800)
    for strip, adc, baseline in itertools.izip(chain.strip, chain.adc, chain.baseline):
#        print strip, adc
        h_adc.SetBinContent(strip + 1, adc)
        h_baseline.SetBinContent(strip + 1, baseline)
    h_adc.SetMaximum(1000)
    h_adc.GetXaxis().SetTitle("strip")
    h_adc.GetYaxis().SetTitle("ADC counts")
    h_adc.Draw()
    h_baseline.SetLineWidth(2)
    h_baseline.SetLineColor(ROOT.kCyan+1)
    h_baseline.Draw("same")
    h_adc.Draw("same")
    latexLabel = TLatex()
    latexLabel.SetTextSize(0.75 * c1.GetTopMargin())
    latexLabel.SetNDC()
    latexLabel.SetTextFont(42) # helvetica
    latexLabel.DrawLatex(0.27, 0.96, "lumi %i  orbit %i  bx %i  detid %i" % (chain.lumi, chain.orbit, chain.bx, chain.detid))
    c1.Print("plots/hip_%i.png" % i)

