from frames import *
from model import *
from ocr import *
import numpy as np
import csv   


# Take frames from video

def detection(video_path):
    path_frames = frames_maker(video_file = video_path)
    print(path_frames,": PATH OF FRAMES")
    
    ## time wait - for processing
    for filename in os.listdir(path_frames):
        image = os.path.join(path_frames, filename)
    # checking if it is a file
    if os.path.isfile(image):
        image_final,cordinates_final = detect_part(image)
            
        new_img = image_final.crop(translate_box(coordinates=cordinates_final))
        
        ## OCR
        ocr_outpout = ocr(np.array(new_img))
        print("OCR -- : ",ocr_outpout)
        
        # Append the output to a CSV
        with open(CSV_PATH, 'w', newline='') as f:
            f.writerow(ocr_outpout)
            


        
    
    





# Append the output to a CSV

# print output & option to tune the model by user
