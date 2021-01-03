from pygame import mixer
import os
import random

mixer.init()
#musik auf raspi kopieren via usb stick
#zufallsgenerator um verschiedene Songs aus dem Ordner auszuwählen

def randomfile():
    
    file_name = random.choice(os.listdir("/home/pi/Music")) #change dir name to whatever
    return file_name



def play():
    global musicfile
    
    musicfile = randomfile()
    mixer.music.load("/home/pi/Music/" + musicfile)
    mixer.music.set_volume(0.6)
    mixer.music.play()
    shuffle()
    

def shuffle():
    while True:
        print("Press 'p' to pause")
        print("Press 'r' to resume")
        print("Press 'n' for a new song")
        print("Press 'l' to initiate loop playing")
        ch = input("['p','r']>>>")
        if ch == "p":
            mixer.music.pause()
        elif ch == "r":
            mixer.music.unpause()
        elif ch == "n":
            play()
        elif ch == "l":
            loop()
        
def loop():
    while True:
        print("Press 'p' to pause")
        print("Press 'r' to resume")
        print("Press 'n' for a new song")
        print("Press 's' to initiate shuffle play ")
        ch = input("['p','r']>>>")
        if ch == "p":
            mixer.music.pause()
        elif ch == "r":
            mixer.music.unpause()
        elif ch == "n":
            mixer.music.load("/home/pi/Music/" + musicfile)
            mixer.music.set_volume(0.6)
            mixer.music.play()
            loop()

        elif ch == "s":
            shuffle()


play()



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