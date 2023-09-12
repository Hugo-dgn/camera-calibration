import cv2

def get_corners(img, size):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, size,None)

    # If found, add object points, image points (after refining them)
    if ret == True:

        corners2 = cv2.cornerSubPix(gray,corners, size,(-1,-1),criteria)
        return corners2