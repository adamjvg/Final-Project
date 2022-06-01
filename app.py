#################################################
# Import Dependencies
#################################################
from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import NumberRange
from tensorflow.keras.models import load_model
import numpy as np
from flask_cors import CORS


#################################################
# Load Model
#################################################
bot_model = load_model('bot_trained.h5')


#################################################
# Define prediction function
#################################################
def return_prediction(model, user_obj):
    acct_age = user_obj['account_age']
    no_fwers = user_obj['no_follower']
    no_fwing = user_obj['no_following']
    no_twts = user_obj['no_tweets']
    no_rtwts = user_obj['no_retweets']

    bot_or_not = [[acct_age, no_fwers, no_fwing, no_twts, no_rtwts]]

    classes = np.array(['spammer', 'non-spammer'])
    class_ind = model.predict_classes(bot_or_not)

    return classes[class_ind][0]


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

# Configure a secret SECRET_KEY
app.config['SECRET_KEY'] = "cNrKZARNyYCxma8hgFNqJXE8fUVEb9v4nXtV"

#################################################
# Class setup
#################################################
class UserData(FlaskForm):
    account_age = TextField('Account Age')
    no_follower = TextField('No of Followers')
    no_following = TextField('No Following')
    no_tweets = TextField('No of Tweets')
    no_retweets = TextField('No of Retweets')
    submit = SubmitField('Analyse')


#################################################
# Flask Routes
#################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    # Create instance of the form.
    form = UserData()
    # If the form is valid on submission
    if form.validate_on_submit():
        # Grab the data from the input on the form
        session['account_age'] = form.account_age.data
        session['no_follower'] = form.no_follower.data
        session['no_following'] = form.no_following.data
        session['no_tweets'] = form.no_tweets.data
        session['no_retweets'] = form.no_retweets.data

        return redirect(url_for("prediction"))

    return render_template('index.html', form = form)

@app.route('/prediction')
def prediction():
    # Defining content dictionary
    content = {}

    content['account_age'] = float(session['account_age'])
    content['no_follower'] = float(session['no_follower'])
    content['no_following'] = float(session['no_following'])
    content['no_tweets'] = float(session['no_tweets'])
    content['no_retweets'] = float(session['no_retweets'])

    results = return_prediction(model = bot_model, user_obj = content)

    return render_template('prediction.html', results = results)


#################################################
# Python Debug
#################################################
if __name__ == '__main__':
    app.run(debug=True)