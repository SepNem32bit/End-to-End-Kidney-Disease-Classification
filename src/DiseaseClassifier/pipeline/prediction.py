import numpy as np
from tensorflow.keras.model import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline():
    def __init__(self,filename):
        self.filename=filename

    def predict(self):
        #load model
        model=load_model(os.path.join("artifact","training","model.h5"))
        #random image for prediction
        imagename=self.filename
        test_image=image.load_img(imagename,target_size=(224,224))
        #converting the image to array
        test_image=image.img_to_array(test_image)
        #The model expects a batch of images as input, even if it's a single image, so it requires a 4D array of shape (batch_size, height, width, channels).
        # Adding a new dimension to test_image at axis=0 turns it into a batch of one image. 
        # After expand_dims, the shape becomes (1, 224, 224, 3), which is compatible with what the model expects.
        test_image=np.expand_dims(test_image,axis=0)
        # finds the index of the highest probability along the specified axis (axis=1, which corresponds to the class dimension). 
        # The result is an array of class indices with the highest predicted probability for each image in the batch.
        result=np.argmax(model.predict(test_image),axis=1)
        print(result)
        #The output, result, will be an array of the predicted class indices for each image in the batch. Since you have only one image in the batch, 
        # result is a 1D array with a single element (e.g., [1] or [0]), and its shape is (1,)
        if result[0]==1:
            prediction="Tumor"
            return [{"image":prediction}]
        else:
            prediction="Normal"
            return [{"image":prediction}]
