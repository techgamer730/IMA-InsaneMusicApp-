# IMA-InsaneMusicApp-
A (currently cli only) app which can play audio files (through vlc via the python-vlc library).
Current features:
Navigate through artists, albums and songs
Shuffle, play whole albums, or play certain songs.
Duration left of current song displayed
Lyrics support (currently loads from a .lrc file with same name as audio file)
Search functionality, to search through song names, album names and artist names.
Can play songs over multiple discs.
Decently optimised as cli-only
As vlc is used, atmos files can also be played, even if to use via atmos for headphones.
To-do:
Actually play the songs searched for lol
Select albums, without going through an artist first
Play or shuffle all songs by a particular artist, or all songs in whole of library.
Add settings to change codec, lyrics toggle, playback device, airpods mode(audio delay), change library location, default codec
Allow song.link links to be created for easy song sharing.
Add playlists
Allow users to select which codec they want, if there's multiple avalable for an album/song (there may be atmos and lossless versions for instance).
Make the main loop update every 0.1 seconds to make lyrics work better
Add discord activity integration