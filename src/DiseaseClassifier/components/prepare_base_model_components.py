import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path

from src.DiseaseClassifier.entity.config_entity import PrepareBaseMLConfig

#downloading the pre-trained vgg16
#In PrepareBaseModel, self.config is an instance of PrepareBaseMLConfig, which contains the model parameters such as params_image_size, params_weights, etc.
class PrepareBaseModel:
    #look at the parameters
    def __init__(self,config:PrepareBaseMLConfig):
        self.config=config

    def get_base_model(self):
        self.model=tf.keras.applications.vgg16.VGG16(
            #The reason you're using self.config is because you are passing an instance of PrepareBaseMLConfig into the PrepareBaseModel class. 
            # This configuration object contains all the necessary parameters that were extracted from the params.yaml file (e.g., IMAGE_SIZE, WEIGHTS, INCLUDE_TOP).
            # If you wanted to use self.params, you'd need to ensure that params is accessible in this context. 
            # But since self.config contains the params from the configuration, it's appropriate to use self.config.params_image_size etc., within the PrepareBaseModel class.
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )
        self.save_model(path=self.config.base_model_path,model=self.model)
    
    #Why Use @staticmethod?
    # No Need for self: If the method doesn't need to access or modify the instance's attributes or methods, it’s better to make it a static method.
    # Grouping Related Functions: Sometimes, it’s just about logically grouping functions that belong together. Even if the function doesn't use instance variables, it might conceptually belong to the class.

    #This method keep some layers of the pre-trained model
    @staticmethod
    def prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till>0):
            #This line freezes all layers except the last freeze_till layers. Here's how it works:
            # The slice model.layers[:-freeze_till] grabs all layers except the last freeze_till layers (that's why you have the negative sign).
            # For example, if freeze_till = 5, this means the last 5 layers will remain trainable, while the rest will be frozen.
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        #The convolutional layers in models like VGG16 output a 3D tensor (height, width, and channels), but fully connected layers (like Dense) expect a 1D vector. 
        #The Flatten layer is used to reshape that 3D tensor into a single vector, which can be fed into a Dense layer.
        flatten_in=tf.keras.layers.Flatten()(model.output)
        #creating the custom dense layer which we didn't freeze
        prediction=tf.keras.layers.Dense(
            units=classes,
            activation='softmax'
        )(flatten_in)

        full_model=tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )
        # Initialize optimizer after creating the new model
        optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
        
        full_model.compile(
            optimizer=optimizer,
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )

        full_model.summary()
        for layer in full_model.layers:
            print(f"{layer.name}: {layer.trainable}")
        return full_model
    
    def update_base_model(self):
        self.full_model=self.prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)
    