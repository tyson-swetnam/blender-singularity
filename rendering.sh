#!/bin/bash
BLEND="/tmp/foo.blend"
/home/${USER}/blender --background "$BLEND" \
	--use-extension 1 \
	-noaudio -nojoystick \
	-E CYCLES -t 0 \
	-P "config.py"
