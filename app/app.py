from flask import Flask, render_template, request, session, redirect, url_for, flash
from random import *
import json, urllib2, sys, os

my_app = Flask(__name__)
my_app.secret_key = os.urandom(64)

@my_app.route('/')
def root():
    return render_template("index.html")
