import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from pathlib import Path

from src.DiseaseClassifier.entity.config_entity import TrainingMLConfig

#What kwargs Does:
# It enables you to pass an arbitrary number of keyword arguments (arguments with names) to a function.
# Inside the function, kwargs is treated as a dictionary, where each key corresponds to the argument name and each value corresponds to the argument value.

class Training:
    #look at the parameters
    def __init__(self,config:TrainingMLConfig):
        self.config=config

    def get_base_model(self):
        self.model=tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    #This code was copied from the keras documentation
    #This code configures TensorFlow's ImageDataGenerator objects to load and process image data from a directory for both training and validation purposes. 
    #It handles optional data augmentation for the training data and ensures that validation data is loaded without augmentation
    
    def train_valid_generator(self):
        #It sets up data generators for both training and validation datasets using the images from a specified directory.
        #The variable datagenerator_kwargs is used to pass common preprocessing settings to the ImageDataGenerator in your code, 
        #but it was not explicitly defined in the snippet. Typically, this dictionary would contain parameters that control how the images are preprocessed before being fed into the model.
        datagenerator_kwargs = dict(
            #This is used to normalize the pixel values in the images. For instance, rescale=1./255 scales pixel values from [0, 255] to [0, 1], which is common when feeding image data into neural networks.
            rescale = 1./255,
            validation_split=0.20
        )

        #all properties for the dataflow
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            #Chooses how to resize the images
            interpolation="bilinear"
        )
        #The ImageDataGenerator is initialized using datagenerator_kwargs, which is presumably a dictionary containing common preprocessing steps
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        #generating validation data
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        #If augmentation is enabled (self.config.params_is_augmentation is True), a new ImageDataGenerator is created with several data augmentation techniques applied
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                #Randomly shifts images horizontally and vertically by 20%.
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            #it is used again to load the training data from the same directory as the validation set
            train_datagenerator = valid_datagenerator

        #generating training data
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )




    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)


    def train(self):
        #This divides and calculates the number of batches (or "steps") in one epoch. It's computed as the total number of training samples divided by the batch size of self.train_generator.
        self.step_per_epoch=self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps=self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.step_per_epoch,
            #Defines how many batches of validation data will be processed after each epoch.
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )
        self.save_model(path=self.config.trained_model_path,model=self.model)