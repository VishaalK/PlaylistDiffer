# coding: utf-8
from spotipy.oauth2 import SpotifyClientCredentials
import os
import spotipy
client_credentials_manager = SpotifyClientCredentials(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
playlists = sp.user_playlists('vishaalk')
import pickle