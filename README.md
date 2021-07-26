# virtual-finger-draw

This program detects the index finger and draws as the index finger moves around

It uses only two modules, Mediapipe and OpenCV

mediapipe read images in RGB format, so thats why when reading image using opencv
the image is converted to RGB from BGR and then back to BGR before it is displayed
