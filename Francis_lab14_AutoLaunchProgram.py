# IT 280 – Lab #14: Program Launch Instructions by Francis @ 2022

#this script only works on linux and MacOS, *WILL NOT work on windows.
#need to install modules by running "pip3 install playsound", "pip3 install pillow", and "pip3 install PyObjC"

from PIL import Image
from playsound import playsound

print('Input the image name. *might need to include the full path if it is not in the current directory.' )
target = input()
with Image.open(target) as img:
    img.show()

print('Input the audio name. *might need to include the full path if it is not in the current directory.' )
target2 = input()
playsound(target2)
~                              
