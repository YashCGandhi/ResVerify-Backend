import subprocess
import json

def get_pdf_title(pdf_path):
    command = ['exiftool', '-Title', '-j', pdf_path]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    metadata = json.loads(result.stdout.decode('utf-8'))[0]
    title = metadata.get('Title', '')
    
    # Check if the title is already a JSON object (list of dictionaries)
    try:
        title_list = json.loads(title)
    except json.JSONDecodeError:
        # If not, create a new list with a single dictionary
        title_list = [{'value': title}]

    return {'Title': title_list}

def modify_and_save_metadata(pdf_path, metadata):
    # Add a new dictionary to the Title list
    title_dict = {'new_key': 'new_value'}
    metadata['Title'].append(title_dict)
    
    # Convert the Title list to a JSON string
    title_json = json.dumps(metadata['Title'])
    
    # Use exiftool to write the modified Title metadata back to the PDF
    command = ['exiftool', f'-Title={title_json}', '-overwrite_original', pdf_path]
    subprocess.run(command)

pdf_path = "sample_name.pdf"
metadata = get_pdf_title(pdf_path)
print(metadata)

modify_and_save_metadata(pdf_path, metadata)
