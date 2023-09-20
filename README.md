# google-classroom-remove-guardians
Based on https://developers.google.com/classroom/guides/manage-guardians?hl=en
add same instructions

## Set up the environment:

Have Python installed on your computer.
Install the Google Client Library for Python using pip:

```
pip install --upgrade google-api-python-client
```
## Authentication:

Create a new project in the Google Developers Console.
Enable the Classroom API for this project.
Create OAuth 2.0 credentials.
Download the credentials file in JSON format.
Use this file for authentication in your Python script.

## Write the script:
In the Python script, you need to initialize the API client and call the above command.

Sample code:
```
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

# Load credentials from 'credentials.json'
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'credentials.json',
    ['https://www.googleapis.com/auth/classroom.guardianlinks.students']
)
flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true'
)

print(f"Please go to the following URL and authorize the application: {authorization_url}")
code = input("Enter the authorization code: ")
flow.fetch_token(code=code)

credentials = flow.credentials
service = build('classroom', 'v1', credentials=credentials)
student_id = 'student@email'
guardian_id = 'user.guardian@email'

try:
    service.userProfiles().guardians().delete(
        studentId=student_id,
        guardianId=guardian_id
    ).execute()
    print(f"Guardian {guardian_id} has been removed from student {student_id}.")
except Exception as e:
    print(f"An error occurred: {e}")
```

Note: The above code is just an example. You will need to adjust the authentication procedure and add proper error handling and other necessary elements.

## Run the script:
After saving the script, you can run it in the terminal or console:
```
python your_script_name.py
```
Remember that in order to remove a guardian, you must have the appropriate permissions in the Classroom API and ensure that the guardian exists for the provided studentId and guardianId.
