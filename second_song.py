#!/usr/bin/env pytho
from util import *
from char_duration_calc2 import *

song_name = 'Carly_Rae_Jepsen_-_Call_Me_Maybe'
words_lyric_path = 'lyric_database/aligned/Test/Sing/{}.words'.format(song_name)
#    song_name = '2pac_-_Let_Em_Have_It'
#    words_lyric_path = 'lyric_database/aligned/Test/Rap/{}.words'.format(song_name)
audiofile = 'songs_wav/{}.wav'.format(song_name)
words,start,end = split_song_to_wordMusic(words_lyric_path,audiofile)
text_verse = 'We were the kings and queens of promise We were the victims of ourselves'
generative_text = 'We Have only broken our dreams'
generative_other = 'bad and this is crazy but you look right'
generative_rap = 'You want it for a long time'
text = generative_other

char_dur_time = calc_time_per_char(words_lyric_path)
char_dur_average = calc_avetime_per_char(char_dur_time)    

def find_best_wordMusic(text,words,start,end):
    token = text.split(' ')
    file_name = []
    char_dur_time = calc_time_per_char(words_lyric_path)
    char_dur_average = calc_avetime_per_char(char_dur_time)
    for tok in token:
        ind_list = [i for i,w in enumerate(words) if(tok.upper() == w)]
        length_list = [end[i]-start[i] for i in ind_list]
        best_word_duration = best_word_time(tok,length_list,char_dur_average)
        ind = ind_list[length_list.index(best_word_duration)]
        file_name.append(str(start[ind])+'_'+str(end[ind])+'_'+tok.upper()+'.wav')
    return file_name

file_name = find_best_wordMusic(text,words,start,end)
make_music(file_name)
