import FWCore.ParameterSet.Config as cms

# trigger names should be written as:
# 'HLT_name_v' or 'HLT_name_v#'
# i.e. '_v' must be present at the end, no errant spaces
# specify '_v#' if only that specific version is desired (not typical)

#updated the triggerlist with dilepton triggers (Line 175 and below) and some more for 0 lepton triggers from Semra's study. Didn't delete the ones that was already here.  -BB
triggerNameList = cms.vstring(
    # handle duplicates
	list(sorted(set([
    'HLT_AK8DiPFJet250_200_TrimMass30_v',
    'HLT_AK8DiPFJet280_200_TrimMass30_v',
    'HLT_AK8DiPFJet300_200_TrimMass30_v',
    'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v',
    'HLT_AK8PFHT800_TrimMass50_v',
    'HLT_AK8PFHT850_TrimMass50_v',
    'HLT_AK8PFHT900_TrimMass50_v',
    'HLT_AK8PFJet360_TrimMass30_v',
    'HLT_AK8PFJet400_TrimMass30_v',
    'HLT_AK8PFJet420_TrimMass30_v',
    'HLT_AK8PFJet450_v',
    'HLT_AK8PFJet500_v',
    'HLT_AK8PFJet550_v',
    'HLT_CaloJet500_NoJetID_v',
    'HLT_CaloJet550_NoJetID_v',
    'HLT_DiCentralPFJet55_PFMET110_v',
    'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v',
    'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v',
    'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v',
    'HLT_DoubleMu8_Mass8_PFHT300_v',
    'HLT_DoubleMu8_Mass8_PFHT350_v',
    'HLT_Ele15_IsoVVVL_PFHT350_v',
    'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v',
    'HLT_Ele15_IsoVVVL_PFHT400_v',
    'HLT_Ele15_IsoVVVL_PFHT450_v',
    'HLT_Ele15_IsoVVVL_PFHT450_CaloBTagCSV_4p5_v',
    'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v',
    'HLT_Ele15_IsoVVVL_PFHT600_v',
    'HLT_Ele20_eta2p1_WPLoose_Gsf_v',
    'HLT_Ele20_WPLoose_Gsf_v',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
    'HLT_Ele25_eta2p1_WPTight_Gsf_v',
    'HLT_Ele27_WPTight_Gsf_v',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_v',
    'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v',
    'HLT_Ele32_WPTight_Gsf_v',
    'HLT_Ele35_WPTight_Gsf_v',
    'HLT_Ele45_WPLoose_Gsf_v',
    'HLT_Ele50_IsoVVVL_PFHT400_v',
    'HLT_Ele50_IsoVVVL_PFHT450_v',
    'HLT_Ele105_CaloIdVT_GsfTrkIdT_v',
    'HLT_Ele115_CaloIdVT_GsfTrkIdT_v',
    'HLT_Ele135_CaloIdVT_GsfTrkIdT_v',
    'HLT_Ele145_CaloIdVT_GsfTrkIdT_v',
    'HLT_HT350_DisplacedDijet40_DisplacedTrack_v',
    'HLT_HT350_DisplacedDijet80_DisplacedTrack_v',
    'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v',
    'HLT_HT430_DisplacedDijet40_DisplacedTrack_v',
    'HLT_HT430_DisplacedDijet60_DisplacedTrack_v',
    'HLT_HT430_DisplacedDijet80_DisplacedTrack_v',
    'HLT_HT500_DisplacedDijet40_DisplacedTrack_v',
    'HLT_HT650_DisplacedDijet60_Inclusive_v',
    'HLT_HT650_DisplacedDijet80_Inclusive_v',
    'HLT_HT750_DisplacedDijet80_Inclusive_v',
    'HLT_IsoMu16_eta2p1_MET30_v',
    'HLT_IsoMu20_v',
    'HLT_IsoMu22_v',
    'HLT_IsoMu22_eta2p1_v',
    'HLT_IsoMu24_v',
    'HLT_IsoMu24_eta2p1_v',
    'HLT_IsoMu27_v',
    'HLT_IsoTkMu22_v',
    'HLT_IsoTkMu24_v',
    'HLT_Mu15_IsoVVVL_PFHT350_v',
    'HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v',
    'HLT_Mu15_IsoVVVL_PFHT400_v',
    'HLT_Mu15_IsoVVVL_PFHT450_v',
    'HLT_Mu15_IsoVVVL_PFHT450_CaloBTagCSV_4p5_v',
    'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v',
    'HLT_Mu15_IsoVVVL_PFHT600_v',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v',
    'HLT_Mu45_eta2p1_v',
    'HLT_Mu50_v',
    'HLT_Mu50_IsoVVVL_PFHT400_v',
    'HLT_Mu50_IsoVVVL_PFHT450_v',
    'HLT_Mu55_v',
    'HLT_PFHT180_v',    
    'HLT_PFHT200_v',
    'HLT_PFHT250_v',
    'HLT_PFHT300_v',
    'HLT_PFHT300_PFMET100_v',
    'HLT_PFHT300_PFMET110_v',
    'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v',
    'HLT_PFHT350_v',
    'HLT_PFHT370_v',
    'HLT_PFHT380_SixPFJet32_v',
    'HLT_PFHT380_SixJet32_DoubleBTagCSV_p075_v',
    'HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v',
    'HLT_PFHT380_SixPFJet32_DoublePFBTagDeepCSV_2p2_v',
    'HLT_PFHT400_v',
    'HLT_PFHT400_SixJet30_v',
    'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v',
    'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v',
    'HLT_PFHT430_v',
    'HLT_PFHT430_SixJet40_BTagCSV_p056_v',
    'HLT_PFHT430_SixJet40_BTagCSV_p080_v',
    'HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v',
    'HLT_PFHT380_SixPFJet40_PFBTagDeepCSV_1p5_v',
    'HLT_PFHT430_SixPFJet40_v',
    'HLT_PFHT450_SixJet40_v',
    'HLT_PFHT450_SixJet40_BTagCSV_p056_v',
    'HLT_PFHT450_SixPFJet40_PFBTagCSV_1p5_v',
    'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p5_v',
    'HLT_PFHT475_v',
    'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v',
    'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v',
    'HLT_PFHT510_v',
    'HLT_PFHT590_v',
    'HLT_PFHT600_v',
    'HLT_PFHT650_v',
    'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v',
    'HLT_PFHT680_v',
    'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v',
    'HLT_PFHT700_PFMET95_PFMHT95_IDTight_v',
    'HLT_PFHT750_4JetPt50_v',
    'HLT_PFHT750_4JetPt70_v',
    'HLT_PFHT800_4JetPt50_v',
    'HLT_PFHT780_v',
    'HLT_PFHT800_v',
    'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v',
    'HLT_PFHT800_PFMET85_PFMHT85_IDTight_v',
    'HLT_PFHT890_v',
    'HLT_PFHT900_v',
    'HLT_PFHT1050_v',
    'HLT_PFJet450_v',
    'HLT_PFJet500_v',
    'HLT_PFJet550_v',
    'HLT_PFMET90_PFMHT90_IDTight_v',
    'HLT_PFMET100_PFMHT100_IDTight_v',
    'HLT_PFMET100_PFMHT100_IDTight_PFHT60_v',
    'HLT_PFMET110_PFMHT110_IDTight_v',
    'HLT_PFMET110_PFMHT110_IDTight_PFHT60_v',
    'HLT_PFMET120_PFMHT120_IDTight_v',
    'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v',
    'HLT_PFMET120_PFMHT120_IDTight_HFCleaned_v',
    'HLT_PFMET120_PFMHT120_IDTight_PFHT60_HFCleaned_v',
    'HLT_PFMET130_PFMHT130_IDTight_v',
    'HLT_PFMET130_PFMHT130_IDTight_PFHT60_v',
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMET140_PFMHT140_IDTight_PFHT60_v',
    'HLT_PFMET500_PFMHT500_IDTight_CalBTagCSV_3p1_v',
    'HLT_PFMET700_PFMHT700_IDTight_CalBTagCSV_3p1_v',
    'HLT_PFMET800_PFMHT800_IDTight_CalBTagCSV_3p1_v',
    'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v',
    'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v',
    'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_PFHT60_v',
    'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v',
    'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_PFHT60_v',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_HFCleaned_v',
    'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
    'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_PFHT60_v',
    'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
    'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_PFHT60_v',
    'HLT_Photon90_CaloIdL_PFHT500_v',
    'HLT_Photon90_CaloIdL_PFHT600_v',
    'HLT_Photon90_CaloIdL_PFHT700_v',
    'HLT_Photon135_PFMET100_v',
    'HLT_Photon165_HE10_v',
    'HLT_Photon165_R9Id90_HE10_IsoM_v',
    'HLT_Photon175_v',
    'HLT_Photon200_v',
    'HLT_Photon300_NoHE_v',
    'HLT_TkMu50_v',
    'HLT_TkMu100_v',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v',
    'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v',
    'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT250_v',
    'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v',
    'HLT_DoubleMu4_Mass8_DZ_PFHT350_v', 
    'HLT_DoubleMu8_Mass8_PFHT250_v', 
    'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v',
    'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v',
    'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v', 
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v', 
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v', 
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v',
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v', 
    'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v', 
    'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v', 
    'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250_v', 
    'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v', 
    'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v', 
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v', 
    'HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v',
    'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v',
    'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v',
    'HLT_AK8PFJetFwd400_v',
    'HLT_CaloMET350_HBHECleaned_v',
    'HLT_DiCentralPFJet430_v',
    'HLT_DiJet110_35_Mjj650_PFMET110_v',
    'HLT_DiPFJetAve300_HFJEC_v',
    'HLT_MET200_v',
    'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v',
    'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
    'HLT_MonoCentralPFJet80_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
    'HLT_MonoCentralPFJet80_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
    'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v',
    'HLT_PFJetFwd400_v',
    'HLT_PFMET170_HBHECleaned_v',
    'HLT_PFMET200_HBHE_BeamHaloCleaned_v',
    'HLT_PFMET250_HBHECleaned_v',
    'HLT_PFMET300_HBHECleaned_v',
    'HLT_PFMET300_v',
    'HLT_PFMETTypeOne120_PFMHT120_IDTight_v',
    'HLT_PFMETTypeOne130_PFMHT130_IDTight_v',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
    'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v',
    'HLT_TripleJet110_35_35_Mjj650_PFMET110_v',
    ])))
)
