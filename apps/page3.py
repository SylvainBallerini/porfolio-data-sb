import os
import dash

import dash_table
from numpy.lib.utils import source
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app

import pandas as pd

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
#from IPython.display import display 


#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df = pd.read_csv("assets/data_film_06.csv")

option = []
for i, row in df.iterrows():
  dico = {}
  #print(f"{row['primaryTitle']} {row['startYear']}  {row['tconst']}")
  dico['label'] = str(row['primaryTitle']) + " , " + str(row['startYear'])
  dico['value'] = row['tconst']
  option.append(dico)

def create_df(df, string):
    string.lower()
    df = df.loc[df['title_lower'].str.contains(string)]
    return df

def KNN_Movie(df, film):
    #Entrainement Model
    X = df.drop(['tconst','primaryTitle','genres','language','title_lower','image'], axis= 1)
    y = df['primaryTitle']
    scaler = MinMaxScaler().fit(X)
    X_scaled = scaler.transform(X)
    model = KNeighborsClassifier(weights='distance', n_neighbors = 6)
    model.fit(X_scaled,y)  
    
    #Préparation film
    film = film.drop(['tconst','primaryTitle','genres','language','title_lower','image'], axis= 1)
    film_scaled = scaler.transform(film)
    new_film = model.kneighbors(film_scaled,  return_distance=False)
    df_new_film = df.iloc[new_film[0,:]]
    df_new_film = df_new_film[['primaryTitle','startYear','runtimeMinutes','genres','averageRating','numVotes','image']]
    #display(df_new_film)
    return df_new_film

#app.layout = html.Div(children=[
layout = dbc.Container(children=[  
    
    html.H4('Recommandation'),

    html.P("Projet de l'école avec comme problèmatique : faire un système de recommandation de film (comme Netflix) pour un cinéma dans la Creuse.\
    On a utilisé la base de données IMDB qui référence des millions de films.\
    Ensuite on a décidé de ne garder que 5000 films pour obtenir un catalogue aussi large que Netflix.\
    Les films doivent être en version française et d'une durée entre 1h30 et 2h30."),
    html.P("Une fois ce travail de sélection et de nettoyage fait sur le dataset, il faut utiliser le Machine Learning pour la recommandation.\
    Dans un premier temps j'ai entrainé un modèle avec l'algorithme du KNN (k-nearest neighbors ou les plus proches voisins en français).\
    En mettant en features (caractéristiques) la durée du film, les genres du film, l'année de sortie, on obtient un modêle prêt pour la recommandation.\
    Ainsi si vous selectionnez un film dans le menu déroulant ou en le tapant vous aurez le film que vous avez choisi et 5 films qui sont les plus proches en se basant sur les 3 features que j'ai cités avant."),
    html.H5("Technologies utilisées : scikit-learn KNN, pandas, numpy, css, html, python"),

    html.H6("Sélectionnez un film que vous aimez"),
    dcc.Dropdown(
        id='demo-dropdown',
        options = option
    ),
    html.Div(id='dd-output-container'),
    html.P(),

    html.Div(id="table_container_2"), 
    
])

@app.callback(
    dash.dependencies.Output('table_container_2', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')],
    prevent_initial_call = True
    )            
def display_KNN(tconst_movie):
    try :
        
        film = df.loc[df['tconst']== tconst_movie]
        dataframe = KNN_Movie(df, film)
        #dataframe = dataframe[['tconst', 'primaryTitle', 'startYear', 'runtimeMinutes',\
        #'genres', 'averageRating', 'numVotes']]
        dataframe = dataframe.reset_index()
        
        row_movie = []
        for i, row in dataframe.iterrows():            
            fiche = dbc.Col(html.Div([
                    html.Img(src=row['image'], className="img-fluid"),
                    html.P(str(row['startYear']) + " : " + str(row['runtimeMinutes']) + " mn"),
                    html.P(row['primaryTitle']),
                    html.P("Genre(s)" + str(row['genres'])),
                    #html.P('Genre')
                ]), md=4)            
            row_movie.append(fiche)        

    except Exception as e:
        print(e)
        return "Veillez entrer un ID (tconst) valide"
    
    return [                
                dbc.Row(
                   row_movie 
                )
            ]

#pour retourner un dataframe
'''
dash_table.DataTable(
                    columns=[{'name': str(i), 'id': str(i)} for i in dataframe.columns],
                    data=dataframe.to_dict('records'),
                ),
'''