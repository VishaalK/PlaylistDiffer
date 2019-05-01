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
    # tracks = playlists['tracks']
    tracks = sp.user_playlist_tracks('vishaalk', playlist_id='2AQQoLYh2L7CPZxQXoQmTK', fields='items(track(name))', limit=10, offset=0)
    tracks_names = [track['track']['name'] for track in tracks['items']]
    second = playlists['items'][1]
    # return (first['name'] + ' and ' + second['name'])
    return render_template('playlist.html', tracks=tracks_names)