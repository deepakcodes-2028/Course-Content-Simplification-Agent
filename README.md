# 🎓 AI Course Content Simplifier

> **An AI-powered tool that converts complex academic content into clear, easy-to-understand explanations — powered by IBM Granite on IBM watsonx.ai.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![IBM Granite](https://img.shields.io/badge/IBM-Granite%204-052FAD)
![watsonx.ai](https://img.shields.io/badge/IBM-watsonx.ai-052FAD)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 What is This Project?

Students often struggle to understand complex textbooks, research papers, and lecture notes filled with difficult words and jargon.

This project solves that problem by using **IBM Granite AI** to read any academic content and rewrite it in a way that is easy to understand — based on the student's learning level.

---

## ✨ Key Features

- 🧠 **AI-Powered Simplification** — Uses IBM Granite to simplify real academic content
- 🎯 **4 Learning Levels** — Beginner, Intermediate, Advanced, Expert
- 📄 **5 Structured Outputs** — Explanation, Key Concepts, Important Points, Examples, Quick Revision
- 🟡 **Demo Mode** — Works offline without any IBM account
- 🟢 **Live IBM Granite Mode** — Connects to real IBM Granite AI using your credentials
- 📚 **Sample Academic Topics** — Biology, Computer Science, Physics, Economics
- 📥 **Download Study Notes** — Save output as `.md` or `.txt` file

---

## 🖥️ Live Demo

👉 **[Click here to try the live app](https://course-content-simplification-agent-r7h9snryfbavgz66cythni.streamlit.app/)**

---

## 🚀 How to Run This Project Locally

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/Course-Content-Simplifier.git
cd Course-Content-Simplifier
```

### Step 2 — Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 3 — Run the App

```bash
streamlit run app.py
```

Open your browser and go to 👉 **http://localhost:8501**

> ✅ The app will run in **Demo Mode** automatically — no IBM account needed to try it!

---

## 🟡 Demo Mode (No IBM Account Needed)

When you run the app **without any credentials**, it automatically switches to **Demo Mode**.

- ✅ Works completely offline
- ✅ Generates structured educational content from your input
- ✅ All 5 output sections work (Explanation, Concepts, Points, Examples, Revision)
- ✅ Perfect for quick testing and evaluation

The sidebar will show:
> 🟡 **Demo Mode Active** — Using the built-in educational engine.

---

## 🟢 Live Mode — Using Real IBM Granite AI

To use real IBM Granite AI, you need two things from IBM Cloud:
1. An **IBM Cloud API Key**
2. A **Watson Studio Project ID**

Follow the steps below to get them.

---

## 🔑 How to Set Up IBM watsonx.ai (Step by Step)

### Step 1 — Create an IBM Cloud Account

Go to 👉 **https://cloud.ibm.com** and sign up for a free account.

---

### Step 2 — Create a Watson Studio Project

1. Go to 👉 **https://dataplatform.cloud.ibm.com**
2. Log in with your IBM Cloud account
3. Click **"New project"**
4. Choose **"Create an empty project"**
5. Give it a name (e.g., `Course Content Simplifier`)
6. Click **"Create"**

---

### Step 3 — Associate Watson Machine Learning Service

1. Inside your project, click the **"Manage"** tab
2. Click **"Services & Integrations"** on the left
3. Click **"Associate service"**
4. Select **WatsonMachineLearning** (Type: watsonx.ai Runtime, Location: Dallas)
5. Click **"Associate"**

---

### Step 4 — Get Your Project ID

1. Inside your project, click the **"Manage"** tab
2. Click **"General"** on the left
3. Scroll down to find **"Project ID"**
4. Copy the UUID (looks like: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

---

### Step 5 — Generate an IBM Cloud API Key

1. Go to 👉 **https://cloud.ibm.com/iam/apikeys**
2. Click **"Create an IBM Cloud API key"**
3. Give it a name (e.g., `granite-key`)
4. Click **"Create"**
5. ⚠️ **Copy the key immediately** — IBM shows it only once!

---

### Step 6 — Add Credentials to the Project

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Open `.env` and fill in your values:

```env
WATSONX_API_KEY=your_actual_api_key_here
WATSONX_PROJECT_ID=your_actual_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-4-h-small
```

Restart the app:

```bash
streamlit run app.py
```

The sidebar will now show:
> 🟢 **Live IBM Granite Mode** — Connected

---

## 📁 Project Structure

```
Course-Content-Simplifier/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Credentials template (safe to share)
├── .env                # Your actual credentials (NOT uploaded to GitHub)
├── .gitignore          # Protects your secret API key from being uploaded
└── README.md           # This file
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python 3.11** | Core programming language |
| **Streamlit** | Web application interface |
| **IBM watsonx.ai** | AI model hosting platform |
| **IBM Granite 4** (`ibm/granite-4-h-small`) | AI language model |
| **ibm-watsonx-ai SDK** | Python library for IBM AI API |
| **python-dotenv** | Loads credentials from `.env` file |
| **IBM Cloud IAM** | Secure API key management |

---

## 📖 How to Use the App

1. **Select a sample topic** from the dropdown (or paste your own content)
2. **Choose your learning level** — Beginner, Intermediate, Advanced, or Expert
3. **Click "✨ Simplify My Content"**
4. View your **5 structured output sections**
5. **Download** your study notes as `.md` or `.txt`

---

## 📚 Learning Levels Explained

| Level | Best For |
|---|---|
| 🧒 **Beginner** | Students new to the topic — simple words, everyday analogies |
| 📗 **Intermediate** | Undergraduate students — clear explanations with key terms |
| 🔬 **Advanced** | Senior students — technical depth with formal terminology |
| 🎓 **Expert** | Researchers — precise, dense, formal academic language |

---

## ⚠️ Important Security Note

- **Never upload your `.env` file to GitHub** — it contains your secret API key
- The `.gitignore` file in this project automatically blocks `.env` from being uploaded
- Use `.env.example` as a safe template to share the required variable names

---

## 🙌 Built With

- [IBM watsonx.ai](https://www.ibm.com/products/watsonx-ai)
- [IBM Granite Models](https://www.ibm.com/granite)
- [Streamlit](https://streamlit.io)

---

*AI Course Content Simplifier · Powered by IBM Granite · IBM watsonx.ai*

## Build by Deepak Balan
