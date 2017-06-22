import math
"""
supply = 300000
ratio = .20
reserve = 60000
cap = reserve / ratio
"""

#   INPUT ETH
#   OUTPUT BANCOR


def buy_in(supply, reserve, e):
    in_bancor = supply * (math.pow(1.0 + (e / reserve), 20 / 100.0) - 1)
    supply += in_bancor
    reserve += e
    print('Issued  (BNC):\t{}'.format(in_bancor))
    print('Supply  (BNC):\t{}'.format(supply))
    print('Reserve (ETH):\t{}'.format(reserve))
    return supply, reserve, in_bancor

#   INPUT BANCOR
#   OUTPUT ETH


def cash_out(supply, reserve, t):
    out_eth = reserve * (math.pow(1.0 + (t / supply), 100.0 / 20) - 1)
    issued = supply * ((1 + (out_eth / reserve))**.20 - 1)
    reserve -= out_eth
    supply -= issued
    print('Issued  (ETH):\t{}'.format(out_eth))
    print('Supply  (BNC):\t{}'.format(supply))
    print('Reserve (ETH):\t{}'.format(reserve))
    return supply, reserve, out_eth


def robotrade(supply, reserve, e):
    i = 0
    while reserve > 0:
        i += 1
        print('========================================')
        print('Trading Round:\t{}'.format(i))
        print('\n')
        supply, reserve, t = buy_in(supply, reserve, e)
        print('\n')
        supply, reserve, e = cash_out(supply, reserve, t)


robotrade(300000, 60000, 1000)
