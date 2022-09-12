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
    print(f"\nOrignal - {results}")
    print(f"\nFinal Code - {final}")
    
    for ocr_text in final:
        if checkAlphanumeric(ocr_text):
            pass
        else:
            final.pop(final.index(ocr_text))
        try:
            if len(ocr_text) <= 4:
                final.pop(final.index(ocr_text))
        except:
            pass
        try:
            if checkInt(ocr_text):
                final.pop(final.index(ocr_text))
        except:
            pass
        try:
            if len(int(ocr_text))<= 4:
                final.pop(final.index(ocr_text))
        except:
            pass
    return final

# check if string is alphanumeric
def checkAlphanumeric(str):
    flag_l = False
    flag_n = False
    for i in str:
       
        # if string has letter
        if i.isalpha():
            flag_l = True
 
        # if string has number
        if i.isdigit():
            flag_n = True
     
    if flag_l and flag_n:
        return True
    
# check if string is only numeric
def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False