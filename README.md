# Slack Assignment - An Incoming Webhook

## Description
This task is to demo that an Incoming Webhook is an easy way to post messages from external sources to Slack. In our example, we will see that a message will be posted in the channel #bring-an-umbrella when today's predicted precipitation is > 0 mm.

![Image of Channel](https://user-images.githubusercontent.com/30242361/28349219-4f55ee3a-6bf6-11e7-84ae-b17326423df3.png)

## How it works
1. A new team is created in Slack: sfjf22
1. A new channel #bring-an-umbrella is created: https://sfjf22.slack.com/messages/C69CPNX8T/
1. Set up the Incoming WebHooks at App Directory for the following:
   1. Create a new channel #bring-an-umbrella and specify it at the "Post to Channel" field
   1. Copy the URL from "Webhook URL" field which is where we want to send the JSON payload to.
1. Implement a Python script **bin/weather_app.py** which will query an online weather service for weather information.
   1. In our example, we use http://api.wunderground.com which provides free weather API service.
   1. We would need an API key from the free account to add to the HTTP Request URL.
   1. The script will take 3 arguments from the command line: API key, State and City.
   1. The response returned from api.wunderground.com contains a field "precip_today_metric" which will be used.
1. Finally we will set up a CRON job to execute the python script every 30 min.

## Online Weather Resources
1. This example uses the free online services from Weather Underground https://www.wunderground.com
1. An API Key is required to make a HTTP Request for the weather data. The API Key for this demo is specified in the replied email to Nicole C.
1. If we are getting the weather data for State=GA and City=Ashburn, the HTTP Request URL will be http://api.wunderground.com/api/<API_KEY>/conditions/q/GA/Ashburn.json with API_KEY substituted.
1. The data returned from wunderground would be like the following:
```
{
  "response": {
    "version": "0.1",
    "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
    "features": {
      "conditions": 1
    }
  },
  "current_observation": {
    .
    .
    .
    "precip_today_string": "1.39 in (35 mm)",
    "precip_today_in": "1.39",
    "precip_today_metric": "35",
    .
    .
    .
  }
}
```

## CRON Job
1. We would need to create a CRON Job to execute the Python script **weather_app.py** in a 30 min period and send a message to our channel if it is supposed to rain for that day
1. Create a CRON Job as show below
```
1. $ crontab -e
2. Put the following line in the editor
   */30 * * * * python /Users/jfung/slack-incoming-webhook/bin/weather_app.py <API KEY> GA Ashburn
3. Specify the API_KEY (which is available from my email replied to Nicole C.) and the State and City.
```
