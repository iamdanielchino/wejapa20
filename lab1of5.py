'''adding a noble gas entry to hydrogen and helium dictionary
    then checking its true or false value'''


elements = {'hydrogen': {'number': 1, 'weight': 1.00794,
                         'symbol': 'H', 'is_noble_gas': 'False' },
            'helium': {'number': 2, 'weight': 4.002602,
                       'symbol': 'He', 'is_noble_gas': 'True'}}

print(elements['hydrogen']['is_noble_gas'])

print(elements['helium']['is_noble_gas'])

