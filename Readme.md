# 🍔 McDonald's Reviews Sentiment Analysis Using NLP & BiLSTM

<p align="center">
  <b>Natural Language Processing | Deep Learning | LSTM | TensorFlow | Streamlit</b>
</p>

<p align="center">
  An NLP-based deep learning application that analyzes McDonald's customer reviews and predicts sentiment using a Bidirectional LSTM model.
</p>

---

## 📌 Project Overview

Customer reviews provide valuable insights into customer experiences, satisfaction, and opinions.

This project uses **Natural Language Processing (NLP)** and a **Bidirectional Long Short-Term Memory (BiLSTM)** neural network to analyze McDonald's customer reviews and predict sentiment.

The project includes data preprocessing, exploratory data analysis, model training, and an interactive Streamlit application for sentiment prediction.

### 🎯 Objectives

* 🍔 Analyze customer reviews of McDonald's.
* 🧹 Clean and preprocess textual data.
* 🔤 Convert text into numerical sequences using tokenization.
* 🧠 Build a Bidirectional LSTM deep learning model.
* 📊 Evaluate the trained model.
* 🌐 Develop an interactive sentiment analysis application.

---

## ✨ Key Features

* 📂 Raw and cleaned review datasets.
* 🔍 Exploratory Data Analysis (EDA).
* 🧹 Text preprocessing and cleaning.
* 🔢 Text tokenization and sequence preparation.
* 🧠 Bidirectional LSTM model.
* 💾 Saved model and tokenizer files.
* 🌐 Interactive Streamlit web application.
* 📈 Model training and evaluation notebooks.

---

## 🛠️ Technologies Used

| Technology           | Purpose                                |
| -------------------- | -------------------------------------- |
| Python               | Core programming language              |
| Pandas               | Data manipulation                      |
| NumPy                | Numerical operations                   |
| NLP                  | Text processing                        |
| TensorFlow           | Deep learning                          |
| Keras                | Neural network development             |
| LSTM                 | Sequential text learning               |
| Scikit-learn         | Data splitting and evaluation, if used |
| Matplotlib / Seaborn | Data visualization, if used            |
| Jupyter Notebook     | Data exploration and experimentation   |
| Streamlit            | Interactive web application            |     |

---

## 🔄 Project Workflow

The project follows these stages:

**Raw Reviews → Data Cleaning → EDA → Tokenization → Model Training → Evaluation → Sentiment Prediction**

### 1. Data Collection

Load the original McDonald's customer reviews dataset.

### 2. Data Preprocessing

Clean the text and prepare the review data for NLP.

### 3. Exploratory Data Analysis

Explore the dataset to understand review characteristics and distributions.

### 4. Text Tokenization

Convert text into numerical sequences that can be processed by the neural network.

### 5. Model Development

Build a Bidirectional LSTM model to learn sequential patterns in review text.

### 6. Model Evaluation

Evaluate the model using suitable classification metrics.

### 7. Application Development

Use Streamlit to provide an interface for entering text and viewing sentiment predictions.

---

## 🧠 Deep Learning Model

The project uses a **Bidirectional LSTM (BiLSTM)** architecture.

### Model Architecture

| Layer              | Configuration                                      | Purpose                                       |
| ------------------ | -------------------------------------------------- | --------------------------------------------- |
| Embedding          | Vocabulary size: 10,000; embedding dimensions: 128 | Converts token IDs into dense vectors         |
| Bidirectional LSTM | 128 LSTM units                                     | Learns sequential patterns in both directions |
| Dense              | 62 neurons, ReLU activation                        | Learns higher-level patterns                  |
| Dropout            | 0.5                                                | Helps reduce overfitting                      |
| Output             | 3 neurons, Softmax activation                      | Produces probabilities for three classes      |

The model uses a Softmax output layer to generate class probabilities. The predicted class corresponds to the highest probability.

**Note:** The vocabulary size, sequence length, output labels, and preprocessing configuration must match the actual training pipeline.

---

## 📂 Project Structure

```text
Sentiment Analysis Project/
│
├── .vscode/
│
├── app/
│   └── app.py
│
├── data/
│   ├── clean_data/
│   │   └── clean_data.csv
│   │
│   └── raw/
│       └── McDonald_s_Reviews.csv
│
├── model/
│   ├── LSTM_MODEL.pkl
│   ├── split.pkl
│   └── tokenizer.pkl
│
├── notebook/
│   ├── EDA.ipynb
│   ├── model_training.ipynb
│   └── preprocessing.ipynb
│
├── report/
│
└── Readme.md
```

---

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.12 with compatible package versions
* Git
* Visual Studio Code
* pip

### Step 1: Clone the Repository

```bash
git clonehttps://github.com/akashbulids/mcdonalds-sentiment-analysis/edit/main/Readme.md
```

Replace the placeholders with your actual GitHub username and repository name.

### Step 2: Navigate to the Project

```bash
cd https://github.com/akashbulids/mcdonalds-sentiment-analysis/edit/main/Readme.md
```

### Step 3: Create a Virtual Environment

For Windows PowerShell:

```powershell
py -3.12 -m venv .venv
```

### Step 4: Activate the Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

If a `requirements.txt` file is available:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install the packages required by your application and training code.

For example:

```bash
python -m pip install streamlit tensorflow pandas numpy scikit-learn
```

**Important:** Your saved model uses `.pkl` filenames. Confirm how `LSTM_MODEL.pkl` was saved and which libraries are needed to load it. A TensorFlow/Keras model saved as a native Keras model normally uses a `.keras` or `.h5` file, whereas a pickled object requires the appropriate loading method.

---

## ▶️ Run the Streamlit Application

From the project root directory, execute:

```bash
python -m streamlit run app/app.py
```

Once Streamlit starts, open the local URL shown in the terminal. The default address is:

**http://localhost:8501**

Ensure the model and tokenizer files are present at the paths expected by `app/app.py`.

---

## 📊 Model Evaluation

Model performance should be evaluated on unseen test data.

Recommended evaluation metrics:

| Metric           | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Accuracy         | Percentage of predictions that are correct                   |
| Precision        | How many predictions for a class are correct                 |
| Recall           | How many actual examples of a class are correctly identified |
| F1-score         | Harmonic mean of precision and recall                        |
| Confusion Matrix | Displays correct and incorrect predictions by class          |

### Model Results

Add your actual evaluation results here after running your trained model.

* **Test Accuracy:** Add measured value.
* **Precision:** Add measured value.
* **Recall:** Add measured value.
* **F1-score:** Add measured value.

*No model performance values are assumed or fabricated in this README.*

---

## 🎯 Potential Applications

* 🍔 Customer feedback analysis.
* ⭐ Restaurant review analysis.
* 💬 Customer opinion classification.
* 📊 Understanding customer satisfaction.
* 🏢 Supporting customer experience research.

---

## 🚀 Future Improvements

* Improve model performance through hyperparameter tuning.
* Compare LSTM and Bidirectional LSTM models.
* Evaluate predictions on additional customer reviews.
* Improve text preprocessing and handling of unseen words.
* Deploy the application to a suitable hosting platform.

---

## 👨‍💻 Author

**Akash R**

Aspiring Machine Learning Engineer

📍 Bangalore, India

🔗 GitHub: [Visit my GitHub profile](https://github.com/YOUR_USERNAME)

---

## ⭐ Support

If you find this project useful, consider giving the repository a star on GitHub.

Thank you for visiting my project! 🚀
