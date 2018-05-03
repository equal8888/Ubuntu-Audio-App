#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

import os
import subprocess

# Bit depth Button functions
def select_bitdepth_16():
    subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s16le" /etc/pulse/daemon.conf', shell=True)
def select_bitdepth_24():
    subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s24le" /etc/pulse/daemon.conf', shell=True)
def select_bitdepth_32():
    subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s32le" /etc/pulse/daemon.conf', shell=True)

# primary sample rate button functions
def select_prisamplerate_44100():
    subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 44100" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_48000():
    subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 48000" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_88200():
    subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 88200" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_96000():
    subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_192000():
    subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 192000" /etc/pulse/daemon.conf', shell=True)

# alternative sample rate button functions
def select_altsamplerate_44100():
    subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 44100" /etc/pulse/daemon.conf', shell=True)
def select_altsamplerate_48000():
    subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 48000" /etc/pulse/daemon.conf', shell=True)
def select_altsamplerate_88200():
    subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 88200" /etc/pulse/daemon.conf', shell=True)
def select_altsamplerate_96000():
    subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True)
def select_altsamplerate_192000():
    subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 192000" /etc/pulse/daemon.conf', shell=True)

# resample methods
def select_prisamplerate_default():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c ; resample-method = speex-float-1" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_optimised():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-float-10" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_srcsincmediumquality():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-medium-quality" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_srcsincbestquality():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-best-quality" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_srczeroorderhold():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-zero-order-hold" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_srclinear():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-linear" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_trivial():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = trivial" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_speexfloatN():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-float-N" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_speexfixedN():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-fixed-N" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_ffmpeg():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = ffmpeg" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_soxrmq():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-mq" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_soxrhq():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-hq" /etc/pulse/daemon.conf', shell=True)
def select_prisamplerate_soxrvhq():
    subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-vhq" /etc/pulse/daemon.conf', shell=True)

# default button for now
def defaultpulsebutton():
    subprocess.call('cd ~ && ./Documents/gitfix/Ubuntu-Audio-App/default-settings-pulseaudio.sh', shell=True)

# alsa button for now
def alsabutton():
    subprocess.call('cd ~ && ./Documents/gitfix/Ubuntu-Audio-App/alsa-settings.sh', shell=True)

# kill pulse
def killpulse():
    subprocess.call('pulsespawn=$(grep "autospawn" /etc/pulse/client.conf) && sudo sed -i "/${pulsespawn}/ c autospawn = no" /etc/pulse/client.conf && pulseaudio --kill', shell=True)

# restart pulse
def restartpulse():
    subprocess.call('pulsespawn=$(grep "autospawn" /etc/pulse/client.conf) && sudo sed -i "/${pulsespawn}/ c ; autospawn = yes" /etc/pulse/client.conf && pulseaudio --kill ; pulseaudio --start', shell=True)

# ok button for now
def Confirm():
    subprocess.call('sudo alsa force-reload', shell=True)

# samplerate button for now
def showsamplerate():
        subprocess.call('currentbitrate1=$(pacmd list-sinks | grep sample) && notify-send "$currentbitrate1"', shell=True)

# test calling
def donothing():
   x = 0
# Render main  window
def main():
    root = tk.Tk()
    root.title("Audio Powertool")
    root.minsize(width=730, height=258)
#    root.maxsize(width=740, height=225)
    root.geometry("715x220")

    # define var's
    var = IntVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()

    # gives weight to the cells in the grid
    rows = 0
    while rows < 50:
        root.rowconfigure(rows, weight=1)
        root.columnconfigure(rows, weight=1)
        rows += 1

    # Defines and places the notebook widget
    nb = ttk.Notebook(root)
    nb.grid(row=1, column=1, columnspan=50, rowspan=49, sticky='NESW')

    # Adds tab 1 of the notebook
    page1 = ttk.Frame(nb)
    nb.add(page1, text='PulseAudio')

    # page1 frame
    frame99 = tkinter.LabelFrame(page1)
    frame99.grid(row=1, column=2, sticky='NESW', padx=5, pady=5)

    # Adds tab 2 of the notebook
    page2 = ttk.Frame(nb)
    nb.add(page2, text='ALSA')

    # Menubar
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    prefmenu = Menu(menubar, tearoff=0)
#    prefmenu.add_command(label="Settings", command=donothing)
    menubar.add_cascade(label="Preferences", menu=prefmenu)

    helpmenu = Menu(menubar, tearoff=0)
#    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    # PAGE1 Maincode

    # Blue frame
    frame97 = tkinter.LabelFrame(frame99)
    frame97.grid(row=1, column=2, columnspan=7, rowspan=5, sticky='NESW')

    background_label = Label(frame97, bg="blue")
    background_label.place(width=800, height=100)

    label = Label(frame99, text=" Set bit depth ")
    label.grid(row=1, column=1, padx=1, pady=5)

    select_bitdepth_1=Radiobutton(frame99, command=select_bitdepth_16, text='16 Bit', variable=var, value=16, width=9)
    select_bitdepth_1.grid(row=2, column=1, sticky='N')

    select_bitdepth_2=Radiobutton(frame99, command=select_bitdepth_24, text='24 Bit', variable=var, value=24, width=9)
    select_bitdepth_2.grid(row=3, column=1, sticky='N')

    select_bitdepth_3=Radiobutton(frame99, command=select_bitdepth_32, text='32 Bit', variable=var, value=32, width=9)
    select_bitdepth_3.grid(row=4, column=1, sticky='N')

    # Separator1
    ttk.Separator(frame99).grid(row=5, column=1, columnspan=11, sticky="ew")

    # Set primary sample rate
    label = Label(frame99, text="Primary Sample rate")
    label.grid(row=6, column=1, columnspan = 2)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_44100, text='44,100 Hz', variable=var1, value=14100, width=9)
    select_prisamplerate_1.grid(row=6, column=3)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_48000, text='48,000 Hz', variable=var1, value=48000, width=9)
    select_prisamplerate_1.grid(row=6, column=4)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_88200, text='88,200 Hz', variable=var1, value=88200, width=9)
    select_prisamplerate_1.grid(row=6, column=5)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_96000, text='96,000 Hz', variable=var1, value=96000, width=9)
    select_prisamplerate_1.grid(row=6, column=6)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_192000, text='192,000 Hz', variable=var1, value=192000, width=9)
    select_prisamplerate_1.grid(row=6, column=7)

    # Set Secondary sample rate
    label = Label(frame99, text="Alternative Sample rate")
    label.grid(row=7, column=1, columnspan = 2)

    select_secsamplerate_1=Radiobutton(frame99, text='44,100 Hz', variable=var2, command=select_altsamplerate_44100, value=14100, width=9)
    select_secsamplerate_1.grid(row=7, column=3)

    select_secsamplerate_1=Radiobutton(frame99, text='48,000 Hz', variable=var2, command=select_altsamplerate_48000, value=48000, width=9)
    select_secsamplerate_1.grid(row=7, column=4)

    select_secsamplerate_1=Radiobutton(frame99, text='88,200 Hz', variable=var2, command=select_altsamplerate_88200, value=88200, width=9)
    select_secsamplerate_1.grid(row=7, column=5)

    select_secsamplerate_1=Radiobutton(frame99, text='96,000 Hz', variable=var2, command=select_altsamplerate_96000, value=96000, width=9)
    select_secsamplerate_1.grid(row=7, column=6)

    select_secsamplerate_1=Radiobutton(frame99, text='192,000 Hz', variable=var2, command=select_altsamplerate_192000, value=192000, width=9)
    select_secsamplerate_1.grid(row=7, column=7)

    # Separator2
    ttk.Separator(frame99).grid(row=8, column=1, columnspan=11, sticky="ew")

    # Set Secondary sample rate
    label = Label(frame99, text="Resample method")
    label.grid(row=9, column=1, columnspan = 2)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='default', variable=var3, command=select_prisamplerate_default, value=1, width=12)
    select_secsamplerate_1.grid(row=9, column=3)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='fast', variable=var3, command=select_prisamplerate_optimised, value=2, width=12)
    select_secsamplerate_1.grid(row=9, column=4)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='medium', variable=var3, command=select_prisamplerate_srcsincmediumquality, value=3, width=12)
    select_secsamplerate_1.grid(row=9, column=5)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='best', variable=var3, command=select_prisamplerate_srcsincbestquality, value=4, width=12)
    select_secsamplerate_1.grid(row=9, column=6)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='zero-orderhold', variable=var3, command=select_prisamplerate_srczeroorderhold, value=5, width=12)
    select_secsamplerate_1.grid(row=9, column=7)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='src-linear', variable=var3, command=select_prisamplerate_srclinear, value=6, width=12)
    select_secsamplerate_1.grid(row=10, column=5)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='trivial', variable=var3, command=select_prisamplerate_trivial, value=7, width=12)
    select_secsamplerate_1.grid(row=10, column=1)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='speex-float-N', variable=var3, command=select_prisamplerate_speexfloatN, value=8, width=12)
    select_secsamplerate_1.grid(row=10, column=2)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='speex-fixed-N', variable=var3, command=select_prisamplerate_speexfixedN, value=9, width=12)
    select_secsamplerate_1.grid(row=10, column=3)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='ffmpeg', variable=var3, command=select_prisamplerate_ffmpeg, value=10, width=12)
    select_secsamplerate_1.grid(row=10, column=4)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='soxr-hq', variable=var3, command=select_prisamplerate_soxrhq, value=12, width=12)
    select_secsamplerate_1.grid(row=10, column=6)

    select_secsamplerate_1=Radiobutton(frame99, indicatoron=0, text='soxr-vhq', variable=var3, command=select_prisamplerate_soxrvhq, value=13, width=12)
    select_secsamplerate_1.grid(row=10, column=7)

    # Separator3 usb1button
    ttk.Separator(frame99).grid(row=11, column=1, columnspan=11, sticky="ew")

    frame98 = tkinter.LabelFrame(frame99, borderwidth=3)
    frame98.grid(row=11, column=6, columnspan=2, sticky='NEW', \
                      padx=5, pady=5)

#   default button for now
    apply_btn=Button(frame99, text='Default Pulseaudio settings', command=defaultpulsebutton )
    apply_btn.grid(row=12, column=1, columnspan=2, padx=5, pady=5)

#   restart pulseaudio
    apply_btn=Button(frame99, text='Apply / Restart pulseaudio', command=restartpulse )
    apply_btn.grid(row=12, column=6, columnspan=4, padx=5, pady=5)

#   samplerate button for now (row=1, column=1)
    apply_btn=Button(frame99, text='PulseAudio sample rate', command=showsamplerate )
    apply_btn.grid(row=1, column=6, sticky='E', rowspan=2, columnspan=2, padx=3, pady=2)

# PAGE2 Maincode


    root.mainloop()

if __name__ == '__main__':
    main()
