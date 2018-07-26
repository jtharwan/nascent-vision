Hello and welcome to the solution for the image classification problem

Prequsites
This solution uses opencv and tensorflow APIs .Please install
both opencv and tensorflow before running any programs or scripts

You can find the code in the code directory 
It has two files namely resize.py and main.py 
The solution resizes the given images before training the network 
The original images are there in the bikes folder and the resized
images are in the bikes_resized folder 

I have extracted some test images to be tested against the trained 
network and they can be found under the test folder. Any image 
to be tested goes into this folder .

I have already resized all the images into a 300x300 resolution found under the bikes_resized folder by running the resize script .
However if you want you can delete all the images(not the folder)
and run the script again to generate the resized images 

To make the model and train the network against the images in the 
bikes_resized folder run the main.py script . The script would make
the model and train the network and finally tests the network for images in the test directory .

The scripts should run fine until the directories , images are in the same order as instructed above as I have given a relative path for reading and writing images in the directories. Just adhere to the convention that resized images go into the bikes_resized folder , original images into the bikes folder and testing images in the test folder .

Enjoy !

For any bugs please report to jtharwani@gmail.com 
