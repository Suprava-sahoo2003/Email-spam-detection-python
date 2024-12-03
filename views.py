from django.shortcuts import render
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from .forms import Messageform

# Load dataset
dataset = pd.read_csv('C:/aiml project/spam detector email/emails.csv')

# Prepare the data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(dataset['text'])
X_train, X_test, y_train, y_test = train_test_split(X, dataset['spam'], test_size=0.2)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

def predictMessage(message): 
    messageVector = vectorizer.transform([message]) 
    prediction = model.predict(messageVector) 
    # Return the prediction and the CSS class for styling
    return ('spam', 'spam') if prediction[0] == 1 else ('not spam', 'ham')

def Home(request):
    result = None
    css_class = ''
    if request.method == 'POST':
        form = Messageform(request.POST)
        if form.is_valid():
            message = form.cleaned_data['text']
            result, css_class = predictMessage(message)
    else:
        form = Messageform()

    return render(request, 'home.html', {'form': form, 'result': result, 'css_class': css_class})

