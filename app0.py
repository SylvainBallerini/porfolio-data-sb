import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Strong import Strong
#import geopandas as gpd
import  pandas as pd
import plotly.express as px
from IPython.core.display import display, HTML

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

server = app.server

df = pd.read_csv('assets/data_visu.csv')

#on vire les unitées dans les années
df['years'] = df['years'].apply(lambda x : (x//10)*10)

#px.set_mapbox_access_token(open(".mapbox_token").read())
fig = px.scatter_geo(df,
                    lat=df.reclat,
                    lon=df.reclong,
                    width=1600, height=800,
                    animation_frame="years",
                    color='main_type',
                    #size = 50 je reviendrais !
                    )

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H4("Sylvain BALLERINI ", className="display-4"),
        html.P("Data Analyst / Scientist junior"),
        html.Hr(),
        html.P(
            "Actuellement en recherche de stage", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("A propos de moi", href="/", active="exact"),
                dbc.NavLink("Chute de météorites", href="/page-1", active="exact"),
                dbc.NavLink("Évolution de la population", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

page_0 = html.Div([
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

page_1 = [ 
                html.H2("Impact des météorites de 1680 à 2020"),
                dcc.Graph(figure=fig)
        ]

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"),
			 [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return page_0                
    elif pathname == "/page-1":
        return page_1
    elif pathname == "/page-2":
        return [
                html.H2("Évolution de la population mondiale entre 1800 et 2100"),
                #html.Iframe(src="../assets/race_bar.html",style={"overflow": "hidden", "height": "800px", "width": "100%"}, )
                html.Iframe(src='https://flo.uri.sh/visualisation/5812050/embed', style={"overflow": "hidden", "height": "800px", "width": "100%"})
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)