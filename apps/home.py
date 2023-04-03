import os
from app import app
import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Div import Div
from dash.exceptions import PreventUpdate

layout = html.Div([
            html.Div([
                html.H3("PROFIL PERSONNEL :"),
                html.P("Développeur passionné, j’ai choisi de me reconvertir en tant que Data Engineer \ Analyst pour répondre à mon intérêt croissant pour les données. \
                Mon expérience en programmation et en architecture logicielle me donne les atouts nécessaires pour aider les entreprises à mieux \
                gérer et analyser leurs données."),
                html.P("Sur ce site en Dash (un framework Python pour la création \
                d'applications web interactives basées sur des graphiques et des visualisations de données.)\
                Je montre mes projets Data")

            ]),
            ], style = {"width" : "800px"})
