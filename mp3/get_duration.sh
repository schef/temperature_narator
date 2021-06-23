#!/bin/bash
for i in ./*.mp3; do echo $i; ffmpeg -i $i 2>&1 | grep Duration; done
