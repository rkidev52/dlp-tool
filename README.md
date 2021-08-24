# Data Loss Prevention Tool

## Getting Started
- Create virtual environment: `virtualenv venv`

- Activate virtual environment: `source venv/bin/activate`

- Install dependencies: `pip install -r requirements.txt`

- Copy .env.example in same directory and rename it as ".env" and write credentials in ".env"

- Migrate DB : `python manage.py migrate`

- Runserver : `python manage.py runserver`

- Navigate to url: `localhost:8000`



## Getting Slack's Credentials

- Create a new Slack workspace

- Go to this link `https://api.slack.com/apps/new` and create a new slack app

- Copy `VERIFICATION_TOKEN`, `OAUTH_ACCESS_TOKEN`, `BOT_USER_ACCESS_TOKEN`, `CLIENT_ID`, `CLIENT_SECRET` app's      credentials and place them in `.env`

- Use ngrok to construct your webhook url and enter this url in Events Subscription in Slack App


## AWS SQS configurations

- Copy this information from AWS User `REGION_NAME`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_KEY_ID` and place it in `.env`

- Make an SQS queue and copy its `QUEUE_URL`, `QUEUE_NAME` and place it in your `.env`
