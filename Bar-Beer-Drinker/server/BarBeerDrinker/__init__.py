from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import render_template
import json

from BarBeerDrinker import database

app = Flask(__name__)

@app.route('/')
def check():
    return app.send_static_file('index.html')

@app.route('/api/bar', methods=["GET"])
def getBars():
    return jsonify(database.getBars())

@app.route('/api/bar/<name>', methods=["GET"])
def getBar(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        bar = database.getBar(name)
        if bar is None:
            return make_response("No bar found with the given name.", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/beer', methods=["GET"])
def getBeers():
    return jsonify(database.getBeers())

@app.route('/api/beer/<name>', methods=["GET"])
def getBeer(name):
    try:
        if name is None:
            raise ValueError("Beer is not specified.")
        beer = database.getBeer(name)
        if beer is None:
            return make_response("No beer found with the given name.", 404)
        return jsonify(beer)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/drinker', methods=["GET"])
def getDrinkers():
    return jsonify(database.getDrinkers())

@app.route('/api/drinker/<name>', methods=["GET"])
def getDrinker(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        drinker = database.getDrinker(name)
        if drinker is None:
            return make_response("No drinker found with the given name.", 404)
        return jsonify(drinker)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/drinker/transactions/<name>', methods=['GET'])
def getTransactions(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        transactions = database.getTransactions(name)
        if transactions is None:
            return make_response("No transactions found for the given name.", 404)
        return jsonify(transactions)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/drinker/beercount/<name>', methods=['GET'])
def getBeerCount(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        beerCount = database.getBeerCount(name)
        if beerCount is None:
            return make_response("Could not find beer count for the given  drinker.", 404)
        return jsonify(beerCount)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/drinker/spending/<name>', methods=['GET'])
def getSpending(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        spending = database.getSpending(name)
        if spending is None:
            return make_response("Could not find spending distribution for the given  drinker.", 404)
        return jsonify(spending)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/bar/drinkers/<name>', methods=['GET'])
def getTopDrinkers(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        drinkers = database.getTopDrinkers(name)
        if drinkers is None:
            return make_response("Could not find top drinkers for the specified bar.", 404)
        return jsonify(drinkers)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/bar/beers/<name>', methods=['GET'])
def getTopBeers(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        beers = database.getTopBeers(name)
        if beers is None:
            return make_response("Could not find top selling beers for the specified bar.", 404)
        return jsonify(beers)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/bar/manuf/<name>', methods=['GET'])
def getTopManuf(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        manufs = database.getTopManuf(name)
        if manufs is None:
            return make_response("Could not find top selling manufacturers for the specified bar.", 404)
        return jsonify(manufs)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/beer/bars/<name>', methods=['GET'])
def getTopBarsForBeer(name):
    try:
        if name is None:
            raise ValueError("Beer is not specified.")
        bars = database.getTopBarsForBeer(name)
        if bars is None:
            return make_response("Could not find top selling bars for the specified beer", 404)
        return jsonify(bars)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/beer/drinkers/<name>', methods=['GET'])
def getTopDrinkersForBeer(name):
    try:
        if name is None:
            raise ValueError("Beer is not specified.")
        drinkers = database.getTopDrinkersForBeer(name)
        if drinkers is None:
            return make_response("Could not find top consumers for the specified beer.", 404)
        return jsonify(drinkers)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)
