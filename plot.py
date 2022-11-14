# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:48:33 2022

@author: amuxf
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

local=r"C:\Users\amuxf\Documents\EIT\Eurecom\clouds\assign2\01\output_stats_history.csv"
vmscaleset= r"C:\Users\amuxf\Documents\EIT\Eurecom\clouds\assign2\02\output_stats_history.csv"
vmscalesetstop= r"C:\Users\amuxf\Documents\EIT\Eurecom\clouds\assign2\02\output2_stats_history.csv"
webapp= r"C:\Users\amuxf\Documents\EIT\Eurecom\clouds\assign2\03-2\output_stats_history.csv"
remote= r"C:\Users\amuxf\Documents\EIT\Eurecom\clouds\assign2\04\output_stats_history.csv"


plt.rcParams["figure.autolayout"] = True
df_local = pd.read_csv(local)[["Requests/s"]]
df_vmss = pd.read_csv(vmscaleset)[["Requests/s"]]
df_webapp = pd.read_csv(webapp)[["Requests/s"]]
df_remote = pd.read_csv(remote)[["Requests/s"]]


t = np.linspace(0, 175, 175)
plt.xticks(range(1, 175))
plt.plot(df_local, 'r', label="local") # plotting local microservice
plt.plot(df_vmss, 'g', label="vmss") # plotting vmss
plt.plot(df_webapp, 'black', label="webapp") #autoscale webapp
plt.plot(df_remote, 'b', label="azure function") #autoscale azure function

plt.legend(loc="upper left")

plt.ylabel("Requests/s")
plt.xlabel("Time")

plt.show()
