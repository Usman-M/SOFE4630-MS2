from google.cloud import pubsub_v1     
import glob                             
import json
import csv
import os 
import random
import numpy as np                      
import time

# Search the current directory for the JSON file (including the service account key) 
# to set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
files=glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=files[0]

# Set the project_id with your project ID
project_id="unique-source-449113-r5"
topic_name = "Labels"   # change it for your topic name if needed

# create a publisher and get the topic path for the publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
print(f"Published messages with ordering keys to {topic_path}.")

# Reference to CSV file
labels_file = "Labels.csv"

# Open CSV
with open(labels_file) as file:
    
    # Define reader to read in content into dictionary
    reader = csv.DictReader(file)
    
    # Iterate through each row in the csv
    for row in reader:
        
        # Serialize row
        row_value=json.dumps(row).encode('utf-8')
        try:    
            future = publisher.publish(topic_path, row_value)
            # Ensure that publishing has been completed successfully
            future.result()    
            print(f"The messages {row} has been published successfully")
        except : 
            print("Failed to publish the message")

       
      