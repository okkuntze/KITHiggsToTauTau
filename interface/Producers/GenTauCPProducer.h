#pragma once

#include "Artus/Utility/interface/Utility.h"


#include "../HttTypes.h"

/**
   \brief GlobalProducer, for CP studies of tau decays. Following quantities are calculated from the input of GenTauDecayProducer :
   
   -Phi* : this is a variable, with which one can say, whether the considered Higgs-Boson is a scalar (CP even) or a pseudoscalar (CP odd)
   -Psi*CP : this is a variable, with which one can figure out, whether the have a CP-mixture or not
*/

class GenTauCPProducer : public HttProducerBase {
public:
	
	virtual std::string GetProducerId() const ARTUS_CPP11_OVERRIDE {
		return "gen_cp";
	}

	virtual void Produce(HttEvent const& event, HttProduct& product,
	                     HttPipelineSettings const& settings) const ARTUS_CPP11_OVERRIDE;
};
