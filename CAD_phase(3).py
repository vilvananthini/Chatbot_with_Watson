import watson_developer_cloud
# Replace these with your own IBM Cloud credentials
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
workspace_id = 'YOUR_WORKSPACE_ID'
# Create a Watson Assistant client
assistant = watson_developer_cloud.AssistantV1(
 username=username,
 password=password,
 version='2018-02-16'
)
# Function to send a user's message to the chatbot
def send_message(message):
 response = assistant.message(
 workspace_id= workspace_id,
 input={
 'text': message
 }
 )
 return response
# Main loop for chatbot interaction
while True:
 user_input = input("You: ")
 
 # Send user's message to the chatbot
 response = send_message(user_input)
 # Extract and print chatbot's reply
 chatbot_reply = response['output']['generic'][0]['text']
 print("Chatbot: " + chatbot_reply