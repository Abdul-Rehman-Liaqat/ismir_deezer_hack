#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 21:36:28 2018

@author: natsuki
"""

import numpy as np
import pandas as pd
import subprocess

audiofile = 'songs_wav/Carly_Rae_Jepsen_-_Call_Me_Maybe_original.wav'
sentences_lyric_path = 'lyric_database/Carly_Rae_Jepsen_-_Call_Me_Maybe_original.srt'


def split_song_to_sentenceMusic(sentences_lyric_path, output_path='songs_wav/result3/'):
    sentences = []
    starts = []
    ends = []
    with open(sentences_lyric_path) as f:
        for i, line in enumerate(f):
            print(line)
            if i % 4 == 1:
                start = line.split(' ')[0]
                s0 = float('{:.5}'.format(start.split(':')[0]))
                s1 = float('{:.5}'.format(start.split(':')[1]))
                s2 = float('{:.5}'.format(start.split(':')[2].split(',')[0]))
                s3 = float('{:.5}'.format(start.split(':')[2].split(',')[1]))
                starttime = 3600*s0 + 60*s1 + s2 + s3/1000
                
                end = line.split(' ')[2]
                e0 = float('{:.5}'.format(end.split(':')[0]))
                e1 = float('{:.5}'.format(end.split(':')[1]))
                e2 = float('{:.5}'.format(end.split(':')[2].split(',')[0]))
                e3 = float('{:.5}'.format(end.split(':')[2].split(',')[1]))
                endtime = 3600*e0 + 60*e1 + e2 + e3/1000
                
                duration = endtime - starttime
                
                starts.append(starttime)
                ends.append(endtime)
                
            if i % 4 == 2:
                sentences.append(line.strip())
                
            if i % 4 == 3:
                #subprocess.run(['sox', audiofile, '{}_{}_{}.wav'.format(output_path, starts[-1], ends[-1], sentences[-1]), 'trim', str(starts[-1], '='+str(ends[-1]))])
                subprocess.run(['sox', audiofile, output_path + '{}_{}.wav'.format(starts[-1], ends[-1]), 'trim', str(starts[-1]), '='+str(ends[-1])])

    return sentences, starts, ends

def find_sentenceMusic(text, sentences, start, end, df):
    token = text.split('\n')
    file_name = []
    for tok in token:
        print(tok)
        if tok == '':
            continue
        ind_list = [i for i, w in enumerate(sentences) if(w == tok)]
        length_list = [end[i]-start[i] for i in ind_list]
        ind_dict = dict(zip(ind_list, length_list))
        sorted_by_value = sorted(ind_dict.items(), key=lambda kv: kv[1])
        print(ind_list)
        
        if len(sorted_by_value) == 1:
            ind = sorted_by_value[0][0]
        else:
            ind = sorted_by_value[int(len(sorted_by_value)/2)][0]
        file_name.append(str(start[ind]) +'_'+ str(end[ind])+ '.wav')
    return file_name

    
def make_sentence_music(file_name, output_file='songs_wav/text_to_music/temp_sent.wav', output_file_cp = 'songs_wav/text_to_music/temp_sent_cp.wav'):
    file1 = file_name[0]
    file2 = file_name[1]
    subprocess.run(['sox','songs_wav/result3/'+file1,'songs_wav/result3/'+file2,output_file])   

    for i,file in enumerate(file_name[2:]):
        subprocess.run(['cp',output_file,output_file_cp])
        subprocess.run(['sox',output_file_cp,'songs_wav/result3/'+file,output_file])   
  

sentences, start, end = split_song_to_sentenceMusic(sentences_lyric_path)
df = pd.DataFrame([start, end, sentences])
test_input = 'Try to chase me\nSo call me, maybe\nHey I just met you\n'
file_name = find_sentenceMusic(test_input, sentences, start, end, df)
make_sentence_music(file_name)