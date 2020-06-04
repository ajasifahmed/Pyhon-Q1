x =10
def calc_tax(sales_total, tax_rate):
    tax = sales_total * tax_rate
    return tax

def calc_gst(sales_total, tax, gst_rate):
    net = sales_total + tax
    gst = net * gst_rate
    return gst
