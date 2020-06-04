#from sales_calculation import *
#from calculations import *
#import calculations
import calculations as cal
#import sales_calculation as scal
tax_for_this_order =0
tax_for_this_order = cal.calc_tax(sales_total=101.37, tax_rate=.05)
print(tax_for_this_order)
print(cal.x)

#tax_for_this_order = scal.calc_tax(sales_total=101.37, tax_rate=.05)
#print(tax_for_this_order)
#print(scal.x)
#print(tax_for_this_order)