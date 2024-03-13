def bonAppetit(bill, k, b):
    total = sum(bill)
    anna_share = (total - bill[k]) // 2

    if anna_share == b:
        return "bonappetit"
    else:
        return b - anna_share


result = bonAppetit([3, 10, 2, 8], 1, 12)
print("Anna owes " + str(result))
