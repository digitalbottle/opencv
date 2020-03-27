# Barcode Detection

Capture of the bar code on express lists or other surfaces.

## File checklist:

Report.pdf

Codes


Inside "Codes" directory:

capture.py (running environment: python2.7+opencv2.4)

1.jpg        2.jpg        3.jpg           (3 testing pictures)

Result_1.jpg Result_2.jpg Result_3.jpg    (3 results)

Final.jpg(cut out bar code for 1.jpg)


All the figures shown in the report can be obtained by running capture.py.

Please change the jpg number in line 6 of capture.py:

	`image=cv2.imread('1.jpg',1)`

And then check for the Result.jpg and Final.jpg in the same directory afterwards.

Thank you for reading.
