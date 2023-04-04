import sys
import time


class RentCalc():
    def __init__(self):
        self.rent = 0
        self.laundry = 0
        self.storage = 0
        self.misc = 0
        self.incometotal = 0
        
        self.taxes = 0
        self.insurance = 0
        self.utilitiestotal = 0
        self.electricity = 0
        self.water = 0
        self.sewer = 0
        self.garbage = 0
        self.gas = 0
        self.hoa = 0
        self.lawn_snow = 0
        self.vacancy = 0
        self.repairs = 0
        self.capex = 0 #Capitol Expendatures
        self.prop_mngmnt = 0
        self. mortgage = 0
        self.expenses_total = 0

        self.downpayment = 0
        self.closingcost = 0
        self.rehabbudget = 0
        self.miscother = 0
        self.investent_total = 0
        self.cashflow = 0

    def type_string(self, string, delay=0.03, newline = True): #custom self.type_string function creates the illusion of typing in real time
        for char in string:
            sys.stdout.write(char) #write each character to the screen individually
            sys.stdout.flush() #this eliminates the 'buffer' in the system memory and allows each character to be 'flushed' to the screen after each time delay instead of waiting for the whole string to process and then self.type_stringing to the screen
            time.sleep(delay) #this creates a small time delay, in seconds, between each character being self.type_stringed to the screen (using the delay variable I've set for the function).
        if newline == False:
            pass
        else:
            print("\n") #with writing and flushing each character directly without a new line character built in, I'm adding it here with the option to remove it at certain points in the application

    def incomeCalc(self):
        self.incometotal = 0
        while True: #input for rent income
            try:
                rent = input("\nHow much do you charge monthly for RENT? (Don't worry about utilities for now). ")
                if '$' in rent:
                    self.rent = int(rent[1::])
                    self.incometotal += self.rent
                else:
                    self.rent = int(rent)
                    self.incometotal += self.rent
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        
        while True: #input for laundry income
            try:
                laundry = input("\nDo you charge for the use of LAUNDRY facilities? If so, how much per month? If this doesn't apply to your property, just input 0. ")
                if '$' in laundry:
                    self.laundry = int(laundry[1::])
                    self.incometotal += int(laundry[1::])
                else:
                    self.laundry = int(laundry)
                    self.incometotal += int(laundry)
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue

        while True: #input for storage income
            try:
                storage = input("\nDo you charge for the use of any STORAGE facilities? If so, how much? If this doesn't apply to your property, just input 0. ")
                if '$' in storage:
                    self.storage = int(storage[1::])
                    self.incometotal += int(storage[1::])
                else:
                    self.storage = int(storage)
                    self.incometotal += int(storage)
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        while True: #input for storage income
            try:
                misc = input("\nIf you have any miscellaneous monthly income that doesn't fit into the previous cetegories, enter that total here. Otherwise, you can just put 0. ")
                if '$' in misc:
                    self.misc = int(misc[1::])
                    self.incometotal += int(misc[1::])
                else:
                    self.misc = int(misc)
                    self.incometotal += int(misc)
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        print("\n|---------- INCOME ----------|")
        print(f'\n   Rental ---------- ${self.rent}')
        print(f'   Laundry ---------- ${self.laundry}')
        print(f'   Storage ---------- ${self.storage}')
        print(f'   Misc ---------- ${self.misc}')
        print('\n|----------------------------|')
        print(f'   Total ---------- ${self.incometotal}')
        correct = input('\nDoes this information look correct? (y/n)? ')
        if correct.lower == 'y':
            return
        elif correct.lower() == 'n':
            self.type_string("\nNo worries! Let's just do that again so we can get the right information...\n")
            self.incomeCalc()

    def expenseCalc(self):
        self.expenses_total = 0
        self.utilitiestotal = 0

        while True: #input for taxes expenses
            try:
                taxes = input("\nEnter the TAXES you pay on your property per month: ")
                if '$' in taxes:
                    self.taxes = int(taxes[1::])
                    self.expenses_total += int(taxes[1::])
                else:
                    self.taxes = int(taxes)
                    self.expenses_total += int(taxes)
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue

        while True: #input for insurance
            try:
                insurance = input("\nHow much do you pay per month for INSURANCE on  your property? ")
                if '$' in insurance:
                    self.insurance = int(insurance[1::])
                    self.expenses_total += self.insurance
                else:
                    self.insurance = int(insurance)
                    self.expenses_total += self.insurance
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        
        while True:
            whopays = input("\nDoes the tenant pay for their own utilities? (Enter 1 or 2): 1 - [Tenant covers cost fo all utilities] / 2 - [I cover the cost of all utilities]\n(Utilities includes electricity, water, sewer, garbage, and gas.) ")
            if int(whopays) == 2:
                while True: #input for electricity
                    try:
                        electricity = input("\nPlease enter the average monthly cost for ELECTRICITY: ")
                        if '$' in electricity:
                            self.electricity = int(electricity[1::])
                            self.utilitiestotal += int(electricity[1::])
                        else:
                            self.electricity = int(electricity)
                            self.utilitiestotal += int(electricity)
                        break
                    except:
                        self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                        continue
                while True: #input for water
                    try:
                        water = input("\nPlease enter the average monthly cost for WATER:  ")
                        if '$' in water:
                            self.water = int(water[1::])
                            self.utilitiestotal += int(water[1::])
                        else:
                            self.water = int(water)
                            self.utilitiestotal += int(water)
                        break
                    except:
                        self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                        continue

                while True: #input for sewer
                    try:
                        sewer = input("\nPlease enter the average monthly cost for SEWAGE: ")
                        if '$' in sewer:
                            self.sewer = int(sewer[1::])
                            self.utilitiestotal += int(sewer[1::])
                        else:
                            self.sewer = int(sewer)
                            self.utilitiestotal += int(sewer)
                        break
                    except:
                        self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                        continue
                while True: #input for garbage
                    try:
                        garbage = input("\nPlease enter the average monthly cost for GARBAGE: ")
                        if '$' in garbage:
                            self.garbage = int(garbage[1::])
                            self.utilitiestotal += int(garbage[1::])
                        else:
                            self.garbage = int(garbage)
                            self.utilitiestotal += int(garbage)
                        break
                    except:
                        self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                        continue
                while True: #input for gas
                    try:
                        gas = input("\nPlease enter the average monthly cost for GAS: ")
                        if '$' in gas:
                            self.gas = int(gas[1::])
                            self.utilitiestotal += int(gas[1::])
                        else:
                            self.gas = int(gas)
                            self.utilitiestotal += int(gas)
                        break
                    except:
                        self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                        continue
                self.expenses_total += self.utilitiestotal
                break
            #end of utilities
            elif int(whopays) == 1:
                self.type_string("\nExcellent! That makes our job a little easier. ^_^ Let's continue gathering any other property related expenses...")
                break

            
        while True: #input for HOA
            try:
                hoa = input("\nHow much do you pay per month in Home Owner's Association (HOA) fees? ")
                if '$' in hoa:
                    self.hoa = int(hoa[1::])
                    self.expenses_total += self.hoa
                else:
                    self.hoa = int(hoa)
                    self.expenses_total += self.hoa
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        
        while True: #input for lawn/snow
            try:
                lawnsnow = input("\nHow much do you pay per month for LAWN/SNOW management? ")
                if '$' in lawnsnow:
                    self.lawn_snow = int(lawnsnow[1::])
                    self.expenses_total += self.lawn_snow
                else:
                    self.lawn_snow = int(lawnsnow)
                    self.expenses_total += self.lawn_snow
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        
        while True: #input for vacancy
            try:
                vacancy = input("\nHow much do you set aside per month for VACANCY funds? ")
                if '$' in vacancy:
                    self.vacancy = int(vacancy[1::])
                    self.expenses_total += self.vacancy
                else:
                    self.vacancy = int(vacancy)
                    self.expenses_total += self.vacancy
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        
        while True: #input for repairs
            try:
                repairs = input("\nHow much do you set aside per month to cover unexpected REPAIRS? ")
                if '$' in repairs:
                    self.repairs = int(repairs[1::])
                    self.expenses_total += self.repairs
                else:
                    self.repairs = int(repairs)
                    self.expenses_total += self.repairs
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue

        while True: #input for capex, new roof, bigger repairs
            try:
                capex = input("\nHow much do you set aside per month for capitol expendatures (CapEx)? \nThese are bigger repairs, such as replacing the roof every 20 years, new appliances, or new carpet for example. ")
                if '$' in capex:
                    self.capex = int(capex[1::])
                    self.expenses_total += self.capex
                else:
                    self.capex = int(capex)
                    self.expenses_total += self.capex
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        
        while True: #input for property management
            try:
                prop = input("\nHow much do you pay per month regarding PROPERTY MANAGEMENT? ")
                if '$' in prop:
                    self.prop_mngmnt = int(prop[1::])
                    self.expenses_total += self.prop_mngmnt
                else:
                    self.prop_mngmnt = int(prop)
                    self.expenses_total += self.prop_mngmnt
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        
        while True: #input for mortgage
            try:
                mort = input("\nHow much is you MORTGAGE per month? ")
                if '$' in mort:
                    self.mortgage = int(mort[1::])
                    self.expenses_total += self.mortgage
                else:
                    self.mortgage = int(mort)
                    self.expenses_total += self.mortgage
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue

        print("\n|---------- Expenses ----------|")
        print(f'   Taxes ---------- ${self.taxes}')
        print(f'   Insurance ---------- ${self.insurance}')
        print(f'   Utilities ---------- ${self.utilitiestotal}')
        print(f'\tElectricity ------ ${self.electricity}')
        print(f'\tWater ---------- ${self.water}')
        print(f'\tSewer ---------- ${self.water}')
        print(f'\tGarbage ---------- ${self.water}')
        print(f'\tGas ---------- ${self.water}')
        print(f'   HOA ---------- ${self.hoa}') #HOA
        print(f'   Lawn/Snow ---------- ${self.lawn_snow}') #lawn/snow
        print(f'   Vacancy ---------- ${self.vacancy}') #vacancy
        print(f'   Repairs ---------- ${self.repairs}') #repairs
        print(f'   CapEx ---------- ${self.capex}') #CopEx
        print(f'   Property Management ------ ${self.prop_mngmnt}') #propertymanagement
        print(f'   Mortgage ---------- ${self.mortgage}') #mortgage
        print('|----------------------------|')
        print(f'   Total ---------- ${self.expenses_total}')
        correct = input('\nDoes this information look correct? (y/n)? ')
        if correct.lower == 'y':
            return
        elif correct.lower() == 'n':
            self.type_string("\nThat's ok! Let's just do that again so we can get the right information...")
            self.expenseCalc()

    def cashFlow(self):
        self.type_string("\nHere is your total monthly cash flow!")
        print("\n|---------- Cash Flow ----------|\n")
        print(f"\t      ${self.incometotal - self.expenses_total}")
        print("\n|---------- $$$$$$$$$ ----------|")
        self.cashflow = self.incometotal - self.expenses_total

    def cashROI(self):
        self.investent_total = 0
        #down payment
        while True:
            try:
                down = input("\nHow much did you put towards a DOWNPAYMENT for this property? ")
                if '$' in down:
                    self.downpayment = int(down[1::])
                    self.investent_total += self.downpayment
                else:
                    self.downpayment = int(down)
                    self.investent_total += self.downpayment
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        #closing costs
        while True: 
            try:
                closing = input("\nWhat was your CLOSING COST? ")
                if '$' in closing:
                    self.closingcost = int(closing[1::])
                    self.investent_total += self.closingcost
                else:
                    self.closingcost = int(closing)
                    self.investent_total += self.closingcost
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        #rehab budget
        while True: 
            try:
                rehab = input("\nWhat is your REHAB budget? (Money spent on repairs after purchase) ")
                if '$' in rehab:
                    self.rehabbudget = int(rehab[1::])
                    self.investent_total += self.rehabbudget
                else:
                    self.rehabbudget = int(rehab)
                    self.investent_total += self.rehabbudget
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        #misc other
        while True: #input for misc
            try:
                misc = input("\nInput any additional miscellaneous costs from investing/purchasing this property (Enter 0 if there are none): ")
                if '$' in misc:
                    self.miscother = int(misc[1::])
                    self.investent_total += self.miscother
                else:
                    self.miscother = int(misc)
                    self.investent_total += self.miscother
                break
            except:
                self.type_string("Hmm... Something deosn't look right. Try that again?\n")
                continue
        #total investment = (^added^)
        if self.cashflow == 0: #if you didn't check your cash flow first, calculate cashflow now
            self.cashflow = self.incometotal - self.expenses_total
        print("\n\t       Cash on Cash")
        print("|---------- Return on Investment ----------|")
        print(f'\n       Downpayment ---------- ${self.downpayment}')
        print(f'       Closing Cost ---------- ${self.closingcost}')
        print(f'       Rehab Cost ---------- ${self.rehabbudget}')
        print(f'       Misc ---------- ${self.miscother}')
        print('  <--------------------------------------->')
        print(f'\n       Annual Cash Flow ---------- ${self.cashflow * 12}')
        print(f'       Total Investment ---------- ${self.investent_total}\n')
        
        self.type_string(f'Annual Cash Flow / Total Investment = Return on Investment', newline=False)

        print('\n|---------------------------------------------|')
        print(f'     Return on Investment ---------- {round(((self.cashflow * 12) / self.investent_total) * 100, 2)}%')
        #cash flow * 12 = annual cash flow
        #annual cashflow/total investment = cash on cash Return On Investment

    def initiateCalc(self):
        self.type_string("\nWelcome to your personal return on investment calculator!\n")
        self.type_string("This calculation program will incorporate four different aspects of your fincances regarding your rental property...\n")
        self.type_string("Income\nExpenses\nCash Flow\n and...\nCash on Cash ROI (Return On Investment)\n")
        
        while True:
            start = input("Where would you like to begin? 1 - [income] or 2 - [expenses] ")
            if int(start) == 1:
                self.incomeCalc()
                break
            elif int(start) == 2:
                self.expenseCalc()
                break
        if self.incometotal > 0:
            self.type_string("\nAmazing! Now that we have your total monthly income calculated, let's move onto your expenses!\n")
            self.expenseCalc()
        elif self.expenses_total > 0:
            self.type_string("\nAmazing! Now that we have your monthly expenses calculated, let's move onto your total monthly income!")
            self.incomeCalc()
        
        self.type_string("\nFantastic! We have your income and expenses calculated!")
        while True:
            if self.incometotal > 0 and self.expenses_total > 0:
                self.type_string("\nWhat would you like to do next?")
                next = input("\n1 - [View Monthly Cash Flow]\n2 - [Calculate Cash on Cash Return on Investment]\n3 - [Recalculate Income]\n4 - [Recalculate Expenses]\n5 - [Quit] ")
                if int(next) == 1:
                    self.cashFlow()
                elif int(next) == 2:
                    self.cashROI()
                elif int(next) == 3:
                    self.incomeCalc()
                elif int(next) == 4:
                    self.expenseCalc()
                elif int(next) == 5:
                    break
        self.type_string("\nThank you for using this return on investment calculator! <3")
            
            


duplex = RentCalc()
duplex.initiateCalc()