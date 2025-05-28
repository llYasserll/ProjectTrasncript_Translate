from helpers.WhisperModel import transcribe
from helpers.VideoDownload import downloadVideoWithoutAudio
from helpers.VideoDownload import downloadAudio
from helpers.WhisperModel import subtitleVideo

# descarga el audio
downloadAudio("tu url")
# descarga el video sin audio
downloadVideoWithoutAudio("tu url")
# transcribe tu audio
# Escoge true para ver como se va transcribiendo o false para no ver
transcribe("Tu modelo de IA","tu ruta absoluta de mp3", True, "nombre de tu archivo SRT")

# Subtitula el video
subtitleVideo("ruta absoluta de tu archivo mp4", "ruta absoluta de ", r"subtitles=C\\:path del srt generado")

#TIPS
#Para videos mas amplios es recomendable cortarlos para minimizar el tiempo si vas a usar el modelo de IA large
#Tienes metodos en editvideo.py en la carpeta Helpers


