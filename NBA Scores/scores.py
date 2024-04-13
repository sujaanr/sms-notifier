import requests
from twilio.rest import Client

account_sid = # Placeholder for your Twilio account SID
auth_token = # Placeholder for your Twilio auth token
client = Client(account_sid, auth_token)

def fetch_scores():
    """Fetches NBA scores from Sportsdata.io."""
    api_key = 'your_api_key_here'
    url = 'https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}'  # Replace {date} with the actual date you want data for, e.g., '2022-12-25'
    headers = {
        'Ocp-Apim-Subscription-Key': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        scores = response.json()
        return scores
    else:
        return "Failed to retrieve scores"

def send_sms(scores):
    """Sends an SMS with the scores."""
    body = "\n".join([f"{game['team1']} {game['score1']} - {game['team2']} {game['score2']}" for game in scores])
    message = client.messages.create(
        body=body,
        from_= '+1234567890',  # Replace with your Twilio phone number
        to= '+1234567890'  # Replace with your phone number
    )
    print(f"Message sent: {message.sid}")

def main():
    scores = fetch_scores()
    if isinstance(scores, str):
        print(scores)  
    else:
        send_sms(scores)

if __name__ == "__main__":
    main()
