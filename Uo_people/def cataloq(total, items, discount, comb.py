def cataloq(total, items, discount, combo, item_price):
    if items == 1:
        discount = 0
        combo = items * discount
        total = item_price + combo

    elif items == 2:
        discount = 0.1
        combo = items * discount
        total = item_price + combo

    elif items == 3:
        discount = 0.25
        combo = items * discount
        total = item_price + combo
    return total
