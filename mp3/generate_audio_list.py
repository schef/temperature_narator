#!/usb/bin/env python3
from mutagen.mp3 import MP3

index = 1
temperature = 0

for i in range(1000, 1126):
    filename = "./%s.mp3" % (i)
    audio = MP3(filename)
    audio_len_ms = int(audio.info.length * 1000)
    string = "    %d: Word(%d, %d), #%s" % (temperature, index, audio_len_ms, filename)
    index += 1
    temperature += 1
    print(string)

temperature = -1
for i in range(2001, 2016):
    filename = "./%s.mp3" % (i)
    audio = MP3(filename)
    audio_len_ms = int(audio.info.length * 1000)
    string = "    %d: Word(%d, %d), #%s" % (temperature, index, audio_len_ms, filename)
    index += 1
    temperature -= 1
    print(string)