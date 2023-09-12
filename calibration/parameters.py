import cv2

import data

def get_parameters():
    sdata = data.Data()

    param = cv2.calibrateCamera(sdata.data["objp"], sdata.data["imp"], sdata.shape[::-1],None,None)

    return param