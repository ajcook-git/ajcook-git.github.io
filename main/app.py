import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv("../data/data.csv")

fig1 = px.line(
    df,
    x='act_starttime',
    y='act_distance',
    color='name',
    labels=dict(
        act_starttime='Start time',
        act_distance='Distance (m)'
    ),
    title='Time vs. Distance (Feb Challenge)'
)

fig1.to_html('../index.html')

print('Created ../index.html')
