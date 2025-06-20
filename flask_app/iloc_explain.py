# iloc_explain.py

import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, dash_table
from  loadCsv import load_data

def create_iloc_explain_app(server):
    app = Dash(__name__, server=server, url_base_pathname='/iloc/')

    # url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

    csvDf = pd.read_csv(load_data('FuelConsumptionCo2'))
    dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in csvDf.columns],
    data=csvDf.head().to_dict('records'),
    style_table={'overflowX': 'auto'},
    style_cell={'textAlign': 'center', 'padding': '5px'},
    style_header={'backgroundColor': 'lightblue', 'fontWeight': 'bold'}
    )

    # Create a sample DataFrame
    data = {
        "ENGINESIZE": [2.0, 2.4, 3.5],
        "CYLINDERS": [4, 4, 6],
        "FUELCONSUMPTION_COMB": [8.5, 9.6, 11.1],
        "CO2EMISSIONS": [196, 221, 255]
    }
    df = pd.DataFrame(data)

    # Create a table-like figure
    header = dict(values=["Index", "ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB", "CO2EMISSIONS"],
                  fill_color='paleturquoise',
                  align='center')
    cells = dict(values=[[0, 1, 2], df.ENGINESIZE, df.CYLINDERS, df.FUELCONSUMPTION_COMB, df.CO2EMISSIONS],
                 fill_color='lavender',
                 align='center')

    fig = go.Figure(data=[go.Table(header=header, cells=cells)])
    fig.update_layout(title="Understanding .iloc vs .loc")

    # Build the layout
    app.layout = html.Div([ # main div
        html.Div([ # child div_1
            html.H2("Understanding .iloc vs .loc"),
            dcc.Graph(figure=fig),
            html.Div([
                html.P(".iloc[1, 2] → 9.6 (2nd row, 3rd column)", style={"color": "blue"}),
                html.P(".loc[1, 'FUELCONSUMPTION_COMB'] → 9.6", style={"color": "green"}),
            ])
        ]),
        html.Div([ # child div_2
            html.H2("CSV Read Test"),
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in csvDf.columns],
                data=csvDf.head().to_dict('records'),
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'center', 'padding': '5px'},
                style_header={'backgroundColor': 'lightblue', 'fontWeight': 'bold'}
            )
        ])

    ])


    return app

