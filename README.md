# ✨ InspAIre Bot

**InspAIre Bot** – A Telegram bot for daily motivation and text beautification

---

## 📖 About

**InspAIre Bot** helps users:

- Get **random motivational quotes** from an external API
- **Beautify any text** with emojis and text styles (bold, italic, code, spoiler, etc.)
- Set **daily reminders** for motivation at a convenient time
- Send **feedback** to the developer

The bot supports dialogue, handles **15+ types of queries**, and responds correctly to unknown commands.

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.11** | Main programming language |
| **Aiogram 3.x** | Telegram Bot API integration |
| **Aiohttp** | Async HTTP requests to API |
| **APScheduler** | Scheduler for daily notifications |
| **SQLite3** | User data and feedback storage |
| **ZenQuotes API** | Source of random motivational quotes |

---

## 🚀 Installation & Setup (Windows)

### 1. Download the project

**Option 1 - GitHub:**
```bash
git clone https://github.com/your-username/InspAIre_Bot.git
cd InspAIre_Bot

Option 2 - Download ZIP:

Click "Code" → "Download ZIP"

Extract the archive to any folder

2. Install Python 3.11
If Python is not installed:

Download Python 3.11 from python.org

During installation, check "Add Python to PATH"

Verify installation:
python --version
3.Create virtual environment:
python -m venv venv
4. Activate virtual environment
bash
venv\Scripts\activate
5. Install dependencies
bash
pip install -r requirements.txt
6. Configure bot token
Open main.py and find the line:

python
TOKEN = "8749688320:AAF0SWMkLUVnY7xXZyZocXKBgvldnbhuQRc"

Important: If uploading to GitHub, change it to:

python
TOKEN = "YOUR_TOKEN_HERE"

How to get a token:

Message @BotFather on Telegram

Send /newbot command

Choose a name and username for your bot

Copy the token you receive
7. Run the bot
bash
python main.py
After starting, you will see:

text
✅ Bot started! Waiting for messages...
To stop the bot: press Ctrl + C

📋 Commands & Features
Button / Command	Description
/start	Start the bot, welcome message
💡 Random Quote	Get a random motivational quote
✍️ Beautify My Text	Beautify any text with emojis & styles
⏰ Daily Reminder	Set daily reminder time
📝 Feedback	Send feedback to developer
❓ Help	Show help information
👤 About	Bot information


Dialogue Commands (bot understands):
You type	Bot responds
hi, hello, hey	Greeting
how are you	Tells its status
good, great	Happy for you
thanks, thank you	Gratitude
joke	Tells a joke
love, i love you	Returns love


🖼 Examples
1. /start command
text
🌟 Welcome to InspAIre Bot!

I take your words and make them beautiful with emojis and fancy fonts!

👇 Click ✍️ Beautify My Text to try it now!



2. Beautify My Text
You send:

text
The best way out is always through


Bot replies:

text
✨ Your beautified text: ✨

✨ The best way out is always through ✨

📝 Style: bold_italic | Emojis: motivational


3. Random Quote
text
💡 Your daily spark:

🔥 Believe in yourself and all that you are! 🔥


4. Daily Reminder
You send:

text
09:00

Bot replies:

text
✅ Daily reminder set!

Time: 09:00

I'll send you a motivational quote every day at this time!



5. Unknown command handling
You send: what can you do?

Bot replies:

text
🤔 I don't understand that. Click ❓ Help to see what I can do!

 Project Structure
text
InspAIre_Bot/
│
├── main.py                 # Main bot code (logic, handlers)
├── database.py             # SQLite database operations
├── stickers.py             # Helper functions for stickers
├── requirements.txt        # Dependencies list
├── README.md               # Documentation (this file)
│
└── inspaire_bot.db         # Database (auto-created)


🗄 Database (SQLite)
The bot automatically creates inspaire_bot.db with the following tables:

Table users
Field	Type	Description
user_id	INTEGER	Unique user ID (Primary Key)
username	TEXT	User's username
first_name	TEXT	User's first name
notify_time	TEXT	Daily reminder time (HH:MM)


Table feedback
Field	Type	Description
id	INTEGER	Unique record ID
user_id	INTEGER	User ID
message	TEXT	Feedback text
date	TIMESTAMP	Submission date and time


⚠️ Error Handling
Situation	Bot Response
Empty input	Asks for text again
Unknown command	Suggests using menu or Help
Invalid time format	Shows error message with example
API connection error	Sends fallback quote
Missing data in DB	Handles gracefully
Text too long	Asks to shorten (max 500 characters)


🔧 Troubleshooting
Issue: pip not recognized
Solution:

bash
python -m pip install -r requirements.txt



Issue: ModuleNotFoundError
Solution: Reinstall dependencies:

bash
pip uninstall aiogram aiohttp apscheduler -y
pip install aiogram aiohttp apscheduler


Issue: Bot doesn't respond
Solution:

Check that token is correct

Check internet connection

Restart the bot

Issue: Database error
Solution: Delete inspaire_bot.db and restart the bot (it will be recreated)



📬 Feedback
If you have questions, suggestions, or found a bug:

Send 📝 Feedback command in the bot

Or email: traganbekbatyrhan@gmail.com


👨‍💻 Author
Field	Value
Student	[Turganbek Batyrkhan]
Group	[IT2-2510 SE]
Course	Python Programming
Project Type	Telegram chatbot
Date	2026-05-21


📄 License
This project is distributed under the MIT License.

text
MIT License

Copyright (c) 2025 [Batyrkhan]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...


🔗 Useful Links
GitHub Repository

Telegram Bot

Aiogram Documentation

ZenQuotes API


📸 Screenshots
![alt text](image.png)

![](image-1.png)

![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)


