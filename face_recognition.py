"""
face detection using face_recognition library
Sys req: CMake, dlib, face_recogntion, PIL
"""
def faceDetect(pics):
    for picture in pics:
        image = face_recognition.load_image_file(picture)

        # Find all the faces in the image using a pre-trained convolutional neural network.
        # This method is more accurate than the default HOG model, but it's slower
        # unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
        # this will use GPU acceleration and perform well.
        face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
        
        flag = False
        if (len(face_locations)>0):
            flag = True
        
        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            print(
                "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,
                                                                                                      right))

            # You can access the actual face itself like this:
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            pil_image.show()
            
            
def detectAndFlagSingle(pic):
    image = face_recognition.load_image_file(pic)
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
        
        flag = False
        if (len(face_locations)>0):
            flag = True
            
    return flag
    
    
shop_images = glob('/Users/gaut/Desktop/all_images/*.jpg')

yCount = 1
nCount = 1
for pic in shop_images:
    if detectAndFlag(pic):
        shutil.move(pic, '/Users/gaut/Desktop/projects/.../faceDetection/withFace/{}.jpg'.format(yCount))
        yCount+=1
    else:
        shutil.move(pic, '/Users/gaut/Desktop/projects/.../faceDetection/noFace/{}.jpg'.format(nCount))
        nCount+=1
   

