#include "Artus/Consumer/interface/LambdaNtupleConsumer.h"
#include "Artus/Utility/interface/DefaultValues.h"
#include <TMath.h>
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/PrefireWeightProducer.h"
#include <assert.h>

void PrefireWeightProducer::Init(setting_type const& settings)
{
	ProducerBase<HttTypes>::Init(settings);
	
        // set variables
	std::string filename = settings.GetPrefireEfficiencyMapsSource();
        
                
        TDirectory *savedir(gDirectory);
        TFile *savefile(gFile);
        TFile rootFile(filename.c_str(), "READ");
        gSystem->AddIncludePath("-I$ROOFITSYS/include");
	effMap = (TEfficiency*)rootFile.Get("prefireEfficiencyMap");
        rootFile.Close();
        gDirectory = savedir;
        gFile = savefile;
        
        LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("prefire_weight", [](event_type const& event, product_type const& product) {
		return product.m_prefire_weight;
	});
        LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("prefire_weight_up", [](event_type const& event, product_type const& product) {
                return product.m_prefire_weight_up;
        });
        LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("prefire_weight_down", [](event_type const& event, product_type const& product) {
                return product.m_prefire_weight_down;
        });
        LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("prefire_weight_2017", [](event_type const& event, product_type const& product) {
		return product.m_prefire_weight_2017;
	});
        LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("prefire_weight_2017_up", [](event_type const& event, product_type const& product) {
                return product.m_prefire_weight_2017_up;
        });
        LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("prefire_weight_2017_down", [](event_type const& event, product_type const& product) {
                return product.m_prefire_weight_2017_down;
        });
}

void PrefireWeightProducer::Produce(event_type const& event, product_type& product,
                                      setting_type const& settings) const
{
	//2016
        double noPrefireEfficiency = 1.0;
        double upShift = 0.0;
        double downShift = 0.0;
        for (std::vector<KBasicJet*>::iterator jet = (product.m_validJets).begin();
                                 jet != (product.m_validJets).end(); ++jet)
             {
                 if (std::abs((*jet)->p4.Eta()) >= 2.0 && std::abs((*jet)->p4.Eta()) < 3.5 && (*jet)->p4.Pt() >=30){
                     //std::cout << "Found jet with abs(eta): " << std::abs((*jet)->p4.Eta()) << " and pt: " << (*jet)->p4.Pt() << " leading to pre-firing with probability of " << effMap->GetEfficiency(effMap->FindFixBin(std::abs((*jet)->p4.Eta()), (*jet)->p4.Pt())) << std::endl;
                     double nom = 1.0 - effMap->GetEfficiency(effMap->FindFixBin(std::abs((*jet)->p4.Eta()), (*jet)->p4.Pt()));
                     //errLow is chosen to go to upshift and vice versa because smaller prefire likelihood results in larger event weight
                     double err = effMap->GetEfficiencyErrorLow(effMap->FindFixBin(std::abs((*jet)->p4.Eta()), (*jet)->p4.Pt()));
                     upShift = std::sqrt(upShift * upShift * nom * nom + err * err * noPrefireEfficiency *noPrefireEfficiency);
                     err = effMap->GetEfficiencyErrorUp(effMap->FindFixBin(std::abs((*jet)->p4.Eta()), (*jet)->p4.Pt()));
                     if (err>0.9) std::cout << err << " at pt=" << (*jet)->p4.Pt() << " and abs(eta)=" << std::abs((*jet)->p4.Eta()) <<std::endl;
                     downShift = std::sqrt(downShift * downShift * nom * nom + err * err * noPrefireEfficiency * noPrefireEfficiency);
                     noPrefireEfficiency *= nom;
                 }
             }
        product.m_prefire_weight = noPrefireEfficiency;
        product.m_prefire_weight_up = std::min(1.0, noPrefireEfficiency + upShift);
        product.m_prefire_weight_down = std::max(0.0, noPrefireEfficiency - downShift);
        
        //2017
        std::string filename2017 = settings.GetPrefireEfficiencyMapsSource2017();
        TFile rootFile(filename2017.c_str(), "READ");
        TH2F* effMap2017 = (TH2F*)rootFile.Get("L1prefiring_jet_2017BtoF");
        noPrefireEfficiency = 1.0;
        upShift = 0.0;
        downShift = 0.0;
        for (std::vector<KBasicJet*>::iterator jet = (product.m_validJets).begin();
                                 jet != (product.m_validJets).end(); ++jet)
             {
                 if (std::abs((*jet)->p4.Eta()) >= 1.75 && std::abs((*jet)->p4.Eta()) < 3.5 && (*jet)->p4.Pt() >=40){
                     //std::cout << "Found jet with abs(eta): " << std::abs((*jet)->p4.Eta()) << " and pt: " << (*jet)->p4.Pt() << " leading to pre-firing with probability of " << effMap->GetEfficiency(effMap->FindFixBin(std::abs((*jet)->p4.Eta()), (*jet)->p4.Pt())) << std::endl;
                     
                     double nom = 1.0 - effMap2017->GetBinContent(effMap2017->GetXaxis()->FindBin((*jet)->p4.Eta()), effMap2017->GetYaxis()->FindBin((*jet)->p4.Pt()));
                     //errLow is chosen to go to upshift and vice versa because smaller prefire likelihood results in larger event weight
                     double err = effMap2017->GetBinErrorLow(effMap2017->GetXaxis()->FindBin((*jet)->p4.Eta()), effMap2017->GetYaxis()->FindBin((*jet)->p4.Pt()));
                     upShift = std::sqrt(upShift * upShift * nom * nom + err * err * noPrefireEfficiency *noPrefireEfficiency);
                     err = effMap2017->GetBinErrorUp(effMap2017->GetXaxis()->FindBin((*jet)->p4.Eta()), effMap2017->GetYaxis()->FindBin((*jet)->p4.Pt()));
                     if (err>0.9) std::cout << err << " at pt=" << (*jet)->p4.Pt() << " and abs(eta)=" << std::abs((*jet)->p4.Eta()) <<std::endl;
                     downShift = std::sqrt(downShift * downShift * nom * nom + err * err * noPrefireEfficiency * noPrefireEfficiency);
                     noPrefireEfficiency *= nom;
                 }
             }
        rootFile.Close();
        product.m_prefire_weight_2017 = noPrefireEfficiency;
        product.m_prefire_weight_2017_up = std::min(1.0, noPrefireEfficiency + upShift);
        product.m_prefire_weight_2017_down = std::max(0.0, noPrefireEfficiency - downShift);
}
