#!/usr/bin/env python3

import requests
import json
import boto3
def lambda_handler(event, context):
    # Set the API endpoint and authentication token
    endpoint = 'https://api.github.com/repos/{owner}/{repo}/statuses/{sha}'
    token = 'your-authentication-token-here'

    # Set the parameters for the build status
    state = 'success' # Can be 'pending', 'success', 'error', or 'failure'
    description = 'Build succeeded!'
    context = 'continuous-integration/build'

    # Set the data payload for the API request
    # @state Can be one of: error, failure, pending, success
    data = {
        'state': state,
        'target_url': 'https://your-build-server.com/build-status',
        'description': description,
        'context': context
    }

    # Replace the placeholders with the actual values
    owner = 'your-github-account'
    repo = 'your-github-repository'
    sha = 'pull-request-sha'

    # Send the API request
    response = requests.post(
        endpoint.format(owner=owner, repo=repo, sha=sha),
        headers={'Authorization': f'token {token}'},
        data=json.dumps(data)
    )

    # Check if the request was successful
    if response.status_code == 201:
        print('Build status updated successfully!')
    else:
        print(f'Error updating build status: {response.status_code} - {response.text}')
