import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Summer20UL16APV
Summer20UL16APVsamples = [
    # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
    MCSample('WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 1457339),
    MCSample('WWG_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 800000, 693392),
    MCSample('WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 3018000),
    MCSample('WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5261000, 4768918), # subtotal = 64296, straight subtotal = 71000
    MCSample('WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11_ext1-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5261000, 4768918), # subtotal = 4704622, straight subtotal = 5190000
    MCSample('WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5153000, 4674738), # subtotal = 73734, straight subtotal = 81000
    MCSample('WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11_ext1-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5153000, 4674738), # subtotal = 4601004, straight subtotal = 5072000
    MCSample('WW_TuneCP5_13TeV-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 15859000),
    MCSample('WZG_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 584000, 515418),
    MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5554000, 5042470), # subtotal = 145164, straight subtotal = 160000
    MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11_ext1-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5554000, 5042470), # subtotal = 4897306, straight subtotal = 5394000
    MCSample('WZ_TuneCP5_13TeV-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 7934000),
    MCSample('ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 16862000),
    MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5383000, 4797810), # subtotal = 71860, straight subtotal = 81000
    MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11_ext1-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5383000, 4797810), # subtotal = 4725950, straight subtotal = 5302000
    MCSample('ZZ_TuneCP5_13TeV-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 1282000),
    MCSample('ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5518000, 3592772),
    MCSample('ST_s-channel_4f_leptonDecays_TuneCP5down_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2249000, 1462624),
    MCSample('ST_t-channel_top_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 56994000),
    MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 3176485),
    MCSample('ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2300000),
    MCSample('ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2300000),
    MCSample('tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 3723000, 1006530),
    MCSample('TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5792000, 2856626),
    MCSample('TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 1700000, 852414),
    MCSample('TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2900000, 1459398),
    MCSample('TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 6277000, 3118292),
    MCSample('TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 4298000),
    MCSample('TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 4092000),
    MCSample('TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 8272000),
    MCSample('TTWW_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 278000),
    MCSample('TTWZ_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 140000),
    MCSample('TTZZ_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 140000),
    MCSample('TTTT_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 4207000, 1837028),
    MCSample('TTWH_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 140000),
    MCSample('TTZH_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 140000),
    MCSample('TTTJ_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 138000),
    MCSample('ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5013363, 1648005),
    MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 19077000),
    MCSample('QCD_Pt_120to170_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 28652000),
    MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 11000000),
    MCSample('QCD_Pt_15to30_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 19143000),
    MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 27953000),
    MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5262000),
    MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2999000),
    MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 54096000),
    MCSample('QCD_Pt_30to50_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 18944000),
    MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 1000000),
    MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 50782000),
    MCSample('QCD_Pt_50to80_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 19928000),
    MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 61972000),
    MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 35527000),
    MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 29743000),
    MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 90947213, 61192708),
    MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 95170542),
    MCSample('GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 8461618),
    MCSample('GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 19037560),
    MCSample('GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 4338294),
    MCSample('GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 8246771),
    MCSample('GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5069975),
    MCSample('GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 3936783),
    MCSample('ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 7784090),
    MCSample('ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 7531529),
    MCSample('ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 6632524),
    MCSample('ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2030858),
    MCSample('ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 703970),
    MCSample('ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 136393),
    MCSample('ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 111838),
    MCSample('WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 21734530),
    MCSample('WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2119975),
    MCSample('WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 17870845),
    MCSample('WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2467498),
    MCSample('WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2344130),
    MCSample('WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 2510487),
    MCSample('WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 8000572),
    MCSample('WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 5144427),
    MCSample('WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 7668058),
    MCSample('WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v2', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 7740501),
    MCSample('QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 13823774),
    MCSample('QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 67431856),
    MCSample('QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 56868784),
    MCSample('QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 36599034),
    MCSample('QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 15808790),
    MCSample('QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 10031077),
    MCSample('QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 4996082),
    MCSample('QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 56868784),
    MCSample('QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 36599034),
    MCSample('TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 37505000),
    MCSample('TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 16365000),
    MCSample('TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 21583000),
    MCSample('TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 16973000),
    MCSample('TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 16828000),
    MCSample('TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 16848000),
    MCSample('TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 16469000),
    MCSample('TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 16401000),
    MCSample('TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 132178000),
    MCSample('TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 55704000),
    MCSample('TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 55755500),
    MCSample('TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 46535000),
    MCSample('TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 56968000),
    MCSample('TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 56088000),
    MCSample('TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 56527000),
    MCSample('TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 53342000),
    MCSample('TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 55376000),
    MCSample('TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 57211000),
    MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 97600000),
    MCSample('TTToHadronic_TuneCP5down_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 39035000),
    MCSample('TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 36956000),
    MCSample('TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 39491000),
    MCSample('TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 39151000),
    MCSample('TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_preVFP_v11-v1', 'RunIISummer20UL16MiniAODAPVv2', 'Constant', 39751000),
]
