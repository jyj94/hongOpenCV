import numpy as np
import cv2

def print_matInfo(name, image):
    if image.dtype == 'uint8': mat_type = 'CV_8U'
    elif image.dtype == 'int8': mat_type = 'CV_8S'
    elif image.dtype == 'uint16': mat_type = 'CV_16U'
    elif image.dtype == 'int16': mat_type = 'CV_16S'
    elif image.dtype == 'float32': mat_type = 'CV_32F'
    elif image.dtype == 'float64': mat_type = 'CV_64F'
    nchannel = 3 if image.ndim == 3 else 1
    
    print(f'{name},: {image.dtype}, channel({nchannel}) -> mat_type{mat_type}')