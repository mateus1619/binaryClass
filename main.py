
from model.model import Model
from quart import Quart, render_template

model = Model()
app = Quart(__name__)

@app.route("/")
async def home():
    items = await model.get_modules()
    return await render_template('home.htm', items=items)

@app.route("/videos/<id>")
async def get_video(id):
    return await model.get_video(id)







if __name__ == '__main__':
    app.run()