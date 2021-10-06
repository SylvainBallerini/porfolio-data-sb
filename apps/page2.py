import os
from app import app
import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Div import Div
from dash.exceptions import PreventUpdate

layout = [
        html.H2("Évolution de la population mondiale entre 1800 et 2100"),
        html.P("Problématique : quelle est l'évolution de la population entre 1800 et 2100."),
        html.P("Ici j'ai utilisé un bar chart race qui permet rapidement de voir les 20 pays avec la plus forte population."),
        html.Iframe(src='https://flo.uri.sh/visualisation/5812050/embed', style={"overflow": "hidden", "height": "800px", "width": "100%"})
        ]