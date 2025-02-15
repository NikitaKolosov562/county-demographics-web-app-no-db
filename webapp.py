from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    states = get_state_options()
    #print(states)
    return render_template('home.html', state_options=states)
@app.route('/pagetwo')
def pagetwo():
    states = get_state_options()
    return render_template('page2.html', state_options=states)
@app.route('/showFact')
def render_fact():
    states = get_state_options()
    state = request.args.get('state')
    fact=highest_pop2014(state)
    factC=highest_popc2014(state)    
    return render_template('home.html', state_options=states, funFact=fact, funFactC=factC)
@app.route('/showFact2')
def render_fact2():
    states = get_state_options()
    state = request.args.get('state')
    factC=owner(state)
    factCC=ownerc(state)    
    return render_template('page2.html', state_options=states, funFactC=factC, funFactCC=factCC)
        
def get_state_options():
    """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    states=[]
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
    options=""
    for s in states:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

def county_most_under_18(state):
    """Return the name of a county in the given state with the highest percent of under 18 year olds."""
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest=0
    county = ""
    for c in counties:
        if c["State"] == state:
            if c["Age"]["Percent Under 18 Years"] > highest:
                highest = c["Age"]["Percent Under 18 Years"]
                county = c["County"]
    return county
    
def percent_65_and_older(state):
    """Return the name of a county in the given state with the highest percent of over 18 year olds."""
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest=0
    county = ""
    for c in counties:
        if c["State"] == state:
            if c["Age"]["Percent 65 and Older"] > highest:
                highest = c["Age"]["Percent 65 and Older"]
                county = c["County"]
    return county
def highest_pop2014(state):
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest=0
    for c in counties:
        if c["State"] == state:
            if c["Population"]["2014 Population"] > highest:
                highest=c["Population"]["2014 Population"]
                county = c["County"]
    answerOne=highest
    return answerOne             
def highest_popc2014(state):
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest=0
    for c in counties:
        if c["State"] == state:
            if c["Population"]["2014 Population"] > highest:
                highest=c["Population"]["2014 Population"]
                county = c["County"]
    answerTwo=county
    return answerTwo  
def owner(state):
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest=0
    for c in counties:
        if c["State"] == state:
            if c["Housing"]["Homeownership Rate"] > highest:
                highest=c["Housing"]["Homeownership Rate"]
                county = c["County"]
    answerOne1=highest
    return answerOne1
def ownerc(state):
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest=0
    for c in counties:
        if c["State"] == state:
            if c["Housing"]["Homeownership Rate"] > highest:
                highest=c["Housing"]["Homeownership Rate"]
                county = c["County"]
    answerOne2=county
    return answerOne2
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production
