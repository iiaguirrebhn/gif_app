from flask import Flask, render_template
import random

app = Flask(__name__)

# list of animal images
images = [
     "https://c.tenor.com/vIcPkYD36RUAAAAd/cat-cute.gif",
    "https://c.tenor.com/vIcPkYD36RUAAAAd/cat-cute.gif",
    "https://c.tenor.com/GTcT7HODLRgAAAAC/smiling-cat-creepy-cat.gif",
    "https://c.tenor.com/C0ORB81amc8AAAAd/gato-arabe.gif",
    "https://c.tenor.com/rC2iPMjyF48AAAAd/bingus-sphynx-cat.gif",
    "https://c.tenor.com/e75Iv5Pi3jwAAAAC/hot-dog-trooper-dogs.gif",
    "https://c.tenor.com/sDU10mpmaaEAAAAd/perro-wave.gif",
    "https://c.tenor.com/i3pR9emucLgAAAAC/what-dog.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
