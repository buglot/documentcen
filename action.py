import pypdfium2 as pdfium
import os
import log
import uuid
import cv2
import img2pdf
from ultralytics import YOLO
import tkinter as tk
from PIL import Image
class Pdf2Img:
    def __init__(self,filename,log:log.LOG):
        self.pdf = pdfium.PdfDocument(filename)
        self.log = log
        self.folder = ""
    def size(self)->int:
        return len(self.pdf)
    def run(self):
        self.log.add("เริ่มแตกไฟล์เป็นภาพ\n")
        self.folder = str(uuid.uuid1())
        if os.path.exists(self.folder)==False:
            os.mkdir(self.folder)
        for i in range(self.size()):
            page = self.pdf[i]
            self.log.add(f"แตกเป็นภาพ{i+1:15d}\\{self.size()}\n")
            image = page.render(scale=4).to_pil()
            image.save(os.path.join(self.folder,f"output_{i:04d}.jpg"))
    def path(self)->str:
        return self.folder

class predict:
    def __init__(self,folder:str,val:float,model:str,log:log.LOG):
        self.model = YOLO(os.path.join("model",model))
        self.fl = folder
        self.val = val
        self.log = log
    def run(self):
        self.log.add(f"เริ่มเดาภาพที่จะปิด\n")
        listimg = os.listdir(self.fl)
        size = len(listimg)
        class_names = ['answer']
        class_colors = {
                'answer': (255, 255, 255),  # Blue
        }
        self.folder = str(uuid.uuid1())
        if os.path.exists(self.folder)==False:
            os.mkdir(self.folder)
        for i,file in enumerate(listimg):

            original_img = cv2.imread(os.path.join(self.fl,file))
            original_h, original_w = original_img.shape[:2]
            resized_img = cv2.resize(original_img, (640, 640))
            self.log.add(f"กำลังcensoredภาพ {i+1:15d}\\{size}\n")
            results = self.model.predict(resized_img)
            for result in results:
                for box in result.boxes:
                    confidence = float(box.conf[0])  # Get confidence score
                    if confidence >= self.val:
                        x1, y1, x2, y2 = box.xyxy[0]  # Bounding box (on resized image)
                        
                        # Scale bounding boxes back to original image size
                        x1 = int(x1 * (original_w / 640))
                        y1 = int(y1 * (original_h / 640))
                        x2 = int(x2 * (original_w / 640))
                        y2 = int(y2 * (original_h / 640))

                        # Get class ID and confidence
                        class_id = int(box.cls[0])


                        # Get class name
                        class_name = class_names[class_id]

                        # Get color for the class
                        color = class_colors.get(class_name, (255, 255, 255))  

                        # Draw bounding box
                        cv2.rectangle(original_img, (x1, y1), (x2, y2), color, -1)
            original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
            cv2.imwrite(os.path.join(self.folder,file),original_img_rgb)

    def path(self)->str:
        return self.folder

class savepdf:
    def __init__(self,folder,savefolder,log:log.LOG):
        self.fl = folder
        self.savefolder = savefolder
        self.log = log
    def run(self): 
        self.folder = str(uuid.uuid1())
        if os.path.exists(self.folder)==False:
            os.mkdir(self.folder)
        listimg = os.listdir(self.fl)
        self.log.add("เริ่มบีบอัดไฟล์\n")
        pdf = pdfium.PdfDocument.new()
        size = len(listimg)

        image_paths = [os.path.join(self.fl, img_path) for img_path in listimg]
        output_pdf = os.path.join(self.savefolder)
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(image_paths))

        self.log.add(f"PDF created successfully: {output_pdf}\n")
    def path(self)->str:
        return self.folder
    

