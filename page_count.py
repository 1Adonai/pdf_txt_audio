import os
from pdfminer.hight_level import extract_text


path = os.getcwd()
path_orig = path + "/file"
path_mod = path + "/result"
files = os.listdir(path_orig)
for file in files:
    f = os.path.join(path_orig, file)
    pdf = pdfplumber.open(f)

    pages = pdf.pages

    for page in pages:
        page_path = os.path.join(path_mod, f"page_{page.page_number}.pdf")
        with open(page_path, "wb") as f:
            page.save(f)
