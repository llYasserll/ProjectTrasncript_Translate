from moviepy import *

def cutAudio(path, init, end, output):
    
    audio = AudioFileClip(path)

    audio_cortado = audio.subclipped(init, end)

    audio_cortado.write_audiofile(output)



