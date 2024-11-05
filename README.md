# IMA-InsaneMusicApp-
A (currently cli only) app which can play audio files (through vlc via the python-vlc library).
Current features:
<ul>
<li>Navigate through artists, albums and songs</li>
<li>Shuffle, play whole albums, or play certain songs.</li>
<li>Duration left of current song displayed</li>
<li>Lyrics support (currently loads from a .lrc file with same name as audio file)</li>
<li>Search functionality, to search through song names, album names and artist names.</li>
<li>Can play songs over multiple discs.</li>
<li>Decently optimised as cli-only</li>
<li>As vlc is used, atmos files can also be played, even if to use via atmos for headphones.</li>
</ul>
To-do:
<ul>
<li>Actually play the songs searched for lol</li>
<li>Select albums, without going through an artist first</li>
<li>Play or shuffle all songs by a particular artist, or all songs in whole of library.</li>
<li>Add settings for:
<ul>
<li>Toggling lyrics being displayed</li>
<li>Default playback device</li>
<li>Airpods mode (adding audio delay so lyrics display correctly)</li>
<li>Change library location(to read from)</li>
<li>Default codec(if multiple codecs are available)</li>
</ul>
<li>Allow song.link links to be created for easy song sharing.
<li>Add playlists</li>
<li>Allow users to select which codec they want, if there's multiple avalable for an album/song (there may be atmos and lossless versions for instance).
<li>Make the main loop update every 0.1 seconds to make lyrics work better
<li>Add discord activity integration
