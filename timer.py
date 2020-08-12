import pyautogui as pg
import time
import sys

def playpause(countdown):
	print('start counting down: {0} minutes'.format(countdown))
	time.sleep(countdown * 60)
	pg.press('playpause')
	print('finished counting down')

# amount of time before play/pause the song in minute
countdown = float(sys.argv[1])
playpause(countdown)