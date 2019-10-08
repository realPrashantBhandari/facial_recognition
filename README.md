# facial_recognition
The program uses pythons facial recognition libraries to build an easy implementation of the system. The repository have 2 files.

# buildingFacesDataset.py 
This python script builds the dataset for the facial recognition system. It creates a bounding box around the persons face in the picture/video and svae the newly created face in the dataset folder. The image is save with a user defined id which will be the tag for that image.
# NOTE - Create a folder called dataset in your working directory before running this program

# face_encoding.py
This python script uses the camera attached to the sytem to take the image of the person. This image is then compared with the rest of the images in the dataset folder. If a match is found, the program returns the name of the matched image.

# Requirements
  1. install python 3.6 in your environment
  2. install open cv  using the follwoing command - pip install opencv-python
  3. install dlib by going to the following link - https://pypi.org/simple/dlib/ 
     then right click the version that meets your requirements and select copy link address
     open cmd on your system and tyle the following command - python -m pip install Past_link_here
     (the final command should look like this python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf )
     
  4. install facial recognition lib using the following command - pip install face_recognition
  
# You are done, Enjoy !!
  
