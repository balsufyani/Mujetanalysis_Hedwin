import FWCore.ParameterSet.Config as cms

cutFlowAnalyzer = cms.EDAnalyzer('CutFlowAnalyzer',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
#    muons = cms.InputTag("cleanPatTrackerMuonsTriggerMatch"),
#    muJets = cms.InputTag("TrackerMuJetProducer05"),
    muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
    muJets = cms.InputTag("PFMuJetProducer05"),
    muJetOrphans = cms.InputTag("PFMuJetProducer05", "Orphans"),
    DiMuons_Iso_Max = cms.double(2.0),
    nThrowsConsistentVertexesCalculator = cms.int32(100000),
    barrelPixelLayer = cms.int32(1),
    endcapPixelLayer = cms.int32(1),
    runDisplacedVtxFinder = cms.bool(False),
    runPixelHitRecovery = cms.bool(True),
    trajectoryInput = cms.string("TrackRefitter"),
    NavigationSchool   = cms.string('SimpleNavigationSchool'),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    Propagator = cms.string("RungeKuttaTrackerPropagator"),
    signalHltPaths = cms.vstring(
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v1',
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2',
    ),
    backupHltPaths = cms.vstring(
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v1',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v2',
    ),
    otherMuHltPaths = cms.vstring(
        'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v2',
        'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v2',
        'HLT_DoubleMu33NoFiltersNoVtx_v2',
        'HLT_DoubleMu38NoFiltersNoVtx_v2',
        'HLT_DoubleMu8_Mass8_PFHT250_v1',
        'HLT_DoubleMu8_Mass8_PFHT300_v4',
        'HLT_L2DoubleMu23_NoVertex_v2',
        'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v2',
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v2',
        'HLT_Mu10_CentralPFJet30_BTagCSV0p54PF_v3',
        'HLT_Mu17_Mu8_DZ_v2',
        'HLT_Mu17_Mu8_SameSign_DZ_v1',
        'HLT_Mu17_Mu8_v1',
        'HLT_Mu17_TkMu8_DZ_v2',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v2',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v2',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v2',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v2',
        'HLT_Mu17_TrkIsoVVL_v2',
        'HLT_Mu17_v2',
        'HLT_Mu20_Mu10_DZ_v1',
        'HLT_Mu20_Mu10_SameSign_DZ_v1',
        'HLT_Mu20_Mu10_v1',
        'HLT_Mu27_TkMu8_v2',
        'HLT_Mu30_TkMu11_v2',
        'HLT_Mu40_TkMu11_v2',
        'HLT_Mu8_TrkIsoVVL_v3',
        'HLT_Mu8_v3',
        'HLT_TripleMu_12_10_5_v2',
    )
)
