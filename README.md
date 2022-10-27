# Premier-League-Face-Recognition-API
An unofficial API client to search players using the player reference image and get the player Stats data from the Premier League
<h2>Setup Details</h2>
Follow the following instructions to run the application and start using the api in your local pc
<li>Clone the repository</li>
<li>Open the terminal, navigate to the folder where your clone of this repository is located and type:
  
  `$ pip install -r requirements.txt` </li>

<li> Type $ python main.py in the terminal and the script will run for as long as you let it. </li>

<H2>Home Page</H2>
<ul>
  <li>Upload the photo of the Premier League Player photo whose stats you want to know; The Machine learning model will predict the player name from the feature vectors  (uploaded image) and fetch the player stats</li></br>
  Example: Stats of Cristiano Ronaldo | upload the Clear photo of Cristiano Ronaldo
  <br> <img src="home.jpg"><br>
</ul>

<H2>Prediction Page</H2>
<ul>
  <li>The model has successfully predicted the Player and Fetched the Premier League stats of the Player</li></br>
  Example: It Successfully Predicted the Person present in the uploaded image and fetched the stats
  <br> <img src="predict.jpg"><br>
</ul>
<H2>Project Progress</H2>
<ul>
  <li>successfully trained the model with 2022/23 season players photos with an accuracy of 92%</li>
</ul>

###### (Credits: Used the face_recognition python library to train the model and predict the player in the image)
