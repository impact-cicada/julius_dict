# -*- coding: utf-8 -*-
import socket
import subprocess
import random

# WAV再生コマンドフォーマット
cmd_fmt = 'aplay -D plughw:3,0 ~/voice/enogu_voice/{}'

# ボイスリスト
vlist_oha = ['anzu_oha.wav',  'tamaki_oha.wav',  'haru_oha.wav',  'nao_oha.wav']
vlist_oya = ['anzu_oya.wav',  'tamaki_oya.wav',  'haru_oya.wav',  'nao_oya.wav']
vlist_itt = ['anzu_itte.wav', 'tamaki_itte.wav', 'haru_itte.wav', 'nao_itte.wav']
vlist_oka = ['anzu_oka.wav',  'tamaki_oka.wav',  'haru_oka.wav',  'nao_oka.wav']

# Julius接続
host = 'localhost'
port = 10500
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

def set_enable_mic(enable):
    capture = '62' if enable else '0'
    subprocess.call('amixer sset Mic {} -c 2'.format(capture), shell=True)

def play_voice(name):
    set_enable_mic(False)
    subprocess.call(cmd_fmt.format(name), shell=True)
    set_enable_mic(True)

def speak_response(word):
    print("WORD:" + word)
    if word == 'おはよう[/s]':
        print("=>おはよう")
        play_voice(random.choice(vlist_oha))

    if word == 'おやすみ[/s]':
        print("=>おやすみ")
        play_voice(random.choice(vlist_oya))

    if word == 'いってきます[/s]':
        print("=>いってらっしゃい")
        play_voice(random.choice(vlist_itt))

    if word == 'ただいま[/s]':
        print("=>おかえり")
        play_voice(random.choice(vlist_oka))

res = ''
while True:
    # 音声認識の区切り[\n.]まで受信
    while (res.find('\n.') == -1):
        res += sock.recv(1024).decode('utf-8')

    # 認識文字列を抽出
    word = ''
    for line in res.split('\n'):
        index = line.find('WORD=')
        if index != -1:
            line = line[index+6:line.find('"', index+6)]
            if line != '[s]':
                word = word + line

    # 認識文字列にキーワードがあれば対応
    speak_response(word)

    res = ''
