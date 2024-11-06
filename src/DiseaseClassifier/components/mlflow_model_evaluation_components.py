import os
from pathlib import Path
import tensorflow as tf
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from src.DiseaseClassifier.utils.common import save_json
from src.DiseaseClassifier.config.config_manager import EvaluationMLConfig

###To be reviewed###

#What kwargs Does:
# It enables you to pass an arbitrary number of keyword arguments (arguments with names) to a function.
# Inside the function, kwargs is treated as a dictionary, where each key corresponds to the argument name and each value corresponds to the argument value.

class Evaluation:
    def __init__(self,config:EvaluationMLConfig):
        self.config=config

    #This code was copied from the keras documentation
    #This code configures TensorFlow's ImageDataGenerator objects to load and process image data from a directory for both training and validation purposes. 
    #It handles optional data augmentation for the training data and ensures that validation data is loaded WITHOUT augmentation
    
    def _valid_generator(self):
        #It sets up data generators for both training and validation datasets using the images from a specified directory.
        #The variable datagenerator_kwargs is used to pass common preprocessing settings to the ImageDataGenerator in your code, 
        #but it was not explicitly defined in the snippet. Typically, this dictionary would contain parameters that control how the images are preprocessed before being fed into the model.
        datagenerator_kwargs = dict(
            #This is used to normalize the pixel values in the images. For instance, rescale=1./255 scales pixel values from [0, 255] to [0, 1], which is common when feeding image data into neural networks.
            rescale = 1./255,
            #it will load the whole data then split
            validation_split=0.30
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

    #independent function which can be accessed from anywhere
    @staticmethod
    def load_model(path:Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    


    def evaluation(self):
        self.model=self.load_model(self.config.trained_model_path)
        self._valid_generator
        self.score=self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores={"loss":self.score[0],"accuracy":self.score[1]}
        #from common in utility
        save_json(path=Path('score.json'),data=scores)


    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        # Start a run
        with mlflow.start_run():
            #logging all parameters and metrics
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else:
                #saving the model
                mlflow.keras.log_model(self.model, "model")