import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output
import pandas as pd
# Connect to main app.py file
from app import app, server
# Connect to your app pages
from apps import home, page1, page2, page3, projets_streamlit

#server = app.server
# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#00c49a",
    "font-family" : 'Work Sans'
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H3("Menu", className="display-4"),
        html.P("Sylvain", className="names"),
        html.P("BALLERINI", className="names"),
        html.Hr(),
        html.P(
            "Sélectionner la page :", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("home", href="/home", active="exact"),
                html.H4("Projets"),
                dbc.NavLink("Système de recommandation", href="/page3", active="exact"),
                dbc.NavLink("Impact des météorites", href="/page1", active="exact"),
                #dbc.NavLink("Bar chart race", href="/page2", active="exact"),

                #dbc.NavLink("Streamlit", href='/projets_streamlit', active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    elif pathname == '/page3':
        return page3.layout
    elif pathname == '/home' :
        return home.layout
    elif pathname == '/projets_streamlit':
        return projets_streamlit.layout
    else:
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )


if __name__ == '__main__':
    app.run_server(debug=True, port=3000, dev_tools_hot_reload=False)
