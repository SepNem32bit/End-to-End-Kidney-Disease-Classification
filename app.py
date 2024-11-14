from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.DiseaseClassifier.utils.common import decodeImage
from src.DiseaseClassifier.pipeline.prediction import PredictionPipeline

####Need to reviewed

#These variables control the language and encoding used by the program, ensuring the app operates with the UTF-8 encoding standard. 
# This is particularly useful when dealing with non-ASCII characters, which are common in internationalized applications.
os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

#This line initializes a Flask application instance
app=Flask(__name__)
#allows the application to handle requests from different origins (i.e., other domains)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename="InputImage.jpg"
        self.classifier=PredictionPipeline(self.filename)

#This decorator defines a route in the Flask app for the home page ("/")
@app.route("/",methods=['GET'])
#With @cross_origin() above home, it applies CORS just to this endpoint, 
#allowing cross-origin requests from different domains when visiting this route
@cross_original()
def home():
    #means this file should exist in the templates folder within the application directory. 
    #This file likely contains the frontend for the home page.
    return render_template('index.html')
#we can get html templates from bootstrap

#GET and POST methods allow flexibility in accessing this route, though POST is commonly used for operations that change the server state, like training a model.
#The POST method is used to send data to the server to create or update a resource
#The GET method is used to retrieve data from the server.
@app.route("/train",methods=['GET','POST'])
#With @cross_origin() above home, it applies CORS just to this endpoint, 
#allowing cross-origin requests from different domains when visiting this route
@cross_original()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training Finished"


@app.route("/predict",methods=['POST'])
@cross_original()
def predictionRoute():
    #This line retrieves the image data from the JSON payload of the incoming POST request. 
    # The assumption here is that image is base64 encoded or some other format that can be decoded for processing
    image=request.json['image']
    #This line calls decodeImage, a function that presumably decodes the image data and saves it as clApp.filename ("InputImage.jpg").
    decodeImage(image,clApp.filename)
    #this line runs the prediction using the predict method of clApp.classifier, an instance of PredictionPipeline. result would contain the model's prediction output
    result=clApp.classifier.predict()
    #The prediction result is returned as a JSON response using jsonify, which makes it easy for a client (such as a frontend application) to interpret.
    return jsonify(result)


if __name__=="__main__":
    clApp=ClientApp()
    # #local host
    # app.run(host='0.0.0.0',port=8080)
    #AWS
    app.run(host='0.0.0.0',port=8080)
    # #Azure
    # app.run(host='0.0.0.0',port=88) 