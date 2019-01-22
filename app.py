# -*- coding: utf-8 -*-
# import json
# import base64
# import datetime
# import requests
#
import numpy as np
import pandas as pd
from iexfinance.stocks import Stock
# import flask
import dash
# from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
# import plotly.graph_objs as go
# from plotly import tools
#
# from _getnews import update_news
# from _gettopbar import get_top_bar

# server = flask.Flask(__name__)
# app = dash.Dash(__name__, server=server)
#
#
# external_css = [
#     "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
#     "https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",
#     "https://cdn.rawgit.com/amadoukane96/8f29daabc5cacb0b7e77707fc1956373/raw/854b1dc5d8b25cd2c36002e1e4f598f5f4ebeee3/test.css",
#     "https://use.fontawesome.com/releases/v5.2.0/css/all.css"
# ]
#
# for css in external_css:
#     app.css.append_css({"external_url": css})
#
#
#
#
# @app.callback(Output("live_clock", "children"), [Input("interval", "n_intervals")])
# def update_time(n):
#     return datetime.datetime.now().strftime("%H:%M:%S")
#
# @app.callback(Output("news", "children"), [Input("i_news", "n_intervals")])
# def update_news_div(n):
#     return update_news()

l_symbol = ['FB','AMZN','NFLX','GOOG']

data = np.array([['GOOG','Google Inc', '123', '$10'],
                ['AAPL', 'Apple Computer', '234', '$5']
                ])
df = pd.DataFrame( data= data, columns = ['Symbol', 'Company', 'Price', 'Change'])

def generate_table( dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

external_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__ , external_stylestreets = external_css)
colors = {
    'background' : '#232b2b',
    'text' :    '#a9ebff'
}

app.layout = html.Div(   children =[
    # html.H1(
    #     children = 'Hello World',
    #     style = {
    #         'textAlign': 'center',
    #         'color': colors['text']
    #     }
    # ),
    # html.Div(
    #     children = 'Dash: A web application framework for Python',
    #     style = {
    #         'textAlign': 'center',
    #         'color': colors['text']
    #     }
    #
    # ),
    generate_table(df)
])

for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == "__main__":
    app.run_server(debug=True, threaded=True)
