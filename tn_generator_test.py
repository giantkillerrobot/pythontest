# importing Image class from PIL package  
from PIL import Image 
   
# creating a object  
image = Image.open(r"firstimage.jpg") 
MAX_SIZE = (100, 100) 
  
image.thumbnail(MAX_SIZE) 
  
# creating thumbnail 
image.save('pythonthumb.png') 
image.show() 