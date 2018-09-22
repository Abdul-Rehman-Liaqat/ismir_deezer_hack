#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 22:32:53 2018

@author: natsuki
"""

import subprocess



audiofile = 'songs_wav/30_Seconds_to_Mars_-_Kings_and_Queens.wav'
words = []
start = []
end = []


with open('lyric_database/aligned/Test/Sing/30_Seconds_to_Mars_-_Kings_and_Queens.words') as f:
    for line in f:
        data = line.strip().split(' ')
        print(data)
        words.append(data[2])
        start.append(float(data[0]))
        end.append(float(data[1]))
        if(words[-1] != 'OH' or words[-1] != 'sp'):
            subprocess.run(['sox',audiofile,'songs_wav/result/{}_{}_{}.wav'.format(start[-1],end[-1],words[-1]),'trim',str(start[-1]),'='+str(end[-1])])



text_verse = 'We were the kings and queens of promise We were the victims of ourselves'
generative_text = 'We Have only broken our dreams'

text = generative_text

def make_music(text):
    pass

token = text.split(' ')
file_name = []
for tok in token:
    ind = words.index(tok.upper())
    file_name.append(str(start[ind])+'_'+str(end[ind])+'_'+tok.upper()+'.wav')


file1 = file_name[0]
file2 = file_name[1]
subprocess.run(['sox','songs_wav/result/'+file1,'songs_wav/result/'+file2,"songs_wav/text_to_music/temp.wav"])   
for i,file in enumerate(file_name[2:]):
    subprocess.run(['sox','songs_wav/text_to_music/temp.wav','songs_wav/result/'+file,"songs_wav/text_to_music/temp.wav"])   
    


#    109.0625_109.1225_WE.wav
#     0.6425_1.2725_THE.wav