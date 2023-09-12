import cv2
import os
import time
import numpy as np

from squares.process import get_corners

def capture(args):
    cap = cv2.VideoCapture(args.camera)

    t = time.time()

    objp = np.zeros((args.x*7,args.y), np.float32)
    objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

    while True:
        ret, frame = cap.read()
        if time.time() - t > args.dt:
            print("attempting to find chessboard")
            t = time.time()
            corners = get_corners(frame, (args.x, args.y))
        else:
            corners = None
        if corners is not None:
            frame = cv2.drawChessboardCorners(frame, (args.x, args.y), corners, True)
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
            
        if corners is not None:
            if input("save? (y/n)") == "y":
                if not os.path.exists("data"):
                    os.makedirs("data")
                cv2.imwrite("data/chessboard.png", frame)
            t = time.time()

    cap.release()
    cv2.destroyAllWindows()