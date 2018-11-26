from sqlalchemy import create_engine
from sqlalchemy import sql

from BarBeerDrinker import config

engine = create_engine(config.database_uri)

def getBars():
    with engine.connect() as con:
        query = sql.text("SELECT name, license,address,state,phone From BarBeerDrinker.bars;")
        rs = con.execute(query)
        return [dict(row) for row in rs]

def getBar(name):
    with engine.connect() as con:
        query = sql.text("SELECT name,license,address,state,phone From BarBeerDrinker.bars WHERE name = :name;")
        rs = con.execute(query, name=name)
        result = rs.first()
        if result is None:
            return None
        else:
            return dict(result)

def getDrinkers():
    with engine.connect() as con:
        query = sql.text("SELECT DISTINCT name, address, state, phone FROM BarBeerDrinker.drinkers;")
        rs = con.execute(query)
        return [dict(row) for row in rs]

def getDrinker(name):
    with engine.connect() as con:
        query = sql.text("SELECT name, address, state, phone FROM BarBeerDrinker.drinkers WHERE name = :name;")
        rs = con.execute(query, name=name)
        result = rs.first()
        if result is None:
            return None
        else:
            return dict(result)

def getBeers():
    with engine.connect() as con:
        query = sql.text("SELECT DISTINCT name, type, manuf FROM BarBeerDrinker.items WHERE type='beer';")
        rs = con.execute(query)
        return [dict(row) for row in rs]

def getBeer(name):
    with engine.connect() as con:
        query = sql.text("SELECT name, type, manuf FROM BarBeerDrinker.items WHERE name = :name;")
        rs = con.execute(query, name=name)
        result = rs.first()
        if result is None:
            return None
        else:
            return dict(result)

def getTransactions(name):
    with engine.connect() as con:
        query = sql.text("""SELECT bills.bar, transactions.time, contains.item, items.type, contains.quantity, transactions.total, transactions.tip FROM ((((BarBeerDrinker.make INNER JOIN transactions ON make.tid = transactions.tid) INNER JOIN bills ON make.tid = bills.tid)
        INNER JOIN contains ON make.tid = contains.tid) INNER JOIN items ON contains.item = items.name) WHERE make.drinker = :name GROUP BY bills.bar ORDER BY transactions.time ASC;""")
        rs = con.execute(query, name=name)
        if rs is None:
            return None
        else:
            return [dict(row) for row in rs]

def getBeerCount(name):
    with engine.connect() as con:
        query = sql.text("""SELECT contains.item as beer, SUM(contains.quantity) as quantity
                            FROM ((BarBeerDrinker.make INNER JOIN contains ON make.tid = contains.tid)
                            INNER JOIN items ON contains.item = items.name)
                            WHERE items.type = 'beer' AND make.drinker = :name
                            GROUP BY items.name;""")
        rs = con.execute(query, name=name)
        if rs is None:
            return None
        else:
            return [dict(row) for row in rs]

def getSpending(name):
    with engine.connect() as con:
        query = sql.text("""SELECT bills.bar as bar, SUM(transactions.total) as amount
                            FROM(( BarBeerDrinker.bills INNER JOIN transactions ON bills.tid = transactions.tid) INNER JOIN make ON bills.tid = make.tid)
                            WHERE make.drinker = :name
                            GROUP BY bills.bar;""")
        rs = con.execute(query, name=name)
        if rs is None:
            return None
        else:
            return [dict(row) for row in rs]

def getTopDrinkers(name):
    with engine.connect() as con:
        query = sql.text("""SELECT  make.drinker as drinker, SUM(transactions.total) as amount
                            FROM ((BarBeerDrinker.make INNER JOIN transactions ON make.tid = transactions.tid) INNER JOIN bills ON make.tid = bills.tid)
                            WHERE bills.bar = :name
                            GROUP BY make.drinker
                            ORDER BY amount DESC
                            LIMIT 15;""")
        rs = con.execute(query, name=name)
        if rs is None:
            return None
        else:
            return [dict(row) for row in rs]

def getTopBeers(name):
    with engine.connect() as con:
        query = sql.text("""SELECT  contains.item as beer, SUM(contains.quantity) as quantity
                            FROM ((BarBeerDrinker.contains INNER JOIN bills ON contains.tid = bills.tid) INNER JOIN items ON contains.item = items.name)
                            WHERE items.type = 'beer' AND bills.bar = :name
                            GROUP BY contains.item;""")
        rs = con.execute(query, name=name)
        if rs is None:
            return None
        else:
            return [dict(row) for row in rs]

def getTopManuf(name):
    with engine.connect() as con:
        query = sql.text("""SELECT  items.manuf as manuf, SUM(contains.quantity) as quantity
                            FROM ((BarBeerDrinker.contains INNER JOIN bills ON contains.tid = bills.tid) INNER JOIN items ON contains.item = items.name)
                            WHERE items.type = 'beer' AND bills.bar = "Bates PLC"
                            GROUP BY manuf;""")
        rs = con.execute(query, name=name)
        if rs is None:
            return None
        else:
            return [dict(row) for row in rs]

def getTopBarsForBeer(name):
    with engine.connect() as con:
        query = sql.text("""SELECT bills.bar as bar, SUM(contains.quantity) as quantity
                            FROM (BarBeerDrinker.bills INNER JOIN contains ON bills.tid = contains.tid)
                            WHERE contains.item = :name
                            GROUP BY bar
                            ORDER BY quantity DESC
                            LIMIT 15;""")
        rs = con.execute(query, name=name)
        if rs is None:
            return None
        else:
            return [dict(row) for row in rs]

def getTopDrinkersForBeer(name):
    with engine.connect() as con:
        query = sql.text("""SELECT make.drinker as drinker, SUM(contains.quantity) as quantity
                            FROM (BarBeerDrinker.make INNER JOIN contains ON make.tid = contains.tid)
                            WHERE contains.item = 'Bud light'
                            GROUP BY drinker
                            ORDER BY quantity DESC
                            LIMIT 15;""")
        rs = con.execute(query, name=name)
        if rs is None:
            return None
        else:
            return [dict(row) for row in rs]
