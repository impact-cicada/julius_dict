# -*- coding: utf-8 -*-
import socket
import subprocess

# WAV再生コマンドフォーマット
cmd_fmt = 'aplay -D plughw:3,0 ~/voice/enogu_voice/{}'

# Julius接続
host = 'localhost'
port = 10500
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

def play_voice(name):
    subprocess.call(cmd_fmt.format(name), shell=True)

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
    print("WORD:"+word)
    if word == 'おはよう[/s]':
        print("=>おはよう")
        play_voice('anzu_oha.wav')

    if word == 'おやすみ[/s]':
        print("=>おやすみ")
        play_voice('anzu_oya.wav')

    if word == 'いってきます[/s]':
        print("=>いってらっしゃい")
        play_voice('anzu_itte.wav')

    if word == 'ただいま[/s]':
        print("=>おかえり")
        play_voice('anzu_oka.wav')

    res = ''
