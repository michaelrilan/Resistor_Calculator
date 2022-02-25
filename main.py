from numerize import numerize
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen,SwapTransition
from kivy.properties import ObjectProperty

Builder.load_file('resist.kv')

Window.size = (400,500)
class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)
        self.first_digit_four = None
        self.second_digit_four = None
        self.multiplier_four = None
        self.tolerance_four = None

        self.first_digit_five =None
        self.second_digit_five = None
        self.third_digit_five = None
        self.multiplier_five = None
        self.tolerance_five = None

        self.first_digit_six = None
        self.second_digit_six = None
        self.third_digit_six = None
        self.multiplier_six = None
        self.tolerance_six = None

        self.black = 0
        self.brown = 1
        self.red = 2
        self.orange = 3
        self.yellow = 4
        self.green = 5
        self.blue = 6
        self.violet = 7
        self.gray = 8
        self.white = 9


    def spinner_first_digit_four_clicked(self,value):
        if value == "brown":
            self.ids['first_digit_four'].background_color = (139/255,69/255,19/255,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.brown)
            self.first_digit_four = self.brown
        elif value == "red":
            self.ids['first_digit_four'].background_color = (1,0,0,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.red)
            self.first_digit_four = self.red
        elif value == "orange":
            self.ids['first_digit_four'].background_color = (1,165/255,0,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.orange)
            self.first_digit_four = self.orange
        elif value == "yellow":
            self.ids['first_digit_four'].background_color = (1,1,0,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.yellow)
            self.first_digit_four = self.yellow
        elif value == "green":
            self.ids['first_digit_four'].background_color = (0,1,0,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.green)
            self.first_digit_four = self.green
        elif value == "blue":
            self.ids['first_digit_four'].background_color = (0,0,1,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.blue)
            self.first_digit_four = self.blue
        elif value == "violet":
            self.ids['first_digit_four'].background_color = (149/255,0,179/255,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.violet)
            self.first_digit_four = self.violet
        elif value == "gray":
            self.ids['first_digit_four'].background_color = (128/255,128/255,128/255,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.gray)
            self.first_digit_four = self.gray
        elif value == "white":
            self.ids['first_digit_four'].background_color = (1,1,1,1)
            self.ids['equiv_spinner_first_digit_four'].text = "First Digit = " + str(self.white)
            self.first_digit_four = self.white

    def spinner_second_digit_four_clicked(self,value):
        if value == "black":
            self.ids['second_digit_four'].background_color = (0,0,0,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.black)
            self.second_digit_four = self.black
            print(self.second_digit_four)
        elif value == "brown":
            self.ids['second_digit_four'].background_color =  (139/255,69/255,19/255,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.brown)
            self.second_digit_four = self.brown
            print(self.second_digit_four)
        elif value == "red":
            self.ids['second_digit_four'].background_color = (1,0,0,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.red)
            self.second_digit_four = self.red
        elif value == "orange":
            self.ids['second_digit_four'].background_color = (1,165/255,0,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.orange)
            self.second_digit_four = self.orange
        elif value == "yellow":
            self.ids['second_digit_four'].background_color = (1,1,0,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.yellow)
            self.second_digit_four = self.yellow
        elif value == "green":
            self.ids['second_digit_four'].background_color = (0,1,0,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.green)
            self.second_digit_four = self.green
        elif value == "blue":
            self.ids['second_digit_four'].background_color = (0,0,1,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.blue)
            self.second_digit_four = self.blue
        elif value == "violet":
            self.ids['second_digit_four'].background_color = (149/255,0,179/255,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.violet)
            self.second_digit_four = self.violet
        elif value == "gray":
            self.ids['second_digit_four'].background_color = (128/255,128/255,128/255,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.gray)
            self.second_digit_four = self.gray
        elif value == "white":
            self.ids['second_digit_four'].background_color = (1,1,1,1)
            self.ids['equiv_spinner_second_digit_four'].text = "Second Digit = " + str(self.white)
            self.second_digit_four = self.white

    def spinner_multiplier_four_clicked(self, value):
        if value == "x1 black":
            number = (self.first_digit_four*10)+self.second_digit_four
            equation = number*1
            self.ids['multiplier_four'].background_color = (0, 0, 0, 1)
            self.ids['equiv_spinner_multiplier_four'].text ='Resistance = '+ str(equation) + 'Ω'
            self.multiplier_four = equation

        elif value == "x10 brown":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 10
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(equation) + 'Ω'
            self.ids['multiplier_four'].background_color = (139 / 255, 69 / 255, 19 / 255, 1)
            self.multiplier_four = equation
            print(self.second_digit_four)
        elif value == "x100 red":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 100
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_four'].background_color = (1, 0, 0, 1)
            self.multiplier_four = equation
        elif value == "x1k orange":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 1000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_four'].background_color = (1, 165 / 255, 0, 1)
            self.multiplier_four = equation
        elif value == "x10k yellow":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 10000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_four'].background_color = (1, 1, 0, 1)
            self.multiplier_four = equation

        elif value == "x100k green":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 100000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_four'].background_color = (0, 1, 0, 1)
            self.multiplier_four = equation
        elif value == "x1M blue":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 1000000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_four'].background_color = (0, 0, 1, 1)
            self.multiplier_four = equation
        elif value == "x10M violet":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 10000000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_four'].background_color = (149 / 255, 0, 179 / 255, 1)
            self.multiplier_four = equation
        elif value == "x100M gray":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 100000000
            metric = numerize.numerize(equation)
            rep = metric.replace('B','')
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(rep) + 'GΩ'
            self.ids['multiplier_four'].background_color = (128 / 255, 128 / 255, 128 / 255, 1)
            self.multiplier_four = equation
        elif value == "x1G white":

            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 1000000000
            metric = numerize.numerize(equation)
            rep = metric.replace('B', '')
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(rep) + 'GΩ'
            self.ids['multiplier_four'].background_color = (1, 1, 1, 1)
            self.multiplier_four = equation
        elif value == "x0.1 Gold":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 0.1
            metric = numerize.numerize(equation)
            rep = metric.replace('B', '')
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_four'].background_color = (218/255, 165/255, 32/255, 1)
            self.multiplier_four = equation
        elif value == "x0.01Silver":
            number = (self.first_digit_four * 10) + self.second_digit_four
            equation = number * 0.01
            metric = numerize.numerize(equation)
            rep = metric.replace('B', '')
            self.ids['equiv_spinner_multiplier_four'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_four'].background_color = (132 / 255, 132 / 255, 130 / 255, 1)
            self.multiplier_four = equation

    def spinner_tolerance_four_clicked(self,value):
        if value == "±1% brown":
            tolerance = self.multiplier_four * .01
            min = self.multiplier_four - tolerance
            max = self.multiplier_four + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)




            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance+'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min+'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max+'G'

            self.ids['equiv_spinner_tolerance_four'].text = ""
            self.ids['equiv_spinner_tolerance_four'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' +\
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' +\
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_four'].background_color = (139 / 255, 69 / 255, 19 / 255, 1)


        elif value == "±2% red":

            tolerance = self.multiplier_four * .02
            min = self.multiplier_four - tolerance
            max = self.multiplier_four + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_four'].text = ""
            self.ids['equiv_spinner_tolerance_four'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_four'].background_color = (0, 1, 0, 1)
        elif value == "±0.25% blue":
            tolerance = self.multiplier_four * .0025
            min = self.multiplier_four - tolerance
            max = self.multiplier_four + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_four'].text = ""
            self.ids['equiv_spinner_tolerance_four'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_four'].background_color = (0, 0, 1, 1)
        elif value == "±0.1% violet":
            tolerance = self.multiplier_four * .001
            min = self.multiplier_four - tolerance
            max = self.multiplier_four + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_four'].text = ""
            self.ids['equiv_spinner_tolerance_four'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_four'].background_color = (149 / 255, 0, 179 / 255, 1)
        elif value == "±0.05% gray":
            tolerance = self.multiplier_four * .0005
            min = self.multiplier_four - tolerance
            max = self.multiplier_four + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_four'].text = ""
            self.ids['equiv_spinner_tolerance_four'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_four'].background_color = (128 / 255, 128 / 255, 128 / 255, 1)
        elif value == "±5% gold":
            tolerance = self.multiplier_four * .05
            min = self.multiplier_four - tolerance
            max = self.multiplier_four + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_four'].text = ""
            self.ids['equiv_spinner_tolerance_four'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_four'].background_color = (218 / 255, 165 / 255, 32 / 255, 1)
        elif value == "±10% silver":
            tolerance = self.multiplier_four * .1
            min = self.multiplier_four - tolerance
            max = self.multiplier_four + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_four'].text =""
            self.ids['equiv_spinner_tolerance_four'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_four'].background_color = (132 / 255, 132 / 255, 130 / 255, 1)





    def spinner_first_digit_five_clicked(self,value):
        if value == "brown":
            self.ids['first_digit_five'].background_color = (139/255,69/255,19/255,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.brown)
            self.first_digit_five = self.brown
        elif value == "red":
            self.ids['first_digit_five'].background_color = (1,0,0,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.red)
            self.first_digit_five = self.red
        elif value == "orange":
            self.ids['first_digit_five'].background_color = (1,165/255,0,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.orange)
            self.first_digit_five = self.orange
        elif value == "yellow":
            self.ids['first_digit_five'].background_color = (1,1,0,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.yellow)
            self.first_digit_five = self.yellow
        elif value == "green":
            self.ids['first_digit_five'].background_color = (0,1,0,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.green)
            self.first_digit_five = self.green
        elif value == "blue":
            self.ids['first_digit_five'].background_color = (0,0,1,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.blue)
            self.first_digit_five = self.blue
        elif value == "violet":
            self.ids['first_digit_five'].background_color = (149/255,0,179/255,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.violet)
            self.first_digit_five = self.violet
        elif value == "gray":
            self.ids['first_digit_five'].background_color = (128/255,128/255,128/255,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.gray)
            self.first_digit_five = self.gray
        elif value == "white":
            self.ids['first_digit_five'].background_color = (1,1,1,1)
            self.ids['equiv_spinner_first_digit_five'].text = "First Digit = " + str(self.white)
            self.first_digit_five = self.white

    def spinner_second_digit_five_clicked(self,value):
        if value == "black":
            self.ids['second_digit_five'].background_color = (0,0,0,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.black)
            self.second_digit_five = self.black

        elif value == "brown":
            self.ids['second_digit_five'].background_color =  (139/255,69/255,19/255,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.brown)
            self.second_digit_five = self.brown
        elif value == "red":
            self.ids['second_digit_five'].background_color = (1,0,0,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.red)
            self.second_digit_five = self.red
        elif value == "orange":
            self.ids['second_digit_five'].background_color = (1,165/255,0,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.orange)
            self.second_digit_five = self.orange
        elif value == "yellow":
            self.ids['second_digit_five'].background_color = (1,1,0,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.yellow)
            self.second_digit_five = self.yellow
        elif value == "green":
            self.ids['second_digit_five'].background_color = (0,1,0,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.green)
            self.second_digit_five = self.green
        elif value == "blue":
            self.ids['second_digit_five'].background_color = (0,0,1,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.blue)
            self.second_digit_five = self.blue
        elif value == "violet":
            self.ids['second_digit_five'].background_color = (149/255,0,179/255,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.violet)
            self.second_digit_five = self.violet
        elif value == "gray":
            self.ids['second_digit_five'].background_color = (128/255,128/255,128/255,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.gray)
            self.second_digit_five = self.gray
        elif value == "white":
            self.ids['second_digit_five'].background_color = (1,1,1,1)
            self.ids['equiv_spinner_second_digit_five'].text = "Second Digit = " + str(self.white)
            self.second_digit_five = self.white

    def spinner_third_digit_five_clicked(self,value):
        if value == "black":
            self.ids['third_digit_five'].background_color = (0,0,0,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.black)
            self.third_digit_five = self.black
        elif value == "brown":
            self.ids['third_digit_five'].background_color =  (139/255,69/255,19/255,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.brown)
            self.third_digit_five = self.brown
        elif value == "red":
            self.ids['third_digit_five'].background_color = (1,0,0,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.red)
            self.third_digit_five = self.red
        elif value == "orange":
            self.ids['third_digit_five'].background_color = (1,165/255,0,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.orange)
            self.third_digit_five = self.orange
        elif value == "yellow":
            self.ids['third_digit_five'].background_color = (1,1,0,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.yellow)
            self.third_digit_five = self.yellow
        elif value == "green":
            self.ids['third_digit_five'].background_color = (0,1,0,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.green)
            self.third_digit_five = self.green
        elif value == "blue":
            self.ids['third_digit_five'].background_color = (0,0,1,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.blue)
            self.third_digit_five = self.blue
        elif value == "violet":
            self.ids['third_digit_five'].background_color = (149/255,0,179/255,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.violet)
            self.third_digit_five = self.violet
        elif value == "gray":
            self.ids['third_digit_five'].background_color = (128/255,128/255,128/255,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.gray)
            self.third_digit_five = self.gray
        elif value == "white":
            self.ids['third_digit_five'].background_color = (1,1,1,1)
            self.ids['equiv_spinner_third_digit_five'].text = "Third Digit = " + str(self.white)
            self.third_digit_five = self.white

    def spinner_multiplier_five_clicked(self, value):
        if value == "x1 black":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number*1
            self.ids['multiplier_five'].background_color = (0, 0, 0, 1)
            self.ids['equiv_spinner_multiplier_five'].text ='Resistance = '+ str(equation) + 'Ω'
            self.multiplier_five = equation

        elif value == "x10 brown":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 10
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (139 / 255, 69 / 255, 19 / 255, 1)
            self.multiplier_five = equation
            print(self.second_digit_five)
        elif value == "x100 red":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 100
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (1, 0, 0, 1)
            self.multiplier_five = equation
        elif value == "x1k orange":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 1000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (1, 165 / 255, 0, 1)
            self.multiplier_five = equation
        elif value == "x10k yellow":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 10000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (1, 1, 0, 1)
            self.multiplier_five = equation

        elif value == "x100k green":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 100000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (0, 1, 0, 1)
            self.multiplier_five = equation
        elif value == "x1M blue":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 1000000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (0, 0, 1, 1)
            self.multiplier_five = equation
        elif value == "x10M violet":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 10000000
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (149 / 255, 0, 179 / 255, 1)
            self.multiplier_five = equation
        elif value == "x100M gray":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 100000000
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (128 / 255, 128 / 255, 128 / 255, 1)
            self.multiplier_five = equation
        elif value == "x1G white":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 1000000000
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (1, 1, 1, 1)
            self.multiplier_five = equation
        elif value == "x0.1 Gold":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 0.1
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (218/255, 165/255, 32/255, 1)
            self.multiplier_five = equation
        elif value == "x0.01Silver":
            number = (self.first_digit_five*100)+(self.second_digit_five*10)+self.third_digit_five
            equation = number * 0.01
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_five'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_five'].background_color = (132 / 255, 132 / 255, 130 / 255, 1)
            self.multiplier_five = equation

    def spinner_tolerance_five_clicked(self,value):
        if value == "±1% brown":
            tolerance = self.multiplier_five * .01
            min = self.multiplier_five - tolerance
            max = self.multiplier_five + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)

            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance+'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min+'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max+'G'

            self.ids['equiv_spinner_tolerance_five'].text = ""
            self.ids['equiv_spinner_tolerance_five'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' +\
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' +\
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_five'].background_color = (139 / 255, 69 / 255, 19 / 255, 1)


        elif value == "±2% red":

            tolerance = self.multiplier_five * .02
            min = self.multiplier_five - tolerance
            max = self.multiplier_five + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_five'].text = ""
            self.ids['equiv_spinner_tolerance_five'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_five'].background_color = (0, 1, 0, 1)

        elif value == "±0.25% blue":
            tolerance = self.multiplier_five * .0025
            min = self.multiplier_five - tolerance
            max = self.multiplier_five + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_five'].text = ""
            self.ids['equiv_spinner_tolerance_five'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_five'].background_color = (0, 0, 1, 1)
        elif value == "±0.1% violet":
            tolerance = self.multiplier_five * .001
            min = self.multiplier_five - tolerance
            max = self.multiplier_five + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_five'].text = ""
            self.ids['equiv_spinner_tolerance_five'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_five'].background_color = (149 / 255, 0, 179 / 255, 1)
        elif value == "±0.05% gray":
            tolerance = self.multiplier_five * .0005
            min = self.multiplier_five - tolerance
            max = self.multiplier_five + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_five'].text = ""
            self.ids['equiv_spinner_tolerance_five'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_five'].background_color = (128 / 255, 128 / 255, 128 / 255, 1)
        elif value == "±5% gold":
            tolerance = self.multiplier_five * .05
            min = self.multiplier_five - tolerance
            max = self.multiplier_five + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_five'].text = ""
            self.ids['equiv_spinner_tolerance_five'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_five'].background_color = (218 / 255, 165 / 255, 32 / 255, 1)
        elif value == "±10% silver":
            tolerance = self.multiplier_five * .1
            min = self.multiplier_five - tolerance
            max = self.multiplier_five + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_five'].text =""
            self.ids['equiv_spinner_tolerance_five'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_five'].background_color = (132 / 255, 132 / 255, 130 / 255, 1)





    def spinner_first_digit_six_clicked(self,value):
        if value == "brown":
            self.ids['first_digit_six'].background_color = (139/255,69/255,19/255,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.brown)
            self.first_digit_six = self.brown
        elif value == "red":
            self.ids['first_digit_six'].background_color = (1,0,0,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.red)
            self.first_digit_six = self.red
        elif value == "orange":
            self.ids['first_digit_six'].background_color = (1,165/255,0,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.orange)
            self.first_digit_six = self.orange
        elif value == "yellow":
            self.ids['first_digit_six'].background_color = (1,1,0,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.yellow)
            self.first_digit_six = self.yellow
        elif value == "green":
            self.ids['first_digit_six'].background_color = (0,1,0,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.green)
            self.first_digit_six = self.green
        elif value == "blue":
            self.ids['first_digit_six'].background_color = (0,0,1,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.blue)
            self.first_digit_six = self.blue
        elif value == "violet":
            self.ids['first_digit_six'].background_color = (149/255,0,179/255,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.violet)
            self.first_digit_six = self.violet
        elif value == "gray":
            self.ids['first_digit_six'].background_color = (128/255,128/255,128/255,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.gray)
            self.first_digit_six = self.gray
        elif value == "white":
            self.ids['first_digit_six'].background_color = (1,1,1,1)
            self.ids['equiv_spinner_first_digit_six'].text = "First Digit = " + str(self.white)
            self.first_digit_six = self.white

    def spinner_second_digit_six_clicked(self,value):
        if value == "black":
            self.ids['second_digit_six'].background_color = (0,0,0,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.black)
            self.second_digit_six = self.black

        elif value == "brown":
            self.ids['second_digit_six'].background_color =  (139/255,69/255,19/255,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.brown)
            self.second_digit_six = self.brown
        elif value == "red":
            self.ids['second_digit_six'].background_color = (1,0,0,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.red)
            self.second_digit_six = self.red
        elif value == "orange":
            self.ids['second_digit_six'].background_color = (1,165/255,0,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.orange)
            self.second_digit_six = self.orange
        elif value == "yellow":
            self.ids['second_digit_six'].background_color = (1,1,0,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.yellow)
            self.second_digit_six = self.yellow
        elif value == "green":
            self.ids['second_digit_six'].background_color = (0,1,0,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.green)
            self.second_digit_six = self.green
        elif value == "blue":
            self.ids['second_digit_six'].background_color = (0,0,1,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.blue)
            self.second_digit_six = self.blue
        elif value == "violet":
            self.ids['second_digit_six'].background_color = (149/255,0,179/255,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.violet)
            self.second_digit_six = self.violet
        elif value == "gray":
            self.ids['second_digit_six'].background_color = (128/255,128/255,128/255,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.gray)
            self.second_digit_six = self.gray
        elif value == "white":
            self.ids['second_digit_six'].background_color = (1,1,1,1)
            self.ids['equiv_spinner_second_digit_six'].text = "Second Digit = " + str(self.white)
            self.second_digit_six = self.white

    def spinner_third_digit_six_clicked(self,value):
        if value == "black":
            self.ids['third_digit_six'].background_color = (0,0,0,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.black)
            self.third_digit_six = self.black
        elif value == "brown":
            self.ids['third_digit_six'].background_color =  (139/255,69/255,19/255,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.brown)
            self.third_digit_six = self.brown
        elif value == "red":
            self.ids['third_digit_six'].background_color = (1,0,0,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.red)
            self.third_digit_six = self.red
        elif value == "orange":
            self.ids['third_digit_six'].background_color = (1,165/255,0,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.orange)
            self.third_digit_six = self.orange
        elif value == "yellow":
            self.ids['third_digit_six'].background_color = (1,1,0,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.yellow)
            self.third_digit_six = self.yellow
        elif value == "green":
            self.ids['third_digit_six'].background_color = (0,1,0,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.green)
            self.third_digit_six = self.green
        elif value == "blue":
            self.ids['third_digit_six'].background_color = (0,0,1,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.blue)
            self.third_digit_six = self.blue
        elif value == "violet":
            self.ids['third_digit_six'].background_color = (149/255,0,179/255,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.violet)
            self.third_digit_six = self.violet
        elif value == "gray":
            self.ids['third_digit_six'].background_color = (128/255,128/255,128/255,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.gray)
            self.third_digit_six = self.gray
        elif value == "white":
            self.ids['third_digit_six'].background_color = (1,1,1,1)
            self.ids['equiv_spinner_third_digit_six'].text = "Third Digit = " + str(self.white)
            self.third_digit_six = self.white

    def spinner_multiplier_six_clicked(self, value):
        if value == "x1 black":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number*1
            self.ids['multiplier_six'].background_color = (0, 0, 0, 1)
            self.ids['equiv_spinner_multiplier_six'].text ='Resistance = '+ str(equation) + 'Ω'
            self.multiplier_six = equation

        elif value == "x10 brown":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 10
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (139 / 255, 69 / 255, 19 / 255, 1)
            self.multiplier_six = equation
            print(self.second_digit_six)
        elif value == "x100 red":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 100
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (1, 0, 0, 1)
            self.multiplier_six = equation
        elif value == "x1k orange":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 1000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (1, 165 / 255, 0, 1)
            self.multiplier_six = equation
        elif value == "x10k yellow":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 10000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (1, 1, 0, 1)
            self.multiplier_six = equation

        elif value == "x100k green":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 100000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (0, 1, 0, 1)
            self.multiplier_six = equation
        elif value == "x1M blue":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 1000000
            metric = numerize.numerize(equation)
            self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (0, 0, 1, 1)
            self.multiplier_six = equation
        elif value == "x10M violet":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 10000000
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (149 / 255, 0, 179 / 255, 1)
            self.multiplier_six = equation
        elif value == "x100M gray":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 100000000
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (128 / 255, 128 / 255, 128 / 255, 1)
            self.multiplier_six = equation
        elif value == "x1G white":
            number = (self.first_digit_six * 100) + (self.second_digit_six * 10) + self.third_digit_six
            equation = number * 1000000000
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (1, 1, 1, 1)
            self.multiplier_six = equation
        elif value == "x0.1 Gold":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 0.1
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (218/255, 165/255, 32/255, 1)
            self.multiplier_six = equation
        elif value == "x0.01Silver":
            number = (self.first_digit_six*100)+(self.second_digit_six*10)+self.third_digit_six
            equation = number * 0.01
            metric = numerize.numerize(equation)
            if 'B' in metric:
                rep = metric.replace('B', '')
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(rep) + 'GΩ'
            else:
                self.ids['equiv_spinner_multiplier_six'].text = 'Resistance = ' + str(metric) + 'Ω'
            self.ids['multiplier_six'].background_color = (132 / 255, 132 / 255, 130 / 255, 1)
            self.multiplier_five = equation

    def spinner_tolerance_six_clicked(self,value):
        if value == "±1% brown":
            tolerance = self.multiplier_six * .01
            min = self.multiplier_six - tolerance
            max = self.multiplier_six + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)

            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance+'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min+'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max+'G'

            self.ids['equiv_spinner_tolerance_six'].text = ""
            self.ids['equiv_spinner_tolerance_six'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' +\
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' +\
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_six'].background_color = (139 / 255, 69 / 255, 19 / 255, 1)


        elif value == "±2% red":

            tolerance = self.multiplier_six * .02
            min = self.multiplier_six - tolerance
            max = self.multiplier_six + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_six'].text = ""
            self.ids['equiv_spinner_tolerance_six'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_six'].background_color = (0, 1, 0, 1)

        elif value == "±0.25% blue":
            tolerance = self.multiplier_six * .0025
            min = self.multiplier_six - tolerance
            max = self.multiplier_six + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_six'].text = ""
            self.ids['equiv_spinner_tolerance_six'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_six'].background_color = (0, 0, 1, 1)
        elif value == "±0.1% violet":
            tolerance = self.multiplier_six * .001
            min = self.multiplier_six - tolerance
            max = self.multiplier_six + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_six'].text = ""
            self.ids['equiv_spinner_tolerance_six'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_six'].background_color = (149 / 255, 0, 179 / 255, 1)
        elif value == "±0.05% gray":
            tolerance = self.multiplier_six * .0005
            min = self.multiplier_six - tolerance
            max = self.multiplier_six + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_six'].text = ""
            self.ids['equiv_spinner_tolerance_six'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_six'].background_color = (128 / 255, 128 / 255, 128 / 255, 1)
        elif value == "±5% gold":
            tolerance = self.multiplier_six * .05
            min = self.multiplier_six - tolerance
            max = self.multiplier_six + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_six'].text = ""
            self.ids['equiv_spinner_tolerance_six'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_six'].background_color = (218 / 255, 165 / 255, 32 / 255, 1)
        elif value == "±10% silver":
            tolerance = self.multiplier_six * .1
            min = self.multiplier_six - tolerance
            max = self.multiplier_six + tolerance
            metric_tolerance = numerize.numerize(tolerance)
            metric_min = numerize.numerize(min)
            metric_max = numerize.numerize(max)
            if 'B' in metric_tolerance:
                rep_tolerance = metric_tolerance.replace('B', '')
                metric_tolerance = rep_tolerance + 'G'
            if 'B' in metric_min:
                rep_min = metric_min.replace('B', '')
                metric_min = rep_min + 'G'
            if 'B' in metric_max:
                rep_max = metric_max.replace('B', '')
                metric_max = rep_max + 'G'
            self.ids['equiv_spinner_tolerance_six'].text =""
            self.ids['equiv_spinner_tolerance_six'].text = 'Tolerance = ' + str(metric_tolerance) + 'Ω' + \
                                                            "\n" + "Minimum Ω = " + str(metric_min) + 'Ω' + \
                                                            '\n' + "Maximum Ω = " + str(metric_max) + 'Ω'
            self.ids['tolerance_six'].background_color = (132 / 255, 132 / 255, 130 / 255, 1)

    def spinner_temp_six_clicked(self,value):
        if value == "brown":
            self.ids['temp_six'].background_color = (139 / 255, 69 / 255, 19 / 255, 1)
            self.ids['equiv_spinner_temp_six'].text = "100 ppm/℃ TCR"
        elif value == "red":
            self.ids['temp_six'].background_color = (1, 0, 0, 1)
            self.ids['equiv_spinner_temp_six'].text = "50 ppm/℃ TCR"
        elif value == "orange":
            self.ids['temp_six'].background_color = (1, 165 / 255, 0, 1)
            self.ids['equiv_spinner_temp_six'].text = "15 ppm/℃ TCR"
        elif value == "yellow":
            self.ids['temp_six'].background_color = (1, 1, 0, 1)
            self.ids['equiv_spinner_temp_six'].text = "25 ppm/℃ TCR"
        elif value == "blue":
            self.ids['temp_six'].background_color = (0, 0, 1, 1)
            self.ids['equiv_spinner_temp_six'].text = "10 ppm/℃ TCR"
        elif value == "violet":
            self.ids['temp_six'].background_color = (149 / 255, 0, 179 / 255, 1)
            self.ids['equiv_spinner_temp_six'].text = "5 ppm/℃ TCR"



class ResistApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.sm = ScreenManager(transition = SwapTransition())
        self.sm.add_widget(FirstWindow(name="welcome_screen"))
        self.sm.add_widget(SecondWindow(name="second_screen"))
        return self.sm
    def change_screen(self, screen):
        # the same as in .kv: app.root.current = screen

        self.sm.current = screen





ResistApp().run()
fsdfsdfsdf
jsdnhfgkldfjasdlkfsd;aklfks;ldkf;