import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

df = pd.read_csv(
    "SMSSpamCollection",
    sep="\t",
    names=["label", "text"],
    encoding="latin-1"
)

print(df.head())
print("Rows:", len(df))

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("nb", MultinomialNB())
])

model.fit(df["text"], df["label"])

joblib.dump(model, "spam_model.pkl")

print("Model trained successfully!")