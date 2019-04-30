from flask import Flask, render_template
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

@app.route('/')
def hello_world():
    client_credentials_manager = SpotifyClientCredentials(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'])
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = sp.user_playlists('vishaalk')
    first = playlists['items'][0]
    second = playlists['items'][1]
    return (first['name'] + ' and ' + second['name'])