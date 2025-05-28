import whisper
import subprocess


#model ia: tiny, base, small, medium, large, turbo
def transcribe(aimodel, path, showOutputTranscribe, nameArchive):
    model = whisper.load_model(aimodel)
    result = model.transcribe(path, verbose=showOutputTranscribe)

    def write_srt(result, output_path=nameArchive):
        def format_timestamp(seconds):
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            secs = int(seconds % 60)
            millis = int((seconds - int(seconds)) * 1000)
            return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

        with open(output_path, "w", encoding="utf-8") as f:
            for i, segment in enumerate(result["segments"], start=1):
                start = format_timestamp(segment["start"])
                end = format_timestamp(segment["end"])
                text = segment["text"].strip()
                f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

    write_srt(result)
    print(f"✅ Transcripción completa. Archivo SRT guardado como {nameArchive}")

def subtitleVideo(path1, path2, path3):
    comando = [
        "ffmpeg",
        "-i", f"{path1}",
        "-vf", path3,
        "-c:v", "h264_nvenc",
        "-c:a", "copy",
        f"{path2}"
    ]

    print("Ejecutando comando:", " ".join(comando))

    try:
        subprocess.run(comando, check=True)
        print("✅ Video generado con subtítulos incrustados.")
    except subprocess.CalledProcessError as e:
        print("❌ Error al ejecutar ffmpeg:", e)
