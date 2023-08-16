def callAffinda(path):
    import os
    from pathlib import Path
    from pprint import pprint
    from time import time
    from affinda import AffindaAPI, TokenCredential
    from affinda.models import WorkspaceCreate, CollectionCreate
    import ast

    print("affinda called")
    token = os.environ.get("TOKEN", None)

    file_pth = Path(path)
    print(path, "this is path")

    credential = TokenCredential(token=token)
    client = AffindaAPI(credential=credential)

    my_organisation = client.get_all_organizations()[0]

    workspace_body = WorkspaceCreate(
        organization=my_organisation.identifier,
        name="My Workspace" + str(time()),
    )
    recruitment_workspace = client.create_workspace(body=workspace_body)

    collection_body = CollectionCreate(
        name="Resumes", workspace=recruitment_workspace.identifier, extractor="resume"
    )
    resume_collection = client.create_collection(collection_body)

    with open(file_pth, "rb") as f:
        resume = client.create_document(
            file=f, file_name=file_pth.name, collection=resume_collection.identifier
        )

    resume = resume.as_dict()
    return {
        "education": resume["data"]["education"],
        "work_experience": resume["data"]["work_experience"],
    }
    # file_data = ast.literal_eval(resume)

    # Checking the keys at the top level of the dictionary to understand the structure
    file_data.keys()

    # Extracting the education details
    education_details = file_data["data"]["education"]
    pprint(education_details)

    # Extracting the work experience details
    work_experience_details = file_data["data"]["work_experience"]
    # return education_details, work_experience_details
    return file_data


if "__main__" == __name__:
    pass
