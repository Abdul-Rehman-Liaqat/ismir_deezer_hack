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
            subprocess.run(['sox',audiofile,'songs_wav/result/{}_{}_{}.wav'.format(start[-1],end[-1],words[-1]),'trim',str(start[-1]),str(end[-1])])



text = 'We were the kings and queens of promise We were the victims of ourselves'
generative_text = 'We Have only broken our dreams'


def make_music(text):
    pass

token = text.split(' ')
file_name = []
for tok in token:
    ind = words.index(tok.upper())
    file_name.append(str(start[ind])+'_'+str(end[ind])+'_'+tok+'.wav')
    
    
