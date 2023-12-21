
# import streamlit and other necessary modules
import streamlit as st
import pickle
import string
import numpy as np
import pandas as pd
from textblob import TextBlob


pickle_in = open("sentiment_model.pkl", "rb")
sentiment_model = pickle.load(pickle_in)
pickle_in = open("tfidf.pkl", "rb")
tfidf = pickle.load(pickle_in)
pickle_in = open("stopwords.pkl", "rb")
stopw = pickle.load(pickle_in)

@st.cache_data()

def sentiment(user_input):   
    text= user_input.lower()
    text= text.translate(str.maketrans('', '', string.punctuation))
    text= text.translate(str.maketrans('', '', string.digits))
    text=' '.join(x for x in text.split() if x not in stopw)

    proba = np.round(sentiment_model.predict_proba([text])*100,2)[0]
    classes = ['Negative', 'Neutral', 'Positive']    
    df = pd.DataFrame(data=proba, index=classes, columns=['Percentage'])
    pol= TextBlob(text).polarity

    return df,pol

@st.cache_data()

def keywords(user_input):   
    text= user_input.lower()
    text= text.translate(str.maketrans('', '', string.punctuation))
    text= text.translate(str.maketrans('', '', string.digits))
    text=' '.join(x for x in text.split() if x not in stopw)
    
    tf_idf_vector = tfidf.transform([text])
    tuples = zip(tf_idf_vector.tocoo().col, tf_idf_vector.tocoo().data)
    sorted_items = sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)
    feature_names = tfidf.get_feature_names_out()
    
    score_val = []
    feature_val = []
    for i,score in sorted_items:
        score_val.append(round(score,3))
        feature_val.append(feature_names[i])
        
    results= {}
    n=len(sorted_items)
    for i in range(min(20,n)):
        results[feature_val[i]]=score_val[i]
        
    imp_words = pd.DataFrame.from_dict(results, orient='index', columns=['score']).reset_index(names='Keywords')
    imp_words

def main():
    # display the app title
    st.title("NLP - Important Keywords Extraction & Sentiment Analysis")

    # get user input as a text area widget
    user_input = st.text_area("Enter a review: ",'Type here...')

    # when the analyze button is clicked
    if st.button("Analyze"):
        df,pol = sentiment(user_input)
        st.subheader("Sentiment Analysis: ")
        st.dataframe(df)
        st.subheader("Polarity of the review is: ")
        st.write(np.round(pol,3))
        st.subheader("Important Keywords: ")
        keyword = keywords(user_input)

# run the main function
if __name__ == "__main__":
    main()
