# Constants
SHARES_PURCHASED = 2000
PURCHASE_PRICE_PER_SHARE = 40.00
SALE_PRICE_PER_SHARE = 42.75
COMMISSION_RATE = 0.03

# Calculate purchase details
purchase_amount = SHARES_PURCHASED * PURCHASE_PRICE_PER_SHARE
purchase_commission = purchase_amount * COMMISSION_RATE

# Calculate sale details
sale_amount = SHARES_PURCHASED * SALE_PRICE_PER_SHARE
sale_commission = sale_amount * COMMISSION_RATE

# Calculate net amount
net_amount = sale_amount - purchase_amount - purchase_commission - sale_commission

# Display all results
print(f"Amount paid for stock: ${purchase_amount:,.2f}")
print(f"Commission paid on purchase: ${purchase_commission:,.2f}")
print(f"Amount stock sold for: ${sale_amount:,.2f}")
print(f"Commission paid on sale: ${sale_commission:,.2f}")
print(f"Net amount: ${net_amount:,.2f}")

# Display profit/loss message
if net_amount > 0:
    print("Joe made a profit!")
else:
    print("Joe lost money!") 