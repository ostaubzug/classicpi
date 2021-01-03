from pygame import mixer
import os
import random
import RPi.GPIO as GPIO
import time

mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(23, GPIO.OUT)

def blinkstartup():
    for i in range(3):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.1)

# mixer.music.get_busy()
# to check if the music is playing implementation later when working with the gpio pins
def randomfile():    
    file_name = random.choice(os.listdir("/home/pi/Music")) #change dir name to whatever
    return file_name


def play():
    global musicfile
    
    musicfile = randomfile()
    mixer.music.load("/home/pi/Music/" + musicfile)
    mixer.music.set_volume(0.9)
    mixer.music.play()
    
def playloop():
    global musicfile
    mixer.music.load("/home/pi/Music/" + musicfile)
    mixer.music.set_volume(0.9)
    mixer.music.play()
    

    

def shuffle():
    loop = False
    pause = False
    while True:
        if GPIO.input(13) == 1:
            #loop
            if loop == True:
                loop = False
                GPIO.output(23, GPIO.LOW)
                time.sleep(0.5)
            elif loop == False:
                loop = True
                GPIO.output(23, GPIO.HIGH)
                time.sleep(0.5)            
            
        elif GPIO.input(19) == 1:
            # next song
            if loop == True:
                GPIO.output(23, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(23, GPIO.HIGH)
                playloop()
                time.sleep(0.3)
            elif loop == False:
                GPIO.output(23, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(23, GPIO.LOW)
                play()
                time.sleep(0.3)
                
        elif GPIO.input(26) == 1 and pause == False:
            #start stop
            mixer.music.pause()
            GPIO.output(23, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(23, GPIO.LOW)
            pause = True
            time.sleep(0.3)
            
        elif GPIO.input(26) == 1 and pause == True:
            mixer.music.unpause()
            GPIO.output(23, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(23, GPIO.LOW)
            pause = False
            time.sleep(0.3)
            
        elif mixer.music.get_busy() == False:
            if loop == False:
                play()
            if loop == True:
                playloop()

        
blinkstartup()
play()
shuffle()

