#!/bin/env python

#python imports
import itertools

# ROOT setup
import ROOT
from ROOT import TCanvas, TLatex, TChain, TH1I, TLegend
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
nEntries = 50
print 'processing nEntries= %i / %i' % (nEntries, chain.GetEntries())

subdet = {
# TIB:3 TID:4 TOB:5 TEC:6
    3: "TIB",
    4: "TID",
    5: "TOB",
    6: "TEC",
}

for i in xrange(nEntries):
    chain.GetEntry(i)
    h_adc = TH1I('adc_%i' % i, 'adc_%i' % i, 800, 0, 800)
    h_baseline = TH1I('baseline_%i' % i, 'baseline_%i' % i, 800, 0, 800)
    h_cluster = TH1I('cluster_%i' % i, 'cluster_%i' % i, 800, 0, 800)
    for strip, adc, baseline, clusteredstrip in itertools.izip(chain.strip, chain.adc, chain.baseline, chain.clusteredstrip):
#        print strip, adc
        h_adc.SetBinContent(strip + 1, adc)
        h_baseline.SetBinContent(strip + 1, baseline)
        h_cluster.SetBinContent(strip + 1, clusteredstrip)
    h_adc.SetMaximum(1000)
    h_adc.GetXaxis().SetTitle("strip")
    h_adc.GetYaxis().SetTitle("ADC counts")
    h_adc.Draw()
    h_baseline.SetLineWidth(2)
    h_baseline.SetLineColor(ROOT.kCyan + 1)
    h_baseline.Draw("same")
    h_cluster.SetLineWidth(2)
    h_cluster.SetLineColor(ROOT.kRed + 1)
    h_cluster.Draw("same")
    h_adc.Draw("same")
    latexLabel = TLatex()
    latexLabel.SetTextSize(0.75 * c1.GetTopMargin())
    latexLabel.SetNDC()
    latexLabel.SetTextFont(42) # helvetica
    latexLabel.DrawLatex(0.27, 0.96, "lumi %i  orbit %i  bx %i  event %i" % (chain.lumi, chain.orbit, chain.bx, chain.event))
    latexLabel.DrawLatex(0.17, 0.86, "detid %i" % (chain.detid))
    latexLabel.DrawLatex(0.17, 0.81, "%s" % (chain.layer))
    legend = TLegend(0.57,0.70,0.83,0.92)
    legend.SetTextFont(42)
    legend.SetFillStyle(0)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetLineColor(ROOT.kWhite)
    legend.SetShadowColor(ROOT.kWhite)
    legend.AddEntry(h_adc, 'adc counts', 'l')
    legend.AddEntry(h_baseline, 'baseline', 'l')
    legend.AddEntry(h_cluster, 'clusters', 'l')
    legend.Draw("same")
    c1.Print("plots/hip_%i.pdf" % i)
    c1.Print("plots/hip_%i.png" % i)

