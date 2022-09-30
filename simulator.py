import streamlit as st

import pandas as pd
import numpy as np
import os
from os.path import exists
import time
import joblib
from io import StringIO
import datetime
import math
import calendar
import random
from datetime import timedelta
from datetime import date






import seaborn as sns
import scipy.stats as stats


import warnings
warnings.filterwarnings('ignore')

st.set_page_config(layout='wide')

def unlf(k, sigma):
    result = stats.norm(0, 1).pdf(k) - k * (1-stats.norm(0, 1).cdf(k))
    return sigma * result

mus = st.sidebar.slider('Demand of the Product',0,4000,10)

sigmas =  st.sidebar.slider('sigma',0,100,30)

cst = st.sidebar.slider('Cost of item in ($)',1,100,1)

hld_cst = st.sidebar.slider('Holding Cost of item in (%)',0.0,1.0,0.1)
lead = st.sidebar.slider('Lead Time in days',1,30,3)

csl_prt = st.sidebar.slider('Cycle Service Level in (%)',0.0,1.0,0.5)




# Demand = N(100, 15)
mu = mus
sigma = sigmas
variance = sigma **2
# Days per year
T_total = 365
# Total Demand (units/year)
D = mu
# Demand per day (unit/day)
D_day = D/T_total
# Standard Deviation per day
sigma_Day = sigma /math.sqrt(T_total)
# Cost of item ($/unit)
c = cst
# Holding Cost (%/year)
h = hld_cst
c_e = c * h

# Lead Time (days)
LD = lead
# Order Quantity Q*
Q = D_day * 15
# Weeks per year
T_total = 365
# Cost per Stock Out
B1 = 50000

# 1. We fix CSL = 95%
CSL = csl_prt

# Average during lead time period
mu_ld = math.floor(mu * LD /(T_total))
st.write("Average demand during lead time: {:,} units".format(mu_ld))
# Standard deviation 
sigma_ld = sigma * math.sqrt(LD /(T_total))
st.write("Standard deviation during lead time: {:,} units".format(math.floor(sigma_ld)))
# Level of Service to fix k
k = round(stats.norm(0, 1).ppf(CSL),2)
st.write("k = {:,}".format(round(k, 2)))
# Reorder Point
s = mu_ld + k * sigma_ld
st.write("Reoder point with CSL: {:,} units".format(math.floor(s)))

