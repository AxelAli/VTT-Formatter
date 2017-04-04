# VTT-Formatter
Get TXT from VTT Subtitle files. For Datasets.
Mostly for data science , chatbots and seq2seq models!


## Example Input-Output
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
Create a folder with the subs , in this case "Vsaucesubs"

You will get another folder called, in this case, "Vsaucesubstxt"

```
python VTT\ Formatter.py <SUB-DIR>
#Example
python VTT\ Formatter.py ./Vsaucesubs
```
You will also get an "allcombined.txt" file, which includes all the text in a single txt, for datasets.


### Protip
Get "youtube-dl" >  https://rg3.github.io/youtube-dl/

If your video doesnt have custom Captions.
```
youtube-dl --write-auto-sub --skip-download --sub-lang <language(en,es,fr)> '<VIDEOURL/CHANNELURL/PLAYLISTURL>'
```
or if it has custom Captions.
```
youtube-dl --all-subs --skip-download  --sub-lang <language(en,es,fr)> '<VIDEOURL/CHANNELURL/PLAYLISTURL>'
```
