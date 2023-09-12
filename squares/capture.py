import cv2
import os
import time
import numpy as np

from inputimeout import inputimeout

import data
from squares.process import get_corners

def capture(args):
    cap = cv2.VideoCapture(args.camera)

    t = time.time()

    objp = np.zeros((args.x*args.y, 3), np.float32)
    objp[:,:2] = np.mgrid[0:args.x,0:args.y].T.reshape(-1,2)

    sdata = data.Data()

    while True:
        ret, frame = cap.read()
        if time.time() - t > args.dt:
            print("attempting to find chessboard")
            t = time.time()
            corners, shape = get_corners(frame, (args.x, args.y))
        else:
            corners = None
        if corners is not None:
            frame = cv2.drawChessboardCorners(frame, (args.x, args.y), corners, True)
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
            
        if corners is not None:
            try:
                if inputimeout(prompt='save ? (y/n):', timeout=args.dt) == "y":
                    sdata.add(objp, corners, shape)
                    print("saved")
            # Catch the timeout error
            except Exception:
                sdata.add(objp, corners, shape)
                print("saved")
            
            t = time.time()

    cap.release()
    cv2.destroyAllWindows()