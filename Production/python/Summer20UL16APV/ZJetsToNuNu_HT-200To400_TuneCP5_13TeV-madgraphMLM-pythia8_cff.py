import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/0D2FC061-C265-BC49-AC7C-A006383B798B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/15A93E11-B325-E149-97F0-EBD0BF3386EF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/1A990836-F7E1-DC4F-84A8-3C4C5ACB9BB8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/46F4C26B-4FFD-5745-9FBC-ED37DD063DEA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/4B63B249-61C9-F648-B64B-7B1144E9E5F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/51C48546-CB23-2F46-83D2-3ED4B63390A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/940639AD-06C5-EF41-A14E-62415450563C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/C46144C2-9311-0A42-8981-AE982115BD42.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/D2218DEF-0A4C-D549-89B9-ACC9775B74BC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/D46E5B50-DDF7-0E4A-8527-E58E036CB997.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/D701DA19-64D9-484B-9A61-63BD1CA67D06.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/E570E26A-3E38-CE46-9EE0-130C40354CF5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/ECACDA4B-1AD3-F945-8023-FB128E2A0B95.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/11C0B3DA-9538-2C4E-A0D7-A5B31F7AE613.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/15CE8653-CE02-4947-ADA1-AA44BA29B59B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/3617AC54-475F-F349-B4CB-B2A32C286EC8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/3B25E36D-C34A-C349-A3F1-8CD8A8988360.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/8073581F-D9F3-DA47-A033-38EE13D94CF3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BB568245-6207-484C-AAAC-E0A1481F84A7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C2575EF3-8DDE-294D-A291-7DB59878D886.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C80ADCF1-0594-3144-8F35-905CEFE78266.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D5BD1F0B-353E-0C46-80FB-5FB0CC44E82F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E5CE3379-C9F8-7F4E-B9FD-B3249FBB2D26.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/EE0D9EFF-1817-644A-B861-04787658892A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0085D3EB-F0AD-154E-9260-165BCA9034E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0E37B10D-FE20-E046-88EA-E97B898154CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1FFEE39B-520E-A447-9427-F3A59867D5E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/21A4D935-B107-944E-B2B1-F7855A33A4AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/29D28EFC-C31A-2D46-BE6A-0ABDF99EED6D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2EA7D735-503D-F546-AE5B-6825CC92AC69.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3A336AB2-77C9-F940-BC53-4B67FFDD9697.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3ABC7686-DD15-294E-9ACD-F3A7969E8771.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3C3C5FF7-1BF2-A047-924C-8CD391E80D26.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/48419B98-7FB7-154D-8173-16793A7E2E3D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/4CD0AC23-C3D2-6F4A-A298-1784FFFC498B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/520B910E-EF3F-DD41-A3B0-E1BE465A9780.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5A892B22-D38B-1045-876C-9503CBDE3C0E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/62CC9523-F518-F74F-B5D8-2086A0F66F6E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6C64090C-36FF-A847-9475-9B2FFE79C588.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6F0869ED-6EE4-F942-AAC4-1AFA755829F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/75ABE328-3FF8-7C48-8290-EE1D83A135CD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/842A5D6F-17F1-5C4F-A68A-FA8FE240EF64.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/8BAB6E99-E12E-C34E-B9F6-CA35FDCFFA31.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9721A890-EF54-6646-86E2-1B3F8D8A41B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9C3267AE-9764-A441-B717-CA7BA0C9468F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9FFEA4F0-9BC4-F64F-828D-FFE4B67E6011.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A04795CA-DCA6-274B-A0E9-E1024D3317DC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A068C2D7-C8E5-614B-8B86-5D60B89E246F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A3327806-94D2-C140-BD6C-9AC1256D1865.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A874E43C-A950-A943-9BAA-F05D14682917.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B8B57C9C-FD8B-4548-9F91-5A8D37631882.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C513B4BE-92D8-674B-9B9B-A07160EB4384.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C7325C65-8209-924D-B307-EB8D4CF6A183.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CC09072F-A38A-6546-A464-2663D20CAB8A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CFEB609E-F827-ED4F-A4F5-B82182F988C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D1B89FF6-7E7C-BB45-8969-DE1FC933D74E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D281A855-A336-CD49-B482-BEA51E082B71.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D8A83506-E052-9F4B-9F49-DD54DC1F2ED4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EC132125-142E-D74E-90F2-B4530D447F01.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EFB042EA-AC1F-C24A-8751-D2E39A0C4F4C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FC811432-C4B4-4546-A7BC-8FF6A2E31678.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/FCE850CD-89EA-514A-986E-5DFC5D4E8349.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/08B40592-2633-434F-99B6-0008D2678668.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/11D45C94-8B78-A041-BAB3-DA290B0343CF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/187C04BB-7CCD-5841-A938-41EC2F97CD07.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/1C6DD638-64B9-B34B-8CBD-62762D368664.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2613031A-A2D5-644C-80A9-AAC11664E106.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2A7A0FC8-89D1-D743-B810-6F5F9C0DC318.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2AF9BEC5-85F8-984B-97A4-7B01C4FF6277.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2D9CDA00-A6A5-0141-9510-A46F51295B37.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/31B2228A-2DC3-9147-931D-34BA148EAEB9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/390CBB5C-7900-F348-AEC9-018B845FC856.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3A76D9F4-E578-AF4B-B93F-6D702C755671.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3AB6F19E-59E4-384D-A375-7E5F56C5C20C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/4346C6E4-EE9E-D045-B300-EA0FDF11FB85.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/47EDC993-1103-8643-9F8A-65AADDF5C99E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/4C1A62B3-1842-0C43-A7CA-3B7EA569E237.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/517567AE-F815-4E4A-A5E4-F915AC6565ED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/692BDDF1-110B-2346-B067-7923A7BD1D70.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6BAF26A7-C3C5-E344-95EF-41F7202A2D3D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6E3687D5-DFD2-924A-8438-FADDF384BDC1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/70219216-FCC7-844A-A6B3-7C0938D0B29B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/723A38B0-DCA7-1D4F-9A6A-00CAE8166C82.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/793ED3B6-790B-D644-83A2-91355A3B544C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/7BCFD556-0858-3647-840E-36D75F28E4C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/98998EC2-C6E3-E549-9DD5-F27C56C1FFB8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9FC559E4-CB75-9C45-8CC5-B8DCF16BCFF1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A8338F6A-8582-A149-A90D-C07FDB9A97F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B11DD64B-7D76-704D-98D6-FA5913ED0DAA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B5021777-361A-C645-B000-2375DDFDAC35.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/BA0DDC16-5F6A-9145-A15E-2E4DDF877B57.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/BB4D63C9-C0C6-C840-A76B-018B966EEFD1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/BFC6B833-5787-964C-83A2-5BA93EE2CC09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/C5BBCBC4-2298-6249-BB82-3C10FF771100.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/C6FD7F83-312E-5941-8A0B-233B8F1E1F47.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/C734F77A-7926-C544-BF70-B32FE0A4905D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D379385B-0940-FB46-A3D9-AC8652DAE5BD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E02DFFBD-35A7-A34D-85D5-002B213C5797.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/EB31720D-0E12-C740-82FA-E91211076CB2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F7C530E1-EEE5-2D4F-B118-C119FACAEF1E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F7DFE14B-1693-4B41-BA88-45F01BB4C381.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/FADEE8C6-8958-A440-8C28-D7878B7897E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/FCC6D248-6D1B-5D4B-B7C6-5F498377769C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/05441184-1093-7140-A765-397C67CFE559.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0C0E8C84-CA6B-2A4C-8470-A43A945A0EFA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/10C1FE96-8B7E-C249-906B-8BCC0F12B419.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/21506789-ADFE-9C44-9787-5CBC5B9FE95B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/32B81B0B-72C4-BF4B-BF56-30007045CCEA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/468D7AFD-B7CA-5045-ADF7-6636710CCEFE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4B730172-75ED-7446-B668-299E687D044B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4EBCBF65-CF73-E542-A982-EEEF98FAC814.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/503F3AB4-A42B-7943-8194-7C58C00636C4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5943F463-CA78-4B4A-B962-64F68FE15D8D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6181A984-6409-4042-B7C4-259E45D33672.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/79EF6EAD-5DC8-0A47-991C-077308A46E7C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8E15A157-3EA9-9047-9F58-DBED66C985B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/91C6AF2C-8203-8649-BE1B-7BED0E0A9269.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/949C6A26-C983-A241-9953-0F2A2E1763D5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A186BBE1-C613-5041-8399-CE61EA1158AC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A2048BE3-9101-CE41-A7EE-E3884CD1D0A3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/AD2629F4-B1EB-E64B-AF65-05BD95A2F7B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/AD572CF3-84FE-7947-A868-5A9857F27357.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BE873F87-CF08-024A-AD6C-B379EF1B2E11.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/CE5275A7-445A-2242-B292-0A5E351BB36A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D59CFBC3-DFFD-6643-B307-2A4BBB2E15BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DBA1485C-9730-D943-B90B-45505AB039CB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DC9FD482-BF6F-0340-BA18-40994AD28D15.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DCB67807-2FE0-F541-A34A-8D04BA3BCF2B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/EC0224D2-497E-5549-984C-4A87E362DF3F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F049B53A-A705-D54E-9E39-F258F6B4E71B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F18C0C4A-04B5-C34A-B310-C8DDB83280EB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0B3367AF-A199-1143-A17E-329296ABB3E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0CB7B34F-6BEF-1944-87E2-0AE8D0385AFD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/1899848C-635C-DE4C-9000-6CD31B576485.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/189AD78E-8830-C144-9D01-5F35AFF8260B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/2D9977B7-0D81-694C-9939-C727D6C57C08.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3280B5BB-1CD3-FE4E-B027-0776B6A89EDB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3E71601F-9A98-9340-B05B-5D3608EE3FE4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5A53EB88-7D99-0749-A024-2E0117873901.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/75D24E18-28A6-4044-BB07-97B500AB88E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/8A0B2544-F3AA-5941-9279-9F8FF83E34D1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/8CBED27A-1DAE-B642-95BA-5084753717E9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/8F4703F0-4F63-074A-B77A-6BBF03C1A88D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B46E323A-EC9A-7F4C-89C8-AD749CD710F0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B6B146CB-4F39-114F-A225-1DC710ADC103.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/C41F07FA-B2DC-0843-9F41-8164EAB33A06.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E430527F-E891-2B4D-8927-F53D7245D4A5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/FEB1BADC-3C83-0D4D-89F4-DE2D7797CC61.root',
] )
