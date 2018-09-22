    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Sat Sep 22 10:44:30 2018
    
    @author: abdulliaqat
    """
            
    from util import *
    
    
    song_name = 'Carly_Rae_Jepsen_-_Call_Me_Maybe'
    words_lyric_path = 'lyric_database/aligned/Test/Sing/{}.words'.format(song_name)
#    song_name = '2pac_-_Let_Em_Have_It'
#    words_lyric_path = 'lyric_database/aligned/Test/Rap/{}.words'.format(song_name)
    audiofile = 'songs_wav/{}.wav'.format(song_name)
    words,start,end = split_song_to_wordMusic(words_lyric_path,audiofile)
    text_verse = 'We were the kings and queens of promise We were the victims of ourselves'
    generative_text = 'We Have only broken our dreams'
    generative_other = 'this is bad and this is crazy but you look right'
    generative_rap = 'You want it for a long time'
    text = generative_other
    
    

    file_name = find_wordMusic(text,words,start,end)
    make_music(file_name)
