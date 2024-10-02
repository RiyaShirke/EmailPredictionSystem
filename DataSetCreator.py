import pandas as pd
import random
from datetime import datetime, timedelta

# Define sample data for each column
subjects = ["Meeting Request", "Product Offering", "Follow Up", "Monthly Report", "Special Offer"]
bodies = [
    "Hello, we would like to schedule a meeting.",
    "Here is an update on the latest product offerings.",
    "Just following up on our previous conversation.",
    "Please find attached the monthly report.",
    "Take advantage of our special offer this week!"
]
levels = ["Cold", "Hot", "High"]

# Function to generate random date and time
def generate_random_datetime():
    start_date = datetime(2023, 1, 1)
    random_days = random.randint(0, 365)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    return start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)

# Function to generate random response time
def generate_random_response_time():
    response_delay = random.randint(5, 72)  # response delay in hours
    return timedelta(hours=response_delay)

# Generate 10,000 rows
data = []
for _ in range(10000):
    subject = random.choice(subjects)
    body = random.choice(bodies)
    time_sent = generate_random_datetime()
    response_time = time_sent + generate_random_response_time()
    level = random.choice(levels)
    engagement_score = random.randint(0, 100)  # engagement score between 0 and 100
    
    data.append([subject, body, time_sent, response_time, level, engagement_score])

# Create DataFrame
df = pd.DataFrame(data, columns=["Email Subject", "Email Body", "Time Sent", "Response Time", "Level", "Engagement score"])

# Display the first few rows
df.head()

# Optionally, save to CSV
df.to_csv('email_engagement_dataset.csv', index=False)
