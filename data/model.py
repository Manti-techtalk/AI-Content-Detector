from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd

# Load data
df = pd.read_csv("cleaned.csv")
X = df["text"]
y = df.drop(columns=["text"]) 

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Create a text classification pipeline with TF-IDF and Logistic Regression
model = make_pipeline(
    TfidfVectorizer(max_features=50000, ngram_range=(1, 2), stop_words="english"),
    LogisticRegression(max_iter=1000)
)

# Train
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", model.score(X_test, y_test))
print(classification_report(y_test, y_pred))

# Save entire pipeline (TF-IDF + model together)
dump(model, "text_classifier_pipeline.pkl")
