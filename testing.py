from helpers.WhisperModel import transcribe
from helpers.VideoDownload import downloadVideo
from helpers.VideoDownload import downloadAudio
from helpers.WhisperModel import subtitleVideo
from helpers.EditVideo import cutVideo
from helpers.EditAudio import cutAudio
from helpers.WhisperModel import traducir_srt

# descarga el audio
#downloadAudio("https://www.youtube.com/watch?v=o-fgWea75O4&t=1804s")
# descarga el video
#downloadVideo("src de youtube")
# transcribe tu audio
# Escoge true para ver como se va transcribiendo o false para no ver
### EJEMPLO DE PATH (C:\\Users\\Yasser\\Desktop\\Proyecto_Whisper\\e_commerce_part10.mp3)
#transcribe("path de tu audio.mp3", True, "path del srt.srt")

# OPCIONAL: Si es necesario traducir del ingles a espaniol usa:
#traducir_srt("srt a traducir.srt", "path de salida traducido.srt")

# Subtitula el video
# subtitleVideo(r"Path de tu video.mp4", r"Nombre de salida.mp4", r"subtitles=Path de tu srt.srt")


#TIPS
#Para videos mas amplios es recomendable cortarlos para minimizar el tiempo si vas a usar el modelo de IA large
#Tienes metodos en editvideo.py en la carpeta Helpers
# cutVideo("path de tu video a cortar.mp4", inicio, fin, nombre de salida.mp4)
# cutAudio("path de tu video.mp3", inicio, fin, nombre de salida.mp3)




