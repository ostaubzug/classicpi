from pygame import mixer
mixer.init()
import os
import random

#musik auf raspi kopieren via usb stick
#zufallsgenerator um verschiedene Songs aus dem Ordner auszuwählen

def randomfile():
    
    file_name = random.choice(os.listdir("/home/pi/Music")) #change dir name to whatever
    return file_name



def play(musicfile):
    print("hello")

    mixer.music.load("/home/pi/Music/01 Tchaikovsky_ Swan Lake - Scene 1.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()






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