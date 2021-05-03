from flask import Flask, request, Response
# from werkzeug.utils import secure_filename
from flask_restful import Resource , reqparse ,Api
import werkzeug
# from imageProcessing import imagePreProcess

app = Flask(__name__)
api = Api(app)

# TODO: add some security for calling the api 
# TODO: limit the size of it 
# TODO: add allowed extentions 


class UploadImage(Resource):
   def post(self):
     parse = reqparse.RequestParser()
     parse.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
     args = parse.parse_args()
     image_file = args['image']
     image_file.save(image_file.filename)
    #  imagePreProcess(image_file.filename)
     return "all is ok by now"

class SayHello(Resource):
  def get(self):
    return "Hello"

api.add_resource(SayHello,'/')
api.add_resource(UploadImage,'/uploadImage')
app.run(port=5000)