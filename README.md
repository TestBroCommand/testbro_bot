# Prerequisites
Before you begin, ensure you have the following installed:

Python (version 3.6 or higher)
pip (Python package installer)
# Setup
1. Clone the Repository
git clone https://github.com/TestBroCommand/testbro_bot.git
cd testbro_bot
2. Create a Virtual Environment
On Windows:
python -m venv venv
venv\Scripts\activate
On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Environment Variables
testbro_bot/app/utils/.env

API_KEY=our_api_key_here
BOT_TOKEN=our_bot_token_here

6. Run the Bot
After setting up the environment variables, you can start the bot:

python bot.py
