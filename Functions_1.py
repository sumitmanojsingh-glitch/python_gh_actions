def Calculate_Tax(price,VAT):
    return price*(100+VAT)/100

orders=[100,200,300]

for price in orders:
    print(f"{Calculate_Tax(price,10)}")