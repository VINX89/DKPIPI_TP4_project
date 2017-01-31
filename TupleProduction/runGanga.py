"""
 Script to produce tuples on the grid using Ganga:
"""
__author__ = "Vincenzo Battista <vincenzo.battista@cern.ch>"

import os , re

#Define input data, options and nicknames here
data = { "D2KPiPi_2011_MU_S21" : { "File" : "datacards/MC/MC201121163020Beam3500GeV-2011-MagUp-Nu2-Pythia8Sim08aDigi13Trig0x40760037Reco14aStripping20r1NoPrescalingFlaggedSTREAMSDST.py",
                                   "Options" : ["options/D2KPiPi_opts_MC_restrip21.py",
                                                "options/2011MU_tags.py",
                                                "/afs/cern.ch/lhcb/software/releases/DBASE/AppConfig/v3r269/options/DaVinci/DV-RedoCaloPID-Stripping21.py"],
                                   "Year" : "2011",
                                   "Polarity": "MU",
                                   "Stripping": "21"},
         "D2KPiPi_2011_MD_S21" : { "File" : "datacards/MC/MC201121163020Beam3500GeV-2011-MagDown-Nu2-Pythia8Sim08aDigi13Trig0x40760037Reco14aStripping20r1NoPrescalingFlaggedSTREAMSDST.py",
                                   "Options" : ["options/D2KPiPi_opts_MC_restrip21.py",
                                                "options/2011MD_tags.py",
                                                "/afs/cern.ch/lhcb/software/releases/DBASE/AppConfig/v3r269/options/DaVinci/DV-RedoCaloPID-Stripping21.py"],
                                   "Year" : "2011",
                                   "Polarity": "MD",
                                   "Stripping": "21"},
         "D2KPiPi_2012_MU_S21" : { "File" : "datacards/MC/MC201221163020Beam4000GeV-2012-MagUp-Nu25-Pythia8Sim08eDigi13Trig0x409f0045Reco14aStripping20NoPrescalingFlaggedSTREAMSDST.py",
                                   "Options" : ["options/D2KPiPi_opts_MC_restrip21.py",
                                                "options/2012MU_tags.py",
                                                "/afs/cern.ch/lhcb/software/releases/DBASE/AppConfig/v3r269/options/DaVinci/DV-RedoCaloPID-Stripping21.py"],
                                   "Year" : "2012",
                                   "Polarity": "MU",
                                   "Stripping": "21"},
         "D2KPiPi_2012_MD_S21" : { "File" : "datacards/MC/MC201221163020Beam4000GeV-2012-MagDown-Nu25-Pythia8Sim08eDigi13Trig0x409f0045Reco14aStripping20NoPrescalingFlaggedSTREAMSDST.py",
                                   "Options" : ["options/D2KPiPi_opts_MC_restrip21.py",
                                                "options/2012MD_tags.py",
                                                "/afs/cern.ch/lhcb/software/releases/DBASE/AppConfig/v3r269/options/DaVinci/DV-RedoCaloPID-Stripping21.py"],
                                   "Year" : "2012",
                                   "Polarity": "MD",
                                   "Stripping": "21"}
         }

def makeJob(nickname, year, polarity):
    print '======================================'   
    print 'Submitting job with nickname'
    print nickname
    print 'input data file'
    print data[nickname]["File"]
    print 'and options'
    for opt in data[nickname]["Options"]:
        print opt
    print '======================================'

    #print "Building DaVinci application..."
    #theApp = GaudiExec()
    #theApp.directory = "$HOME/gitdev/DaVinciDev_v42r1"
    #theApp.options = data[nickname]["Options"]

    print "Building Ganga job"
    #job=Job(name = nickname )
    #job.application= theApp
    job = Job(application=DaVinci(version='v36r1p3'))
    job.name = nickname
    job.application.optsfile = data[nickname]["Options"]
    job.application.extraopts  =  (
        'from Configurables import DaVinci                     ; ' +
        'DaVinci().TupleFile     = "DTT_'+ nickname + '.root"  ; ' +
        'DaVinci().EvtMax        =              -1             ; ' +
        'DaVinci().DataType      =     "'+ year +'"              ; '
        )
    #job.application.extraOpts  =     (
    #    'from Configurables import DaVinci                     ; ' +
    #    'DaVinci().TupleFile     = "DTT_'+ nickname + '.root"  ; ' +
    #    'DaVinci().EvtMax        =              -1             ; ' +
    #    'from Configurables import CondDB                      ; ' + 
    #    'CondDB().UseLatestTags  =    ['+ year +']             ; ' +
    #    'DaVinci().DataType      =     '+ year +'              ; '
    #    )
    job.inputdata  = job.application.readInputData( data[nickname]["File"] ) 
    job.outputfiles= [DiracFile(namePattern='*.root',locations=['CERN-USER']) ] # keep my Tuples on grid element (retrive manually) 
    job.splitter = SplitByFiles(filesPerJob = 20 , maxFiles = -1 , ignoremissing = True)
    job.backend    = Dirac()
    job.submit()
    print "Done. Job submitted!"

#makeJob("D2KPiPi_2011_MU_S21", "2011", "MU")
#makeJob("D2KPiPi_2011_MD_S21", "2011", "MD")
makeJob("D2KPiPi_2012_MU_S21", "2012", "MU")
makeJob("D2KPiPi_2012_MD_S21", "2012", "MD")
