import easyocr
import re


text_reader = easyocr.Reader(['en']) #Initialzing the ocr

def ocr(img_path):
    
    results = text_reader.readtext(img_path)
    data = []
    finall = []
    for (bbox, text, prob) in results:
        data = data + [text]

    for i in data:
        m = re.search("^[a-zA-Z0-9_]*$", i)
        if m==None:
            data.remove(i)
            
    final = [i for i in data if not i.isalpha()]
    return final