import pandas as pd
import dash
from dash import dcc, html, dash_table
import os

robotoFont = [
    "https://fonts.googleapis.com/css2?family=Roboto&display=swap"
]

def readCsv(server):
    dash_app = dash.Dash(__name__, server=server, url_base_pathname='/gen/', external_stylesheets=robotoFont)
    
    URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"   
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "..", "assets", "data", "dataset.csv")

    df = pd.read_csv(csv_path)
    
    # Define layout with DataTable
    tbl = html.Div([
        html.H1("Laptop Pricing Dataset", style={'font-family': 'Roboto'}),
        
        dash_table.DataTable(
            id='data-table',
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict('records'),
            page_size=10,  # Number of rows per page
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left', 'font-family': 'Roboto'},
        )
    ])

    dash_app.layout = html.Div(
        [
            tbl,
            html.Br(),

            html.H2("Column Names", style={'font-family': 'Roboto'}),
            html.Div([
                html.P(col) for col in df.columns
            ])
        ]
    )

    
    return dash_app
