# Simple Research Tool with Reflection

What Does This Tool Do For You?
You type a research topic (like "effects of coffee on sleep") and the tool automatically:

Searches the web and academic papers for you
Writes a detailed research report with sources
Improves the report by reflecting on it
Converts it into a nicely formatted webpage (HTML)


What You Need Before Starting

A computer (Windows, Mac, or Linux)
Internet connection
Two API keys (like passwords to access the tools):

OpenAI API key → from platform.openai.com
Tavily API key → from tavily.com



Both have free tiers to get started.

One-Time Setup (Do This Only Once)
Step 1 — Install Python
Go to python.org/downloads and download Python. During installation, check the box that says "Add Python to PATH".
Step 2 — Download the Tool
Go to the GitHub repository page and click the green "Code" button → "Download ZIP". Extract the ZIP folder somewhere on your computer (like your Desktop).
Step 3 — Open Terminal / Command Prompt

Windows: Press Windows key + R, type cmd, press Enter
Mac: Press Cmd + Space, type terminal, press Enter

Then navigate to your extracted folder by typing:
bashcd Desktop/simple-research-tool
Step 4 — Install Dependencies
Type this and press Enter:
bashpip install -r requirements.txt
Wait for it to finish. This installs everything the tool needs.
Step 5 — Add Your API Keys
Inside the folder, create a new text file called .env and write:
OPENAI_API_KEY=your-openai-key-here
TAVILY_API_KEY=your-tavily-key-here
Save it. This is the only file that's personal to you.

Every Time You Want to Use It
Step 1 — Open main.py in any text editor
Find this line near the bottom:
pythonprompt_ = "Radio observations of recurrent novae"
Replace it with your own topic, for example:
pythonprompt_ = "effects of coffee on sleep"
Save the file.
Step 2 — Run the Tool
In your terminal, type:
bashpython main.py
Press Enter and wait. You'll see it working — searching, thinking, writing.
Step 3 — Get Your Report
The tool will print your full research report in the terminal. The HTML version can be saved to a file and opened in any browser like a webpage.

What Kind of Topics Can You Research?
Anything! For example:

"Latest treatments for diabetes"
"History of the Roman Empire"
"How does solar energy work"
"Best programming languages in 2026"
"Climate change effects on agriculture"


Summary in Plain Words
StepWhat HappensYou type a topicTool searches web + academic papersWait ~1-2 minutesTool writes a full sourced reportReflection happensTool improves the report automaticallyHTML is generatedYou get a nice webpage-style document
It's like having a personal research assistant that reads hundreds of sources and writes a clean report for you — in just a couple of minutes. 🎯
