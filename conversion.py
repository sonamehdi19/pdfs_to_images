from pdf2image import convert_from_path
import glob
import os
import os
import subprocess
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input directory', required=True)
parser.add_argument('--dest', help='destination directory', required=True)
args = parser.parse_args()

#pdf_dir = r"/Users/sonamehdizade/Desktop/Dataset/batch7/"
#save_path = r'/Users/sonamehdizade/Desktop/Dataset/batch7/batch7_images/'
# os.chdir(pdf_dir)

for pdf_file in glob.glob(os.path.join(args.input, "*.pdf")):
    pages = convert_from_path(pdf_file, 500)
    for page in pages:
        c_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        completeName = os. path. join(args.dest, "out_" + c_time + ".jpg")
        page.save(completeName, 'JPEG')
