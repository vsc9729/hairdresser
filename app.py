
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from keras import models
from keras.preprocessing import image
import numpy as np
from tensorflow import Graph
import cv2
from flask import Flask, request, render_template, redirect, url_for
import base64
from io import BytesIO

img_height, img_width=64,64

app = Flask(__name__)    

model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model=keras.models.load_model('face_shape.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/oblong')
def oblong():
    return render_template('oblong.html')

@app.route('/oval')
def oval():
    return render_template('oval.html')

@app.route('/square')
def square():
    return render_template('square.html')

@app.route('/roundface')
def roundface():
    return render_template('round.html')




@app.route('/process', methods = ['POST'])
def get_post_javascript_data():
    base64Image = str(request.form.get('base64Image')).replace("data:image/jpeg;base64,", "");
    imgdata = base64.b64decode(base64Image)
    img = Image.open(BytesIO(imgdata))
    width, height = img.size

    left = 35
    top = 0
    right = width-35
    bottom = height
    
    img = img.crop((left, top, right, bottom))

    newsize = (64, 64)
    img = img.resize(newsize)
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)

    with model_graph.as_default():
        with tf_session.as_default():
            model=keras.models.load_model('face_shape.h5')
            a = model.predict(x)

        
    my_context = {
        "one": f'{a[0][0]*100} % heart shaped',
        "two": f'{a[0][1]*100} % Oblong',
        "three": f'{a[0][2]*100} % Oval',
        "four": f'{a[0][3]*100} % Round',
        "five": f'{a[0][4]*100} % Square'
    }
    a= a[0]
    max_shape = max(a)
    if max_shape == a[0]:
        return url_for('heart')
    elif max_shape == a[1]:
        return url_for('oblong')
    elif max_shape == a[2]:
        return url_for('oval')
    elif max_shape == a[3]:
        return url_for('roundface')
    elif max_shape == a[4]:
        return url_for('square')
     


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    