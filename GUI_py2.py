# -*- coding: utf-8 -*-

import Tkinter as tk
import tkFileDialog
import numpy as np
import argparse
import cv2
import ttk
from keras.applications import ResNet50
from keras.applications import InceptionV3
from keras.applications import Xception # TensorFlow ONLY
from keras.applications import VGG16
from keras.applications import VGG19
from keras.applications import imagenet_utils
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img

def selectPath():
  filename = tkFileDialog.askopenfilename()
  if filename != '':
    path.set(filename)
  else:
    filename = 'error'
    path.set(filename)

  return filename

def clickMe():
  MODELS = {
	"VGG16": VGG16,
	"VGG19": VGG19,
	"InceptionV3": InceptionV3,
	"Xception": Xception, # TensorFlow ONLY
	"ResNet50": ResNet50
  }

  if number.get() in ("InceptionV3", "Xception"):
    inputShape = (299, 299)
    preprocess = preprocess_input
  elif number.get() in ("VGG16", "VGG19", "ResNet50"):
    inputShape = (224, 224)
    preprocess = imagenet_utils.preprocess_input

  Network = MODELS[number.get()]
  model = Network(weights="imagenet")

  image = load_img(path.get(), target_size=inputShape)
  image = img_to_array(image)

  image = np.expand_dims(image, axis=0)

  image = preprocess(image)

  preds = model.predict(image)
  P = imagenet_utils.decode_predictions(preds)

  for (i, (imagenetID, label, prob)) in enumerate(P[0]):
    print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))

  pa =  path.get().encode('utf-8')
  orig = cv2.imread(pa)
  (imagenetID, label, prob) = P[0][0]
  cv2.putText(orig, "Label: {}, {:.2f}%".format(label, prob * 100),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
  cv2.imshow("Classification", orig)
  cv2.waitKey(0)

win = tk.Tk()
win.title("Python GUI")

path = tk.StringVar()
ttk.Label(win, text='input photo:').grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Entry(win, textvariable = path).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Button(win, text = "input", command = selectPath).grid(row = 0, column = 2, padx = 10, pady = 10)

ttk.Label(win, text='Chooes a MODEL:').grid(row = 1, column = 0, padx = 10, pady = 10)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = ('VGG16', 'VGG19', 'InceptionV3', 'Xception', 'ResNet50')
numberChosen.grid(row = 1, column = 1, padx = 10, pady = 10)
numberChosen.current(0)

ttk.Button(win, text = "action", command=clickMe).grid(row = 2, column = 2, padx = 10, pady = 10)

win.mainloop()
