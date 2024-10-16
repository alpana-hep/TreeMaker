import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/5EE1F968-F1E9-4B41-9755-0CE441C17FFB.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/A41B819A-F75F-C341-90C5-673FDA5FFBBD.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/06450FB4-66BE-384F-863A-AEE265DC6DA1.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/BDD3E7D5-454F-394A-8523-A5547A46D433.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/1A3698FA-51C3-BE49-913B-69A6C6AE8DF2.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/948ADD8D-4031-EF42-83E2-7757A0A044C8.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/0C572CE8-E9BF-F943-9A99-6D1DECBC20C8.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/E565B7AD-CB26-0A40-B9FA-16C03F379AEF.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/7D1505FC-735C-3D46-BDE9-4898ABE029DF.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/84FEBA74-0BEA-6C45-AD35-CA446237A520.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/564421C4-E191-3249-AD1C-E69712737F7A.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/DFC0A5B3-BA83-6F4B-9A77-B6859C6598E1.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/C60B117C-5543-7642-83F5-D5569B621D8A.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/69F9D11A-D8A7-E241-87E2-4D0D80880E86.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/3AAC7F45-D81A-5943-B535-163D385059E0.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/FD7963C4-4083-C744-88BA-867626C28E7E.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/C3E5899A-D7F4-234F-80C9-C149396A15D9.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/1F0536AA-D4EA-2247-A80C-00198ED54483.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/B7D2D5A8-AEDF-E543-9ACC-B992C4380242.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/15BC5728-38EB-F34A-8652-607698E28019.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/6FA7BC4C-1611-E64B-977F-1D5BEDA7C250.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/2D411CF2-5B6F-634A-8A91-4501BAC0E4E7.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/10ABE0C3-4BD6-D346-BE04-BBD6DE6FC016.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/CE13EF21-6821-D741-98F5-3B0EC91F328F.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/E834E65D-7B0B-EF4F-B2FF-9047DE77441A.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/4E36F64A-5672-774C-933C-3D115E5CB3D9.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/E2DA843C-FF43-7B4C-AE5E-5A6790FDF7ED.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/8BC96D83-75FE-6A49-B23C-884362A080EA.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/A36DFEDF-5CC0-9346-A039-EA3D80B4C131.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/7BC25DE7-3CC7-8847-ACDF-E1E1F478D85F.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/48BFF6CE-277C-C74D-B0D8-47773865A4AA.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/34011CCE-5E8C-3641-A163-787E5F2E976C.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/46D413B1-CFD2-944F-9CCC-5DA4EBD26ED8.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/738394B2-A983-434F-9CB8-70162F05256F.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/04049EC8-5BE8-094D-80BE-CBB04AA826F9.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/66836369-9B54-A445-9D53-C5251BC18EA4.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/911F99AA-62F8-724C-AA61-30F7D95CA8AE.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/7AC3EA9B-6365-0A4A-83B6-7AC6385548E5.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/131FCE85-B29E-8D47-B79B-2FE4BDE97869.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/4A044F7B-777F-0B4E-8614-D15928FB15C7.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/65F93076-AEDF-8740-82E0-FE5F9CE7A6E1.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/8C85A139-D462-1C48-BDA3-D08586851140.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/206F395C-4813-6B4D-A9BA-04E23DA02E85.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/72436EC2-F245-B046-A61E-82ACD71E484F.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/28CE29BD-EDA1-754B-A514-1693830CCFC1.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/A9AA7D18-C70D-BF4E-B6B4-05E2FB1A8A4C.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/92018CAB-AE13-A548-BE93-E5180EE82743.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/A33E16D0-82E9-534A-9959-1DFE28CCB423.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/CB59D115-D7B3-A146-B3E8-0F2485F6BB46.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/8A11D3D8-BAB0-124E-99F1-8FB91E0E6888.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/0A5F102A-6004-A945-BDDE-CC4FD96C9ABA.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/6FAA7F6F-CA33-7E4C-89B1-BDF934007FBA.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/D7606CBD-E9B0-C044-B08C-6595CA9534F8.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/0DB1C912-D504-4D45-8207-C8F66F9169EA.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/A64C5967-3AFF-C642-A37F-8DDF67C0A66E.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/91F772C0-8411-C447-AF5E-D9C37F2746B6.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/6626EAA0-7677-1841-9F20-D2C66CBFC331.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/03D86330-2801-244E-96B1-46D9161E0E7D.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/0DA15F18-743E-8D4F-9F6D-8705B49AB835.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/514C1D79-D3F8-5A45-B044-C133B3D40612.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/EA6214A8-001F-6E4D-89B8-B0A4ABA31163.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/E24F2065-2F1B-F742-80BB-7F1755DF4EBE.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/6742A2CA-5D7B-8E47-BDEF-6A4707C93019.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/B8C0E0F6-0D5A-0F47-9C18-086E6B7FE8FA.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/53B43E6C-C7D2-2248-B758-D4A667521034.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/47286859-3969-104A-BAC5-62CAE3FB5171.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/4D3EE4F3-824D-4043-B0F5-C337A7B18163.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/0E9436F4-0555-BD4A-B9DB-E79D6742C525.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/EE4C291A-7AB3-5F46-8D7A-9FEEE21D70F3.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/6F29CDDE-CE5B-C64D-BE43-0014442E0C92.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/92A821CC-EC79-C34A-B743-113D76A0FA72.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/142CA39B-F1E0-D14D-9E07-BB6B3415F169.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/D576DB92-FA61-6F4E-A6FF-1E7D3D1DBB07.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/384AAD51-CA47-1544-BCF2-352550731472.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/DEA2F7F2-2686-3048-8E91-27D83CE0083F.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/7C835FDB-19D3-BA45-96EB-C3723AE7FC6D.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/908D9B11-7B29-D54D-9854-12C99E13794B.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/02C2DCAC-83D9-6B4E-BA84-9A5989843270.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/9B305993-7097-5D43-A5C8-9F461864A06A.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/F2001320-993E-9D4F-8419-E3DEF7279120.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/33B6B7EF-F046-1C40-9FD3-2704325654E6.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/D5976842-EA1F-DE4F-83A4-4BC0EFA81583.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/3F28323D-AE97-A442-AC9B-66B9D6CD8F07.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/F8B6E639-9455-EB4B-A2BD-6455C01FEA99.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/E65CF26A-5F4C-AC44-B16A-8BEF1560C6B9.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/81EDC129-7301-4C4F-9746-B3A394E00931.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/87E0EDAE-4091-744C-8766-E08E71A04895.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/1A0350F9-A5B9-E347-AFA5-3B3D9F8F65B2.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/F35F674A-A534-5044-B8D8-DFF52BB3162C.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/15879D9E-151E-0948-B250-B734266F6450.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/F94334C2-CC26-4540-8904-750DA2B07EC2.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/60777323-23B3-A94D-8647-9B9691580DC7.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/8764F5FC-B6D4-B04C-B07C-987088407BCF.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/9162E6B7-0395-5746-8898-D1BF06F0F278.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/A44B6C03-7457-704A-B812-DB507481F67E.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/4B72E121-5452-264E-8041-282CC9F06094.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/DAFAA430-BF39-5B4B-A44C-CB02D9483F93.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/59D349D1-2299-4E4F-AA72-E9E704C3B1A7.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/9D4D371D-6074-4A49-8AC9-87F158383612.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/A98ED478-8662-4A4F-9730-0A9FA1C8E00F.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/93D1D550-73DC-0F4C-BD02-977704D29A6A.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/4139DC92-A728-ED4B-ADEA-3E19737DAF65.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/9778D5C0-8F8D-E343-873C-96FE59B10BF8.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/59AF9E78-1F1B-C741-A81A-5BF12C717087.root',
    '/store/data/Run2017D/SinglePhoton/MINIAOD/UL2017_MiniAODv2-v1/100000/7E675C57-1355-9E4B-B2B3-B693B4AEBB33.root',
] )