
#include <Math/VectorUtil.h>

#include "Artus/Utility/interface/SafeMap.h"
#include "Artus/Utility/interface/Utility.h"
#include "Artus/Utility/interface/DefaultValues.h"
#include "Artus/KappaAnalysis/interface/KappaEnumTypes.h"
#include "Artus/KappaAnalysis/interface/KappaTypes.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Consumers/HttLambdaNtupleConsumer.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/DiJetQuantitiesProducer.h"


void HttLambdaNtupleConsumer::Init(setting_type const& settings)
{
	// add possible quantities for the lambda ntuples consumers

	// settings for synch ntuples
	LambdaNtupleConsumer<KappaTypes>::AddUInt64Quantity("evt", [](KappaEvent const& event, KappaProduct const& product)
	{
		return event.m_eventInfo->nEvent;
	});

	bool bInpData = settings.GetInputIsData();
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("npu", [bInpData](KappaEvent const& event, KappaProduct const& product)
	{
		if (bInpData)
			return DefaultValues::UndefinedFloat;
		return static_cast<KGenEventInfo*>(event.m_eventInfo)->nPUMean;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("puweight", [](KappaEvent const& event, KappaProduct const& product)
	{
		return SafeMap::GetWithDefault(product.m_weights, std::string("puWeight"), 1.0);
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("trigweight_1", [](KappaEvent const& event, KappaProduct const& product)
	{
		return SafeMap::GetWithDefault(product.m_weights, std::string("triggerWeight_1"), 1.0);
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("trigweight_2", [](KappaEvent const& event, KappaProduct const& product)
	{
		return SafeMap::GetWithDefault(product.m_weights, std::string("triggerWeight_2"), 1.0);
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("idisoweight_1", [](KappaEvent const& event, KappaProduct const& product)
	{
		return SafeMap::GetWithDefault(product.m_weights, std::string("identificationWeight_1"), 1.0);
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("idisoweight_2", [](KappaEvent const& event, KappaProduct const& product)
	{
		return SafeMap::GetWithDefault(product.m_weights, std::string("identificationWeight_2"), 1.0);
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("weight", [settings](KappaEvent const& event, KappaProduct const& product)
	{
		return SafeMap::GetWithDefault(product.m_weights, settings.GetEventWeight(), 1.0);
	});

	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("nDiLeptonVetoPairsOS", [](event_type const& event, product_type const& product)
	{
		return product.m_nDiElectronVetoPairsOS + product.m_nDiMuonVetoPairsOS;
	});
	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("nDiLeptonVetoPairsSS", [](event_type const& event, product_type const& product)
	{
		return product.m_nDiElectronVetoPairsSS + product.m_nDiMuonVetoPairsSS;
	});
	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("dilepton_veto", [](event_type const& event, product_type const& product)
	{
		return ((product.m_nDiElectronVetoPairsOS + product.m_nDiMuonVetoPairsOS) >= 1) ? 1 : 0;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("mt_tot", [](event_type const& event, product_type const& product)
	{
		return sqrt(pow(SafeMap::Get(LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities(),std::string("mt_tt"))(event,product),2)+pow(SafeMap::Get(LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities(),std::string("lep1MetMt"))(event,product),2)+pow(SafeMap::Get(LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities(),std::string("lep2MetMt"))(event,product),2));
	});

	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("EventTauPnPi0s", [](event_type const& event, product_type const& product)
    {
		std::cout << "size:"<< event.m_genTaus->size() << std::endl;
			if (event.m_genTaus->size()>1){
				std::cout << "size:"<< event.m_genTaus->size() << std::endl;
				if (event.m_genTaus->at(0).charge()==1){
					return event.m_genTaus->at(0).nPi0s;
				}
				else 
					return event.m_genTaus->at(1).nPi0s;
			}
			else
				return DefaultValues::UndefinedInt;
    });
	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("EventTauNnPi0s", [](event_type const& event, product_type const& product)
    {
			if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==-1){
					return event.m_genTaus->at(0).nPi0s;
				}
				else 
					return event.m_genTaus->at(1).nPi0s;
			}
			else
				return DefaultValues::UndefinedInt;
    });

	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("EventTauPnProngs", [](event_type const& event, product_type const& product)
    {
            if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==1){
					return event.m_genTaus->at(0).nProngs;
				}
				else 
					return event.m_genTaus->at(1).nProngs;
			}
			else
				return DefaultValues::UndefinedInt;
    });	
	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("EventTauNnProngs", [](event_type const& event, product_type const& product)
    {
            if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==-1){
					return event.m_genTaus->at(0).nProngs;
				}
				else 
					return event.m_genTaus->at(1).nProngs;
			}
			else
				return DefaultValues::UndefinedInt;
    });
	
	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("EventTauPE", [](event_type const& event, product_type const& product)
    {
            if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==1){
					return event.m_genTaus->at(0).p4.E();
				}
				else 
					return event.m_genTaus->at(1).p4.E();
			}
			else
				return DefaultValues::UndefinedFloat;
    });

	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("EventTauNE", [](event_type const& event, product_type const& product)
    {
            if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==-1){
					return event.m_genTaus->at(0).p4.E();
				}
				else 
					return event.m_genTaus->at(1).p4.E();
			}
			else
				return DefaultValues::UndefinedFloat;
    });

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("EventTauPvisE", [](event_type const& event, product_type const& product)
    {
            if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==1){
					return event.m_genTaus->at(0).visible.p4.E();
				}
				else 
					return event.m_genTaus->at(1).visible.p4.E();
			}
			else
				return DefaultValues::UndefinedFloat;
    });
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("EventTauNvisE", [](event_type const& event, product_type const& product)
    {
            if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==-1){
					return event.m_genTaus->at(0).visible.p4.E();
				}
				else 
					return event.m_genTaus->at(1).visible.p4.E();
			}
			else
				return DefaultValues::UndefinedFloat;
    });

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("CosThetaP", [](event_type const& event, product_type const& product)
    {
		RMFLV Tau;
		RMFLV Pi; 
		RMFLV Taunb;
		RMFLV Pinb; 
		float CosTheta;
		float u,v;
		RMFLV chargPart1,chargPart2;
            if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==1){
					chargPart1 = event.m_genTaus->at(0).p4;
					RMFLV ProngImp = chargPart1;
					RMFLV::BetaVector boostvec = ProngImp.BoostToCM();ROOT::Math::Boost M(boostvec);
					Pinb = event.m_genTaus->at(0).visible.p4;
					Taunb= event.m_genTaus->at(0).p4;
					Pi = M* Pinb;
					Tau =  Taunb;
					u = Tau.Px()*Pi.Px()+Tau.Py()*Pi.Py()+Tau.Pz()*Pi.Pz();
					v = sqrt(Tau.Px()*Tau.Px()+Tau.Py()*Tau.Py()+Tau.Pz()*Tau.Pz())*sqrt(Pi.Px()*Pi.Px()+Pi.Py()*Pi.Py()+Pi.Pz()*Pi.Pz());
					CosTheta = u / v;
					return CosTheta;
				}
				else {
					chargPart1 = event.m_genTaus->at(1).p4;
					RMFLV ProngImp = chargPart1;
					RMFLV::BetaVector boostvec = ProngImp.BoostToCM();ROOT::Math::Boost M(boostvec);
					Pinb = event.m_genTaus->at(1).visible.p4;
					Taunb= event.m_genTaus->at(1).p4;
					Pi = M* Pinb;
					Tau =  Taunb;
					u = Tau.Px()*Pi.Px()+Tau.Py()*Pi.Py()+Tau.Pz()*Pi.Pz();
					v = sqrt(Tau.Px()*Tau.Px()+Tau.Py()*Tau.Py()+Tau.Pz()*Tau.Pz())*sqrt(Pi.Px()*Pi.Px()+Pi.Py()*Pi.Py()+Pi.Pz()*Pi.Pz());
					CosTheta = u / v;
					return CosTheta;
				}
			}
			else
				return DefaultValues::UndefinedFloat;
    });

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("CosThetaN", [](event_type const& event, product_type const& product)
    {
		RMFLV Tau;
		RMFLV Pi;
		RMFLV Taunb;
		RMFLV Pinb;  
		float CosTheta;
		float u,v;
		RMFLV chargPart1,chargPart2;
            if (event.m_genTaus->size()>1){
				if (event.m_genTaus->at(0).charge()==-1){
					chargPart1 = event.m_genTaus->at(0).p4;
					RMFLV ProngImp = chargPart1;
					RMFLV::BetaVector boostvec = ProngImp.BoostToCM();ROOT::Math::Boost M(boostvec);
					Pinb = event.m_genTaus->at(0).visible.p4;
					Taunb= event.m_genTaus->at(0).p4;
					Pi = M* Pinb;
					Tau =  Taunb;
					u = Tau.Px()*Pi.Px()+Tau.Py()*Pi.Py()+Tau.Pz()*Pi.Pz();
					v = sqrt(Tau.Px()*Tau.Px()+Tau.Py()*Tau.Py()+Tau.Pz()*Tau.Pz())*sqrt(Pi.Px()*Pi.Px()+Pi.Py()*Pi.Py()+Pi.Pz()*Pi.Pz());
					CosTheta = u / v;
					return CosTheta;
				}
				else {
					chargPart1 = event.m_genTaus->at(1).p4;
					RMFLV ProngImp = chargPart1;
					RMFLV::BetaVector boostvec = ProngImp.BoostToCM();ROOT::Math::Boost M(boostvec);
					Pinb = event.m_genTaus->at(1).visible.p4;
					Taunb= event.m_genTaus->at(1).p4;
					Pi = M* Pinb;
					Tau = M* Taunb;
					u = Tau.Px()*Pi.Px()+Tau.Py()*Pi.Py()+Tau.Pz()*Pi.Pz();
					v = sqrt(Tau.Px()*Tau.Px()+Tau.Py()*Tau.Py()+Tau.Pz()*Tau.Pz())*sqrt(Pi.Px()*Pi.Px()+Pi.Py()*Pi.Py()+Pi.Pz()*Pi.Pz());
					CosTheta = u / v;
					return CosTheta;
				}
			}
			else
				return DefaultValues::UndefinedFloat;
    });

	LambdaNtubleConsumer<HttTypes>::AddFloatQuantity("Cos", [](event_type const&event, product_type const & product)
	{ 
		RMFLV Tau;
		RMFLV Pi;
		RMFLV Taunb;
		RMFLV Pinb;
		RMFLV chargPart;
		float Cos;
		float u,v;
		if (event.m_genTaus->size()>1){
			for(unsigned i = 0; i<=1;++i) {
				std::cout << i << std::endl;
				chargPart = event.m_genTaus->at(i).p4;
				RMFLV ProngImp = chargPart;
				RMFLV::BetaVector boostvec = ProngImp.BoostToCM();
				ROOT::MATH::Boost M(boostvec);
				Pinb = event.m_genTaus->at(i).visible.p4;
				Taunb = event.m_genTaus->at(i).p4;
				Pi = M*Pinb;
				Tau = Taunb;
				u = Tau.Px()*Pi.Px()+Tau.Py()*Pi.Px()+Tau.Pz()*Pi.Pz();
				v = sqrt(Tau.Px()*Tau.Px()+Tau.Py()*Tau.Py()+Tau.Pz()*Tau.Pz())*sqrt(Pi.Px()*Pi.Px()+Pi.Py()*Pi.Py()+Pi.Pz()*Pi.Pz());
				Cos = u / v;
				return Cos;
			}}
		else
			 return DefaultValues::UndefinedFloat;
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("Omega", [](event_type const& event, product_type const& product)
    {
		RMFLV Tau1,Tau2;
		RMFLV Pi1,Pi2;
		RMFLV Taunb1,Taunb2;
		RMFLV Pinb1,Pinb2;  
		float CosTheta1,CosTheta2,Omega;
		float u1,u2,v1,v2;
		RMFLV chargPart1,chargPart2;
            if (event.m_genTaus->size()>1){
					chargPart1 = event.m_genTaus->at(0).p4;
					chargPart2 = event.m_genTaus->at(1).p4;
					RMFLV ProngImp1 = chargPart1;
					RMFLV::BetaVector boostvec1 = ProngImp1.BoostToCM();
					ROOT::Math::Boost M(boostvec1);
					RMFLV ProngImp2 = chargPart2;
					RMFLV::BetaVector boostvec2 = ProngImp2.BoostToCM();
					ROOT::Math::Boost N(boostvec2);
					Pinb1 = event.m_genTaus->at(0).visible.p4;
					Taunb1= event.m_genTaus->at(0).p4;
					Pinb2 = event.m_genTaus->at(1).visible.p4;
					Taunb2= event.m_genTaus->at(1).p4;
					Pi1 = M* Pinb1;
					Tau1 =  Taunb1;
					u1 = Tau1.Px()*Pi1.Px()+Tau1.Py()*Pi1.Py()+Tau1.Pz()*Pi1.Pz();
					v1 = sqrt(Tau1.Px()*Tau1.Px()+Tau1.Py()*Tau1.Py()+Tau1.Pz()*Tau1.Pz())*sqrt(Pi1.Px()*Pi1.Px()+Pi1.Py()*Pi1.Py()+Pi1.Pz()*Pi1.Pz());
					CosTheta1 = u1 / v1;
					Pi2 = M* Pinb2;
					Tau2 =  Taunb2;
					u2 = Tau2.Px()*Pi2.Px()+Tau2.Py()*Pi2.Py()+Tau2.Pz()*Pi2.Pz();
					v2 = sqrt(Tau2.Px()*Tau2.Px()+Tau2.Py()*Tau2.Py()+Tau2.Pz()*Tau2.Pz())*sqrt(Pi2.Px()*Pi2.Px()+Pi2.Py()*Pi2.Py()+Pi2.Pz()*Pi2.Pz());
					CosTheta2 = u2 / v2;
					Omega = (CosTheta1+CosTheta2)/(1+CosTheta1*CosTheta2);
					return Omega;
				
			}
			else
				return DefaultValues::UndefinedFloat;
    });

	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("m_vis", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diLepMass"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mvis", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diLepMass"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("ptvis", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diLepPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("H_pt", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diLepMetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("H_mass", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diLepMetMass"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pt_tt", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diLepMetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pt_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1Pt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("e_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1E"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("eta_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1Eta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("phi_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1Phi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("m_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1Mass"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("q_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1Charge"]);

	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("dZ_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1Dz"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("d0_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1D0"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("errDZ_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1ErrDz"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("errD0_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1ErrD0"]);

	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("iso_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1IsoOverPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mt_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1MetMt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pt_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2Pt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("e_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2E"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("eta_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2Eta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("phi_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2Phi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("m_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2Mass"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("q_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2Charge"]);

	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("dZ_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2Dz"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("d0_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2D0"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("errDZ_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2ErrDz"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("errD0_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2ErrD0"]);

	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("iso_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2IsoOverPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mt_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep2MetMt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("met", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["metPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("metphi", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["metPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("metcov00", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["metCov00"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("metcov01", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["metCov01"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("metcov10", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["metCov10"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("metcov11", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["metCov11"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pfmet", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["pfMetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pfmetphi", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["pfMetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pfmetcov00", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["pfMetCov00"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pfmetcov01", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["pfMetCov01"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pfmetcov10", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["pfMetCov10"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pfmetcov11", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["pfMetCov11"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mvamet", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["mvaMetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mvametphi", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["mvaMetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mvacov00", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["mvaMetCov00"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mvacov01", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["mvaMetCov01"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mvacov10", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["mvaMetCov10"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mvacov11", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["mvaMetCov11"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pzetavis", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["pZetaVis"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pzetamiss", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["pZetaMiss"]);
	
	LambdaNtupleConsumer<KappaTypes>::AddRMFLVQuantity("jlv_1", LambdaNtupleConsumer<KappaTypes>::GetRMFLVQuantities()["leadingJetLV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpt_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["leadingJetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jeta_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["leadingJetEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jphi_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["leadingJetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jm_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["leadingJetMass"]);

	LambdaNtupleConsumer<KappaTypes>::AddRMFLVQuantity("jlv_2", LambdaNtupleConsumer<KappaTypes>::GetRMFLVQuantities()["trailingJetLV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpt_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["trailingJetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jeta_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["trailingJetEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jphi_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["trailingJetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jm_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["trailingJetMass"]);

	LambdaNtupleConsumer<KappaTypes>::AddRMFLVQuantity("jlv_3", LambdaNtupleConsumer<KappaTypes>::GetRMFLVQuantities()["thirdJetLV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpt_3", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["thirdJetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jeta_3", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["thirdJetEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jphi_3", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["thirdJetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jm_3", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["thirdJetMass"]);
	
	LambdaNtupleConsumer<KappaTypes>::AddRMFLVQuantity("jlv_4", LambdaNtupleConsumer<KappaTypes>::GetRMFLVQuantities()["fourthJetLV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpt_4", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fourthJetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jeta_4", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fourthJetEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jphi_4", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fourthJetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jm_4", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fourthJetMass"]);
	
	LambdaNtupleConsumer<KappaTypes>::AddRMFLVQuantity("jlv_5", LambdaNtupleConsumer<KappaTypes>::GetRMFLVQuantities()["fifthJetLV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpt_5", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fifthJetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jeta_5", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fifthJetEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jphi_5", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fifthJetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jm_5", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fifthJetMass"]);
	
	LambdaNtupleConsumer<KappaTypes>::AddRMFLVQuantity("jlv_6", LambdaNtupleConsumer<KappaTypes>::GetRMFLVQuantities()["sixthJetLV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpt_6", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["sixthJetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jeta_6", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["sixthJetEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jphi_6", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["sixthJetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jm_6", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["sixthJetMass"]);
	
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jmva_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["leadingJetPuID"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jcsv_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["leadingJetCSV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bpt_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["bJetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("beta_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["bJetEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bphi_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["bJetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bmva_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["leadingBJetPuID"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bcsv_1", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["leadingBJetCSV"]);
	
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jmva_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["trailingJetPuID"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jcsv_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["trailingJetCSV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bpt_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["bJet2Pt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("beta_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["bJet2Eta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bphi_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["bJet2Phi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bmva_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["trailingBJetPuID"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bcsv_2", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["trailingBJetCSV"]);
	
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jcsv_3", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["thirdJetCSV"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jcsv_4", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["fourthJetCSV"]);

	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mjj", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diJetMass"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jdeta", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diJetAbsDeltaEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jdphi", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diJetDeltaPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("dijetpt", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diJetPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("dijetphi", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diJetPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("hdijetphi", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["diJetdiLepPhi"]);

	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("njets", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["nJets30"]);
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("njetspt30", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["nJets30"]);
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("njetspt20", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["nJets20"]);
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("njetspt20eta2p4", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["nJets20Eta2p4"]);
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("nbtag", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["nBJets20"]);
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("njetingap", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["nCentralJets30"]);
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("njetingap30", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["nCentralJets30"]);
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("njetingap20", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["nCentralJets20"]);

	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("pt_sv", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["svfitPt"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("eta_sv", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["svfitEta"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("phi_sv", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["svfitPhi"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("m_sv", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["svfitMass"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("mt_sv", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["svfitTransverseMass"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("met_sv", LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["svfitMet"]);

	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("npartons", [](KappaEvent const& event, KappaProduct const& product)
	{
		return event.m_genEventInfo ? event.m_genEventInfo->lheNOutPartons : DefaultValues::UndefinedInt;
	});
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("NUP", LambdaNtupleConsumer<KappaTypes>::GetIntQuantities()["npartons"]);
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("genbosonmass", [](KappaEvent const& event, KappaProduct const& product)
	{
		return LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities().count("genBosonMass") >= 1 ? LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["genBosonMass"](event, product) : DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("genbosonpt", [](KappaEvent const& event, KappaProduct const& product)
	{
		return LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities().count("genBosonPt") >= 1 ? LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["genBosonPt"](event, product) : DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("genbosoneta", [](KappaEvent const& event, KappaProduct const& product)
	{
		return LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities().count("genBosonEta") >= 1 ? LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["genBosonEta"](event, product) : DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("genbosonphi", [](KappaEvent const& event, KappaProduct const& product)
	{
		return LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities().count("genBosonPhi") >= 1 ? LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["genBosonPhi"](event, product) : DefaultValues::UndefinedFloat;
	});


	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("isFake", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedInt;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("visjeteta", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
// 	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("ptvis", [](KappaEvent const& event, KappaProduct const& product)
// 	{
// 		return DefaultValues::UndefinedFloat;
// 	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jrawf_1", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jrawf_2", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpfid_1", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpfid_2", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpuid_1", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("jpuid_2", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("brawf_1", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bpfid_1", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bpuid_1", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("brawf_2", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bpfid_2", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("bpuid_2", [](KappaEvent const& event, KappaProduct const& product)
	{
		return DefaultValues::UndefinedFloat;
	});
	LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("PVnDOF", [](KappaEvent const& event, KappaProduct const& product)
        {
                return event.m_vertexSummary->pv.nDOF;
        });
        LambdaNtupleConsumer<KappaTypes>::AddFloatQuantity("PVchi2", [](KappaEvent const& event, KappaProduct const& product)
        {
                return event.m_vertexSummary->pv.chi2;
        });
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("htxs_stage0cat", [](KappaEvent const& event, KappaProduct const& product)
        {
                return event.m_genEventInfo->htxs_stage0cat;
        });
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("htxs_stage1p1cat", [](KappaEvent const& event, KappaProduct const& product)
        {
                return event.m_genEventInfo->htxs_stage1p1cat;
        });
	LambdaNtupleConsumer<KappaTypes>::AddIntQuantity("htxs_stage1p1finecat", [](KappaEvent const& event, KappaProduct const& product)
        {
                return event.m_genEventInfo->htxs_stage1p1finecat;
        });
        LambdaNtupleConsumer<KappaTypes>::AddBoolQuantity("trg_singlemuon", [settings](KappaEvent const& event, KappaProduct const& product)
        {
                return ((LambdaNtupleConsumer<KappaTypes>::GetBoolQuantities().count(std::string("trg_singlemuon_raw")) > 0) ? (SafeMap::Get(LambdaNtupleConsumer<KappaTypes>::GetBoolQuantities(), std::string("trg_singlemuon_raw")))(event, product) : false) && LambdaNtupleConsumer<KappaTypes>::GetFloatQuantities()["lep1Pt"](event, product) > 23.0;
        });
        LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("pt_ttjj", [](event_type const& event, product_type const& product)
        {
                return product.m_diJetSystemAvailable ? (product.m_diLeptonPlusMetSystem + product.m_diJetSystem).Pt() : DefaultValues::UndefinedFloat;
        });

	// need to be called at last
	KappaLambdaNtupleConsumer::Init(settings);
}
