from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')
options.register ('useBackground',
                   False,
                   VarParsing.multiplicity.singleton,
                   VarParsing.varType.bool,
                   "use background, i.e. non semimu ttbar")
##################################
options.parseArguments()
################################
## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.Tracer = cms.Service("Tracer")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

if options.useBackground:
  process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/sw/lcg/tmp/PAT_Tutorial_Summer14/PATWeekExercise/ttbarEvents_semiMutagged_background.root')
else:
  process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/sw/lcg/tmp/PAT_Tutorial_Summer14/PATWeekExercise/ttbarEvents_semiMutagged_signal.root')
process.load("PhysicsTools.PatExamples.strippedPatTuple_cff")
## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#   process.GlobalTag.globaltag =  ...    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                         ##
#                                         ##
process.maxEvents.input = -1
if options.maxEvents != -1:
 process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))
#                                         ##
#   process.out.outputCommands = [ ... ]  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                         ##
if options.useBackground:
  process.out.fileName = 'patTuple_background_selection.root'
else:
  process.out.fileName = 'patTuple_signal_selection.root'
#                                         ##
#   process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)
