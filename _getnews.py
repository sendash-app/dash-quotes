import requests, json
from urllib.parse import urlencode

import pandas as pd
import dash_html_components as html
import datetime

# JHO's login- Get yours at NewsAPI.org
api_key = '94728df306c14086ad303cc26ddf3eab'

base_url = 'https://newsapi.org/v2/'
params_ini = {
    'apiKey': api_key
}

def GetJson(url, params):
    data = requests.get(url, params = params)
    if data.status_code == 200:
        return json.loads(data.text)
    else:
        return None

def get_news_sources(verbose = False):
    url = base_url + 'sources?'
    params = params_ini
    params['language'] = 'en'
    jdata = GetJson(url, params)
    l_source = []
    for i in jdata['sources']:
        l_source.append(i['id'])

    if verbose:
        print( '--- Found the following news source:')
        print( ",".join( l_source ))

    return l_source

def get_headline( optdict = None , verbose = False):
    url = base_url + 'top-headlines?'
    params = params_ini
    if optdict != None:
        for key in optdict:
            params[key] = optdict[key]

    if verbose:
        print(f'Searching for headline with these params \n {params}\n {url + urlencode(params)}')

    return GetJson(url, params)

def generate_stylish_news_table(dataframe, max_rows=10):
    theme_colors = {
        'grey_dark': '#232b2b',
        'grey_light': '#777777',
        'white': '#ffffff',
        'blue_light': '#a9ebff',
        'blue':   '#3399ff',
        'status_color': "#45df7e"
    }
    return html.Div(
        [
            html.Div(
                # Table
                html.Table(
                    # Header
                    [html.Tr([html.Th('News Headlines')],
                             style = {'color': theme_colors['blue'],
                             })]
                    #[html.Tr([html.Th(col) for col in dataframe.columns])]
                    +
                    # Body
                    [
                        html.Tr(
                            [
                                html.Td(
                                    html.A(
                                        dataframe.iloc[i]["title"],
                                        href=dataframe.iloc[i]["url"],
                                        target="_blank",
                                    )
                                )
                            ], style = {'background-color': theme_colors['grey_light'],
                                }
                        )
                        for i in range(min(len(dataframe), max_rows))
                    ]
                ),
                # Table Style
                #style={"height": "150px", "overflowY": "scroll"},
                style = { 'height': '100%', 'overflowY': 'scroll',
                        'background-color': theme_colors['grey_dark'],
                        'width': '50%',
                        'padding' : '4'
                        }
            ),
            # Status Update
            html.P(
                "Last update : " + datetime.datetime.now().strftime("%H:%M:%S"),
                style={"fontSize": "11", "marginTop": "4", "color": theme_colors['status_color']},
            ),
        ],
        style={"height": "100%"},
    )

# def generate_news_table(dataframe, max_rows=10):
#     return html.Div(
#         [
#             html.Div(
#                 # Table
#                 html.Table(
#                     # Header
#                     [html.Tr([html.Th('News Headlines')]
#                              )]
#                     #[html.Tr([html.Th(col) for col in dataframe.columns])]
#                     +
#                     # Body
#                     [
#                         html.Tr(
#                             [
#                                 # html.Td([
#                                 #     dataframe.iloc[i]["title"],
#                                 #     "\t",
#                                 #     html.A(
#                                 #         html.I(className="fa fa-external-link"),
#                                 #         href=dataframe.iloc[i]["url"],
#                                 #         target="_blank",
#                                 #     )
#                                 html.Td(
#                                     html.A(
#                                         html.I(className="fa fa-external-link"),
#                                                 href=dataframe.iloc[i]["url"],
#                                                 target="_blank",
#                                             )
#                                         )
#                                 if col == 'url' else html.Td(
#                                     dataframe.iloc[i][col]
#                                 )
#                                 for col in dataframe.columns
#                                     ]
#                                 )
#                                 for i in range(min(len(dataframe), max_rows))
#                             ],
#                             className = 'rwd-table'
#                         )
#                 ),
#             # Status Update
#             html.P(
#                 "Last update : " + datetime.datetime.now().strftime("%H:%M:%S"),
#                 style={"fontSize": "11", "marginTop": "4", "color": '#45df7e'},
#             ),
#         ],
#         #style={"height": "100%"},
#     )

def generate_table( dataframe, max_rows=10, id = ''):
    return html.Table( id = id, children = [

        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]

        ]
    )

# retrieve and displays news
def update_news():
    search_term = 'Trump'
    # Getting English News Source
    l_news_sources = get_news_sources()
    news_params_dict = {
        # you can't mix category with source
        # and you can't have language in headlines
        'q' : search_term,
        # 'language' : 'en',
        # 'category' : 'business',
        'sources' : ','.join(l_news_sources)
    }
    json_data = get_headline(news_params_dict, verbose = False)
    if json_data is None:
        return "No news available for your search term: " + search_term
    else:
        json_data = json_data["articles"]
        df = pd.DataFrame(json_data)
        df = pd.DataFrame(df[["title","url",'source', 'publishedAt']])
        return generate_table(df, max_rows = 20)
