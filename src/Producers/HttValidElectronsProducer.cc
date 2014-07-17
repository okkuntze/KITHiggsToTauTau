
#include "Artus/Utility/interface/DefaultValues.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/HttValidElectronsProducer.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Calculations/ParticleIsolation.h"


HttValidElectronsProducer::HttValidElectronsProducer(std::vector<KDataElectron*> product_type::*validElectrons,
                                                     std::vector<KDataElectron*> product_type::*invalidElectrons,
                                                     std::string (setting_type::*GetElectronID)(void) const,
                                                     std::string (setting_type::*GetElectronIsoType)(void) const,
                                                     std::string (setting_type::*GetElectronIso)(void) const,
                                                     std::string (setting_type::*GetElectronReco)(void) const,
                                                     std::vector<std::string>& (setting_type::*GetLowerPtCuts)(void) const,
                                                     std::vector<std::string>& (setting_type::*GetUpperAbsEtaCuts)(void) const) :
	ValidElectronsProducer(validElectrons, invalidElectrons,
	                       GetElectronID, GetElectronIsoType, GetElectronIso, GetElectronReco,
	                       GetLowerPtCuts, GetUpperAbsEtaCuts)
{
}

void HttValidElectronsProducer::Init(setting_type const& settings)
{
	ValidElectronsProducer<HttTypes>::Init(settings);
	
	electronIDType = ToElectronIDType(boost::algorithm::to_lower_copy(boost::algorithm::trim_copy(settings.GetElectronIDType())));
}

bool HttValidElectronsProducer::AdditionalCriteria(KDataElectron* electron,
                                                   event_type const& event, product_type& product,
                                                   setting_type const& settings) const
{
	bool validElectron = ValidElectronsProducer<HttTypes>::AdditionalCriteria(electron, event, product, settings);
	
	double isolationPtSum = DefaultValues::UndefinedDouble;
	
	// require no missing inner hits
	if (validElectron && electronReco == ElectronReco::USER) {
		validElectron = validElectron && (electron->track.nInnerHits == 0);
	}

	// custom WPs for electron ID
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_ID
	if (validElectron && electronID == ElectronID::USER) {
		if (electronIDType == ElectronIDType::SUMMER2013LOOSE)
			validElectron = validElectron && IsMVANonTrigElectronHttSummer2013(&(*electron), false);
		else if (electronIDType == ElectronIDType::SUMMER2013TIGHT)
			validElectron = validElectron && IsMVANonTrigElectronHttSummer2013(&(*electron), true);
		else if (electronIDType != ElectronIDType::NONE)
			LOG(FATAL) << "Electron ID type of type " << Utility::ToUnderlyingValue(electronIDType) << " not yet implemented!";
	}

	// custom electron isolation with delta beta correction
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_Muon_Isolation
	if (validElectron && electronIsoType == ElectronIsoType::USER) {
		isolationPtSum = ParticleIsolation::IsolationPtSum(
				electron->p4, event,
				settings.GetIsoSignalConeSize(),
				settings.GetDeltaBetaCorrectionFactor(),
				settings.GetElectronChargedIsoVetoConeSizeEB(),
				settings.GetElectronChargedIsoVetoConeSizeEE(),
				settings.GetElectronNeutralIsoVetoConeSize(),
				settings.GetElectronPhotonIsoVetoConeSizeEB(),
				settings.GetElectronPhotonIsoVetoConeSizeEE(),
				settings.GetElectronDeltaBetaIsoVetoConeSize(),
				settings.GetElectronChargedIsoPtThreshold(),
				settings.GetElectronNeutralIsoPtThreshold(),
				settings.GetElectronPhotonIsoPtThreshold(),
				settings.GetElectronDeltaBetaIsoPtThreshold()
		);
		
		double isolationPtSumOverPt = isolationPtSum / electron->p4.Pt();
		
		product.m_leptonIsolation[electron] = isolationPtSum;
		product.m_leptonIsolationOverPt[electron] = isolationPtSumOverPt;
		
		if ((electron->p4.Eta() < DefaultValues::EtaBorderEB && isolationPtSumOverPt > settings.GetIsoPtSumOverPtThresholdEB()) ||
		    (electron->p4.Eta() >= DefaultValues::EtaBorderEB && isolationPtSumOverPt > settings.GetIsoPtSumOverPtThresholdEE())) {
			validElectron = false;
		}
	}
	
	// (tighter) cut on impact parameters of track
	validElectron = validElectron
	                && (settings.GetElectronTrackDxyCut() <= 0.0 || std::abs(electron->track.getDxy(&event.m_vertexSummary->pv)) < settings.GetElectronTrackDxyCut())
	                && (settings.GetElectronTrackDzCut() <= 0.0 || std::abs(electron->track.getDz(&event.m_vertexSummary->pv)) < settings.GetElectronTrackDzCut());

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
					(std::abs(electron->p4.Eta()) < 0.8 && electron->idMvaNonTrigV0 > 0.925)
					|| (std::abs(electron->p4.Eta()) > 0.8 && std::abs(electron->p4.Eta()) < DefaultValues::EtaBorderEB && electron->idMvaNonTrigV0 > 0.915)
					|| (std::abs(electron->p4.Eta()) > DefaultValues::EtaBorderEB && electron->idMvaNonTrigV0 > 0.965)
				)
			)
			||
			(
				(electron->p4.Pt() >= 20.0) &&
				(
					(std::abs(electron->p4.Eta()) < 0.8 && electron->idMvaNonTrigV0 > (tightID ? 0.925 : 0.905))
					|| (std::abs(electron->p4.Eta()) > 0.8 && std::abs(electron->p4.Eta()) < DefaultValues::EtaBorderEB && electron->idMvaNonTrigV0 > (tightID ? 0.975 : 0.955))
					|| (std::abs(electron->p4.Eta()) > DefaultValues::EtaBorderEB && electron->idMvaNonTrigV0 > (tightID ? 0.985 : 0.975))
				)
			)
		);

	return validElectron;
}

