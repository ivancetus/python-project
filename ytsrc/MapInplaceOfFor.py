# https://www.youtube.com/shorts/t1C7Mx14ixg


citizens = [('Steve', 10), ('Mark', 8), ('Chris', 19)]


def tax(citizen):
    name = citizen[0]
    taxed_balance = citizen[1]*0.93
    return (name, taxed_balance)


# taxed_citizens = []
# for citizen in citizens:
#     taxed_citizen = tax(citizen)
#     taxed_citizens.append(taxed_citizen)

taxed_citizens = list(map(tax, citizens))

print(taxed_citizens)
