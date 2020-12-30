import numpy as np

def x1y1wh2xyxy(bbox):
    bbox= np.array(bbox).astype(np.float32)
    bbox[2:4]=bbox[:2]+bbox[2:4]
    return bbox.astype(np.int16)

def xyxy2x1y1wh(bbox):
    bbox= np.array(bbox).astype(np.float32)
    bbox[2:4]=bbox[2:4]-bbox[:2]
    return bbox.astype(np.int16)

def cxcywh2xyxy(bbox):
    bbox= np.array(bbox).astype(np.float32)
    bbox[:2]-=bbox[2:4]/2
    bbox[2:4]=bbox[:2]+bbox[2:4]
    return bbox.astype(np.int16)

def xyxy2cxcywh(bbox):
    bbox= np.array(bbox).astype(np.float32)
    bbox[2:4]= bbox[2:4] - bbox[:2]
    bbox[:2]= bbox[:2] + bbox[2:4]/2
    return bbox.astype(np.int16)
