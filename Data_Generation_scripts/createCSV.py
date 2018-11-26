import csv
import names
from faker import Faker
import uuid
import random
from random import randint
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

barNameEnd = [' bar', ' pub', ' club', '']

beers = {
'bud light': 7, 'michelob ultra': 8, 'natural light': 8, 'budweiser': 7,
'stella artois': 7, 'goose island':8, 'land shark lager':7,
'natural ice':8, 'presidente':7, 'miller lite':8, 'coors light':8,
'keystone light':7, 'blue moon':7, 'miller high life':8
}

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
food = ['hamburger', 'fries', 'hot dog', 'nachos', 'cheeseburger', 'quesadillas', 'pizza', 'chips']


def phn(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def createBars():
    df_bars = pd.DataFrame({'bar name':[], 'license':[], 'address':[], 'state':[], 'phone':[]})
    fake = Faker()
    for _ in range(5000):
        name =  fake.company() + barNameEnd[randint(0,3)]
        state = fake.state()
        license = us_state_abbrev[state] + str(randint(1000,9999))
        address = fake.street_address()
        phone = phn(10)
        df_bars = df_bars.append({'bar name':name, 'license':license, 'address':address, 'state':state, 'phone':phone}, ignore_index=True)
    df_bars.to_csv('bars.csv')

def createHours():
    df_hours = pd.DataFrame({'day':[],'open':[], 'close':[]})
    for _ in range(7):
        df_hours = df_hours.append({'day':days[_],'open':'600', 'close':'2400'}, ignore_index=True)
    df_hours.to_csv('hours.csv')

def createOpen():
    df_hours = pd.read_csv('hours.csv',sep='\s*,\s*',
                           header=0, encoding='ascii', engine='python')
    df_bars = pd.read_csv('bars.csv')
    df_open = pd.DataFrame({'bar name': [], 'day': [], 'open': [], 'close': []})
    for bar_name in df_bars['bar name']:
        for day in df_hours['day']:
            df_open = df_open.append({'bar name': bar_name, 'day': day, 'open': 600,'close':2400 }, ignore_index=True)

    df_open.to_csv('open.csv')

def createItems():

    df_open = pd.DataFrame({'item name':[], 'type':[],'manuf':[]})
    df_open = df_open.append({'item name':'bud light', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'michelob ultra', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'natural light', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'budweiser', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'stella artois', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'goose island', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'land shark lager', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'natural ice', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'presidente', 'type':'beer','manuf': 'anheuser-busch'}, ignore_index=True)
    df_open = df_open.append({'item name':'miller lite', 'type':'beer','manuf': 'millercoors'}, ignore_index=True)
    df_open = df_open.append({'item name':'coors light', 'type':'beer','manuf': 'millercoors'}, ignore_index=True)
    df_open = df_open.append({'item name':'keystone light', 'type':'beer','manuf': 'millercoors'}, ignore_index=True)
    df_open = df_open.append({'item name':'blue moon', 'type':'beer','manuf': 'millercoors'}, ignore_index=True)
    df_open = df_open.append({'item name':'miller high life', 'type':'beer','manuf': 'millercoors'}, ignore_index=True)
    df_open = df_open.append({'item name':'chicken fingers', 'type':'food','manuf': 'chef'}, ignore_index=True)
    df_open = df_open.append({'item name':'hamburger', 'type':'food','manuf': 'chef'}, ignore_index=True)
    df_open = df_open.append({'item name':'fries', 'type':'food','manuf': 'chef'}, ignore_index=True)
    df_open = df_open.append({'item name':'hot dog', 'type':'food','manuf': 'chef'}, ignore_index=True)
    df_open = df_open.append({'item name':'nachos', 'type':'food','manuf': 'chef'}, ignore_index=True)
    df_open = df_open.append({'item name':'cheeseburger', 'type':'food','manuf': 'chef'}, ignore_index=True)
    df_open = df_open.append({'item name':'quesadillas', 'type':'food','manuf': 'chef'}, ignore_index=True)
    df_open = df_open.append({'item name':'pizza', 'type':'food','manuf': 'chef'}, ignore_index=True)
    df_open = df_open.append({'item name':'chips', 'type':'food','manuf': 'chef'}, ignore_index=True)

    df_open.to_csv('items.csv')

def createSells():
    df_sells = pd.DataFrame({'bar name':[], 'item name': [], 'price':[]})
    df_bars = pd.read_csv('bars.csv')
    df_items = pd.read_csv('items.csv')
    for bar in df_bars['bar name']:
        for _ in range(2):
            beer_name = random.choice(list(beers))
            df_sells = df_sells.append({'bar name':bar, 'item name' : beer_name, 'price':beers[beer_name]}, ignore_index=True)
        df_sells = df_sells.append({'bar name':bar, 'item name' : food[randint(0,7)], 'price':randint(0,15)}, ignore_index=True)

    df_sells.to_csv('sells.csv')


def createDrinkers():
    fake = Faker()
    df_drinkers = pd.DataFrame({'drinker name':[], 'address':[], 'state':[], 'phone':[]})
    for _ in range(500):
        name = fake.name()
        state = fake.state()
        address = fake.street_address()
        phone = phn(10)
        df_drinkers = df_drinkers.append({'drinker name':name,'address':address, 'state':state, 'phone':phone},ignore_index=True)

    df_drinkers.to_csv('drinkers.csv')

def createLikes():
    df_likes = pd.DataFrame({'drinker name':[], 'item name':[]})
    df_drinkers = pd.read_csv('drinkers.csv')
    df_items = pd.read_csv('items.csv')

    for drinker in df_drinkers['drinker name']:
        for _ in range(2):
            item = random.choice(list(beers))
            df_likes = df_likes.append({'drinker name':drinker, 'item name':item},ignore_index=True)
        df_likes = df_likes.append({'drinker name':drinker, 'item name':food[randint(0,7)]},ignore_index=True)

    df_likes.to_csv('likes.csv')

def createFrequents():
    df_frequents = pd.DataFrame({'drinker_name':[],'bar_name':[]})
    df_drinkers = pd.read_csv('drinkers.csv')
    df_bars = pd.read_csv('bars.csv')

    for drinker_index, drinker in df_drinkers.iterrows():
    	count = 0
    	for bar_index, bar in df_bars.iterrows():
        	if str(bar[4]) == str(drinker[3]):
        		count = count + 1
        		if count < 4:
        			dname = drinker[1]
        			bname = bar[1]
        			df_frequents.append({'drinker_name':dname, 'bar_name':bname}, df_frequents)
        		else:
        			break



    df_frequents.to_csv('frequents.csv', encoding='utf-8')

def createTransactions():
    df_transactions = pd.DataFrame({'transaction id':[], 'total':[], 'tip':[], 'time':[]})
    df_contains = pd.DataFrame({'transaction id':[], 'quantity':[], 'item name':[]})
    df_make = pd.DataFrame({'drinker name':[], 'transaction id':[]})
    df_bill = pd.DataFrame({'bar name':[], 'transaction id':[]})

    df_drinkers = pd.read_csv('drinkers.csv')
    df_bars = pd.read_csv('bars.csv')
    df_items = pd.read_csv('items.csv')
    df_hours = pd.read_csv('hours.csv',sep='\s*,\s*',
                           header=0, encoding='ascii', engine='python')
    df_frequents = pd.read_csv('frequents.csv')
    df_likes = pd.read_csv('likes.csv')
    df_sells = pd.read_csv('sells.csv')

    for _ in range(20000):
        tid = uuid.uuid4()
        freq = df_frequents.sample(1) #get a row
        drinker_name = freq['drinker name']
        bar_name = freq['bar name']
        sell = df_sells.loc[:, 'bar name']
        count = 0
        for bar in bar_name:
            for row in sell:
                count = count + 1
                if row == bar:
                    bar_name = bar
                    break
        item_name = df_sells.ix[count,'item name']
        price = df_sells.ix[count,'price']
        quantity = randint(0,10)
        tax = (price * quantity) * 0.07
        total = (price * quantity) + tax
        tip = randint(0,100)
        time = randint(600,2400)
        df_transactions = df_transactions.append({'transaction id':tid, 'total':total, 'tip':tip, 'time':time},ignore_index=True)
        df_contains = df_contains.append({'transaction id':tid, 'quantity':quantity, 'item name':item_name},ignore_index=True)
        df_make = df_make.append({'drinker name':drinker_name.to_string(index=False), 'transaction id':tid},ignore_index=True)
        df_bill = df_bill.append({'bar name':bar_name, 'transaction id':tid},ignore_index=True)



    df_transactions.to_csv('transactions.csv')
    df_contains.to_csv('contains.csv')
    df_make.to_csv('make.csv')
    df_bill.to_csv('bills.csv')


def main():
    # createBars()
    # createDrinkers()
    # createItems()
    # createHours()
    # createOpen()
    # createSells()
    # createLikes()
    createFrequents()
    # createTransactions()

if __name__ == '__main__':
    main()
