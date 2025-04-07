**Natural Language Processing (NLP) Project: Sentiment Analysis and Keyword Extraction**  

**Objective**:  
To develop a user-friendly web application capable of analyzing customer reviews, identifying key insights, and determining sentiment to assist businesses in understanding customer feedback.  

**Solution**:  
This project began with **exploratory data analysis (EDA)** on hotel reviews, aimed at uncovering patterns and trends in customer feedback. Key steps included:  
- **Data Preprocessing**: Cleaned the text data by converting it to lowercase, removing punctuation and stop words, and lemmatizing words to standardize content.  
- **Keyword Identification**: Visualized significant keywords using **Word Clouds** and bar plots. Analyzed the frequency of n-grams (bigrams and trigrams) to identify impactful phrases in positive and negative reviews.  
- **Sentiment Classification**: Calculated **polarity and subjectivity scores** using TextBlob to classify reviews into sentiment categories: Positive, Neutral, and Negative.  
- **Machine Learning**: Trained and tested algorithms like Logistic Regression, Support Vector Classifier (SVC), Random Forest, and Naïve Bayes on a balanced dataset. Achieved an **impressive accuracy of 91%**, with F1-scores exceeding 85% across all sentiment classes, making Logistic Regression the best-performing model.  
- **Keyword Extraction**: Implemented advanced techniques like **TF-IDF** and **KeyBERT** to identify the most critical words and phrases from input reviews.  
- **Deployment**: Built a web app using **Streamlit**, allowing users to input reviews and view sentiment probabilities, overall sentiment, and keywords extracted dynamically.

**Impact**:  
The resulting web app empowers businesses to gain actionable insights from customer reviews by automatically determining sentiment and extracting meaningful keywords. This enables organizations to:  
- Quickly identify areas for improvement based on negative feedback.  
- Highlight strong points for marketing purposes from positive reviews.  
- Streamline the process of analyzing large volumes of customer feedback, saving time and resources.  

This project highlights expertise in NLP, data preprocessing, visualization, machine learning, and app deployment. The solution provides significant business value by automating review analysis, improving customer satisfaction, and supporting data-driven decision-making.
