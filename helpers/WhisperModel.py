import whisper
import subprocess
from deep_translator import GoogleTranslator


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

def subtitleVideo(path_input, path_output, vf_filter):
    comando = [
        "ffmpeg",
        "-i", path_input,
        "-vf", vf_filter,
        "-c:v", "h264_nvenc",
        "-c:a", "copy",
        path_output
    ]

    print("Ejecutando comando:", " ".join(comando))

    try:
        subprocess.run(comando, check=True)
        print("✅ Video generado con subtítulos incrustados.")
    except subprocess.CalledProcessError as e:
        print("❌ Error al ejecutar ffmpeg:", e)

def traducir_srt(ruta_entrada, ruta_salida):
    traductor = GoogleTranslator(source='en', target='es')
    lineas_traducidas = []

    with open(ruta_entrada, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()

            # Evita traducir números de subtítulo y marcas de tiempo
            if linea == "" or linea.isdigit() or "-->" in linea:
                lineas_traducidas.append(linea)
            else:
                try:
                    traduccion = traductor.translate(linea)
                    if not traduccion:
                        traduccion = linea
                    lineas_traducidas.append(traduccion)
                except Exception as e:
                    print(f"Error traduciendo línea: {linea} -> {e}")
                    lineas_traducidas.append(linea)

    with open(ruta_salida, 'w', encoding='utf-8') as salida:
        for linea in lineas_traducidas:
            salida.write(linea + '\n')

    print("✅ Traducción completada. Guardado en:", ruta_salida)

