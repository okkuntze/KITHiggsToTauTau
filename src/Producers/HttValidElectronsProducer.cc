
#include "Artus/Utility/interface/DefaultValues.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/HttValidElectronsProducer.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Calculations/ParticleIsolation.h"


void HttValidElectronsProducer::InitGlobal(global_setting_type const& globalSettings)
{
	ValidElectronsProducer::InitGlobal(globalSettings);
	
	electronIDType = ToElectronIDType(boost::algorithm::to_lower_copy(boost::algorithm::trim_copy(globalSettings.GetElectronIDType())));
	
	chargedIsoVetoConeSizeEB = globalSettings.GetElectronChargedIsoVetoConeSizeEB();
	chargedIsoVetoConeSizeEE = globalSettings.GetElectronChargedIsoVetoConeSizeEE();
	neutralIsoVetoConeSize = globalSettings.GetElectronNeutralIsoVetoConeSize();
	photonIsoVetoConeSizeEB = globalSettings.GetElectronPhotonIsoVetoConeSizeEB();
	photonIsoVetoConeSizeEE = globalSettings.GetElectronPhotonIsoVetoConeSizeEE();
	deltaBetaIsoVetoConeSize = globalSettings.GetElectronDeltaBetaIsoVetoConeSize();
	
	chargedIsoPtThreshold = globalSettings.GetElectronChargedIsoPtThreshold();
	neutralIsoPtThreshold = globalSettings.GetElectronNeutralIsoPtThreshold();
	photonIsoPtThreshold = globalSettings.GetElectronPhotonIsoPtThreshold();
	deltaBetaIsoPtThreshold = globalSettings.GetElectronDeltaBetaIsoPtThreshold();
	
	isoSignalConeSize = globalSettings.GetIsoSignalConeSize();
	deltaBetaCorrectionFactor = globalSettings.GetDeltaBetaCorrectionFactor();
	isoPtSumOverPtThresholdEB = globalSettings.GetIsoPtSumOverPtThresholdEB();
	isoPtSumOverPtThresholdEE = globalSettings.GetIsoPtSumOverPtThresholdEE();
	
	trackDxyCut = globalSettings.GetElectronTrackDxyCut();
	trackDzCut = globalSettings.GetElectronTrackDzCut();
}

void HttValidElectronsProducer::InitLocal(setting_type const& settings)
{
	ValidElectronsProducer::InitLocal(settings);
	
	electronIDType = ToElectronIDType(boost::algorithm::to_lower_copy(boost::algorithm::trim_copy(settings.GetElectronIDType())));
	
	chargedIsoVetoConeSizeEB = settings.GetElectronChargedIsoVetoConeSizeEB();
	chargedIsoVetoConeSizeEE = settings.GetElectronChargedIsoVetoConeSizeEE();
	neutralIsoVetoConeSize = settings.GetElectronNeutralIsoVetoConeSize();
	photonIsoVetoConeSizeEB = settings.GetElectronPhotonIsoVetoConeSizeEB();
	photonIsoVetoConeSizeEE = settings.GetElectronPhotonIsoVetoConeSizeEE();
	deltaBetaIsoVetoConeSize = settings.GetElectronDeltaBetaIsoVetoConeSize();
	
	chargedIsoPtThreshold = settings.GetElectronChargedIsoPtThreshold();
	neutralIsoPtThreshold = settings.GetElectronNeutralIsoPtThreshold();
	photonIsoPtThreshold = settings.GetElectronPhotonIsoPtThreshold();
	deltaBetaIsoPtThreshold = settings.GetElectronDeltaBetaIsoPtThreshold();
	
	isoSignalConeSize = settings.GetIsoSignalConeSize();
	deltaBetaCorrectionFactor = settings.GetDeltaBetaCorrectionFactor();
	isoPtSumOverPtThresholdEB = settings.GetIsoPtSumOverPtThresholdEB();
	isoPtSumOverPtThresholdEE = settings.GetIsoPtSumOverPtThresholdEE();
	
	trackDxyCut = settings.GetElectronTrackDxyCut();
	trackDzCut = settings.GetElectronTrackDzCut();
}

bool HttValidElectronsProducer::AdditionalCriteria(KDataElectron* electron,
                                                   event_type const& event,
                                                   product_type& product) const
{
	bool validElectron = ValidElectronsProducer::AdditionalCriteria(electron, event, product);
	double isolationPtSum = DefaultValues::UndefinedDouble;
	
	// custom WPs for electron ID
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_ID
	if (validElectron && electronID == ElectronID::USER) {
		if (electronIDType == ElectronIDType::SUMMER2013LOOSE)
			validElectron = validElectron && IsMVANonTrigElectronHttSummer2013(&(*electron), false);
		else if (electronIDType == ElectronIDType::SUMMER2013TIGHT)
			validElectron = validElectron && IsMVANonTrigElectronHttSummer2013(&(*electron), false);
		else if (electronIDType != ElectronIDType::NONE)
			LOG(FATAL) << "Electron ID type of type " << Utility::ToUnderlyingValue(electronIDType) << " not yet implemented!";
	}

	// custom electron isolation with delta beta correction
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_Muon_Isolation
	if (validElectron && electronIsoType == ElectronIsoType::USER) {
		isolationPtSum = ParticleIsolation::IsolationPtSum(
				electron->p4, event,
				isoSignalConeSize,
				deltaBetaCorrectionFactor,
				chargedIsoVetoConeSizeEB,
				chargedIsoVetoConeSizeEE,
				neutralIsoVetoConeSize,
				photonIsoVetoConeSizeEB,
				photonIsoVetoConeSizeEE,
				deltaBetaIsoVetoConeSize,
				chargedIsoPtThreshold,
				neutralIsoPtThreshold,
				photonIsoPtThreshold,
				deltaBetaIsoPtThreshold
		);
		
		double isolationPtSumOverPt = isolationPtSum / electron->p4.Pt();
		
		product.m_leptonIsolation[electron] = isolationPtSum;
		product.m_leptonIsolationOverPt[electron] = isolationPtSumOverPt;
		
		if ((electron->p4.Eta() < DefaultValues::EtaBorderEB && isolationPtSumOverPt > isoPtSumOverPtThresholdEB) ||
		    (electron->p4.Eta() >= DefaultValues::EtaBorderEB && isolationPtSumOverPt > isoPtSumOverPtThresholdEE)) {
			validElectron = false;
		}
	}
	
	// (tighter) cut on impact parameters of track
	validElectron = validElectron
	                && (trackDxyCut <= 0.0 || std::abs(electron->track.getDxy(&event.m_vertexSummary->pv)) < trackDxyCut)
	                && (trackDzCut <= 0.0 || std::abs(electron->track.getDz(&event.m_vertexSummary->pv)) < trackDzCut);

	return validElectron;
}

bool HttValidElectronsProducer::IsMVANonTrigElectronHttSummer2013(KDataElectron* electron, bool tightID) const
{
	bool validElectron = true;
	
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_ID
	validElectron = validElectron &&
		(
			(
				(electron->p4.Pt() < 20.0)
				&&
				(
					(abs(electron->p4.Eta()) < 0.8 && electron->idMvaNonTrigV0 > 0.925)
					|| (abs(electron->p4.Eta()) > 0.8 && abs(electron->p4.Eta()) < DefaultValues::EtaBorderEB && electron->idMvaNonTrigV0 > 0.915)
					|| (abs(electron->p4.Eta()) > DefaultValues::EtaBorderEB && electron->idMvaNonTrigV0 > 0.965)
				)
			)
			||
			(
				(electron->p4.Pt() >= 20.0) &&
				(
					(abs(electron->p4.Eta()) < 0.8 && electron->idMvaNonTrigV0 > (tightID ? 0.925 : 0.905))
					|| (abs(electron->p4.Eta()) > 0.8 && abs(electron->p4.Eta()) < DefaultValues::EtaBorderEB && electron->idMvaNonTrigV0 > (tightID ? 0.975 : 0.955))
					|| (abs(electron->p4.Eta()) > DefaultValues::EtaBorderEB && electron->idMvaNonTrigV0 > (tightID ? 0.985 : 0.975))
				)
			)
		);

	return validElectron;
}

