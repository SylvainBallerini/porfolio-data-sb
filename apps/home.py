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
                html.P("Développeur depuis plus de 3 ans. Je prends le tournant de la donnée en tant que Data Analyst et Data Scientist, et \
                    je souhaite être un pionnier du big data \
                    grâce à la formation Data de l’école \
                    Wild Code School"),
                html.P("Je recherche un stage afin d’analyser \
                        les chiffres et d’élaborer des prédictions \
                        pour optimiser le processus de décision \
                        de l’entreprise "),
            ]),
            html.Div([
                html.H4("EXPÉRIENCE PROFESIONNELLES"),
                html.P(children=[html.Span("2019 - 2020 : "), html.Strong("Technicien informatique "),html.Span("- Sénat")]),
                html.Ul([
                    html.Li("Formation utilisateur"),
                    html.Li('Rédaction de documentation technique'),
                    html.Li("Maintenance / Support / DATA / Tests")
                ]),
                html.Hr(),
                html.P(children=[html.Span("2016 - 2018 : "), html.Strong("Assistant chef de projet / Développeur \
                    Java / SQL "),html.Span("- DSOgroup")]),
                html.Ul([
                    html.Li("Développement d’un ECM mettant en relation les huissiers de justice"),
                    html.Li('Maintenance du site internet'),
                    html.Li("Développement de nouvelles fonctionnalités JAVA / SQL / PL SQL")
                ]),
                html.Hr(),
                html.P(children=[html.Span("2016 Mai - Juillet : "), html.Strong("Développeur WEB"),html.Span(" - Infoway")]),
                html.Ul([
                    html.Li("Dévéloppement de nouvelles fonctionnalités PHP / SQL")                    
                ]),
                html.Hr(),
                html.P(children=[html.Span("2014 : "), html.Strong("Intégrateur Dévéloppeur web"),html.Span(" - E-Loou")]),
                html.Ul([
                html.Li("Mise à jour de différents sites internet"),
                html.Li("E-mailing")                    
                ]),
                html.Hr(),
                html.P(children=[
                html.Span(children=[html.Span("2007 - 2010 : "), html.Strong("Technicien Informatique")]),
                html.Span(" Groupe Hospitalier Diaconesses Croix Saint Simont"),
                ]),
                html.Ul([
                html.Li("Maintenance parc informatique (400 postes de travail)"),
                html.Li("Hotline"),
                ]),
                html.Hr()
            ]),
            html.Div([
                html.H4("PROJETS DATA"),
                html.Ul([
                    html.Li("API d’estimation du prix d’une borne pour véhicule électrique (Entreprise partenaire Beev"),
                    html.Li('Estimation du prix de vente d’une maison'),
                    html.Li("Système de recommandation de film (KNN)"),
                    html.Li(" Analyse des ventes d’une société (SQL / Data studio")
                    ]),
                html.Hr()
                ]),
            html.Div([
                        html.H4("COMPÉTENCES TECHNIQUES"),
                    ])
            ], style = {"width" : "800px"})