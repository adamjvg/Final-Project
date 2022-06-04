# Data Analysis Final Project: Spam or No Spam
## Angadjeet Sanghera, Douglas Robertson and Adam van Geleuken
![good eating](/images/spam.webp)

### [Botfacekiller](https://botfacekiller.herokuapp.com/ "Is it spam")
<Br>

Spend a lot of time on Twitter? Do you ever wonder how much of the ‘Twittersphere’ is actually human beings? Do bots create fake news?
<br><br>
We wondered, so we decided to create an app that has been trained using a neural network using a data set with spammers and non-spammers labeled. From this, we have trained it to be able to predict from a user’s inputted data whether or not it thinks a Twitter account is a bot or not.
<br>
## Key Concepts

Initially, we had the idea of using machine learning to detect sentiment within tweets to predict whether a user was right or left-leaning on the political spectrum. <br> This was refined by trying to see whether Twitter bots were more inclined to use particular words. Then we could predict whether the bot belonged to the left or right, and analyse which side of the political spectrum had more bots and what they were making noise about.
<br><br>
This idea would require a level of machine learning that was above our pay grade and definitely an amount of research and development time unavailable to us. Therefore we decided to drop the sentiment prediction element as it would require making constant Twitter API calls and complex machine learning.
<br>
## Method
NSC Lab was kind enough to provide us with a dataset that contained a few features and whether or not the account was spam or not. This was the dataset we used to train our initial model. Get it [here](http://nsclab.org/nsclab/resources/).
<br><br>
We also obtained a much larger dataset (about 5GB) that contained much more information from Shangbin Feng at Xi'an Jiaotong University,  which contains 300,000 users tweets and metadata. This data set will be employed by us in the future. A sample version of this can be found [here](https://botometer.osome.iu.edu/bot-repository/datasets.html).
<br><br>
We used SKlearn and Tensorflow to create our model and trained it on our dataset which has 95000 spammers and 5000 non-spammers. These are the results our model obtained at various stages: 
___
Two layers, 100 nodes per --
782/782 - 2s - loss: 0.1262 - accuracy: 0.9632
Loss: 0.12624114751815796, Accuracy: 0.9632400274276733

Two layers, 36 nodes per --
782/782 - 3s - loss: 0.1344 - accuracy: 0.9602
Loss: 0.13440033793449402, Accuracy: 0.9602400064468384

Three Layers. 36, 18, 9 nodes --
782/782 - 3s - loss: 0.1295 - accuracy: 0.9630
Loss: 0.1294928640127182, Accuracy: 0.9629999995231628
___
<br>
We used the last model as we felt it used enough layers to get an accurate learning model.
<br><br>
While this model looked good it actually turned out to not be the final option. We had to reduce the number of features the model ran on in order to make the user inputs easier to use. We trimmed the features down to 5 and therefore had to re-run our model. 
<br><br>
The end prediction result looks like this: 

___
Three Layers. 36, 18, 9 nodes --
782/782 - 1s - loss: 0.1810 - accuracy: 0.9509 - 682ms/epoch - 872us/step
Loss: 0.18101263046264648, Accuracy: 0.9509199857711792
___

<br>
We saved the model and created a scaler ‘pkl’ file to go along with it.
<br><br>
We then set about building the Flask app. This proved to be the most difficult part of the process. We fed in our saved model and then provided text fields that would translate the data the user entered on the corresponding index.html file. The idea was that once the user hit ‘analyse’ the flask app would run the input through our model and then spit out whether or not it thought it was a spammer or not based which would be displayed on prediction.html.<br><br>
It did this by running a ‘post’ and ‘get’ function. We used our scaler file to make sure our data was scaled.
<br><br>
This was pretty complicated. It took us the better part of 2 days to get the Flask functioning. We eventually established that the problems lay in the scaler function. 
<br><br>
Heroku has an upload limit of 500mb. Tensorflow as a Python Library we used to process our machine learning model, and since this uses the GPU it was quite a weighty package and incompatible with Heroku.
We had to switch to 'tensorflow.cpu' which would run it locally in our deployment.
<br><br>
One key part of our app used deprecated code, which was present in the version of Tensorflow in the learning material but not the most updated version. To solve this we had to downgrade to the right version.
<br><br>
Once the results were parsed through our model we used a bit of decorative HTML to make sure our site looked good. <br><br>

## Results

This model is pretty basic as it stands. However, on larger datasets, it could be trained to do pretty interesting things. With a data set that contained Twitter handles, for instance, we could perform a call to the Twitter API. From here the user could enter any handle they wanted and our model would be able to predict whether the owner of that handle was a spam account or not. Unfortunately, the time allocated for this project did not allow us to make it this far. 
<br><br>
The dataset we used to train was weighted heavily toward non-spammers. As a result, our app is not the most thrilling thing in the world as it will think it is a non-spammer 95 times out of a hundred. Our model's accuracy of 0.9509 indicates that it will get it right 9509 times out of 10000 which is slightly better than just analyising the data.
<br><br>
In the end this was a good challenge that has a lot of future value if we make small adjustments. 

![good eating](/images/twitter_bird.jpeg)