# 🎓 AI Course Content Simplifier

An AI-powered tool that takes complex academic content — like textbook chapters, lecture notes, or research papers — and explains it in simple, easy-to-understand language.

Powered by **IBM Granite** via **IBM watsonx.ai**.

---

## ✨ What It Does

Paste any difficult academic text and choose your learning level. The app will instantly break it down into:

- 📄 **Simple Explanation** — Easy-to-read version of the content
- 🔑 **Key Concepts** — The most important ideas
- 📌 **Important Points** — Key takeaways to remember
- 💡 **Examples** — A relatable analogy or real-world example
- 📚 **Quick Revision** — A 1–2 sentence summary

---

## 🎯 Learning Levels

| Level | Best For |
|---|---|
| 🧒 Beginner | Students new to the topic — simple words, everyday examples |
| 📗 Intermediate | Undergraduate students — clear explanations with basic terms |
| 🔬 Advanced | Senior students — technical depth with proper terminology |
| 🎓 Expert | Researchers — precise, dense, formal language |

---

## 🚀 How to Run

### Step 1 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2 — Run the app

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

> **No IBM account? No problem!**
> The app runs in **Demo Mode** automatically without any credentials.

---

## 🔑 Enable Live IBM Granite AI (Optional)

To use real IBM Granite AI instead of Demo Mode:

1. Copy the credentials file:
```bash
cp .env.example .env
```

2. Open `.env` and fill in your values:
```env
WATSONX_API_KEY=your_ibm_cloud_api_key
WATSONX_PROJECT_ID=your_watsonx_project_id
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-instruct-v2
```

3. Get your credentials from:
   - **API Key** → https://cloud.ibm.com/iam/apikeys
   - **Project ID** → https://dataplatform.cloud.ibm.com → Your Project → Manage → General

4. Restart the app — the sidebar will show **🟢 Live IBM Granite Mode**

---

## 📁 Project Files

```
Course-Content-Simplifier/
├── app.py              # Main application
├── requirements.txt    # Python packages needed
├── .env.example        # Credentials template (safe to share)
├── .env                # Your actual credentials (NOT shared — gitignored)
├── .gitignore          # Protects your secret keys from being uploaded
└── README.md           # This file
```

---

## 🛠️ Tech Stack

- **Python** 3.10+
- **Streamlit** — Web interface
- **IBM watsonx.ai** — AI model API
- **IBM Granite** (`ibm/granite-13b-instruct-v2`) — AI language model
- **python-dotenv** — Loads credentials from `.env`

---

## 📖 Quick Demo

1. Run `streamlit run app.py`
2. Select a sample topic (e.g., *🔬 Biology: Cellular Respiration*)
3. Choose **Beginner** level
4. Click **✨ Simplify My Content**
5. Download your notes using **📥 Download Study Notes**

---

## ⚠️ Important Notes

- **Never upload your `.env` file to GitHub** — it contains your secret API key
- The `.gitignore` file already protects it automatically
- Demo Mode works offline and requires no IBM account

---

*Built with IBM Granite · IBM watsonx.ai · Streamlit*
