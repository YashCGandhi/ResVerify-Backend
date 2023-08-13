from pprint import pprint
import ast

file_path="output.txt"
with open(file_path, 'r') as file:
    file_content = file.read()
# Converting the file content string into a dictionary
file_data = ast.literal_eval(file_content)

# Checking the keys at the top level of the dictionary to understand the structure
file_data.keys()

# Extracting the education details
education_details = file_data['data']['education']
pprint(education_details)

# Extracting the work experience details
work_experience_details = file_data['data']['work_experience']
pprint(work_experience_details)
