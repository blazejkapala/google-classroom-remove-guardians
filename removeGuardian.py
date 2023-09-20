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
