from moviepy.editor import VideoFileClip


def cutVideo(videoPath, init, end):
    # Ruta del video original
    videoPath = "C:\\Users\\Yasser\\Desktop\\Proyecto_Whisper\\video_1080p.mp4"

    # Carga el video
    video = VideoFileClip(videoPath)

    # Define el tiempo de corte (en segundos)
    init = 10800     # 10 segundos
    end = 12600        # 30 segundos

    # Recorta el video
    video_cortado = video.subclip(init, end)

    # Guarda el video cortado
    video_cortado.write_videofile("video_cortado.mp4", codec="libx264")

    # Cierra los clips para liberar recursos
    video.close()
    video_cortado.close()