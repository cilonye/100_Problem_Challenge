import re


class Calculator:

    def tipSplitCalculator(self, cost):
        tip_info = input('Do you want to tip? (YES/NO) ')
        guest_size = int(input('How many guest? '))

        if re.search('y|Y', tip_info):
            tip_percentage = input('Enter_tip_percentage? ')
            tip = (cost * (float(tip_percentage)/100))
            cost += tip

        return cost/guest_size

    def BMICalculator(self):
        measurement_system = input(
            'Enter A if weight and height are in Kg/m\nEnter B if weight and height are in lbs/in: ')
        weight = float(input('Enter your weight? '))
        height = float(input('Enter your height? '))

        if measurement_system == 'A':
            BMI = weight / height ** 2
        else:
            BMI = (weight * 703)/(height ** 2)

        if BMI < 18.5:
            return 'Underweight'
        elif 18.5 <= BMI <= 24.9:
            return 'Normal weight'
        elif 25 <= BMI <= 29.9:
            return 'Overweight'
        else:
            return 'Obesity'

    def checkOddOrEven(self, num):
        if num % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

    def checkLeapYear(self, year):
        pre_check = (year / 4) % 2

        if pre_check != 0:
            return "The year is not a leap year"

        else:
            add_check = (year / 100) % 2
            if add_check != 0:
                return "The year is a leap year"

            else:
                if (year / 400) % 2 == 0:
                    return "The year is a leap year"

                return "The year is not a leap year"


print(Calculator().checkOddOrEven(2401))
