# 1. Project Name
[cite_start]InspAIre Bot - Daily Motivation & Quote Sticker Generator [cite: 64]

# 2. Project Description
InspAIre is a hybrid Telegram chatbot designed to keep users motivated. It solves the practical task of daily motivation by sending automated quotes at 7:00 AM (Asia/Almaty time), provides random quotes on demand, and generates custom image stickers using the Pillow library. [cite_start]It stores user registration data in an SQLite database[cite: 65].

# 3. Technologies Used
* [cite_start]Python 3.9+ [cite: 66]
* [cite_start]aiogram 3.x (Telegram Bot API) [cite: 66]
* [cite_start]SQLite3 (Database storage) [cite: 66]
* [cite_start]APScheduler (Background tasks/Cron jobs) [cite: 66]
* [cite_start]Pillow (Image/Sticker generation) [cite: 66]

# 4. Installation Instructions
1. [cite_start]Clone the repository or extract the project archive[cite: 67].
2. [cite_start]Open the project in PyCharm or any IDE[cite: 67].
3. [cite_start]Open the terminal and install the required libraries: `pip install -r requirements.txt`[cite: 67].

# 5. Run Instructions
1. [cite_start]Open `main.py`[cite: 68].
2. [cite_start]Replace the placeholder `YOUR_TELEGRAM_BOT_TOKEN_HERE` with your actual token from @BotFather[cite: 68].
3. [cite_start]Run the application: `python main.py`[cite: 68].

# 6. Chatbot Work Examples
* [cite_start]User: `/start` -> Bot registers user in the DB and sends a welcome message[cite: 69].
* [cite_start]User: `/q` -> Bot sends a text quote[cite: 69].
* [cite_start]User: `/qs` -> Bot generates a dark-themed `.webp` image sticker with a quote[cite: 69].
* [cite_start]User: `Who created you?` -> Bot answers based on its built-in dictionary[cite: 69].

# 7. Interface Screenshots
[cite_start]*(Insert screenshots of the Telegram chat and bot interface here before final submission)* [cite: 70]