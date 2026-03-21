#Error flags
err_invalidinput_marketcap = 'a'
err_invalidinput_area = 'b'
err_invalidinput_clearance = 'c'
err_unknown = 'j'

#Scoring
score_invalid_input = 0.2
score_unknown = 0.5

class Valuation():
    #Valuates an industrial warehouse property based on Net Operating Income, 
    #Market Capitalisation Rate, lettable area, rent per square metre, clearance,
    #weighted average lease expiry, purchase price

    #The user has to enter the market capitalisation rate (for the area), 
    #the clearance and the lettable area

    def __init__(self, marketCap, area, clearance):
        self.error_flag = ""
        self.score = 1
        self.marketCap = self.validate_float(marketCap, "marketCap")
        self.area = self.validate_float(area, "area")
        self.clearance = self.validate_float(clearance, "clearance")

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

    def property_value(self, NOI):
        #Property Value = Net Operating Income / Market Capitalisation Rate
        return (NOI / self.marketCap)

    def annual_rent(self, rent_sqm):
        #Annual Rent = Total Lettable Area (sqm) * Market Rent Per SQM
        return self.area * rent_sqm

    def net_yield(self, yearly_rent, annual_expenses, purchase_price):
        #Net Yield(%) = ((Annual Rent - Annual Expenses) / Purchase Price) * 100%
        return ((yearly_rent - annual_expenses) / purchase_price) * 100