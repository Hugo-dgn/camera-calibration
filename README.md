# Camera Calibration

This repository provides tools for calibrating a camera using OpenCV. To perform camera calibration, you will need a calibration board featuring white and black squares, similar to a chessboard.

## Obtaining Calibration Points from the Calibration Board

To capture calibration points from the calibration board, use the following command:

```bash
python main.py capture -x number_of_squares_along_x -y number_of_squares_along_y --camera camera_id --dt time_delay_after_a_successful_detection
```

Place the calibration board in front of your camera, and this command will automatically save the necessary data.

## Checking Saved Data

To check the saved calibration data, run the following command:

```bash
python main.py info
```

This command will display the number of images available for calibration and the shape of these images. To ensure a successful calibration, all images must have the same shape.

## Processing Calibration Parameters

To process the captured data and obtain the camera parameters, execute the following command:

```bash
python main.py process
```

The results will be saved in a file named `solution.yml`.


## Running a Simple Demo

To visualize the camera calibration results, a simple demo is available. This demo will draw the X, Y, and Z axes on the calibration board. Execute the following command:

```bash
python main.py demo
```

## Deleting Data

If you need to delete the previously captured calibration data, whether due to its quality or to calibrate another camera, use the following command:

```bash
python main.py supp
```