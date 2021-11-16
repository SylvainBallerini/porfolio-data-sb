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

layout = [html.H2("Projets Streamlits"),
html.P("Streamlit est un framework open-source Python spécialement conçu pour les Data Analyst et les Data scientists.\
    Ce framework permet de créer des applications web qui pourront intégrer aisément des modèles de machine learning et des outils de visualisation de données."),
html.H3("Dashboard Streamlit : il contient un ensemble de différents projets personnel avec de la datavisualition et du Machine Learning"),
html.P("Covid : dashboard en construction sur l'évolution de la pandémie avec différents graphiques interactifs sur l'évolution de la maladie"),
html.P("Transport en Europe : dashboard interactif sur une analyse des différent moyen de transport en Europe (bus, train, et covoiturage) "),
dcc.Link("Dashboard Streamlit", href="https://share.streamlit.io/sylvainballerini/porfolio_streamlit/main/app.py", target="blank")
]

