import os
import pandas as pd
import platform
import random
import subprocess
import sys
import time
from tkinter import filedialog
from tinytag import TinyTag
import vlc
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
clear()
print("WELCOME TO THE MOST INSANE MUSIC PROGRAM EVER AHHHHHHHHHHHHHHHHHHHH")
def format_library(library_path):
    print("Not implemented yet :(")
    input("Enter to continue")
try:
    settings_config = open(os.path.expanduser('~').replace("\\", "/") + "/IMAconfig.cfg", "r")
    library_path = list(settings_config)[0].replace("libraryPath:", "").replace("\n", "")
except:
    print("Welcome to IMA!")
    time.sleep(3)
    clear()
    print("You need to choose some options to set up IMA before you begin using it")
    time.sleep(4)
    clear()
    print("You can always change these later using the \"Settings\" option in the main menu")
    time.sleep(5)
    clear()
    settings_config = open(os.path.expanduser('~').replace("\\", "/") + "/IMAconfig.cfg", "w")
    print("Step 1/4")
    library_path = input("First type the path to your music library, or type \"GUI\" to open a folder picker: ")
    if "GUI" in library_path:
        library_path = filedialog.askdirectory(initialdir = "~", title = "Select your music library folder")
    library_path = library_path.replace("\\", "/")
    if str(library_path[len(library_path)-1]) !="/":library_path+="/"
    settings_config.write("libraryPath:" + library_path + "\n")
    print("Music library folder path saved!")
    time.sleep(3)
    clear()
    print("Step 2/4")
    displaylyrics = input("Would you like to display lyrics (if they're available) while playing to songs?(Y/N)")
    if displaylyrics.lower() == "y":
        displaylyrics = "true"
    else:
        displaylyrics = "false"
    settings_config.write(f"displayLyrics:{displaylyrics}\n")
    if displaylyrics=="true":
        print("Lyrics will now display when playing music!")
    else:
        print("Lyrics won't display when playing music.")
    time.sleep(3)
    clear()
    print("Step 3/4")
    defaultpage = input("Please select which page you would like to be opened first, when IMA is opened the future:\n1 for the artists page\n2 for the albums page\n3 for the search page\n4 for the main menu\n:")
    if defaultpage=="1":
        defaultpage="artist"
    elif defaultpage=="2":
        defaultpage="album"
    elif defaultpage=="3":
        defaultpage="search"
    elif defaultpage=="4":
        defaultpage="mainmenu"
    settings_config.write(f"startupPage:{defaultpage}\n")
    print("Startup page set successfully!")
    time.sleep(3)
    clear()
    print("Step 4/4")
    format_library_input = input("Finally, if you selected a music library folder that isn't already formatted for use with IMA, would you like IMA to format it now?(Y/N)(check the readme in the IMA github for more information on how the library will be formatted)\n:")
    if format_library_input.lower()=="y":
        format_library(library_path)
    clear()
    print("Welcome to IMA!")
    sleep.wait(3)
def PlayMusicFr(user_artist, user_album, user_song):
    try:
        current_song_info = audio_files_in_album[user_song-1].split("[]")
        current_song_number = current_song_info[0]
        current_song_name = current_song_info[1]
        print("Loading \"" + str(current_song_number) + ". " + str(current_song_name) + "\"...")
        current_song_codec = current_song_info[2].replace(".m4a", "")
        # try:
        current_lyrics_filename=""
        counter = 0
        for fr in current_song_info:
            if counter==1:
                current_lyrics_filename+=fr
            elif counter>1:
                current_lyrics_filename+="[]"+fr
            counter+=1
        current_lyrics = open(library_path + str(os.listdir(library_path)[user_artist-1] + "/" + os.listdir(library_path + os.listdir(library_path)[user_artist-1])[user_album-1] + "/" + str(current_lyrics_filename)).replace("m4a", "lrc"), "r")
        list_of_lyrics = current_lyrics.readlines()
        no_lyrics_current_song = False
        global lyric_timestamp
        global lyric_lines
        global current_lyric_number
        lyric_timestamp = []
        lyric_lines = []
        current_lyric_number = 0
        airpods_mode = False
        last_lyric_timestamp = ""
        counter = -1
        for fr in list_of_lyrics:
            counter+=1
            dont_set_last_lyric_timestamp_until_next_loop_pls = False
            # print("LOOK FRFRFR!!" + str(fr) + " AND LOOK FRFR " + str(fr).split("]")[0][1:6])
            if last_lyric_timestamp == str(fr).split("]")[0][1:6] and counter!=len(list_of_lyrics):
                # print(str(last_lyric_timestamp) + "*****" + str(str(fr).split("]")[0][1:6]))
                if last_lyric_timestamp[4] == "9":
                    lyric_timestamp = lyric_timestamp + [str(fr).split("]")[0][1:4] + str(int(str(fr).split("]")[0][4])+1) + "0"]
                    last_lyric_timestamp = str(fr).split("]")[0][1:4] + str(int(str(fr).split("]")[0][4])+1) + "0"
                    dont_set_last_lyric_timestamp_until_next_loop_pls = True
                else:
                    lyric_timestamp = lyric_timestamp + [str(fr).split("]")[0][1:5] + str(int(str(fr).split("]")[0][5])+1)]
                    last_lyric_timestamp = str(fr).split("]")[0][1:5] + str(int(str(fr).split("]")[0][5])+1)
                    dont_set_last_lyric_timestamp_until_next_loop_pls = True
                # print(str(last_lyric_timestamp) + "*****" + str(lyric_timestamp[counter]))
            else:            
                if str(fr).split("]")[0][1:6] == "00:00":
                    print("it's 00:00 innittttt")
                    lyric_timestamp = lyric_timestamp + [str(fr).split("]")[0][1:5] + str(int(str(fr).split("]")[0][5])+1)]
                else:
                    lyric_timestamp = lyric_timestamp + [str(fr).split("]")[0][1:6]]
            if not dont_set_last_lyric_timestamp_until_next_loop_pls:
                if str(fr).split("]")[0][1:6] == "00:00":
                    print("it's 00:00 innittttt")
                    last_lyric_timestamp = str(fr).split("]")[0][1:5] + str(int(str(fr).split("]")[0][5])+1)
                else:
                    last_lyric_timestamp = str(fr).split("]")[0][1:6]
            lyric_lines = lyric_lines + [str(fr).split("]")[1]]
    except:
        no_lyrics_current_song = True
    # for fr in range(len(lyric_lines)):
    #     print(str(lyric_timestamp[fr]) + " - " + str(lyric_lines[fr]))
    def display_lyric(counter, current_lyric_number):
        mins = counter//60
        secs = counter%60
        if len(str(mins))>=1:
            mins = "0" + str(mins)
        if len(str(secs))<=1:
            secs = "0" + str(secs)
        # print("Current: " + (str(mins) + ":" + str(secs)) + " *** next lyric: " + str(lyric_timestamp[current_lyric_number]))
        if str(current_lyric_number) != str(len(lyric_timestamp)):
            if str(lyric_timestamp[current_lyric_number]) == (str(mins) + ":" + str(secs)):
                current_lyric_number+=1
        return current_lyric_number
    counter = 0
    player = vlc.MediaPlayer(library_path + os.listdir(library_path)[user_artist-1] + "/" + os.listdir(library_path + os.listdir(library_path)[user_artist-1])[user_album-1] + "/" + audio_files_in_album[user_song-1])
    player.play()
    time.sleep(0.2)
    clear()
    current_duration = str(player.get_length())[:(len(str(player.get_length()))-3)]
    current_duration_mins = int(current_duration)//60
    current_duration_secs = int(current_duration)%60
    last_minute = False
    counter = 0
    while True:
        counter+=1
        if str(current_song_codec)=="EC3":
            current_song_codec = "EC3 (Dolby Atmos)"
        print("Currently playing \"" + str(current_song_number) + ". " + str(current_song_name) + "\" with the codec \"" + str(current_song_codec) + "\"")
        if current_duration_mins == 0:
            current_duration_secs-=1
            print(str(current_duration_secs) + " secs remaining")
            if current_duration_secs==0 and last_minute:
                break
        elif current_duration_secs !=0:
            current_duration_secs-=1
            print(str(current_duration_mins) + " mins " + str(current_duration_secs) + " secs remaining")
        elif current_duration_mins == 1 and current_duration_secs>=1:
            print(str(current_duration_mins) + "min " + str(current_duration_secs) + " secs remaining")
        else:
            current_duration_mins-=1
            current_duration_secs=59
            if current_duration_mins == 1:
                print(str(current_duration_mins) + "min " + str(current_duration_secs) + " secs remaining")
            elif current_duration_mins == 0:
                if last_minute:
                    break
                print(str(current_duration_secs) + " secs remaining")
                last_minute = True
            else:
                print(str(current_duration_mins) + " mins " + str(current_duration_secs) + " secs remaining")
        if no_lyrics_current_song:
            print("No lyrics for current song :(")
        else:
            if airpods_mode:
                current_lyric_number = display_lyric(counter-1, current_lyric_number)
            else:
                current_lyric_number = display_lyric(counter, current_lyric_number)
            if current_lyric_number!=0:
                print(str(lyric_lines[current_lyric_number-1]).replace("â€™","\'"))
        time.sleep(1)
        clear()
    clear()
    print("Song finished!")
#player = vlc.MediaPlayer("TRACKING TEST INNIIIIT.mp4")
# player.play()

print("--------------------------------")
print("---------M-A-I-N_M-E-N-U--------")
print("--------------------------------")
print("1. Artists")
print("2. Settings")
print("3. Add new music")
print("4. Search")
mode = int(input(":"))
clear()
if mode==1:
    print("Choose an artist:")
    counter = 0
    artist_dirs = []
    for fr in os.listdir(library_path):
        if os.path.isdir(library_path + str(fr)):
            counter+=1
            artist_dirs = artist_dirs + [fr]
            print(f"{str(counter)}. {fr}")
    user_artist = int(input("Artist ID: "))-1
    counter = 1
    for fr in os.listdir(library_path):
        # print(str(counter) + "****" + str(fr) + "****" + artist_dirs[user_artist])
        if fr == artist_dirs[user_artist]:
            user_artist = counter
            break
        counter+=1
    clear()
    print("Choose an album:")
    counter = 0
    for fr in os.listdir(library_path + os.listdir(library_path)[user_artist-1]):
        print("album found" + str(fr))
        counter+=1
        print(f"{str(counter)}. {fr}")
    user_album = int(input("Album ID: "))
    clear()
    print("Choose a song:")
    counter = 0
    audio_files_in_album = []
    track_numbers_of_audio_files_in_album = []
    print(str(library_path))
    print(str(os.listdir(library_path)[user_artist-1]))
    print(str(os.listdir(library_path + os.listdir(library_path)[user_artist-1])[user_album-1]))
    for fr in os.listdir(library_path + os.listdir(library_path)[user_artist-1] + "/" + os.listdir(library_path + os.listdir(library_path)[user_artist-1])[user_album-1]):
        if ".m4a" in fr:
            # print("song found and added to list: " + str(fr))
            counter+=1
            audio_files_in_album = audio_files_in_album + [fr]
            track_numbers_of_audio_files_in_album = track_numbers_of_audio_files_in_album + [str(fr.split("[]")[0])]
    # for fr in audio_files_in_album
            # print(str(counter) + ". " + fr.split("[]")[0])
    if len(audio_files_in_album)==1:
        print(audio_files_in_album[0].split("[]")[0] + ". " + audio_files_in_album[0].split("[]")[1])
        if input("Option (so much choice ik):") == audio_files_in_album[0][0]:
            PlayMusicFr(user_artist, user_album, 1)
    for counter in range(1,len(audio_files_in_album)):
        # print(str(counter))
        for fr in range(len(audio_files_in_album)):
            # print(str(fr))
            if track_numbers_of_audio_files_in_album[fr] == str(counter):
                # print("song found: " + track_numbers_of_audio_files_in_album[fr] + "!!!!!!" + str(counter))
                print(str(track_numbers_of_audio_files_in_album[fr] + ". " + str(audio_files_in_album[fr].split("[]")[1])))
    print(str(counter+1) + ". Play All Songs In Order")
    print(str(counter+2) + ". Shuffle All Songs")
    user_song = int(input("Option: "))
    if user_song == (counter+1):
        counter = 1
        counter2 = -1
        for fr in range(0, len(audio_files_in_album)):
            for user_song in audio_files_in_album:
                counter2+=1
                # print("current user_song: " + str(user_song) + "and current counter: " + str(counter))
                if int(user_song.split("[]")[0]) == counter:
                    # print("found song fr as number " + str(counter2) + " in audio_files_in_album, which is " + audio_files_in_album[counter2])
                    PlayMusicFr(user_artist, user_album, counter2+1)
                    counter+=1
    elif user_song == (counter+2):
        shuffled_album = random.sample(range(len(audio_files_in_album)), len(audio_files_in_album))
        for user_song in shuffled_album:
            PlayMusicFr(user_artist, user_album, user_song+1)
    else:
        counter = 1
        counter2 = -1
        for fr in range(0, len(audio_files_in_album)):
            for user_song_fr in audio_files_in_album:
                counter2+=1
                # print("current user_song: " + str(user_song) + "and current counter: " + str(counter))
                if int(user_song_fr.split("[]")[0]) == int(user_song):
                    # print("found song fr as number " + str(counter2) + " in audio_files_in_album, which is " + audio_files_in_album[counter2])
                    PlayMusicFr(user_artist, user_album, counter2+1)
                    break
                    counter+=1
elif mode==2:
    # try:
    #     settings_config = open(library_path + "config.cfg", "r")
    # except:
    settings_config = open(library_path + "config.cfg", "w")
    settings_config.writelines("default-codec:aac\n")
    settings_config.writelines("display-lyrics:false\n")
    settings_config.writelines("playback device:\n")
elif mode==3:
    p = subprocess.Popen(["powershell.exe", ".\"~/Documents/powershell scripts frfr/launch_apple_music_downloader.ps1\""], stdout=sys.stdout)
    sys.stdout.flush()
    p.communicate("echo hi")
    sys.stdout.flush()
    print("Finished script")
    for fr in os.listdir("C:/temp/musicapptemp/"):
        print(str(fr))
        for frfr in os.listdir("C:/temp/musicapptemp/" + str(fr)):
            print(str(frfr))
            if "(SOUNDTRACK FROM AND INSPIRED BY THE MOTION PICTURE" in frfr.upper():
                print("found")
                if "DELUXE EDITION" in frfr.upper():
                    new_folder_name = frfr.upper().replace("(SOUNDTRACK FROM AND INSPIRED BY THE MOTION PICTURE", "(")
                else:
                    new_folder_name = frfr.upper().replace("SOUNDTRACK FROM AND INSPIRED BY THE MOTION PICTURE", "")
                os.rename("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr), "C:/temp/musicapptemp/" + str(fr) + "/" + str(new_folder_name))
                print(str(frfr) + " successfully renamed to " + str(new_folder_name))

    for fr in os.listdir("C:/temp/musicapptemp/"):
        print("Opening " + fr)
        for frfr in os.listdir("C:/temp/musicapptemp/" + str(fr)):
            counter = 0
            highest_track_number_disc_1 = 1
            highest_track_number_disc_2 = 1
            highest_track_number_disc_3 = 1
            highest_track_number_disc_4 = 1
            highest_track_number_disc_5 = 1
            print("Opening " + frfr)
            for frfrfr in random.sample(os.listdir("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr)), len(os.listdir("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr)))):
                print("Opening " + frfrfr)
                if ".lrc" not in frfrfr and ".jpg" not in frfrfr and "ec3" not in frfrfr:
                    print("Current file is audio file: " + str(frfrfr))
                    current_tag = TinyTag.get("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(frfrfr))
                    if current_tag.disc=="1":
                        if int(current_tag.track)>int(highest_track_number_disc_1):
                            highest_track_number_disc_1 = current_tag.track
                            print(str(current_tag.title) + "has new highest track number of disc 1, at " + str(current_tag.track))
                    elif current_tag.disc=="2":
                        if int(current_tag.track)>int(highest_track_number_disc_2):
                            highest_track_number_disc_2 = current_tag.track
                            print(str(current_tag.title) + "has new highest track number of disc 2, at " + str(current_tag.track))
                    elif current_tag.disc=="3":
                        if int(current_tag.track)>int(highest_track_number_disc_3):
                            highest_track_number_disc_3 = current_tag.track
                            print(str(current_tag.title) + "has new highest track number of disc 3, at " + str(current_tag.track))
                    elif current_tag.disc=="4":
                        if int(current_tag.track)>int(highest_track_number_disc_4):
                            highest_track_number_disc_4 = current_tag.track
                            print(str(current_tag.title) + "has new highest track number of disc 4, at " + str(current_tag.track))
                    elif current_tag.disc=="5":
                        if int(current_tag.track)>int(highest_track_number_disc_5):
                            highest_track_number_disc_5 = current_tag.track
                            print(str(current_tag.title) + "has new highest track number of disc 5, at " + str(current_tag.track))
            for frfrfr in random.sample(os.listdir("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr)), len(os.listdir("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr)))):
                if ".lrc" not in frfrfr and ".jpg" not in frfrfr and "ec3" not in frfrfr:
                    current_tag = TinyTag.get("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(frfrfr)) 
                    if current_tag.disc=="1":
                        os.rename("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(frfrfr), ("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(int(current_tag.track)) + "[]" + str(frfrfr)))
                    if current_tag.disc=="2":
                        os.rename("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(frfrfr), ("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(int(current_tag.track)+int(highest_track_number_disc_1)) + "[]" + str(frfrfr)))
                    if current_tag.disc=="3":
                        os.rename("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(frfrfr), ("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(int(current_tag.track)+int(highest_track_number_disc_1)+int(highest_track_number_disc_2)) + "[]" + str(frfrfr)))
                    if current_tag.disc=="4":
                        os.rename("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(frfrfr), ("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(int(current_tag.track)+int(highest_track_number_disc_1)+int(highest_track_number_disc_2)+int(highest_track_number_disc_3)) + "[]" + str(frfrfr)))
                    if current_tag.disc=="5":
                        os.rename("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(frfrfr), ("C:/temp/musicapptemp/" + str(fr) + "/" + str(frfr) + "/" + str(int(current_tag.track)+int(highest_track_number_disc_1)+int(highest_track_number_disc_2)+int(highest_track_number_disc_3)+int(highest_track_number_disc_4)) + "[]" + str(frfrfr)))
    for fr in os.listdir("C:/temp/musicapptemp/"):
        print(str("moving ") + str(fr))
        p = subprocess.Popen(["powershell.exe", "robocopy \"C:/temp/musicapptemp/" + str(fr) + "\" \"C:/Users/harry/Desktop/AppleMusicDecrypt-Windows_latest/downloads/" + str(fr) + "/\" /MIR"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        p = subprocess.Popen(["powershell.exe", "Remove-Item -Path \"C:/temp/musicapptemp/" + str(fr) + "\""])
    print("FInishjed innittttt")
elif mode==4:
    songslist, artistlist, albumlist, foundinsongslistsongs, foundinsongslistalbums, foundinsongslistartists, foundinalbumslistsongs, foundinalbumslistalbums, foundinalbumslistartists, foundinartistslistsongs, foundinartistslistalbums, foundinartistslistartists = [], [], [], [], [], [], [], [], [], [], [], []
    for fr in os.listdir(library_path):
        if os.path.isdir(fr):
            for frfr in os.listdir(library_path + fr):
                if os.path.isdir(library_path + fr + "/" + frfr):
                    for frfrfr in os.listdir(f"{library_path}{fr}/{frfr}"):
                        if ".m4a" in frfrfr:
                            songslist+=[frfrfr.split("[]")[1]]
                            albumlist+=[frfr]
                            artistlist+=[fr]
    # for fr in range(0,len(songslist)):
    #     print(str(songslist[fr]) + " in " + str(albumlist[fr]) + " by " + str(artistlist[fr]))
    search_term = str(input("Search term: ")).lower()
    counter = -1
    for fr in songslist:
        counter+=1
        if search_term in fr.lower():
            foundinsongslistsongs+=[fr.lower().replace(search_term, ("|" + search_term + "|"))]
            foundinsongslistalbums+=[albumlist[counter]]
            foundinsongslistartists+=[artistlist[counter]]
    counter = -1
    for fr in albumlist:
        counter+=1
        if search_term in fr.lower() and fr.lower().replace(search_term, ("|" + search_term + "|")) not in foundinalbumslistalbums:
            foundinalbumslistsongs+=[songslist[counter]]
            foundinalbumslistalbums+=[fr.lower().replace(search_term, ("|" + search_term + "|"))]
            foundinalbumslistartists+=[artistlist[counter]]
    counter = -1
    for fr in artistlist:
        counter+=1
        if search_term in fr.lower() and fr.lower().replace(search_term, ("|" + search_term + "|")) not in foundinartistslistartists:
            foundinartistslistsongs+=[songslist[counter]]
            foundinartistslistalbums+=[albumlist[counter]]
            foundinartistslistartists+=[fr.lower().replace(search_term, ("|" + search_term + "|"))]
    # clear()
    pd.set_option('display.max_colwidth', 255)
    if not len(foundinartistslistsongs) and not len(foundinalbumslistsongs) and not len(foundinsongslistsongs):
        print("No results found")
    else:
        if len(foundinsongslistsongs):
            print("Found in song names:") 
            longest_song_name = 0
            longest_album_name = 0
            longest_artist_name = 0
            counter = 0
            for fr in foundinsongslistsongs:
                if longest_song_name==0:
                    longest_song_name = int(len(str(fr)))
                else:
                    if int(len(str(fr))) > longest_artist_name:
                        longest_song_name = int(len(str(fr)))
            for fr in foundinsongslistalbums:
                if longest_album_name==0:
                    longest_album_name = int(len(str(fr)))
                else:
                    if int(len(str(fr))) > longest_album_name:
                        longest_album_name = int(len(str(fr)))
            for fr in foundinsongslistartists:
                if longest_artist_name==0:
                    longest_artist_name = int(len(str(fr)))
                else:
                    if int(len(str(fr))) > longest_artist_name:
                        longest_artist_name = int(len(str(fr)))
            counter = 0
            print("   |Name" + " "*(longest_song_name-4) + "|Artist" + " "*(longest_artist_name-6)+ "|Album" + " "*(longest_album_name-5) + "|")
            for fr in range(0, len(foundinsongslistartists)):
                counter+=1
                print(str(counter) + ". |" + str(foundinsongslistsongs[fr]) + " "*(longest_song_name - int(len(str(foundinsongslistsongs[fr])))) + "|" + str(foundinsongslistartists[fr]) + " "*(longest_artist_name - int(len(str(foundinsongslistartists[fr])))) + "|" + str(foundinsongslistalbums[fr]) + " "*(longest_album_name- len(str(foundinsongslistalbums[fr]))) + "|")
        if len(foundinalbumslistsongs):
            print("Found in album names:") 
            longest_song_name = 0
            longest_album_name = 0
            longest_artist_name = 0
            for fr in foundinalbumslistalbums:
                if longest_album_name==0:
                    longest_album_name = int(len(str(fr)))
                else:
                    if int(len(str(fr))) > longest_album_name:
                        longest_album_name = int(len(str(fr)))
            for fr in foundinalbumslistartists:
                if longest_artist_name==0:
                    longest_artist_name = int(len(str(fr)))
                else:
                    if int(len(str(fr))) > longest_artist_name:
                        longest_artist_name = int(len(str(fr)))
            print("   |Album" + " "*(longest_album_name-5)+ "|Artist" + " "*(longest_artist_name-6) + "|")
            for fr in range(0, len(foundinalbumslistalbums)):
                counter+=1
                print(str(counter) + ". |" + str(foundinalbumslistalbums[fr]) + " "*(longest_album_name - int(len(str(foundinalbumslistalbums[fr])))) + "|" + str(foundinalbumslistartists[fr]) + " "*(longest_artist_name- len(str(foundinalbumslistartists[fr]))) + "|")
        if len(foundinartistslistsongs):
            print("Found in artist names:")
            for fr in foundinartistslistartists:counter+=1;print(str(counter) + ". " + str(fr))
        while True:
            try:
                user_choice = int(input("Number of object to select: "))
                if user_choice<=len(foundinsongslistsongs):
                    print("song selected")
                elif user_choice<=(len(foundinalbumslistsongs)+len(foundinsongslistsongs)):
                    print("album selected")
                elif user_choice<=(len(foundinartistslistsongs)+len(foundinalbumslistsongs)+len(foundinsongslistsongs)):
                    print("artist selected")
                elif user_choice==13543:
                    break
                else:
                    0/0
            except:
                print("nah what on earth did you put 🫨🫨🫨🫨🫨")
    input("Enter to continue")
    # os.system("python main.py")
#fr