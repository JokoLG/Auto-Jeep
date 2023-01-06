# NOT WORKING
# we made a new version with different code to detect the QR code
# we used a test file with the QR code saved but that wasn’t working

import glob
import cv2
import pandas as pd
import pathlib

def read_qr_code(filename):
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """
    
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return

value = read_qr_code('data/00003090-PHOTO-2022-03-19-08-31-34.jpg')

df = pd.DataFrame(columns=['filename', 'qr'])
files = glob.glob('data/*.jpg')

for file in files:

    qr = read_qr_code(file)
    row = {'filename': file, 'qr': qr}
    
    df = df.append(row, ignore_index=True)

df.head()