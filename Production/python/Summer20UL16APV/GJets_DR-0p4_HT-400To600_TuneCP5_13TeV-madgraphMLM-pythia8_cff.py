import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/0EC956FD-E7A2-7D43-AC6A-E24A5E7FA6FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/57D369EB-040A-6441-9FB1-F26276D8CDD4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/62D9E113-57B8-9443-84E1-5E1B9838D5B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/702B98EF-1342-CF4C-B078-979EFCB4F14D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/897863BF-9871-B640-903F-3ECE72F39934.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/04A922AB-4B9C-3545-90E4-E995A3DFE5BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/370712C2-45FE-0F48-8A69-9A813453E59E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/4B194590-B38A-AB49-9397-2D2C11F1038B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/7CC307CD-A602-9A42-9F52-3889D9407833.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/AF1C3FBC-5F76-7C42-BF17-B7DC19F4423A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/B6A64EA9-6F2C-6E43-94DD-CCD39BAADF90.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/B6B525B2-92B3-074A-9D21-959AD9D30F00.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/B91516EF-25C4-344D-9347-E6B7F68409C5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/CF1E1FE0-7B79-1047-AA87-0449407B966A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/CF6AFE89-4F1E-ED40-AD7F-494327E02103.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/FBA8EED3-64F3-604C-B881-4EBACB01AF6B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/13942192-E9E8-1C41-97B4-B9D4C37F27E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/37CAA3DB-73AF-104C-84F2-2CAB68833178.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/4B3420F1-1192-5A42-982F-9717B38844A7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/4E9AC2FF-3FBA-DE49-952B-78E03E05A176.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/50A5DE00-A9FF-4548-8478-9084E59BB6D1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/5FC91F33-14CF-FF45-B80D-C6F0A04C9E44.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/8E8ADFC2-2833-D349-B4ED-88049CC1D05B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/93C829CA-9891-6F4B-A01B-322DFC9DC071.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/BF9A7310-7FDF-2446-9487-8E0D9D5AFD19.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/C0BE5997-8E71-E54C-A780-E4E1C5B6EC38.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/C594B095-3EEA-2544-9815-D79EAB1FB513.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/DA8B4857-6E2F-9A48-80A7-04B835AFAEE3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/DFFED15A-AF54-9547-A03E-6B403DE8C45B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/F88D930A-995F-4542-AE75-EDB813FCCE2B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/01CC3FEB-BBF0-414B-BDEB-7A44873F8A42.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/0932D00F-6760-8843-B0F6-27C13F2490A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/09FDF280-B699-B34C-AE38-63E631474CEA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/0D921D79-725B-104A-A46D-B634E3232303.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/1AC00EBC-AFE2-1042-9A41-AF07216F2A4D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/1CAF711B-1D42-1444-AEC7-E84253CEFDFB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/2C0FA9FC-9040-DF4D-8B0F-CD2FD06B1C0D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/322DDE5C-E64C-9947-ABC9-D922975DF7EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/3A179686-8868-2B42-BA0D-4A96B62E3236.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/3E8AB88B-7F7F-B54E-8B77-7024E362AEAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/5955BF5E-0FB6-8043-BE88-8C0A0E2A1EE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/5F274DC9-D70A-E54C-B235-F5F05384F0F9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/605AD632-F6EA-9E4B-A603-FCD0C5241C41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/6711A3CA-E165-E846-A4CA-2E3F7A47FEA1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/6718ACF7-0669-3F43-99AE-36E8F4989B47.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/67A061F9-F60C-3D46-8EC3-A9FAD020A554.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/6B4554F0-9116-B242-ACB2-7C0236452C5C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/6FD956EA-D9A4-F74F-849F-1F405AEF82E1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/70891CD6-6961-5B4E-85CB-5EB27878E409.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/71FBBF89-9A2B-8845-8B61-6D105E9C33B7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/73672424-B1B1-E543-989C-9BB8BA633072.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/757D8CE8-83EC-1C48-B9CC-CEEB17721CAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/804F53D7-FCDA-B748-8F90-143DC5B94DB0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/826E435C-D102-B047-80D3-DD79D887A01A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/889DCE9D-72F9-9F49-93E2-7AD0BD71DF08.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/99BE3CF9-D4BF-D141-B0C3-10AAFBF2045C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/9DC2E2EF-B426-D94A-858A-EC8CB610C5BD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/ACD5D55B-F42A-E848-9529-CD26736E9EAD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/ACFCC8C6-9A4F-7441-85D0-8577494BC978.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/AE723054-0A13-D942-A1DE-2C282CC4344F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/B25548B5-F181-A54E-95CE-A3C74B876DEE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/B73C5B16-6085-8743-90B8-F2962A547FDA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/BBB72FCF-A15E-594A-ADE7-B0031BF3B2D0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/C2AE3C7C-E18E-FC4E-A146-CC726649B115.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/C4C38F00-ACC7-7441-AEF6-C01BED557C3D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/CC8C0788-87FC-774A-8342-497F789926BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/DAAE07BF-80B5-7C4B-B196-ABA4476372A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/DBB31C05-45AD-074E-8A27-36D413A787B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/DBE49D54-D073-8943-8301-48022C6332FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/DCE56481-6D9F-594A-ACAC-A216C2C7DFB8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/E0ECACE2-6D13-E045-94CF-F611C8815951.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/E1757528-7EE4-A548-93C2-21C2DE0B5098.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/E1775C48-E24C-F343-8838-A5F8C1F75AB0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/E1D414D3-FBB9-8940-8C28-2F8D5D3AB315.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/E1DF5CF4-F53D-F14B-B1D4-22295C3B138D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/E3076B0E-5EF6-A043-8C2A-6C71D27CC987.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/E9960D9A-326D-F345-9A8E-01923217B607.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/FEC3BECC-3A93-6849-9AE8-67B5BD2D30AA.root',
] )
