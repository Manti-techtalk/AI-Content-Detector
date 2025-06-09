# 🧠 AI Content Detector

This project uses a machine learning model that **I personally trained from scratch** using a dataset of over **500,000 labeled essays**. The model distinguishes between **AI-generated** and **Human-written** content with high accuracy.

It combines a custom **scikit-learn** pipeline with a modern **Next.js frontend**, a **Django backend API**, and a **PostgreSQL** database. The result is a full-stack, production-ready system capable of real-time AI content detection.

---

## 🚀 Features

- 🔍 Detects AI vs Human text with high confidence
- ⚙️ Built with a custom ML model using **scikit-learn**
- 🧠 Trained on 500K+ labeled essays from a named dataset
- 🌐 Modern frontend using **Next.js**
- 🐍 Robust backend powered by **Django + DRF**
- 🐘 PostgreSQL for structured data storage

---

## 🧠 About the Model

- Developed entirely by me using **scikit-learn**
- Utilizes **TF-IDF** for feature extraction
- Trained with **Logistic Regression** on labeled data
- Exported via `joblib` and loaded into Django backend
- Designed for real-time prediction

---

## 📊 Dataset Structure (Sample)

| id   | text                                                                                     | generated   |
|-------|------------------------------------------------------------------------------------------|---------|
| 1     | The quick brown fox jumps over the lazy dog.                                            | Human   |
| 2     | In recent years, the proliferation of AI models has revolutionized language processing. | AI      |
| 3     | I walked to the store and bought some apples.                                           | Human   |
| 4     | Artificial intelligence models are designed to predict outcomes from data patterns.    | AI      |

---

## 🖼️ Images

Here are some screenshots showcasing the AI Content Detector:

### 🏠 Homepage

![Screenshot 2025-06-08 at 12 35 08 PM](https://github.com/user-attachments/assets/ef5589d4-fe03-41c7-8d34-ed1cae7d2a98)

### 📩 Text Input Interface

![Screenshot 2025-06-09 at 10 44 30 AM](https://github.com/user-attachments/assets/ba11c102-f402-425a-8e2d-e75753f74cb6)


### 📊 Prediction Results

![Screenshot 2025-06-09 at 10 45 17 AM](https://github.com/user-attachments/assets/32b77d34-8303-4020-8c91-8ffd72809e1e)


---

## 🧑‍💻 Author

Built with ❤️ by **Manti Mokone**  
[GitHub Profile](https://github.com/Manti-techtalk)
