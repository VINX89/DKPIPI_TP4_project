"""
 Script to create a DecayTreeTuple for D2KPiPi with flavour tagging enabled
 and Stripping 21 re-ran on the sample.
 WARNING: the re-run of S21 requires DaVinci v36r1p3
 built against Analysis v13r1p2:
 
 LbLogin -c x86_64-slc6-gcc48-opt
 SetupProject DaVinci v36r1p3
"""
__author__ = "Vincenzo Battista <vincenzo.battista@cern.ch>"

#Some imports
from Configurables import (DaVinci, DecayTreeTuple, EventNodeKiller)
from Gaudi.Configuration import *
from Configurables import *
from DecayTreeTuple.Configuration import *

from StrippingConf.Configuration import StrippingConf, StrippingStream
from StrippingSettings.Utils import strippingConfiguration
from StrippingArchive.Utils import buildStreams
from StrippingArchive import strippingArchive

# Node killer: remove the previous Stripping
event_node_killer = EventNodeKiller('StripKiller')
event_node_killer.Nodes = ['/Event/AllStreams', '/Event/Strip']

# Build a new stream called 'CustomStream' that only
# contains the desired line
strip = 'stripping21'
streams = buildStreams(stripping=strippingConfiguration(strip),
                       archive=strippingArchive(strip))
custom_stream = StrippingStream('CustomStream')
custom_line = 'StrippingD2hhh_KPPLine'

for stream in streams:
    for line in stream.lines:
        if line.name() == custom_line:
            custom_stream.appendLines([line])

# Create the actual Stripping configurable
filterBadEvents = ProcStatusCheck()

sc = StrippingConf(Streams=[custom_stream],
                   MaxCandidates=-1,
                   AcceptBadEvents=False,
                   BadEventSelection=filterBadEvents)

# The output is placed directly into Phys, so we only need to
# define the stripping line here
line = 'D2hhh_KPPLine'

#Create DTT and configure DaVinci
tuple = DecayTreeTuple("D2KPiPi")

tuple.Inputs = ['/Event/Phys/{0}/Particles'.format(line)] # detached stripping Line
#tuple.Inputs = ['/Event/AllStreams/Phys/D2hhh_KPPLine/Particles']
tuple.Decay = "[D- -> ^pi- ^pi- ^K+]CC"
tuple.ReFitPVs = True

branches = {}

descriptor_D = "^([D- -> pi- pi- K+]CC)"
name_dbranch = "D"
branches["D"] = descriptor_D
branches["K"] = "[D- -> pi- pi- ^K+]CC"
branches["Pi1"] = "[D- -> ^pi- pi- K+]CC"
branches["Pi2"] = "[D- -> pi- ^pi- K+]CC"

tuple.addBranches(branches)

tuple.ToolList = [ ]

tuple.addTupleTool("TupleToolMCTruth")
tuple.addTupleTool("TupleToolMCBackgroundInfo")

#adding simple TupleTools
tuple.UseLabXSyntax = False
tuple.RevertToPositiveID = False
tuple.addTupleTool("TupleToolDecay/D")

tuple.addTupleTool("TupleToolMassHypo")
tuple.addTupleTool("TupleToolTrackPosition")
tuple.addTupleTool("TupleToolRecoStats")
tuple.addTupleTool("TupleToolPropertime")
tuple.addTupleTool("TupleToolPid")
tuple.addTupleTool("TupleToolAngles")
tuple.addTupleTool("TupleToolPrimaries")
tuple.addTupleTool("TupleToolTrigger")

#TupleToolEventInfo
tt_eventinfo = tuple.addTupleTool("TupleToolEventInfo")
tt_eventinfo.Verbose = True

#TupleToolStripping
tt_stripping = tuple.addTupleTool("TupleToolStripping")
tt_stripping.Verbose = True
tt_stripping.StrippingList = ['StrippingD2hhh_KPPLineDecision']

#TupleToolTagging
tt_tagging = tuple.addTupleTool("TupleToolTagging")
tt_tagging.Verbose = True
tt_tagging.StoreTaggersInfo = True
tt_tagging.TagBeautyOnly = False

#TupleToolGeometry
tt_geometry = tuple.addTupleTool("TupleToolGeometry")
tt_geometry.Verbose=True
tt_geometry.RefitPVs = True
tt_geometry.FillMultiPV = True

#TupleToolTrackinfo
tt_trackinfo = tuple.addTupleTool("TupleToolTrackInfo")
tt_trackinfo.Verbose = True

#TupleToolKinematic
tt_kinematic = tuple.addTupleTool("TupleToolKinematic")
tt_kinematic.Verbose = True

#Loki-TupleTool
tt_loki_general = tuple.addTupleTool("LoKi__Hybrid__TupleTool")
tt_loki_general.Variables = {"LOKI_ENERGY"     : "E",
                             "LOKI_ETA"        : "ETA",
                             "LOKI_PHI"        : "PHI"}

#TupleTool TISTOS
tt_tistos = tuple.addTupleTool("TupleToolTISTOS")
tt_tistos.TriggerList = [ "L0PhysicsDecision"
                          ,"L0HadronDecision"
                          ,"L0PhotonDecision"
                          ,"L0ElectronDecision"
                          ,"L0MuonDecision"
                          ,"L0DiMuonDecision"
                          ,"Hlt1TrackAllL0TightDecision"
                          ,"Hlt1TrackAllL0Decision"
                          ,"Hlt2Topo2BodySimpleDecision"
                          ,"Hlt2Topo3BodySimpleDecision"
                          ,"Hlt2Topo4BodySimpleDecision"
                          ,"Hlt2CharmHadD2HHHDecision"
                          ]
tt_tistos.VerboseL0 = True
tt_tistos.VerboseHlt1 = True
tt_tistos.VerboseHlt2 = True

#Smear track state
smearer = TrackSmearState("StateSmear")

#DaVinci configuration
DaVinci().TupleFile = "DTT_D2KPiPi.root"
DaVinci().Simulation = True
DaVinci().UserAlgorithms = [ smearer, tuple ] 
DaVinci().EvtMax = -1
DaVinci().SkipEvents = 0
DaVinci().PrintFreq = 5000
DaVinci().DataType = "2012"

#Input file for quick tests
#from GaudiConf import IOHelper
#IOHelper().inputFiles([
#    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/ALLSTREAMS.DST/00058275/0000/00058275_00000001_2.AllStreams.dst'
#    ], clear=True)
