import pygame.mixer as pgm

# Initialize the mixer
pgm.init()

# Load the audio file
pgm.music.load('Music_files/namokar.mp3')

# Play the audio file
pgm.music.play()

# Keep the program running to allow the audio to play
while pgm.music.get_busy():
    pass
