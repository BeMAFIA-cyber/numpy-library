from PIL import Image 
import numpy as np
image=Image.open("random.jpg") 
image_coordinates= np.array(image) 
print(image_coordinates.shape)
print(image_coordinates.size)
print(image_coordinates.ndim)
print(image_coordinates[0,0])
print(image_coordinates.dtype)
crop = image_coordinates[0:200 , 0:200 :]
light=np.clip(crop.astype(np.int16) +50, 0, 255).astype(np.uint8)
dark=np.clip(crop.astype(np.int16) -50, 0, 255).astype(np.uint8)
grayscale= np.array([0.2126,0.7152,0.0722] )
stackthem = image_coordinates @ grayscale
stackthem = stackthem.astype('uint8')
transforthemintoimage = Image.fromarray(stackthem)
#transforthemintoimage.save('gray.jpg')
red = crop[:,:,0]
green = crop[:,:,1] 
blue = crop[:,:,2]
new_picture = (red > green) & (red >blue)
result = crop.copy()
result[~new_picture]= 0
black = np.where(stackthem<100 ,0,255)
white = np.where(stackthem >=100,255,0)
h,w,_ = image_coordinates.shape
top_left = image_coordinates[0:200,0:200,:]
bottom_right = image_coordinates[h-200:h,w-200:w , :]
centre = image_coordinates[
    h//2-100:h//2+100 ,
    w//2-100:w//2+100,
    :
]
print(centre&bottom_right&top_left)
p = np.mean(red) 
o = np.mean(green)
x = np.mean(blue)
print(p) 
print(o) 
print(x)
print(np.max(p and o and x))
def apply_filter():
 print("1 = dark" , '2=light','3=grayscale','4=new_picture', '5= black & white')
 user = int(input('enter a number'))
 if user == 1:
    dark.save('DARK.jpg')
    return apply_filter
 elif user ==2 :
    light.save('LIGHT.jpg')
    return apply_filter
 elif user ==3 :
    transforthemintoimage.save('gray.jpg')
 elif user==4:
    new_picture.save('REDFILTER.jpg')
    return apply_filter
 elif user == 5:
    black&white.save('BW.jpg')
    return apply_filter
 else:
    print('error, pls enter a valid number')
apply_filter()