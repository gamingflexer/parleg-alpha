import easyocr
import re

text_reader = easyocr.Reader(['en']) #Initialzing the ocr

def ocr(img_array):
    
    results = text_reader.readtext(img_array)
    data = []
    final = []
    for (bbox, text, prob) in results:
        data = data + [text]

    for i in data:
        m = re.search("^[a-zA-Z0-9_]*$", i)
        if m==None:
            data.remove(i)
            
    final = [i for i in data if not i.isalpha()]
    print(f"Orignal - {results}")
    print(f"Final Code - {final}")
    return final