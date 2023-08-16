# cloudXBackend

## Overview

### Requirements
pip install -r requirements.txt

### Run locally
python3 main.py

### Deploy using Gunicorn
./deploy_gunicorn.sh

### Endpoints
/test (GET) - Tests if the API is running.
/getuserdetails (POST) - Retrieves the user's details like name, email, and phone.
/resume (POST) - Allows users to upload a resume.
/returnparsed (GET) - Returns parsed sample resume data.
/updatetokens (POST) - Updates tokens in a PDF file.
/protected (GET) - A protected route that validates a session token.
