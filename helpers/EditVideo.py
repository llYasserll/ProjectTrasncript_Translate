from moviepy import *


def cutVideo(videoPath, init, end, name):
    # Carga el video
    video = VideoFileClip(videoPath)

    # Recorta el video
    video_cortado = video.subclipped(init, end)

    # Guarda el video cortado
    video_cortado.write_videofile(name, codec="libx264")

    # Cierra los clips para liberar recursos
    video.close()
    video_cortado.close()