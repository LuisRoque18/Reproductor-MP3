from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

pygame.init() #iniciamos modulo de pygame

#Botón Open Song
def abrirArchivo():
    cancion = filedialog.askopenfilename() #guardar el nombre o la cancion que queremos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.load()


def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()

def resumeSong():
    pygame.mixer.music.unpause()

def volumenMas():
    volumenLevel =  pygame.mixer.music.get_volume() +0.05
    print(volumenLevel)
    pygame.mixer.music.set_volume(volumenLevel)

def volumenMenos():
    volumenLevel =  pygame.mixer.music.get_volume() -0.05
    print(volumenLevel)
    pygame.mixer.music.set_volume(volumenLevel)

raiz=Tk()
raiz.title('Reproductor MP3')
#raiz.iconbitmap("disk-jockey.ico") #descargar la imagen #ident-colorizer
raiz.geometry("900x500")
raiz.resizable(0,0)

#Crear frame
frame = Frame(raiz, bg="#4A4A4A")
frame.pack(fill="both", expand=1)
frame.config


#Titulo Reproductor
tituloMP3 = Label(frame, text="Spotify del Bienestar", font=("Roboto",20,"bold"), bg="#4A4A4A", fg="#FBFBFB")
tituloMP3.place(relx=0.35,rely=0.1)

#Boton Open Song
botonOpenSong=Button(frame, text="Open Song", bg="#42AB49", fg="#FBFBFB", font=("Roboto",15,"bold"), width=10, height=1, command=abrirArchivo)
botonOpenSong.place(relx=0.1,rely=0.5)

#Boton Play Song
botonPlaySong=Button(frame, text="Play Song", bg="#42AB49", fg="#FBFBFB", font=("Roboto",15,"bold"), width=10, height=1, command=playSong)
botonPlaySong.place(relx=0.25,rely=0.5)

#Boton Stop Song
botonStopSong=Button(frame, text="Stop Song", bg="#e2540c", fg="#FBFBFB", font=("Roboto",15,"bold"), width=10, height=1, command=stopSong)
botonStopSong.place(relx=0.40,rely=0.5)

#Resume
botonResumeSong=Button(frame, text="Resume", bg="#ffc400", fg="#FBFBFB", font=("Roboto",15,"bold"), width=10, height=1, command=resumeSong)
botonResumeSong.place(relx=0.55,rely=0.5)

#Pause
botonPauseSong=Button(frame, text="Pause", bg="#550099", fg="#FBFBFB", font=("Roboto",15,"bold"), width=10, height=1, command=pauseSong)
botonPauseSong.place(relx=0.70,rely=0.5)

#volumen +
botonVolumenMas=Button(frame, text="Volumen +", bg="#186919", fg="#FBFBFB", font=("Roboto",15,"bold"), width=10, height=1, command=volumenMas)
botonVolumenMas.place(relx=0.5,rely=0.65)

#volumen -
botonVolumenMenos=Button(frame, text="Volumen -", bg="#FF3333", fg="#FBFBFB", font=("Roboto",15,"bold"), width=10, height=1, command=volumenMenos)
botonVolumenMenos.place(relx=0.3,rely=0.65)


raiz.mainloop()