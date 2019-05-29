# coding: utf-8
from spotipy.oauth2 import SpotifyClientCredentials
import os
client_credentials_manager = SpotifyClientCredentials(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
import spotipy
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
playlists = sp.user_playlists('vishaalk')
import pickle
playlists
pickle.save(open("playlist.p", "wb"), playlists)
pickle.dump(open("playlist.p", "wb"), playlists)
pickle.dump(playlists, open("playlist.p", "wb"))
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', 'get_tracks.py')
get_ipython().run_line_magic('save', 'get_tracks')
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', 'get_tracks 1-17')
