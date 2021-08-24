# Data Loss Prevention Tool

## Getting Started
- Copy .env.example in same directory and rename it as ".env" and write credentials in ".env"

- Run `sh run_local.sh`


## Getting Slack's Credentials

- Create a new Slack workspace

- Go to this link `https://api.slack.com/apps/new` and create a new slack app

- Copy `VERIFICATION_TOKEN`, `OAUTH_ACCESS_TOKEN`, `BOT_USER_ACCESS_TOKEN`, `CLIENT_ID`, `CLIENT_SECRET` app's      credentials and place them in `.env`

- Use ngrok to construct your webhook url and enter this url in Events Subscription in Slack App by appending `/event/hook`


## AWS SQS configurations

- Copy this information from AWS User `REGION_NAME`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_KEY_ID` and place it in `.env`

- Make an SQS queue and copy its `QUEUE_URL`, `QUEUE_NAME` and place it in your `.env`
