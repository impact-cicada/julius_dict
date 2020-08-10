# -*- coding: utf-8 -*-
import socket

host = 'localhost'
port = 10500

# Julius接続
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

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

    if word == 'おやすみ[/s]':
        print("=>おやすみ")

    if word == 'いってきます[/s]':
        print("=>いってらっしゃい")

    if word == 'ただいま[/s]':
        print("=>おかえり")

    res = ''
