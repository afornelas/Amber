import asyncio

from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager


async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        info = await current_session.try_get_media_properties_async()
        # song_attr[0] != '_' ignores system attributes
        info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}
        # converts winrt vector to list
        info_dict['genres'] = list(info_dict['genres'])
        print(info_dict)

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

if __name__ == '__main__':
    current_media_info = asyncio.run(get_media_info())
    print('mid')
    current_media_info = asyncio.run(get_media_info())
