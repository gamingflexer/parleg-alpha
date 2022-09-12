from frames import *
from model import *
from ocr import *
import numpy as np
import csv   

total_boxes = []


def sorted_nicely( l ): 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

# Take frames from video

def detection(video_path):
    no_boxes = []
    path_frames = frames_maker(video_file = video_path)
    print(path_frames,": PATH OF FRAMES\n")
    
    # ## time wait - for processing
    # for filename in os.listdir(path_frames):
    #     image = os.path.join(path_frames, filename)
        
    # checking if it is a file
    file_list = os.listdir(path_frames)
    file_list = sorted_nicely(file_list)
    
    for file1 in file_list:
        file = os.path.join(path_frames, file1)
        if os.path.isfile(file):
            
            image_open = Image.open(file)

            image_np = np.array(image_open)
            image_final,cordinates_final = detect_part(image_np)
                
            new_img = image_final.crop(translate_box(coordinates=cordinates_final))
            
            ## OCR
            ocr_outpout = ocr(np.array(new_img))
            try:
                print("\nOCR -- : ",ocr_outpout[0],"\n")
            except:
                pass
                
            with open("ocr.txt", "a") as file_object:
                if ocr_outpout != []:
                    if len(ocr_outpout[0]) > 4:
                        total_boxes.append(ocr_outpout[0])
                        box_number = len(total_boxes)
                        file_object.write(f"'BOX {box_number}'--> {ocr_outpout[0]}"+"\n")
                        file_object.write(str(ocr_outpout)+f" - {file1}"+"\n")
                        file_object.close()
                else:
                    lenght_no_boxes = len(no_boxes)
                    if lenght_no_boxes == 3 or lenght_no_boxes == 4:
                        no_boxes = []
                        file_object.write("\nNext Box Coming\n")
                        file_object.close()
                    else:
                        no_boxes.append(1)
            
            
detection("/Users/cosmos/Desktop/Projects/parleg-alpha/video/2.mp4")

def gen_frames(camera):  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            #grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            image_np = np.array(frame)
            image_final,cordinates_final = detect_part(image_np)
            new_img = image_final.crop(translate_box(coordinates=cordinates_final))

            # OCR
            try:
                ocr_outpout = ocr(np.array(new_img))
            except:
                print("no data returned")
            
            print("OCR -- : ",ocr_outpout)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            
            
        
    
    





# Append the output to a CSV

# print output & option to tune the model by user
