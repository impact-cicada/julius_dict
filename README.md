# julius導入手順
## 4.5をダウンロード
https://github.com/julius-speech/julius

## 展開
```
cd ~
mkdir julius
cd julius
mv ~/Downloads/julius-master.zip ./
unzip julius-master.zip
mv julius-master julius4.5
```

## インストール（INSTALL.txtのLinux  (tested on Ubuntu-14.04)を参考）
```
sudo apt-get install build-essential zlib1g-dev libsdl2-dev
（sudo apt-get libasound2-dev）※実行しなくて良い
./configure
make
sudo make install
```

## インストール確認
```
julius --version
```

## ディクテーションキットをダウンロード
```
https://osdn.net/dl/julius/dictation-kit-4.5.zip
```
元サイト：http://julius.osdn.jp/index.php?q=dictation-kit.html

## 展開
```
mv ~/Downloads/dictation-kit-4.5.zip ./
unzip dictation-kit-4.5.zip
```

## USBマイクの認識確認（カード番号、デバイス番号をチェック）
```
arecord -l
```

## USBマイクを環境変数に設定
```
export ALSADEV="plughw:1,0"
```

## プロファイルにも追記
```
nano ~/.profile
```

## 動作確認
```
cd dictation-kit-4.5
julius -C main.jconf -C am-gmm.jconf -demo
```
マイクに向かって喋ってみる（この時点ではご認識多し）

# 独自辞書作成
## 流れ
読みファイル作成（greet.yomi）
```
おはよう おはよう
お休み おやすみ
```
音素ファイル作成（greet.phone）
```
cat greet.yomi | yomi2voca.pl > greet.phone
```
```
おはよう  o h a y o u
お休み o y a s u m i
```
構文ファイル作成（greet.grammar）
```
S : NS_B GREET NS_E
GREET:OHAYOU
GREET:OYASUMI
```
語彙ファイル作成（greet.voca）
```
% OHAYOU
おはよう o h a y o u
% OYASUMI
お休み o y a s u m i
% NS_B
[s] silB
% NS_E
[/s] silE
```
オートマトンと単語辞書へコンパイル（greet.dfa、.term、.dict）
```
mkdfa.pl greet
```
辞書を使用して動作確認
```
julius -C ~/julius/dictation-kit-4.5/am-gmm.jconf -nostrip -gram ./greet -input mic
```
「おはよう」か「お休み」のみで認識されるようになる
