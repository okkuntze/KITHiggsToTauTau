
#pragma once

#include "Artus/Core/interface/FilterBase.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttTypes.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttEnumTypes.h"


/** Filter for exclusively defined event category.
 *  Required config tag:
 *  - Category
 */
class EventCategoryFilter: public FilterBase<HttTypes> {
public:

	typedef typename HttTypes::event_type event_type;
	typedef typename HttTypes::product_type product_type;
	typedef typename HttTypes::setting_type setting_type;
	
	virtual std::string GetFilterId() const ARTUS_CPP11_OVERRIDE {
            return "EventCategoryFilter";
    }
    
	virtual void Init(setting_type const& settings) ARTUS_CPP11_OVERRIDE;

	virtual bool DoesEventPass(event_type const& event, product_type const& product,
	                           setting_type const& settings) const ARTUS_CPP11_OVERRIDE;


private:
	HttEnumTypes::EventCategory m_eventCategory;

};


