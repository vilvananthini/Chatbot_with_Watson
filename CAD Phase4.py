 From flask import Flask
 App = Flask(__name)
 SLACK_SIGNING_SECRET = “your_slack_signing_secret” 
\SLACK_API_TOKEN = “your_slack_api_token”
 Slack_client = WebClient(SLACK_API_TOKEN)
 Slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, “/slack/events”, app)

 @slack_events_adapter.on(“message”)
 Def handle_message(event_data): 
Message = event_data[“event”]
 If “subtype” not in message: 
User = message[“user”]
 Text = message[“text”] # Process the text and generate a response
 Response = “Your response goes here.”
 Slack_client.chat_postMessage(channel=message[“channel”], text=response)


 If __name__ == “__main__”:
    App.run(port=3000)
    
    
    output of that program
    
    
