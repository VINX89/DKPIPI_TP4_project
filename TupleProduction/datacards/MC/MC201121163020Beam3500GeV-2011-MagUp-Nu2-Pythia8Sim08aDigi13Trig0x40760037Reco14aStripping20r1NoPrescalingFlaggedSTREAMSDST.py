#-- GAUDI jobOptions generated on Mon Jan 30 14:13:58 2017
#-- Contains event types : 
#--   21163020 - 67 files - 1251745 events - 231.05 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-125461 

#--  StepId : 125461 
#--  StepName : Sim08a - 2011 - MU - Pythia8 
#--  ApplicationName : Gauss 
#--  ApplicationVersion : v45r3 
#--  OptionFiles : $APPCONFIGOPTS/Gauss/Sim08-Beam3500GeV-mu100-2011-nu2.py;$DECFILESROOT/options/@{eventType}.py;$LBPYTHIA8ROOT/options/Pythia8.py;$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : Sim08-20130503 
#--  CONDDB : Sim08-20130503-vc-mu100 
#--  ExtraPackages : AppConfig.v3r171;DecFiles.v27r9 
#--  Visible : Y 


#--  Processing Pass Step-124631 

#--  StepId : 124631 
#--  StepName : Stripping20r1-NoPrescalingFlagged for Sim08 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v32r2p3 
#--  OptionFiles : $APPCONFIGOPTS/DaVinci/DV-Stripping20r1-Stripping-MC-NoPrescaling.py;$APPCONFIGOPTS/DaVinci/DataType-2011.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r171 
#--  Visible : Y 


#--  Processing Pass Step-124629 

#--  StepId : 124629 
#--  StepName : Merge14 for Sim08 
#--  ApplicationName : LHCb 
#--  ApplicationVersion : v35r4 
#--  OptionFiles : $APPCONFIGOPTS/Merging/CopyDST.py 
#--  DDDB : None 
#--  CONDDB : None 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : N 


#--  Processing Pass Step-124915 

#--  StepId : 124915 
#--  StepName : Digi13 with G4 dE/dx - 2011 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v26r3 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/DataType-2011.py;$APPCONFIGOPTS/Boole/Boole-SiG4EnergyDeposit.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r171 
#--  Visible : Y 


#--  Processing Pass Step-124914 

#--  StepId : 124914 
#--  StepName : TCK-0x40760037 Flagged for Sim08 2011 
#--  ApplicationName : Moore 
#--  ApplicationVersion : v12r8g3 
#--  OptionFiles : $APPCONFIGOPTS/Moore/MooreSimProductionWithL0Emulation.py;$APPCONFIGOPTS/Conditions/TCK-0x40760037.py;$APPCONFIGOPTS/Moore/DataType-2011.py;$APPCONFIGOPTS/L0/L0TCK-0x0037.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r171 
#--  Visible : Y 


#--  Processing Pass Step-124974 

#--  StepId : 124974 
#--  StepName : Reco14a for MC - 2011 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v43r2p7 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/DataType-2011.py;$APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r171 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000001_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000002_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000003_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000004_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000005_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000006_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000007_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000008_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000009_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000010_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000011_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000012_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000013_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000014_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000015_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000016_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000017_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000018_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000019_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000020_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000021_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000022_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000023_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000024_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000025_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000026_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000027_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000028_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000029_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000030_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000031_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000032_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000033_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000034_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000035_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000036_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000037_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000038_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000039_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000040_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000041_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000042_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000043_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000044_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000045_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000046_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000047_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000048_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000049_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000050_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000051_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000052_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000053_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000054_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000055_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000056_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000057_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000058_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000059_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000060_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000061_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000062_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000063_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000065_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000066_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000067_1.allstreams.dst',
'LFN:/lhcb/MC/2011/ALLSTREAMS.DST/00028279/0000/00028279_00000068_1.allstreams.dst'
], clear=True)
