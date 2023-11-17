from flask import Flask
from model.model import Model
from config import HEADERS, COOKIES, URL, VIDEO_URL

app = Flask(__name__)
model = Model()


@app.route('/get/modules-aulas')
def get_modules_aulas():
   return model.get_modules_aulas(URL, COOKIES, HEADERS)



@app.route('/get/videos/<id>')
def get_video(id):
    return model.get_video(id, VIDEO_URL, COOKIES, HEADERS)








if __name__ == '__main__':
    app.run()