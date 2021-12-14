import pandas as pd
import plotly.figure_factory as px
import csv

df=pd.read_csv('data.csv')
fig=px.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()
