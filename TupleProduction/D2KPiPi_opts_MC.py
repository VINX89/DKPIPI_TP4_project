"""
 Script to create a DecayTreeTuple for D2KPiPi with flavour tagging enabled:
"""
__author__ = "Vincenzo Battista <vincenzo.battista@cern.ch>"

from Gaudi.Configuration import *
from Configurables import *
from DecayTreeTuple.Configuration import*

tuple = DecayTreeTuple("D2KPiPi")

tuple.Inputs = ['/Event/AllStreams/Phys/B02DPiD2HHHBeauty2CharmLine/Particles'] # detached stripping Line
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
tt_stripping.StrippingList = ['StrippingB02DPiD2HHHBeauty2CharmLineDecision']

#TupleToolTagging
tt_tagging = tuple.addTupleTool("TupleToolTagging")
tt_tagging.Verbose = True
tt_tagging.StoreTaggersInfo = True

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
                          ,"Hlt1TrackAllL0TightDecision"
                          ,"Hlt1TrackAllL0Decision"
                          ,"Hlt2Topo2BodySimpleDecision"
                          ,"Hlt2Topo3BodySimpleDecision"
                          ,"Hlt2Topo4BodySimpleDecision"
                          ,"Hlt2Topo2BodyBBDTDecision"
                          ,"Hlt2Topo3BodyBBDTDecision"
                          ,"Hlt2Topo4BodyBBDTDecision"
                          ,"Hlt2TopoMu2BodyBBDTDecision"
                          ,"Hlt2TopoMu3BodyBBDTDecision"
                          ,"Hlt2TopoMu4BodyBBDTDecision"
                          ,"Hlt2TopoE2BodyBBDTDecision"
                          ,"Hlt2TopoE3BodyBBDTDecision"
                          ,"Hlt2TopoE4BodyBBDTDecision"
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

