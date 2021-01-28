import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv("./data/data.csv")

fig1 = px.line(df, x='act_starttime', y='act_distance', color='name')

app.layout = html.Div([
    html.H1("Strava App"),
    dcc.Graph(id='example_strava', figure=fig1)
])

#@app.callback(
#    Output("graph", "figure"), 
#    [Input("dropdown", "value")])
#def display_color(color):
#    fig = go.Figure(
#        data=go.Bar(y=[2, 3, 1], marker_color=color))
#    return fig

app.run_server(debug=True, port=8050, host="0.0.0.0")