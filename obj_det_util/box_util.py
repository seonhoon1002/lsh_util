import numpy as np

def xywh2xyxy(bbox):
    bbox=bbox.astype(np.float64)
    bbox[2:4]=bbox[:2]+bbox[2:4]
    return bbox.astype(np.int32)

def xyxy2xywh(bbox):
    bbox=bbox.astype(np.float64)
    bbox[2:4]=bbox[2:4]-bbox[:2]
    return bbox.astype(np.int32)

def cxcywh2xyxy(bbox):
    bbox[:2]-=bbox[2:4]/2
    bbox[2:4]=bbox[:2]+bbox[2:4]
    return bbox.astype(np.int32)

def xyxy2cxcywh(bbox):
    bbox[2:4]= bbox[2:4] - bbox[:2]
    bbox[:2]= bbox[:2] + bbox[2:4]/2
    return bbox.astype(np.int32)
