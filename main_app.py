#Library imports
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import hashlib
import cv2
import streamlit.components.v1 as components
from keras.models import load_model
import wikipediaapi 
API = "3a295a2f-5f61-47e8-9e4a-076ab1bc0b5a"

#Wiki API for Informations
wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI)

#PASSWORD
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

#SQL
import sqlite3 
conn = sqlite3.connect('data.db')
#CONNECTION
c = conn.cursor()
#TABLE
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
def add_userdata(username,password):
	#INSERT QUERY
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()
def login_user(username,password):
	#SELECT
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data
def view_all_users():
	#FETCH ALL RECORD
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():

	LogoImage = Image.open('First-modified.png')
	col1, col2, col3 = st.columns([0.1, 0.1, 0.1])
	col2.image(LogoImage, use_column_width=True,width='200px')
	
	#DROPSOWN FOR LOGIN AND SIGNUP
	st.markdown("<h1 style='text-align:center;'>Dog Breed Recognization using deep machine learning</h1>",unsafe_allow_html=True)
	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)


	#HOME
	if choice == "Home":
		

		
		page = wiki_wiki.page('Deep Learning')
		page2 = wiki_wiki.page('Convolutional neural network')
		st.markdown("<h2 style='text-align: center; color: grey;'>Summary about this web app</h2>", unsafe_allow_html=True)
		# st.subheader("Summary about this web app")
		st.text("")
		st.text("")
		image = Image.open('Header.png')
		st.image(image,caption="Process of Model")
		st.text("")
		st.text("")
		

 		
		st.write(page2.text[0:773])
		st.markdown("<a style='text-decoration: none;color: inherit;' href = 'https://en.wikipedia.org/wiki/Convolutional_neural_network '>CNN</a>",unsafe_allow_html=True)
		st.text("")
		st.markdown("<h3 style='text-align:center;'>Example feature extraction using Deep machine learning</h3>" ,unsafe_allow_html= True)
		st.text("")
		feature = Image.open('Feature.jpg')
		# col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
		# col2.image(feature, use_column_width=True)
		col1, col2 = st.columns(2)

		
		
		col1.image(feature, use_column_width=True)
		grayscale = feature.convert('LA')
		col2.image(grayscale, use_column_width=True)
		
	
		
		st.text("")
		st.text("")

		st.write(page.text[0:1850-11])
		st.text("")
		st.markdown("<a href = 'https://en.wikipedia.org/wiki/Deep_machine_learning'>Click here to read full article</a>",unsafe_allow_html=True)
		Html_file = open("Index.html", 'r', encoding='utf-8')
		source_code = Html_file.read() 
		# print(source_code)
		components.html(source_code)

	#LOGIN
	if choice == "Login":
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			create_usertable()
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				model = load_model('dog_breed.h5')
				CLASS_NAMES = ['Scottish Deerhound','Maltese Dog','Bernese Mountain Dog']
				st.markdown("<h3 style='text-align:center; color:orange;margin:10px;'>Dog Breed Prediction</h3>",unsafe_allow_html=True)
				# st.title("Dog Breed Prediction")
				st.markdown("<p style='text-align:center;margin:10px;'>Upload an image of the dog</p>",unsafe_allow_html=True)
				# st.markdown("Upload an image of the dog")
				st.text("")
				st.text("")
				dog_image = st.file_uploader("Choose an image...")
				st.text("")
				st.text("")
				submit = st.button('Predict')
				if submit:


					if dog_image is not None:
						file_bytes = np.asarray(bytearray(dog_image.read()), dtype=np.uint8)
						opencv_image = cv2.imdecode(file_bytes, 1)
						
						st.image(opencv_image, channels="BGR")
						opencv_image = cv2.resize(opencv_image, (224,224))
						opencv_image.shape = (1,224,224,3)
						Y_pred = model.predict(opencv_image)
						Result = CLASS_NAMES[np.argmax(Y_pred)]
						
						
						st.title(str("The Dog Breed is "+ Result))
						if(Result == 'Scottish Deerhound'):
							st.subheader(Result)
							page_py = wiki_wiki.page('Scottish Deerhound')
							st.write(page_py.text[0:1500])
							st.markdown("<a href='https://en.wikipedia.org/wiki/Scottish_Deerhound'>Click here to know about this breed</a>",unsafe_allow_html=True)
							
						elif(Result == 'Maltese Dog'):
							page_py = wiki_wiki.page('Maltese Dog')
							st.write(page_py.text[0:1501])
							st.markdown("<a href='https://en.wikipedia.org/wiki/Maltese_Dog'>Click here to know about this breed</a>",unsafe_allow_html=True)
						elif(Result == 'Bernese Mountain Dog'):
							page_py = wiki_wiki.page(Result)
							st.write(page_py.text[0:1500])
							st.markdown("<a href='https://en.wikipedia.org/wiki/Bernese_Mountain_Dog'>Click here to know about this breed</a>",unsafe_allow_html=True)
						
						
        								
			else:
				st.warning("Incorrect Username/Password")
	#SIGNUP
	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
		confirm_password = st.text_input("Re-enter_Password",type='password')
		if(new_password==confirm_password):
			if st.button("Signup"):
				create_usertable()
				add_userdata(new_user,make_hashes(new_password))
				st.success("You have successfully created a valid Account")
				st.info("Go to Login Menu to login")

		
if __name__ == '__main__':
        main()




# col1, col2 = st.columns(2)

# original = Image.open(image)
# col1.header("Original")
# col1.image(original, use_column_width=True)

# grayscale = original.convert('LA')
# col2.header("Grayscale")
# col2.image(grayscale, use_column_width=True)