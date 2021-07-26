# virtual-finger-draw

This program detects the index finger and draws as the index finger moves around

It uses only two modules, Mediapipe and OpenCV

Mediapipe requires images in RGB format, so thats why when reading image using OpenCV
the image should be converted to RGB from BGR and then back to BGR before it is displayed
