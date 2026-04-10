#Error flags
err_invalidinput_marketcap = 'a'
err_invalidinput_area = 'b'
err_invalidinput_clearance = 'c'
err_unrecognised_location = 'd'
err_unknown = 'j'

#Scoring
score_invalid_input = 20
score_unrecognised_location = 20
score_unknown = 50

class Valuation():
    #Valuates an industrial warehouse property based on Net Operating Income, 
    #Market Capitalisation Rate, lettable area, rent per square metre, clearance,
    #weighted average lease expiry, purchase price

    #The user has to enter the market capitalisation rate (for the area), 
    #the clearance, the location and the lettable area

    def __init__(self, marketCap, area, clearance, location):
        self.error_flag = ""
        self.score = 100
        self.marketCap = self.validate_market_cap(marketCap)
        self.area = self.validate_float(area, "area")
        self.clearance = self.validate_float(clearance, "clearance")
        self.location = location
        self.values = {}

    def adjust_score(self, adjustment):
        new_score = self.score - adjustment
        if new_score >= 0:
            self.score = new_score

    def validate_float(self, s_num, numtype, percentage = False):
        #Checks if number is a number
        try:
            val = float(s_num)
            if val < 0:
               return self.manage_input_error(numtype)
            if percentage == True:
                if val > 100:
                    return self.manage_input_error(numtype)
                if val > 1 and val< 100:
                    val /= 100        
            return val 

        except:
            #Return default
            return self.manage_input_error(numtype)
    
    def validate_market_cap(self, s_num):
        try:
            val = float(s_num)
            if val < 0:
                return self.manage_input_error("marketCap")
            # Convert percentage inputs
            if val > 1:
                val /= 100  # 5 -> 0.05
            # Sanity bounds for industrial market cap
            if val < 0.01 or val > 0.15:
                self.error_flag += str(err_invalidinput_marketcap)
                self.adjust_score(score_invalid_input)
                return 0.05  # fallback
            return val

        except:
            return self.manage_input_error("marketCap")

    def manage_input_error(self, numtype):
        if numtype == "marketCap":
           self.error_flag += str(err_invalidinput_marketcap)
           self.adjust_score(score_invalid_input)
           return 0.05 #Average market capitalisation for Sydney industrial is roughly 5%

        if numtype == "area":
           self.error_flag += str(err_invalidinput_area)
           self.adjust_score(score_invalid_input)
           return 12800 #Average warehouse area for Sydney industrial is roughly 12800 sqm
        
        if numtype == "clearance":
            self.error_flag += str(err_invalidinput_clearance)
            self.adjust_score(score_invalid_input)
            return 12 #Average warehouse clearance for Sydnye industrial is roughly 12m

        self.error_flag = err_unknown
        self.adjust_score(score_unknown)
        return 1

    def NOI(self, yearly_rent, expense_ratio):
        #Calculates annual net operating income for the warehouse
        # Get location params if not provided
        noi = yearly_rent * (1 - expense_ratio)
        return noi

    def property_value(self, NOI):
        #value = NOI / market capitalisation
        if self.marketCap == 0:
            return 0
        return (NOI / self.marketCap)

    def rent_per_sqm(self, R_base, F_location):
        F_height = 1 + 0.04 * (self.clearance - 8)
        # crude size factor
        if self.area < 5000:
            F_size = 1.1
        elif self.area > 30000:
            F_size = 0.9
        else:
            F_size = 1.0
        F_quality = 1.1   # assume prime
        return R_base * F_height * F_size * F_location * F_quality

    def annual_rent(self, rent_sqm):
        return self.area * rent_sqm

    def net_yield(self, yearly_rent, annual_expenses, purchase_price):
        #Net Yield(%) = ((Annual Rent - Annual Expenses) / Purchase Price) * 100%
        if purchase_price == 0:
            return 0
        return ((yearly_rent - annual_expenses) / purchase_price) * 100
    
    def get_location_params(self):
        # Base parameters by industrial precinct
        precincts = {
            "South Sydney": (180, 1.2, 0.12),
            "Inner West": (170, 1.1, 0.13),
            "Central West": (150, 1.0, 0.15),
            "South West": (130, 0.95, 0.16),
            "Outer West": (110, 0.9, 0.18),
        }
        # Map suburbs to precincts
        suburb_map = {
            "Alexandria": "South Sydney",
            "Botany": "South Sydney",
            "Mascot": "South Sydney",
            "Banksmeadow": "South Sydney",
            "Marrickville": "Inner West",
            "St Peters": "Inner West",
            "Tempe": "Inner West",
            "Eastern Creek": "Central West",
            "Erskine Park": "Central West",
            "Wetherill Park": "Central West",
            "Huntingwood": "Central West",
            "Moorebank": "South West",
            "Liverpool": "South West",
            "Prestons": "South West",
            "Ingleburn": "South West",
            "Penrith": "Outer West",
            "St Marys": "Outer West",
            "Mount Druitt": "Outer West",
        }
        # Suburb-specific overrides
        suburb_params = {
            "Alexandria": (200, 1.3, 0.11),
            "Mascot": (190, 1.25, 0.11),
            "Botany": (185, 1.2, 0.12),
            "Wetherill Park": (155, 1.05, 0.14),
            "Eastern Creek": (160, 1.05, 0.14),
            "Moorebank": (145, 1.0, 0.15),
            "Prestons": (135, 0.95, 0.16),
            "Penrith": (115, 0.9, 0.18),
        }
        location = self.location
        # STEP 1: Suburb override (highest priority)
        if location in suburb_params:
            return suburb_params[location]
        # STEP 2: Suburb to precinct
        if location in suburb_map:
            precinct = suburb_map[location]
            return precincts[precinct]
        # STEP 3: Direct precinct input
        if location in precincts:
            return precincts[location]
        # STEP 4: Unknown location
        self.error_flag += str(err_unrecognised_location)
        self.adjust_score(score_unrecognised_location)
        return (140, 1.0, 0.15)

    def calculate_values(self, yearly_rent, noi, value, yield_pct):
        if yearly_rent is not None:
            self.values.update({"annual_rent": yearly_rent})
        if noi is not None:
            self.values.update({"NOI": noi})
        if value is not None:
            self.values.update({"value": value})
        if yield_pct is not None:
            self.values.update({"yield": yield_pct})
        self.values.update({"score": str(self.score)})
        if self.error_flag != "":
            self.values.update({"errors": self.error_flag})

    def valuate_warehouse(self):
        params = self.get_location_params()
        R_base = params[0]
        F_location = params[1]
        expense_ratio = params[2]

        rent_sqm = self.rent_per_sqm(R_base, F_location)
        yearly_rent = self.annual_rent(rent_sqm)
        noi = self.NOI(yearly_rent, expense_ratio)
        value = self.property_value(noi)
        yield_pct = self.net_yield(yearly_rent, yearly_rent * expense_ratio, value)

        self.calculate_values(yearly_rent, noi, value, yield_pct)

    def return_values(self):
        return self.values