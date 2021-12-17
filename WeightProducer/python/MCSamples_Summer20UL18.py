import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Summer20UL18
Summer20UL18samples = [
    # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
    MCSample('WWG_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 2500000, 2165674),
    MCSample('WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 20050931),
    MCSample('WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 240000, 216852),
    MCSample('WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 248000, 224734),
    MCSample('WW_TuneCP5_13TeV-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 15679000),
    MCSample('WZG_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 2000000, 1764512),
    MCSample('WZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 19771910),
    MCSample('WWTo1L1Nu2Q_TuneCP5_13TeV-amcatnloFXFX-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 18974055, 12116937),
    MCSample('WZTo1L1Nu2Q_TuneCP5_13TeV-amcatnloFXFX-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 20179969, 12108591),
    MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v3', 'RunIISummer20UL18MiniAODv2', 'Constant', 10294000, 9346132), # subtotal = 271866, straight subtotal = 300000
    MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1_ext1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 10294000, 9346132), # subtotal = 9074266, straight subtotal = 9994000
    MCSample('WZ_TuneCP5_13TeV-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 7940000),
    MCSample('ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 56886000),
    MCSample('ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 19813764),
    MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 250000, 222716),
    MCSample('ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 19365999, 12607741),
    MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 11015956),
    MCSample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 11270430),
    MCSample('TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 19608000, 9840572),
    MCSample('TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 5987999, 2992173),
    MCSample('TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 9904000, 4993106),
    MCSample('TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 19816000, 9854220),
    MCSample('TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 10516349, 5702715),
    MCSample('TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 970179, 530327),
    MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 4503937, 1609601),
    MCSample('TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 14763000),
    MCSample('TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 27797999),
    MCSample('TTTT_TuneCP5_13TeV-amcatnlo-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 13069000, 5714950),
    MCSample('TTHH_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 500000),
    MCSample('TTZH_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 500000),
    MCSample('TTWW_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 944000),
    MCSample('TTWZ_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 498000),
    MCSample('TTZZ_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 498000),
    MCSample('TTTJ_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 500000),
    MCSample('TTTW_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 494000),
    MCSample('TTWH_TuneCP5_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 497000),
    MCSample('ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 10051443, 3300043),
    MCSample('ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 10020658, 3294534),
    MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 19730000),
    MCSample('QCD_Pt_120to170_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 29949000),
    MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 10982000),
    MCSample('QCD_Pt_15to30_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 19991000),
    MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 29676000),
    MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 5491000),
    MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 2997000),
    MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 57910000),
    MCSample('QCD_Pt_30to50_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 19988000),
    MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 1000000),
    MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 52448000),
    MCSample('QCD_Pt_50to80_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 19493000),
    MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 67508000),
    MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 37160000),
    MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 29685000),
    MCSample('DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 26202328),
    MCSample('DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 6166852),
    MCSample('DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 18455718),
    MCSample('DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 1978203),
    MCSample('DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 8908406),
    MCSample('DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 7035971),
    MCSample('DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 17004433),
    MCSample('DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 6678036),
    MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 197649078), # subtotal = 96233328
    MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1_ext1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 197649078), # subtotal = 101415750
    MCSample('GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 14278296),
    MCSample('GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 47508720),
    MCSample('GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 13440413),
    MCSample('GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 11710704),
    MCSample('QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 14527915),
    MCSample('QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 10871473),
    MCSample('QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 5374711),
    MCSample('QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 57336623),
    MCSample('QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 61705174),
    MCSample('QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 49184771),
    MCSample('QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 38599389),
    MCSample('QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 48506751),
    MCSample('ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 28876062),
    MCSample('ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 381695),
    MCSample('ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 22749608),
    MCSample('ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 268224),
    MCSample('ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 19810491),
    MCSample('ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 5968910),
    MCSample('ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 2129122),
    MCSample('WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 58331446),
    MCSample('WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 7444030),
    MCSample('WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 7718765),
    MCSample('WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 66569448),
    MCSample('WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 7306187),
    MCSample('WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 82442496),
    MCSample('WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 14494966),
    MCSample('WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 9335298),
    MCSample('WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 13633226),
    MCSample('TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 146010000),
    MCSample('TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59973000),
    MCSample('TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59919000),
    MCSample('TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 57772000),
    MCSample('TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59958000),
    MCSample('TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 54510000),
    MCSample('TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59970000),
    MCSample('TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59838000),
    MCSample('TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59846000),
    MCSample('TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59992000),
    MCSample('TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59856000),
    MCSample('TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 59926000),
    MCSample('TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v2', 'RunIISummer20UL18MiniAODv2', 'Constant', 478982000),
    MCSample('TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 198188000),
    MCSample('TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 190086000),
    MCSample('TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 199460000),
    MCSample('TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 193212000),
    MCSample('TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 199398000),
    MCSample('TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 190870000),
    MCSample('TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 194748000),
    MCSample('TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 195248000),
    MCSample('TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 199848000),
    MCSample('TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 184710000),
    MCSample('TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 199922000),
    MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 343248000),
    MCSample('TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 139496000),
    MCSample('TTToHadronic_TuneCP5down_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 139820000),
    MCSample('TTToHadronic_TuneCP5up_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 137313999),
    MCSample('TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 138092000),
    MCSample('TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 133148000),
    MCSample('TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 129116000),
    MCSample('TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 135314000),
    MCSample('TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 139624000),
    MCSample('TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 138438000),
    MCSample('TTToHadronic_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_upgrade2018_realistic_v16_L1v1-v1', 'RunIISummer20UL18MiniAODv2', 'Constant', 130518000),
]
