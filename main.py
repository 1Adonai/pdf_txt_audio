from PDF_txt_audio import Ptxt, audio_gtts, path_orig, path_txt, path_audio
import os

print("Конвертировать pdf в txt?([y]es or [n]o):")
set_1 = input()
if set_1 == "y":
    Ptxt(path_orig, path_txt)
    print("готово")
else:
    print("отмена")


print("Конвертировать txt в mp3?([y]es or [n]o):")
set_2 = input()
if set_2 == "y":
    audio_gtts(path_txt, path_audio)
    print("готово")
else:
    print("отмена")


print("Проверить файлы в папках?([y]es or [n]o):")
set_3 = input()
if set_3 == "y":
    print("Папка txt:" + str(os.listdir(path_txt)))
    print("Папка audio:" + str(os.listdir(path_audio)))
