import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

robotoFont = [
    "https://fonts.googleapis.com/css2?family=Roboto&display=swap"
]

def create_dash_app(server):
    dash_app = dash.Dash(__name__, server=server, url_base_pathname='/dash/', external_stylesheets=robotoFont)

    # 📊 Load dataset
    airline_data = pd.read_csv(
        'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
        encoding="ISO-8859-1",
        dtype={
            'Div1Airport': str, 'Div1TailNum': str,
            'Div2Airport': str, 'Div2TailNum': str
        })

    # 🎨 Layout with Roboto font and chart
    dash_app.layout = html.Div(
        style={'fontFamily': 'Roboto', 'padding': '20px'},
        children=[ 
            html.H1('Airline Performance Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
            html.Div([
                "Input Year: ",
                dcc.Input(id='input-year', value='2010', type='number', style={'max-width':'fit-content','padding':'5px', 'font-size': 20}),
            ], style={'font-size': 20}),
            html.Br(),
            html.Br(),
            html.Div(dcc.Graph(id='line-plot')),
        ]
    )

    # add callback decorator
    @dash_app.callback( Output(component_id='line-plot', component_property='figure'),
                Input(component_id='input-year', component_property='value'))
    
    
    # Add computation to callback function and return graph
    def get_graph(yr):
        # Select 2019 data
        df =  airline_data[airline_data['Year']==int(yr)]
        
        # Group the data by Month and compute average over arrival delay time.
        line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
        
        fig = go.Figure(data=go.Scatter(
            x=line_data['Month'], 
            y=line_data['ArrDelay'], 
            mode='lines', 
            marker=dict(color='green')
        ))
        
        fig.update_layout(title={
                    'text': f'Average Arrival Delay per Month in <span style="color:blue;"><b>{yr}</b></span>',
                    'x': 0.5,  # Center the title
                    'xanchor': 'center'
                    },
                    xaxis_title='Month',
                    yaxis_title='Average Delay (minutes)',
                    template='plotly_white')
        return fig

    return dash_app
