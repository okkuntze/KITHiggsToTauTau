
#pragma once

#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttTypes.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttEnumTypes.h"


/** Abstract producer for scale factors effData/effMC
 */
class DataMcScaleFactorProducerBase: public ProducerBase<HttTypes> {
public:

	typedef typename HttTypes::event_type event_type;
	typedef typename HttTypes::product_type product_type;
	typedef typename HttTypes::setting_type setting_type;
	
	DataMcScaleFactorProducerBase(std::vector<std::string>& (setting_type::*GetEfficiencyData)(void) const,
	                              std::vector<std::string>& (setting_type::*GetEfficiencyMc)(void) const,
	                              std::string (setting_type::*GetEfficiencyHistogram)(void) const,
	                              std::string (setting_type::*GetEfficiencyMode)(void) const,
	                              std::string const& weightName);
	
	virtual void Init(setting_type const& settings) override;

	virtual void Produce(event_type const& event, product_type& product,
	                     setting_type const& settings) const override;


private:
	std::vector<std::string>& (setting_type::*GetEfficiencyData)(void) const;
	std::vector<std::string>& (setting_type::*GetEfficiencyMc)(void) const;
	std::string (setting_type::*GetEfficiencyHistogram)(void) const;
	std::string (setting_type::*GetEfficiencyMode)(void) const;
	std::string m_weightName;
	
	std::map<std::string, std::vector<TH2F*> > efficienciesDataByHltName;
	std::map<size_t, std::vector<TH2F*> > efficienciesDataByIndex;
	std::map<std::string, std::vector<TH2F*> > efficienciesMcByHltName;
	std::map<size_t, std::vector<TH2F*> > efficienciesMcByIndex;
	
	HttEnumTypes::DataMcScaleFactorProducerMode m_scaleFactorMode = HttEnumTypes::DataMcScaleFactorProducerMode::NONE;
	
	std::vector<double> GetEfficienciesFromHistograms(std::vector<TH2F*> const& histograms, KLepton* lepton) const;
	
	std::vector<std::vector<double> > GetEfficiencies(
			std::map<std::string, std::vector<TH2F*> > const& efficienciesByHltName,
			std::map<size_t, std::vector<TH2F*> > const& efficienciesByIndex,
			event_type const& event, product_type const& product,
			setting_type const& settings
	) const;

};


/** Producer for the Trigger weights using the functions and paramters provided by the Htt group
 *      See: https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Data_MC_correction_factors
 *
 *  Required config tags:
 *  - TriggerEfficiencyData (vector of ROOT files containing triggerEfficiencies histogram)
 *  - TriggerEfficiencyMc (vector of ROOT files containing triggerEfficiencies histogram)
 *  - TriggerEfficiencyHistogram (default: triggerEfficiencies)
 */
class TriggerWeightProducer: public DataMcScaleFactorProducerBase {
public:

	typedef typename HttTypes::setting_type setting_type;

	virtual std::string GetProducerId() const override {
		return "TriggerWeightProducer";
	}
	
	TriggerWeightProducer();
	
};


/** Producer for the identification weights using the functions and paramters provided by the Htt group
 *
 *  Required config tags:
 *  - IdentificationEfficiencyData (vector of ROOT files containing identificationEfficiencies histogram)
 *  - IdentificationEfficiencyMc (vector of ROOT files containing identificationEfficiencies histogram)
 *  - IdentificationEfficiencyHistogram (default: identificationEfficiencies)
 */
class IdentificationWeightProducer: public DataMcScaleFactorProducerBase {
public:

	typedef typename HttTypes::setting_type setting_type;

	virtual std::string GetProducerId() const override {
		return "IdentificationWeightProducer";
	}
	
	IdentificationWeightProducer();
	
};


/** Abstract producer for extracting pre-computed lep->tau scale factors from ROOT files
 */
class LepTauScaleFactorWeightProducer: public ProducerBase<HttTypes> {
public:

	typedef typename HttTypes::event_type event_type;
	typedef typename HttTypes::product_type product_type;
	typedef typename HttTypes::setting_type setting_type;
	
	LepTauScaleFactorWeightProducer(std::vector<std::string>& (setting_type::*GetWeightFiles)(void) const,
	                                std::vector<std::string>& (setting_type::*GetWeightHistograms)(void) const);
	
	virtual void Init(setting_type const& settings) override;

	virtual void Produce(event_type const& event, product_type& product,
	                     setting_type const& settings) const override;

private:
	std::vector<std::string>& (setting_type::*GetWeightFiles)(void) const;
	std::vector<std::string>& (setting_type::*GetWeightHistograms)(void) const;
	
	std::map<size_t, std::vector<TH1F*> > weightsByIndex;
};

/** Producer for electron->tau fake rate weights
 *
 *  Required config tags:
 *  - EleTauFakeRateWeightFile (ROOT file containing the scale-factor weight histograms)
 *  - EleTauFakeRateHistograms (default provided)
 */
class EleTauFakeRateWeightProducer: public LepTauScaleFactorWeightProducer {
public:

	typedef typename HttTypes::setting_type setting_type;

	virtual std::string GetProducerId() const override {
		return "EleTauFakeRateWeightProducer";
	}
	
	EleTauFakeRateWeightProducer();
};

/** Producer for muon->tau fake rate weights
 *
 *  Required config tags:
 *  - MuonTauFakeRateWeightFile (ROOT file containing the scale-factor weight histograms)
 *  - MuonTauFakeRateHistograms (default provided)
 */
class MuonTauFakeRateWeightProducer: public LepTauScaleFactorWeightProducer {
public:

	typedef typename HttTypes::setting_type setting_type;

	virtual std::string GetProducerId() const override {
		return "MuonTauFakeRateWeightProducer";
	}
	
	MuonTauFakeRateWeightProducer();
};
