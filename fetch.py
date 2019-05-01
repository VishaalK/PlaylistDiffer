import os
import spotipy
import json
from pprint import PrettyPrinter
from spotipy.oauth2 import SpotifyClientCredentials

# convert to environment variables
client_credentials_manager = SpotifyClientCredentials(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# results = sp.search(q='weezer', limit=20)
# for i, t in enumerate(results['tracks']['items']):
    # print (' ', i, t['name'])

playlists = sp.user_playlists('vishaalk')
# print(json.dumps(playlists))

first = playlists['items'][0]
second = playlists['items'][1]
# print(json.dumps(first))

pp = PrettyPrinter(indent=4)
names = [(playlist['name'], playlist['id'], playlist['href']) for i, playlist in enumerate(playlists['items'])]

tracks = sp.user_playlist_tracks('vishaalk', playlist_id='2AQQoLYh2L7CPZxQXoQmTK', fields='items(track(name, href))', limit=10, offset=0)

pp.pprint(tracks['items'])
# print(first[''])
# print(len(playlists))