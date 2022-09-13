import json
import urllib.parse
import boto3
import requests

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    # Check for file name format.
    # stub
    
    # Integrate.io calls

    # get available clusters
    clusters_url = 'https://api.xplenty.com/salk-institute/api/clusters'
    
    headers = { 
      'Accept': 'application/vnd.xplenty+json; version=2',
      'Authorization': 'Basic YOUR_API_KEY_HERE'
    }
    
    result = requests.request("GET", clusters_url, headers=headers)
    
    if result.ok is True:
      clusters = result.json()
      # only use one of these status from here: https://github.com/xplenty/xplenty-api-doc-v2/blob/master/resources/cluster.md
      useable_status = ['available', 'idle', 'pending']
      useable_clusters = [d for d in clusters if d['status'] in useable_status]
    else:
      print('Error getting cluster list from Integrate.io')
      print(result)
      raise Exception(result)
        
    url = "https://api.xplenty.com/salk-institute/api/jobs"
    # data for jobs submission
    payload = json.dumps({ 
      'cluster_id': useable_clusters[0]['id'],
      'package_id':YOUR_PACKAGE_ID_HERE,
      'variables': {
        'UPLOADED_FILENAME':key
      }  
    })
    print('Here is the payload')
    print(payload)
    
    # append a content-type for the POST, use the rest from before.
    headers = {
      'Accept': 'application/vnd.xplenty+json; version=2',
      'Content-Type': 'application/json',
      'Authorization': 'Basic YOUR_API_KEY_HERE'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    
    if response.ok:
      print(f"File {key} successfuly triggered Integrate.Io Package")
    else:
      print("Error, Problem with the job submission")
      print(response)
      print(response.text)
