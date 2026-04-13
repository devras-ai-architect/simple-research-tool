# 🔬 Simple Research Tool with Reflection

A personal AI-powered research assistant that searches the web and academic papers, writes a detailed report, improves it automatically, and converts it into a beautiful HTML webpage — all in just a couple of minutes.

---

## 📋 Table of Contents
- [What This Tool Does](#what-this-tool-does)
- [What You Need](#what-you-need-before-starting)
- [One-Time Setup](#one-time-setup-do-this-only-once)
- [How to Use It](#every-time-you-want-to-use-it)
- [Example Topics](#what-kind-of-topics-can-you-research)
- [How It Works](#how-it-works-summary)

---

## 🤖 What This Tool Does For You

You type a research topic (like *"effects of coffee on sleep"*) and the tool automatically:

1. 🔍 **Searches** the web and academic papers for you
2. 📝 **Writes** a detailed research report with sources
3. 🧠 **Improves** the report by reflecting on it
4. 🌐 **Converts** it into a nicely formatted webpage (HTML)

It's like having a **personal research assistant** that reads hundreds of sources and writes a clean report for you — in just a couple of minutes. 🎯

---

## ✅ What You Need Before Starting

1. A computer (Windows, Mac, or Linux)
2. Internet connection
3. Two API keys (like passwords to access the tools):
   - **OpenAI API key** → from [platform.openai.com](https://platform.openai.com)
   - **Tavily API key** → from [tavily.com](https://tavily.com)

> 💡 Both have **free tiers** to get started — no credit card required initially.

---

## 🛠️ One-Time Setup (Do This Only Once)

### Step 1 — Install Python
Go to [python.org/downloads](https://python.org/downloads) and download Python.
During installation, **check the box that says "Add Python to PATH"**. ✅

### Step 2 — Download the Tool
1. Click the green **"Code"** button on this page
2. Click **"Download ZIP"**
3. Extract the ZIP folder somewhere on your computer (like your Desktop)

### Step 3 — Open Terminal / Command Prompt

**Windows:**
Press `Windows key + R`, type `cmd`, press Enter

**Mac:**
Press `Cmd + Space`, type `terminal`, press Enter

Then navigate to your extracted folder by typing:
```bash
cd Desktop/simple-research-tool
```

### Step 4 — Install Dependencies
Type this and press Enter:
```bash
pip install -r requirements.txt
```
Wait for it to finish. This installs everything the tool needs.

### Step 5 — Add Your API Keys
Inside the folder, create a new text file called `.env` and write:

OPENAI_API_KEY=paste_your-openai-key-here
TAVILY_API_KEY=paste_your-tavily-key-here

Save it. This is the only file that is personal to you.

> ⚠️ **Never share your `.env` file with anyone.** It contains your private API keys.

---

## 🚀 Every Time You Want to Use It

### Step 1 — Open `main.py` in any text editor
Find this line near the bottom:
```python
prompt_ = "Radio observations of recurrent novae"
```
Replace it with your own topic, for example:
```python
prompt_ = "effects of coffee on sleep"
```
Save the file.

### Step 2 — Run the Tool
In your terminal, type:
```bash
python main.py
```
Press Enter and wait. You will see it working — searching, thinking, writing.

### Step 3 — Get Your Report
The tool will print your full research report in the terminal.
The HTML version can be opened in any browser like a webpage.

---

## 🌍 What Kind of Topics Can You Research?

Anything! For example:
- *"Latest treatments for diabetes"*
- *"History of the Roman Empire"*
- *"How does solar energy work"*
- *"Best programming languages in 2026"*
- *"Climate change effects on agriculture"*

---

## 📊 How It Works — Summary

| Step | What Happens |
|------|-------------|
| You type a topic | Tool searches web + academic papers |
| Wait ~1-2 minutes | Tool writes a full sourced report |
| Reflection happens | Tool improves the report automatically |
| HTML is generated | You get a nice webpage-style document |

---

## 📁 Project Structure

simple-research-tool/
├── main.py            # Main pipeline — run this file
├── research_tools.py  # Search tools (arXiv + Tavily)
├── requirements.txt   # Python dependencies
├── .env               # Your API keys (never share this)
└── README.md          # This guide

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| OpenAI GPT-4o | Writing and reflecting on reports |
| Tavily Search | Searching the web |
| arXiv API | Searching academic papers |
| Python | Core programming language |

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
