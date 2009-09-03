

import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from Configuration.GenProduction.PythiaUESettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(8.443e+01),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
processParameters = cms.vstring(
            'MSEL=10',
            'CKIN(3)=120  ! minimum pt hat for hard interactions',
	    'CKIN(4)=170  ! maximum pt hat for hard interactions'),
   # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')

       
   


    )
)
configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string
('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_PhotonJet_120_170_7TeV_cff.py,v $'),
    annotation = cms.untracked.string('PhotonJet-120-170 at 7TeV')
)

ProductionFilterSequence = cms.Sequence(generator)