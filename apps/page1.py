import os
from app import app
import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Div import Div
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd

df = pd.read_csv('assets/data_visu.csv')

#on vire les unitées dans les années
df['years'] = df['years'].apply(lambda x : (x//10)*10)

fig = px.scatter_geo(df,
                    lat=df.reclat,
                    lon=df.reclong,
                    width=1600, height=800,
                    animation_frame="years",
                    color='main_type',
                    #size = 50 je reviendrais !
                    )

layout = [ 
                html.H2("Impact des météorites de 1680 à 2020"),
                html.P("Voici un projet de l'école durant un hackathon d'une durée de 24h, avec la problèmatique suivante : "),
                html.P("Quel est la répartition des chutes de météorite dans le monde, par type entre 1700 et 2100"),
                html.P("En utilisant la bibliothèque Plotly qui est un framework Python j'ai développé un graphique dynamique qui répond à la problèmatique"),
                html.P("En appyant sur play ou en bougeant le curseur on peut ainsi voir les chutes de météorites dans le temps et par type"),
                dcc.Graph(figure=fig)
        ]