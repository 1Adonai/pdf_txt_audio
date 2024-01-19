import os
from pypdf import PdfReader
from gtts import gTTS


path = os.getcwd()
path_orig = path + "/file"
path_txt = path + "/txt"
files = os.listdir(path_orig)
path_audio = path + "/audio"
files_txt = os.listdir(path_txt)


# Pdf to txt
def Ptxt(path_orig, path_txt):
    for file in files:
        pdf_file = os.path.join(path_orig, file)
        reader = PdfReader(pdf_file)
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            with open(f"{path_txt}/page_{i + 1}.txt", "w") as file:
                file.write(str(text))


# txt to audio
def audio_gtts(path_txt, path_audio):
    for file_txt in files_txt:
        txt = os.path.join(path_txt, file_txt)
        with open(txt, "r", encoding="utf-8") as f:
            text_txt = f.read()
        tts = gTTS(text_txt, lang="en")
        audio_name = file_txt[:6] + ".mp3"
        save_audio = os.path.join(path_audio, audio_name)
        tts.save(save_audio)
