# Data Annotation Tool
This is YADAT Yet Another Data Annotation Tool created by me [@arkalsekar](https://www.github.com/arkalsekar)


## Approach 
Currently I am using Haarcascades to perform the face detection for latency and speed. Other detectors like Dlib HOG + SVM or even deep learning based face detector models will perform far better than Haarcascades. The main aim to provide this is to fasten the process of annotating images, and by using deep learning can cause high decrease in the speed.


## Usage 
The usage of it is quiet simple. 

1. Clone this github repository or download and extract all the files.

2. Use ``` detect_single.py ``` to detect just on single images.

3. Use ``` detect_directory.py ``` file to detect images in whole directory and saved the detected images with the bounding box into another directory.

Use the command ```python detect_directory.py -i INPUT_DIRECTORY -o OUTPUT_DIRECTORY ``` where ``` -i ``` flag is for the input directory and ```-o ``` flag is for output directory to stare the detected images with bounding boxes.


## Test 
I created a very small dataset of about 12 images of Elon Musk to test it and it worked absolutely fine. 


## Contribute
I will be adding other deep learning models to make it more robust. Also I am thinking of adding features such as Tagging or generating csv for the images detected with a particular face or something as such. If you have any thing to contribute feel free to make a Pull Request. 
If you face any trouble while using it just feel free to open Issue or connect with me on Twitter [@AbdGeeky](https://twitter.com/AbdGeeky)

