!#/usr/bin/env python
# This script should read the accounts.json file and print out the five
# wealthiest accounts at the bank, in order from highest to lowest balance.
# Output should take the following form:
# <last name>, <first name>: $<balance>
with open('acountsjson') as jsonfile:
    accounts = json.load(jsonfile)
    accounts_sorted = sorted(accounts, key=lambda account = account['balance'])
    for account in accounts_sorted[5:]:
        print('{}, {}: ${}'.format(account['name']['last'],
                                   account['name']['first'],
                                   account['balance']))
