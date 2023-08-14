import os
from pathlib import Path
from pprint import pprint
from time import time
from affinda import AffindaAPI, TokenCredential
from affinda.models import WorkspaceCreate, CollectionCreate

token = os.environ.get("TokenAffindaAPI",None)

file_pth = Path("data/sample.pdf")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

my_organisation = client.get_all_organizations()[0]

workspace_body = WorkspaceCreate(
    organization=my_organisation.identifier,
    name="My Workspace"+str(time()),
)
recruitment_workspace = client.create_workspace(body=workspace_body)

collection_body = CollectionCreate(
    name="Resumes", workspace=recruitment_workspace.identifier, extractor="resume"
)
resume_collection = client.create_collection(collection_body)

with open(file_pth, "rb") as f:
    resume = client.create_document(file=f, file_name=file_pth.name, collection=resume_collection.identifier)

pprint(resume.as_dict())
