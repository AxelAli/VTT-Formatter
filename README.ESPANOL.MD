# VTT-Formatter
Conversion VTT a TXT , principalmente para datasets, chatbots y seq2seq !


## Ejemplo input-output
### Input
```
WEBVTT
Kind: captions
Language: en

00:00:01.060 --> 00:00:05.520
Hey, Vsauce. Michael here.
Let's take a moment to recognize

00:00:05.520 --> 00:00:08.849
the heroes who count.
Canadian

00:00:08.849 --> 00:00:12.769
Mike Smith holds the world record for
the largest number

00:00:12.769 --> 00:00:16.730
counted to in one breath - 125.
```
### Output
```
Hey, Vsauce. Michael here.
Let's take a moment to recognize
the heroes who count.
Canadian
Mike Smith holds the world record for
the largest number
counted to in one breath - 125.
```

### Usage
Crea una carpeta, en este caso "Vsaucesubs" , aqui estan todos tus archivos vtt

El programa creara una carpeta  "Vsaucesubstxt"

```
python VTT\ Formatter.py <SUB-DIR>
#Example
python VTT\ Formatter.py ./Vsaucesubs
```
Tambien conseguiras un archivo "allcombined.txt" que contiene todos los archivos en uno


### Protip
instala "youtube-dl" >  https://rg3.github.io/youtube-dl/

Si tu video no tiene subtitulos
```
youtube-dl --write-auto-sub --skip-download --sub-lang <language(en,es,fr)> '<VIDEOURL/CHANNELURL/PLAYLISTURL>'
```
pero si los tiene...
```
youtube-dl --all-subs --skip-download  --sub-lang <language(en,es,fr)> '<VIDEOURL/CHANNELURL/PLAYLISTURL>'
```
