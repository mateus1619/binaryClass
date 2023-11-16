from model.model import Model
from config import HEADERS, COOKIES, URL, VIDEO_URL



model = Model()



model.get_modules_aulas(URL, COOKIES, HEADERS)

model.get_video(2084289, VIDEO_URL, COOKIES, HEADERS)