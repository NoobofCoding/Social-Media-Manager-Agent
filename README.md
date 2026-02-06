Social Media Manager Agent

An autonomous AI-powered social media management system that analyzes past post performance, generates audience insights, creates optimized posts, and schedules them automatically. Includes a live dashboard UI for monitoring insights and scheduled posts.

🚀 Features

Audience insight extraction from historical post data (posts.csv)

Best posting time + best platform prediction

Keyword extraction and theme analysis

AI-based content generation using templates

Automated scheduling and saving scheduled posts

JSON logs for tracking scheduled content

Flask + Bootstrap dashboard for live monitoring

📂 Project Structure
social_media_agent/
│
├── data/
│   ├── posts.csv              # Input dataset (historical posts)
│   ├── insights.json          # Generated insights
│   └── scheduled_posts.json   # Generated scheduled posts
│
├── ai/
│   ├── insight_engine.py      # Generates insights.json from posts.csv
│   └── content_generator.py   # Generates post content using insights
│
├── agent/
│   ├── scheduler.py           # Scheduling logic
│   └── agent_controller.py    # Main agent controller
│
├── main.py                    # Runs the full agent system
├── ui.py                      # Flask dashboard UI
├── requirements.txt           # Dependencies
└── README.md                  # Documentation

🛠 Tech Stack

Python 3.10+

Pandas (data processing + analytics)

Flask (dashboard UI + API endpoints)

Bootstrap 5 (dashboard UI design)

JSON + CSV storage (lightweight database)

⚙ Installation
1️⃣ Open Project Folder
cd social_media_agent

2️⃣ Install Dependencies
pip install -r requirements.txt

📌 How It Works
1) Audience Insight Engine

Reads data/posts.csv and generates data/insights.json.

This file contains:

best posting time

best platform

top keywords

engagement patterns by time range

best performing themes

predicted theme and time range

Run:

python ai/insight_engine.py

2) Content Generator

Uses insights + templates to generate a platform-optimized post.

Run:

python ai/content_generator.py

3) Agent Scheduling System

The agent generates a post and stores it in:

📌 data/scheduled_posts.json

Run:

python main.py

4) Dashboard UI (Flask + Bootstrap)

The dashboard displays:

Insights (best time, platform, keywords, themes)

Scheduled posts

Post generation logs

Run:

python ui.py


Open in browser:

http://127.0.0.1:5000/

▶ Full Testing Workflow

Run in this exact order:

Terminal 1
python ai/insight_engine.py
python main.py

Terminal 2
python ui.py


Then open:

http://127.0.0.1:5000/

📊 Output Files
data/insights.json (example)
{
  "best_time": "17:00",
  "best_platform": "LinkedIn",
  "top_keywords": ["productivity", "motivation", "code"],
  "preferred_content_type": "technical"
}

data/scheduled_posts.json (example)
[
  {
    "platform": "LinkedIn",
    "scheduled_time": "17:00",
    "post": "AI is redefining industry standards...",
    "hashtags": "#AI #Innovation #Career",
    "status": "scheduled"
  }
]

🔥 Future Improvements

Integration with real social media APIs (LinkedIn/Twitter posting)

ML-based engagement prediction

Sentiment analysis on comments

Database support (PostgreSQL / MongoDB)

Multi-platform scheduling + automation
