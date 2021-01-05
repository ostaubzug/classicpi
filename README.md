This is an attempt to build a minimalistic music player with Raspberry Pi and Python, designed for minimal distraction. I'm mostly using it to play classical music while studying.

It knows three commands (skip, pause and loop)

PICTURE gg

Load your music onto the raspberry pi and adjust the PATH to your music in the randomfile function.

```python
file_name = random.choice(os.listdir("your path")
```

Next you need to make sure that the raspberry loads the python script automaticly after each startup. There are several ways to accomplish this, I've used cron:

```
crontab -e
```

Additionally I've had to uncomment

```
hdmi_force_hotplug=1
```

in the config.txt file to make sure it worked properly.

```
@reboot python /home/pi/yourpath/pythonmusicplayer.py
```

Depending on what GPIO Pins you want to use you need to change them as well. Here is a picture of my Breadboard.

I've added some CAD Files as well so you can print your own buttons for this.

I've added also a USB Soundcard to enhance the quite poor audio quality of the raspberry
