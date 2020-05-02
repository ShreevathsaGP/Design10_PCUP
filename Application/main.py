import urllib
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from calc import CarbonFootprint
from locations import Scrape
from kivy.core.window import Window
from kivy.config import Config
import json
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.garden.navigationdrawer import NavigationDrawer

__version__ = "1.11.1"


def clear_database():
    database = open('footprint.txt', 'w')
    database.write(str("0"))
    database.close()


clear_database()

CarbonFootprintValues = []
CarbonFootprintValues.clear()

names = None
addresses = None
websites = None


class HomeScreen(Screen):
    Window.size = (600, 12000)
    Config.set('graphics', 'resize', False)
    pass


class Educate(Screen):
    info_1 = ObjectProperty(None)
    Window.size = (600, 12000)

    def on_enter(self):
        with open('info_1.txt', 'r') as info_1:
            self.info_1.text = str(info_1.read())
        info_1.close()


class Educate_2(Screen):
    info_1 = ObjectProperty(None)
    Window.size = (600, 12000)

    def on_enter(self):
        with open('info_2.txt', 'r') as info_2:
            self.info_1.text = str(info_2.read())
        info_2.close()


class Educate_3(Screen):
    info_1 = ObjectProperty(None)
    Window.size = (600, 12000)

    def on_enter(self):
        with open('info_3.txt', 'r') as info_3:
            self.info_1.text = str(info_3.read())
        info_3.close()


class Educate_4(Screen):
    info_1 = ObjectProperty(None)
    Window.size = (600, 12000)

    def on_enter(self):
        with open('info_4.txt', 'r') as info_4:
            self.info_1.text = str(info_4.read())
        info_4.close()


class Educate_5(Screen):
    info_1 = ObjectProperty(None)
    Window.size = (600, 12000)

    def on_enter(self):
        with open('info_5.txt', 'r') as info_5:
            self.info_1.text = str(info_5.read())
        info_5.close()


class Educate_6(Screen):
    info_1 = ObjectProperty(None)
    Window.size = (600, 12000)

    def on_enter(self):
        with open('info_6.txt', 'r') as info_6:
            self.info_1.text = str(info_6.read())
        info_6.close()


class Educate_7(Screen):
    info_1 = ObjectProperty(None)
    Window.size = (600, 12000)

    def on_enter(self):
        with open('info_7.txt', 'r') as info_7:
            self.info_1.text = str(info_7.read())
        info_7.close()


class Educate_8(Screen):
    info_1 = ObjectProperty(None)
    Window.size = (600, 12000)

    def on_enter(self):
        with open('info_8.txt', 'r') as info_8:
            self.info_1.text = str(info_8.read())
        info_8.close()


class Calculate(Screen):
    Window.size = (600, 12000)
    family_members = ObjectProperty(None)
    electricity_small = ObjectProperty(None)
    electricity_medium = ObjectProperty(None)
    electricity_large = ObjectProperty(None)
    lpg = ObjectProperty(None)
    no_cars = ObjectProperty(None)
    kmperl = ObjectProperty(None)
    mileage = ObjectProperty(None)

    def get_values(self):
        CarbonFootprintValues.clear()

        z_family_members = str(self.family_members.text)

        if self.electricity_small.active is True:
            z_electricity = 'Small'
        elif self.electricity_medium is True:
            z_electricity = 'Medium'
        elif self.electricity_large.active is True:
            z_electricity = 'Large'
        else:
            z_electricity = 'Medium'

        z_LPG = self.lpg.text
        z_no_cars = self.no_cars.text
        z_kmperl = self.kmperl.text
        z_mileage = self.mileage.text

        calculate = [z_family_members, z_electricity, z_LPG, z_no_cars, z_kmperl, z_mileage]

        for value in calculate:
            CarbonFootprintValues.append(value)

        self.family_members.text = ''
        self.lpg.text = ''
        self.no_cars.text = ''
        self.kmperl.text = ''
        self.mileage.text = ''

        self.electricity_small.active = False
        self.electricity_medium.active = False
        self.electricity_large.active = False
        return 'success'


class Calculate_Personal(Screen):
    Window.size = (600, 12000)
    airplane = ObjectProperty(None)
    bus = ObjectProperty(None)
    train = ObjectProperty(None)

    organic_none = ObjectProperty(None)
    organic_some = ObjectProperty(None)
    organic_most = ObjectProperty(None)
    organic_all = ObjectProperty(None)

    meatdiary_all = ObjectProperty(None)
    meatdiary_average = ObjectProperty(None)
    meatdiary_little = ObjectProperty(None)
    meatdiary_vegetarian = ObjectProperty(None)
    meatdiary_vegan = ObjectProperty(None)

    source_none = ObjectProperty(None)
    source_average = ObjectProperty(None)
    source_most = ObjectProperty(None)
    source_all = ObjectProperty(None)

    def get_values(self):

        z_airplane = self.airplane.text
        z_bus = self.bus.text
        z_train = self.train.text
        if self.organic_none.active is True:
            z_organic = 'None'
        elif self.organic_some.active is True:
            z_organic = 'Some'
        elif self.organic_most.active is True:
            z_organic = 'Most'
        elif self.organic_all.active is True:
            z_organic = 'All'
        else:
            z_organic = 'None'

        if self.meatdiary_all.active is True:
            z_meatdiary = 'Above-average'
        elif self.meatdiary_average.active is True:
            z_meatdiary = 'Average'
        elif self.meatdiary_little.active is True:
            z_meatdiary = 'Below-average'
        elif self.meatdiary_vegetarian.active is True:
            z_meatdiary = 'Lacto-vegetarian'
        elif self.meatdiary_vegan.active is True:
            z_meatdiary = 'Vegan'
        else:
            z_meatdiary = 'Average'

        if self.source_none.active is True:
            z_food_source = 'Foreign'
        elif self.source_average.active is True:
            z_food_source = 'Average'
        elif self.source_most.active is True:
            z_food_source = 'Most'
        elif self.source_all.active is True:
            z_food_source = 'All'
        else:
            z_food_source = 'Average'

        calculate_2 = [z_airplane, z_bus, z_train, z_organic, z_meatdiary, z_food_source]
        for value in calculate_2:
            CarbonFootprintValues.append(value)

        self.airplane.text = ''
        self.bus.text = ''
        self.train.text = ''

        self.organic_none.active = False
        self.organic_some.active = False
        self.organic_most.active = False
        self.organic_all.active = False

        self.meatdiary_all.active = False
        self.meatdiary_average.active = False
        self.meatdiary_little.active = False
        self.meatdiary_vegetarian.active = False
        self.meatdiary_vegan.active = False

        self.source_none.active = False
        self.source_average.active = False
        self.source_most.active = False
        self.source_all.active = False
        return 'success'


class Calculate_Personal_2(Screen):
    Window.size = (600, 12000)
    packaged_aboveaverage = ObjectProperty(None)
    packaged_average = ObjectProperty(None)
    packaged_belowaverage = ObjectProperty(None)
    packaged_none = ObjectProperty(None)

    compost_none = ObjectProperty(None)
    compost_some = ObjectProperty(None)
    compost_all = ObjectProperty(None)

    waste_morefifty = ObjectProperty(None)
    waste_lessfifty = ObjectProperty(None)
    waste_lessthirty = ObjectProperty(None)
    waste_lessten = ObjectProperty(None)

    recycle_yes = ObjectProperty(None)
    recycle_no = ObjectProperty(None)

    def get_values(self):
        if self.packaged_aboveaverage.active is True:
            z_food_packaging = 'Above-average'
        elif self.packaged_belowaverage.active is True:
            z_food_packaging = 'Below-average'
        elif self.packaged_average.active is True:
            z_food_packaging = 'Average'
        elif self.packaged_none.active is True:
            z_food_packaging = 'None'
        else:
            z_food_packaging = 'Average'

        if self.compost_none.active is True:
            z_compost = 'None'
        elif self.compost_some.active is True:
            z_compost = 'Some'
        elif self.compost_all.active is True:
            z_compost = 'All'
        else:
            z_compost = 'None'

        if self.waste_morefifty.active is True:
            z_food_waste = '>50%'
        elif self.waste_lessfifty.active is True:
            z_food_waste = '<50%'
        elif self.waste_lessthirty.active is True:
            z_food_waste = '<30%'
        elif self.waste_lessten.active is True:
            z_food_waste = '<10%'
        else:
            z_food_waste = '<50%'

        if self.recycle_yes.active is True:
            z_recycle = True
        elif self.recycle_no.active is True:
            z_recycle = False
        else:
            z_recycle = False

        calculate_3 = [z_food_packaging, z_compost, z_food_waste, z_recycle]
        for value in calculate_3:
            CarbonFootprintValues.append(value)
        try:
            carbon_footprint = CarbonFootprint(CarbonFootprintValues[0], CarbonFootprintValues[1], CarbonFootprintValues[2],
                        CarbonFootprintValues[3], CarbonFootprintValues[4], CarbonFootprintValues[5],
                        CarbonFootprintValues[6], CarbonFootprintValues[7], CarbonFootprintValues[8],
                        CarbonFootprintValues[9],CarbonFootprintValues[10], CarbonFootprintValues[11],
                        CarbonFootprintValues[12],CarbonFootprintValues[13], CarbonFootprintValues[14],
                        CarbonFootprintValues[15]).calculate()
            print("User's carbon footprint:", str(carbon_footprint))
            database = open('footprint.txt', 'w')
            database.write(str(carbon_footprint))
            database.close()
        except:
            print("User missed inputs")

        self.packaged_aboveaverage.active = False
        self.packaged_average.active = False
        self.packaged_belowaverage.active = False
        self.packaged_none.active = False

        self.compost_none.active = False
        self.compost_some.active = False
        self.compost_all.active = False

        self.waste_morefifty.active = False
        self.waste_lessfifty.active = False
        self.waste_lessthirty.active = False
        self.waste_lessten.active = False

        self.recycle_yes.active = False
        self.recycle_no.active = False


class CarbonFootprintPage(Screen):
    Window.size = (600, 12000)
    pass_footprint = ObjectProperty(None)

    def on_enter(self):
        database = open('footprint.txt', 'r')
        value = database.readline()
        if float(value) == 0:
            self.pass_footprint.text = "!!YOU MISSED SOME INPUTS, PLEASE RECALCULATE!!"
        else:
            self.pass_footprint.text = str(round(float(value), 4))
        clear_database()


class TakeAction(Screen):
    Window.size = (600, 12000)
    info_1 = ObjectProperty(None)

    def on_enter(self):
        with open('action.txt', 'r') as info_1:
            self.info_1.text = str(info_1.read())
        info_1.close()


class TakeAction_2(Screen):
    Window.size = (600, 12000)
    info_1 = ObjectProperty(None)

    def on_enter(self):
        with open('action_2.txt', 'r') as info_2:
            self.info_1.text = str(info_2.read())
        info_2.close()


class TakeAction_3(Screen):
    Window.size = (600, 12000)
    info_1 = ObjectProperty(None)

    def on_enter(self):
        with open('action_3.txt', 'r') as info_3:
            self.info_1.text = str(info_3.read())
        info_3.close()


class TakeAction_4(Screen):
    Window.size = (600, 12000)
    info_1 = ObjectProperty(None)

    def on_enter(self):
        with open('action_4.txt', 'r') as info_4:
            self.info_1.text = str(info_4.read())
        info_4.close()


class TakeAction_5(Screen):
    Window.size = (600, 12000)
    info_1 = ObjectProperty(None)

    def on_enter(self):
        with open('action_5.txt', 'r') as info_5:
            self.info_1.text = str(info_5.read())
        info_5.close()


class TakeAction_6(Screen):
    Window.size = (600,1200)
    info_1 = ObjectProperty(None)

    def on_enter(self):
        with open('action_6.txt', 'r') as info_6:
            self.info_1.text = str(info_6.read())


class NearbyLocation(Screen):
    Window.size = (600, 12000)
    query = ObjectProperty(None)

    def get_locations(self):
        query = str(self.query.text)
        iterations = 0

        for result in Scrape(search=query).scrape():
            iterations += 1
            if iterations == 1:
                names = result

            if iterations == 2:
                addresses = result

            if iterations == 3:
                websites = result

        print("Names: ", names)
        print("Addresses: ", addresses)
        print("Websites: ", websites)

        final_content = []

        for x in range(len(names)):
            data_installment = {'information':'Name: '+str(names[x])+'\n'+'   Address: '+str(addresses[x])+'\n'+'   Website: '+str(websites[x])+'\n'+' '}
            final_content.append(data_installment)

        content_store = open('name_store.txt', 'w')
        json.dump(final_content, content_store)
        content_store.close()
        final_content.clear()

    def on_enter(self):
        self.query.text = ''


class NearbyResults( Screen):
    final_content = ListProperty(None)
    result_1 = ObjectProperty(None)
    result_2 = ObjectProperty(None)
    result_3 = ObjectProperty(None)
    result_4 = ObjectProperty(None)
    result_5 = ObjectProperty(None)
    result_6 = ObjectProperty(None)
    result_7 = ObjectProperty(None)
    result_8 = ObjectProperty(None)
    result_9 = ObjectProperty(None)
    result_10 = ObjectProperty(None)
    result_11 = ObjectProperty(None)
    result_12 = ObjectProperty(None)
    result_13 = ObjectProperty(None)
    result_14 = ObjectProperty(None)

    def on_enter(self):
        with open('name_store.txt', 'r') as content_store:
            self.final_content = json.load(content_store)
            # print(self.final_content)
            # print(len(self.final_content))

        try:
            self.result_1.halign = 'left'
            self.result_1.text = str(str(1)+")"+self.final_content[0]['information'])
        except:
            self.result_1.valign = 'middle'
            self.result_1.halign = 'center'
            self.result_1.text = 'SORRY, THERE WERE NO RESULTS, PLEASE RETURN HOME OR TRY A DIFFERENT SEARCH'
        try:
            self.result_2.text = str(str(2)+")"+self.final_content[1]['information'])
        except:
            self.result_2.text = ''
        try:
            self.result_3.text = str(str(3)+")"+self.final_content[2]['information'])
        except:
            self.result_3.text = ''
        try:
            self.result_4.text = str(str(4)+")"+self.final_content[3]['information'])
        except:
            self.result_4.text = ''
        try:
            self.result_5.text = str(str(5)+")"+self.final_content[4]['information'])
        except:
            self.result_5.text = ''
        try:
            self.result_6.text = str(str(6)+")"+self.final_content[5]['information'])
        except:
            self.result_6.text = ''
        try:
            self.result_7.text = str(str(7)+")"+self.final_content[6]['information'])
        except:
            self.result_7.text = ''
        try:
            self.result_8.text = str(str(8)+")"+self.final_content[7]['information'])
        except:
            self.result_8.text = ''
        try:
            self.result_9.text = str(str(9)+")"+self.final_content[8]['information'])
        except:
            self.result_9.text = ''
        try:
            self.result_10.text = str(str(10)+")"+self.final_content[9]['information'])
        except:
            self.result_10.text = ''
        try:
            self.result_11.text = str(str(11)+")"+self.final_content[10]['information'])
        except:
            self.result_11.text = ''
        try:
            self.result_12.text = str(str(12)+")"+self.final_content[11]['information'])
        except:
            self.result_12.text = ''
        try:
            self.result_13.text = str(str(13)+")"+self.final_content[12]['information'])
        except:
            self.result_13.text = ''
        try:
            self.result_14.text = str(str(14)+")"+self.final_content[13]['information'])
        except:
            self.result_14.text = ''


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class WMGApp(App):
    def build(self):
        Config.set('graphics', 'resize', False)
        return kv


if __name__ == "__main__":
    WMGApp().run()
