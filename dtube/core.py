# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['find_in_vids', 'search_in_vids', 'get_num_vids']

# %% ../00_core.ipynb 3
from pytube import YouTube, Channel
from fastcore.script import call_parse
from fastcore.test import *

# %% ../00_core.ipynb 5
def find_in_vids(o:dict,   # YT videos, dict title:description
                 t:str,    # text to search in title 
                 d:str):   # text to search in description
    r = {k:v for (k,v) in o.items() if t in k and d in v.lower()}
    return {k:l for (k,v) in r.items() for l in v.split('\n') if d in l.lower()} 

# %% ../00_core.ipynb 9
@call_parse
def search_in_vids(yt_name:str,   # YT user name
                   t:str,         # search in title 
                   d:str,         # search in description
                   n_vid:int=10): # number of videos to look into
    'Search by keyword in YouTube video descriptions'
    chan = Channel(f'https://www.youtube.com/user/{yt_name}')
    vids = chan.videos[:n_vid]
    vid_info = {v.title: v.description for v in vids}
    r = {k:v for (k,v) in vid_info.items() if t in k and d in v.lower()}
    return {k:l for (k,v) in r.items() for l in v.split('\n') if d in l.lower()}

# %% ../00_core.ipynb 11
@call_parse
def get_num_vids(yt_name:str,   #YT user id
                n_vid:int=10):  # number of vids to look into
    'Get the number of views for the last `n_vid` for user `yt_name`'
    chan = Channel(f'https://www.youtube.com/user/{yt_name}')
    vids = chan.videos[:n_vid]
    vids_dic = {v.title: v.views for v in vids}
    return {k:v for k,v in sorted(vids_dic.items(), key=lambda i: i[1], reverse=True)}
