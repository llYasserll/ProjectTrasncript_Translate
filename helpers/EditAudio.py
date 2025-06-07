from moviepy import *

def cutAudio(path, init, end, output):
    # Ruta del archivo original
    audio = AudioFileClip(path)

    # Cortar desde el segundo 60 hasta el 120 (de 1:00 a 2:00)
    audio_cortado = audio.subclipped(init, end)

    # Guardar el nuevo archivo
    audio_cortado.write_audiofile(output)



