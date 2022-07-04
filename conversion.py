from pdf2image import convert_from_path
import glob
import os
import os
import subprocess
from datetime import datetime


pdf_dir = r"/Users/sonamehdizade/Desktop/Dataset/batch2/"
save_path = r'/Users/sonamehdizade/Desktop/Dataset/batch2/batch2_images/'
os.chdir(pdf_dir)

for pdf_file in glob.glob(os.path.join(pdf_dir, "*.pdf")):
    pages = convert_from_path(pdf_file, 500)
    for page in pages:
        c_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        completeName = os. path. join(save_path, "out_" + c_time + ".jpg")
        page.save(completeName, 'JPEG')
