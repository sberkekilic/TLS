import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy as np 
from keras.models import load_model
#loading the model for classifying traffic signs
model = load_model('traffic_classifier.h5')

#dictionary for labeling all traffic signs class
classes = { 1:'Hız sınırı (20km/h)',
            2:'Hız sınırı (30km/h)', 
            3:'Hız sınırı (50km/h)', 
            4:'Hız sınırı (60km/h)', 
            5:'Hız sınırı (70km/h)', 
            6:'Hız sınırı (80km/h)', 
            7:'Hız sınırlaması sonu (80km/h)', 
            8:'Hız sınırı (100km/h)', 
            9:'Hız sınırı (120km/h)', 
            10:'Öndeki taşıtı geçmek yasaktır', 
            11:'Kamyonlar için öndeki taşıtı geçmek yasaktır', 
            12:'Ana yol-tali yol kavşağı', 
            13:'Anayol', 
            14:'Yol ver', 
            15:'Dur', 
            16:'Taşıt trafiğine kapalı yol', 
            17:'Kamyon giremez', 
            18:'Girişi olmayan yol', 
            19:'Dikkat', 
            20:'Sola tehlikeli viraj', 
            21:'Sağa tehlikeli viraj', 
            22:'Sola tehlikeli devamlı virajlar', 
            23:'Kasisli yol', 
            24:'Kaygan yol', 
            25:'Sağdan daralan kaplama', 
            26:'Yolda çalışma', 
            27:'Trafik işaret cihazı', 
            28:'Yaya geçidi', 
            29:'Okul geçidi', 
            30:'Bisiklet geçebilir', 
            31:'Buz tutabilir',
            32:'Vahşi hayvanlar geçebilir', 
            33:'Bütün yasaklama ve kısıtlamaların sonu', 
            34:'İlerden sağa mecburi yön', 
            35:'İlerden sola mecburi yön', 
            36:'İleri mecburi yön', 
            37:'İleri ve sağa mecburi yön', 
            38:'İleri ve sola mecburi yön', 
            39:'Sağdan gidiniz', 
            40:'Soldan gidiniz', 
            41:'Ada etrafında dönünüz', 
            42:'Geçme yasağı sonu', 
            43:'Kamyonlar için geçme yasağı sonu'}

#initialising GUI
top = tk.Tk()
top.iconbitmap("sign.ico")
top.geometry('800x600')
top.title('TLS')
top.configure(background='#000000')

#traffic sign explanation
label = Label(top,background='#000000',font=('arial',15,'bold'))
sign_image = Label(top, background='#000000')

def classify(file_path):
	global label_packed
	image = Image.open(file_path)
	image = image.resize((30,30))
	image = np.expand_dims(image, axis=0)
	image = np.array(image)
	pred = model.predict([image])[0]
	result = pred.argmax()
	sign = classes[result+1]
	print(sign)
	#traffic sign explanation
	label.configure(background='#ffffff', foreground='#033801',text=sign)

def show_classify_button(file_path):
	classify_b = Button(top,text="Sorgula",command=lambda:classify(file_path),padx=10,pady=5)
	classify_b.configure(background='#ffffff',foreground='black',font=('arial',10,'bold'))
	classify_b.place(relx=0.79,rely=0.54)

def upload_image():
	try:
		file_path = filedialog.askopenfilename()
		uploaded = Image.open(file_path)
		resized_image = uploaded.resize((150,150), Image.LANCZOS)
		im = ImageTk.PhotoImage(resized_image)

		sign_image.configure(image=im)
		sign_image.image=im
		label.configure(text='')
		show_classify_button(file_path)
	except:
		pass

upload = Button(top,text="Resim yükle",command=upload_image,padx=10,pady=5)
upload.configure(background='#ffffff',foreground='black',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top,text="Trafik Levhaları Sorgulama",pady=20,font=('arial',20,'bold'))
heading.configure(background='#000000',foreground='#ffffff')
heading.pack()
top.mainloop()
