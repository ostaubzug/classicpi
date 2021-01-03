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
    for i in range(5):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.2)

# mixer.music.get_busy()
# to check if the music is playing implementation later when working with the gpio pins
def randomfile():    
    file_name = random.choice(os.listdir("/home/pi/Music")) #change dir name to whatever
    return file_name


def play():
    global musicfile
    
    musicfile = randomfile()
    mixer.music.load("/home/pi/Music/" + musicfile)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    
def playloop():
    global musicfile
    mixer.music.load("/home/pi/Music/" + musicfile)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    

    

def shuffle():
    loop = False
    pause = False
    while True:
        if GPIO.input(13) == 1:
            if loop == True:
                loop = False
                GPIO.output(23, GPIO.LOW)
                time.sleep(0.5)
            elif loop == False:
                loop = True
                GPIO.output(23, GPIO.HIGH)
                time.sleep(0.5)            
            
        elif GPIO.input(19) == 1:
            if loop == True:
                playloop()
                time.sleep(0.5)
            elif loop == False:
                play()
                time.sleep(0.5)

        elif GPIO.input(26) == 1 and pause == False:
            mixer.music.pause()
            pause = True
            time.sleep(0.5)           
        elif GPIO.input(26) == 1 and pause == True:
            mixer.music.unpause()
            pause = False
            time.sleep(0.5)
        elif mixer.music.get_busy() == False:
            play()

        
blinkstartup()
play()
shuffle()



# while True:
#     print("Press 'p' to pause")
#     print("Press 'r' to resume")
#     print("Press 'v' set volume")
#     print("Press 'e' to exit")
#     ch = input("['p','r','v','e']>>>")
#     if ch == "p":
#         mixer.music.pause()
#     elif ch == "r":
#         mixer.music.unpause()
#     elif ch == "v":
#         v = float(input("Enter volume(0 to 1): "))
#         mixer.music.set_volume(v)
#     elif ch == "e":
#         mixer.music.stop()
#         break 