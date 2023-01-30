from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle

app=Flask(__name__)
