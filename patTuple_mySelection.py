## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.Tracer = cms.Service("Tracer")

process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

process.load("RecoJets.Configuration.GenJetParticles_cff")
process.load("RecoJets.JetProducers.ak4GenJets_cfi")

process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/sw/lcg/tmp/PAT_Tutorial_Summer14/PATWeekExercise/ttbarEvents_semiMutagged_background.root')
#process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/sw/lcg/tmp/PAT_Tutorial_Summer14/PATWeekExercise/ttbarEvents_semiMutagged_signal.root')
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
#                                         ##
#   process.out.outputCommands = [ ... ]  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                         ##
process.out.fileName = 'patTuple_selection.root'
#                                         ##
#   process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)
