import cv2
import yaml
import numpy as np

from squares.process import get_corners

def draw(img, corners, imgpts):
    corners = corners.astype(int)
    imgpts = imgpts.astype(int)
    corner = tuple(corners[0].ravel())
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img

def draw_coordinate(args):
    with open('solution.yml') as f:
        param = yaml.load(f, Loader=yaml.FullLoader)[0]

    mtx = np.array(param["mtx"])
    dist = np.array(param["dist"])

    cap = cv2.VideoCapture(args.camera)

    objp = np.zeros((args.x*args.y, 3), np.float32)
    objp[:,:2] = np.mgrid[0:args.x,0:args.y].T.reshape(-1,2)
    objp *= args.lenght

    axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)

    while True:
        ret, frame = cap.read()
        corners, shape = get_corners(frame, (args.x, args.y))

        if corners is not None:

            # Find the rotation and translation vectors.
            retval, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)

            # project 3D points to image plane
            imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)

            frame = draw(frame,corners,imgpts)
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break