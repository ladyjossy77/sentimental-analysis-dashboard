
import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages= True)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

adsData = pd.read_csv(r'C:\\Users\\HP\\Downloads\\mybooks\\project\\ads-proj\\ad-sales-ml-proj\\data\\marketingData.csv',  index_col= 0)
revData = pd.read_csv(r'C:\\Users\\HP\\Downloads\\mybooks\\project\\ads-proj\\ad-sales-ml-proj\\data\\revenueData.csv',  index_col= 0)
salesData = pd.read_csv(r'C:\\Users\\HP\\Downloads\\mybooks\\project\\ads-proj\\ad-sales-ml-proj\\data\\WebTransactionsCSV.csv',  sep=';', header= 0 )
app.layout = html.Div([
    dbc.Row([
        dbc.Col( 
            html.Div([
            dbc.Nav("LOGO"),
            html.Br(),
            html.Div(
                     [
                         "ANALYTICS",
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")], align = 'left'),
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")]),
                     ], className =' nav-subtext'),  
            html.Hr(),
            html.Div(
                      [
                          "MENU",
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")]),
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")]),
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")]),
                     ], className =' nav-subtext'), 
            html.Hr(),
            dbc.Nav(["UTILITIES"], className ='nav-subtext')
            ], className = 'nav-card '),style={"height":"100%"}, 
            width = 2
            ),
        dbc.Col(
                dbc.Row([
        dbc.Row([
            dbc.Col(html.Div(
                children=[html.Div("Hi Marketing Manager", style={'fontWeight': 'bold'}), html.Div("Welcome back!")]), width = 3),
            dbc.Col(
                html.Div([
                    html.I(className = "bi bi-search"),
                    html.I(className ="bi bi-bell-fill"),
                    html.I(className ="bi bi-person-circle"),
                    ],className = 'icon-bar'), width = 3), 
            ], justify = 'between'),
        html.Br(),
        dbc.Row(style = {'height':'20px'}),
        dbc.Row([
            dbc.Col(html.Div([
                dcc.DatePickerRange( id = "dash-date-filter",  
                                    month_format='MMM Do, YY',
                                    end_date_placeholder_text='MMM Do, YY',
                                    start_date= "03 01 19",
                                    calendar_orientation = 'horizontal',
                                    day_size= 25,
                                    style={'fontSize': '10px', }
                                    ), 
                html.Div(id = "dash-date-filter-range") ], 
                             className = 'dashboard-date-filter'
                ),width = 5 ),
            dbc.Col(
                dbc.Button(
                    "DOWNLOAD",
                    className = 'download-button'
                ), width = 2
            )
            ], justify = 'between', className = 'filter-bar'),
        html.Br(),
        dbc.Row(style = {'height':'20px'}),
        html.Div([
            html.Div([
                html.Div("Analysis Overview"),
                html.Br(),
                dbc.Row([
                    dbc.Col(dbc.Card(
                        children = [html.Div("title"), html.Div("value", className = 'value'), html.Div("description")],className = 'summary-cards',),
                            width = 3,),
                    dbc.Col(dbc.Card(
                        children = [html.Div("title"), html.Div("value", className = 'value'), html.Div("description")], className = 'summary-cards',),
                            width = 3),
                    dbc.Col(dbc.Card(
                        children = [html.Div("title"), html.Div("value", className = 'value'), html.Div("description")], className = 'summary-cards',),
                            width = 3),
                    dbc.Col(dbc.Card(
                        children = [html.Div("title"), html.Div("value", className = 'value'), html.Div("description")], className = 'summary-cards',),
                            width = 3),
                ], justify="evenly")
            ], className = 'summary-section'),
            dbc.Row(style = {'height':'20px'}),
            html.Div([
                html.Div("graph title"), 
                html.Br(),
                dcc.Graph("graph")
            ], className = 'summary-section')
            ]),
                ]),
                className = 'dashboard'
                , width=10)
    ]),
    dash.page_container
])

app.callback()

if __name__ == '__main__':
    app.run_server(debug=True)