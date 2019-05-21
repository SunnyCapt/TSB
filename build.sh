#!/usr/bin/env bash
mkdir "textsearch-bot"
mv bot Procfile requirements.txt "textsearch-bot"
cd "textsearch-bot"
heroku create textsearch-bot
git init && echo "git inited"
heroku git:remote -a textsearch-bot
git add . && git commit -am "init" && git push heroku master && echo "run.."
heroku ps:scale bot=1
#heroku logs -t