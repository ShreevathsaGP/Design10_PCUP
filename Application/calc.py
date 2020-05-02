class CarbonFootprint:
    def __init__(self,
                 family_members, electricity, lpg,
                 no_cars,  kmperl, mileage, airplane, bus, train,
                 organic, meatdiary, food_source, food_packaging, compost, food_waste,
                 # miscellaneous_spending,
                 recycle):

        # Household
        self.family_members = int(family_members)
        self.electricity = electricity
        self.lpg = float(lpg)

        # Transport (Does not take into account members of household)
        self.cartype = 'regular'
        
        if len(no_cars) > 0:
            self.no_cars = int(no_cars)
        else:
            self.no_cars = no_cars

        if self.no_cars == '' or 0:
            self.no_cars = 0
            self.kmperl = 0
            self.mileage = 0
        else:
            self.no_cars = int(no_cars)
            if self.no_cars > 0:
                self.kmperl = float(kmperl)
                self.mileage = float(mileage)
            else:
                self.kmperl = 0
                self.mileage = 0

        self.bus = float(bus)
        self.airplane = float(airplane)
        self.train = float(train)

        # Food and waste (Does not take into account members of household)

        self.organic = organic
        self.meatdiary = meatdiary
        self.food_source = food_source
        self.food_packaging = food_packaging
        self.compost = compost
        self.food_waste = food_waste

        # self.miscellaneous_spending = miscellaneous_spending

        if recycle == 'True':
            self.recycle = True
        elif recycle == 'False':
            self.recycle = False
        else:
            self.recycle = recycle

    def calculate(self):
        carbon_total = 0 # Carbon emitted in a year calculated in tons (1 metric ton = 1000kg)
        # Household
        if self.electricity == 'Small':
            carbon_total += 0.98
        elif self.electricity == 'Medium':
            carbon_total += 1.48
        elif self.electricity == 'Large':
            carbon_total += 2.16
        else:
            add = (0.309 * self.electricity)/1000
            carbon_total += add

        if type(self.lpg) == float:
            add = self.lpg * 0.4875
            carbon_total += add
        else:
            print("Could not calculate LPG")

        if type(self.family_members) == int:
            individual_carbon_total = (carbon_total/self.family_members)

        else:
            individual_carbon_total = carbon_total
            print("No. of family members cannot be irrational")

        # Transport
        if self.cartype == 'electric':
            individual_carbon_total += 0
        else:
            # 1 UK (Imperial) gallon = 4.54609 litres
            # 3.156kg CO2 per litre
            # 72.4205km/4.5604 litres

            co2_km = 3.1456
            individual_carbon_total += (((self.mileage/self.kmperl) * co2_km)/1000)

        # 0.062137kg CO2 per km in bus or train
        co2_km_train_bus = 0.062137
        individual_carbon_total += (((self.bus) * co2_km_train_bus)/1000)
        individual_carbon_total += (((self.train) * co2_km_train_bus)/1000)

        # 0.255tonnes CO2 per 1000km in air
        co2tons_km_airplane = 0.000255
        individual_carbon_total += (self.airplane * co2tons_km_airplane)

        # Food and Waste
        if self.organic == 'None':
            individual_carbon_total += 0.7
        elif self.organic == 'Some':
            individual_carbon_total += 0.5
        elif self.organic == 'Most':
            individual_carbon_total += 0.2
        elif self.organic == 'All':
            individual_carbon_total += 0
        else:
            individual_carbon_total += 0.6

        if self.meatdiary == 'Above-average':
            individual_carbon_total += 0.6
        elif self.meatdiary == 'Average':
            individual_carbon_total += 0.4
        elif self.meatdiary == 'Below-average':
            individual_carbon_total += 0.25
        elif self.meatdiary == 'Lacto-vegetarian':
            individual_carbon_total +=0.1
        elif self.meatdiary == 'Vegan':
            individual_carbon_total += 0
        else:
            individual_carbon_total += 0.4

        if self.food_source == 'Foreign':
            individual_carbon_total += 0.5
        elif self.food_source == 'Average':
            individual_carbon_total += 0.3
        elif self.food_source == 'Most':
            individual_carbon_total += 0.2
        elif self.food_source == 'All':
            individual_carbon_total += 0.1
        else:
            individual_carbon_total += 0.3

        if self.food_packaging == 'Above-average':
            individual_carbon_total += 0.6
        elif self.food_packaging == 'Average':
            individual_carbon_total += 0.4
        elif self.food_packaging == 'Below-average':
            individual_carbon_total += 0.2
        elif self.food_packaging == 'None':
            individual_carbon_total += 0.05
        else:
            individual_carbon_total += 0.4

        if self.compost == 'None':
            individual_carbon_total += 0.2
        elif self.compost == 'Some':
            individual_carbon_total += 0.1
        elif self.compost == 'All':
            individual_carbon_total += 0
        else:
            individual_carbon_total += 0.1

        if self.food_waste == '>50%':
            individual_carbon_total += 0.15
        elif self.food_waste == '<50%':
            individual_carbon_total += 0
        elif self.food_waste == '<30%':
            individual_carbon_total -= 0.25
        elif self.food_waste == '<10%':
            individual_carbon_total -= 0.30
        else:
            pass

        # 1.1 tonnes for health, education etc.
        individual_carbon_total += 1.1

        # Miscellaneous spending on products
        individual_carbon_total += 2

        if self.recycle is True:
            individual_carbon_total -= 0.5
        elif self.recycle is False:
            pass
        else:
            pass

        return individual_carbon_total

    def store(self):
        pass

    def show(self):
        pass
