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

print(Calculator().tipSplitCalculator(100))