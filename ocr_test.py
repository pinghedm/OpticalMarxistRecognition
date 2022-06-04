from io import BytesIO
from PIL import Image

import pytesseract
import bottle
from bottle import request
from bottle_cors_plugin import cors_plugin


app = bottle.app()
app.install(cors_plugin("*"))


@app.route("/get_text", method="POST")
def get_text():
    texts = []
    for f in request.files.getlist("image"):
        f_obj = BytesIO()
        f.save(f_obj)
        f_obj.seek(0)
        texts.append(pytesseract.image_to_string(Image.open(f_obj)))
    return {"texts": texts}


app.run(host="localhost", port=8000, server="gunicorn", workers=2)
