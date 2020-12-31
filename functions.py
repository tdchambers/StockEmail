"""
------------------------------------------------------------------------
Functions for Stock Email
------------------------------------------------------------------------
Author: Travis Chambers
tdchambers
__updated__ = "2020"
------------------------------------------------------------------------
"""
import matplotlib
import requests
import numpy
from email.message import EmailMessage
import yfinance as yf
from matplotlib import pyplot as plt

def getStockData(stckname):
    ## get stocks 1 day history 
    stock = yf.Ticker(stckname)
    stockHist = stock.history(period="1d")
    data = stockHist['Close']
    ## return history 
    return data

def getStockGraph(stckname,timePeriod):
    # get stock history based on time period 
    stock = yf.Ticker(stckname)
    histRange = stock.history(period=timePeriod)
    
    ##plot history on graph 
    data = histRange['Close']
    data.plot()
    ## save as accessible file 
    plt.title("{} Price Graph".format(stckname))
    plt.savefig("filename.png")
    
    
    
    return 

def setupEmailSpecs(TO,FROM,Subject,body):
    msg = EmailMessage()
    msg['Subject'] = Subject
    msg['From'] = FROM
    msg['TO'] = TO
    msg.set_content(body)
    
        
    return msg
    
    
    

    

