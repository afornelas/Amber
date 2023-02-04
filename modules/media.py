'''Update Play Pause logic to use Match Cases in python 3.10'''

import asyncio

from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager

# vocab

vocab = {
    'play':['media',9],
    'pause':['media',9],
    'resume':['media',9],
    'stop':['media',9],
    'toggle':['media',5],
    'skip':['media',8],
    'next':['media',7],
    'previous':['media',8],
    'music':['media',4],
    'song':['media',4],
    'what':['media',4],
    'is':['media',4],
    'playing':['media',4],
    'now':['media',4],
    'artist':['media',4],
    'thumbnail':['media',4],
    'show':['media',4],
    'information':['media',4]
}

async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        info = await current_session.try_get_media_properties_async()
        # song_attr[0] != '_' ignores system attributes
        info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}
        # converts winrt vector to list
        info_dict['genres'] = list(info_dict['genres'])
        return info_dict

async def play():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        await current_session.try_play_async()

async def pause():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        await current_session.try_pause_async()

async def toggle_play_pause():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        await current_session.try_toggle_play_pause_async()

async def next():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        await current_session.try_skip_next_async()

async def previous():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        await current_session.try_skip_previous_async()

# parse method

def parse(text):
    # do something
    phrase = text.split()
    try:
        if 'what' in phrase:
            info = asyncio.run(get_media_info())
            if 'artist' in phrase:
                print(info['artist'])
            elif 'title' in phrase or 'song' in phrase:
                print(info['title'])
        else:
            if 'play' in phrase or 'resume' in phrase:
                asyncio.run(play())
            elif 'pause' in phrase or 'stop' in phrase:
                asyncio.run(pause())
            elif 'toggle' in phrase:
                asyncio.run(toggle_play_pause())
            elif 'skip' in phrase or 'next' in phrase:
                asyncio.run(next())
            elif 'previous' in phrase:
                asyncio.run(previous())
        return 1
    except Exception as e:
        print(e)
        return 0

# while True:
#     parse(str(input()))