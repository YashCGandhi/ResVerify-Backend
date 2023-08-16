import json
import os
from pprint import pprint
from flask import Flask, jsonify, request, send_file
import base64
from ganache import ganache_connecter
from descope import (
    REFRESH_SESSION_TOKEN_NAME,
    SESSION_TOKEN_NAME,
    AuthException,
    DeliveryMethod,
    DescopeClient,
)
from callAffindaAPI import callAffinda
import exiftool_editor

RESUME_NAME = None
app = Flask(__name__)

try:
    path = os.path.dirname(os.path.abspath(__file__))
    upload_folder = os.path.join(path, "assets")
    os.makedirs(upload_folder, exist_ok=True)
    app.config["UPLOAD_FOLDER"] = upload_folder
except Exception as e:
    app.logger.info("Error in creating upload folder:")
    app.logger.error("Exception occured: {}".format(e))


@app.route("/test", methods=["GET"])
def test():
    try:
        response = jsonify(message="Success")
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify(message=e)
        response.status = 500
        return response


@app.route("/getuserdetails", methods=["POST"])
def get_user_details():
    try:
        name, email, phone = (
            json.loads(request.form["name"]),
            json.loads(request.form["email"]),
            json.loads(request.form["phone"]),
        )

        response = jsonify(message="Ok")
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify(message=e)
        response.status = 401
        return response


@app.route("/resume", methods=["POST"])
def getResume():
    try:
        file = request.files["resume"]
        path_assets = os.path.join(upload_folder, file.filename)

        # global RESUME_NAME
        # RESUME_NAME = path_assets
        file.save(path_assets)
        response = jsonify(message="Success")
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify(message=e)
        response.status = 500
        return response


@app.route("/returnparsed", methods=["GET"])
def return_parsed():
    try:
        path = os.path.join(upload_folder, "sample.pdf")

        # res = callAffinda(path)
        res = {
            "education": [
                {
                    "accreditation": {
                        "education": "PhD in Computer Science and " "Engineering",
                        "input_str": "PhD in Computer Science and " "Engineering",
                        "match_str": "",
                    },
                    "dates": {
                        "completion_date": "2021-09-01",
                        "is_current": False,
                        "raw_text": "Sep 2021- Aug 2027 (Exp)",
                    },
                    "grade": {
                        "metric": "GPA",
                        "raw": "GPA: 3.52/4.00",
                        "value": "3.52/4.00",
                    },
                    "id": 30417449,
                    "location": {
                        "city": "Santa Cruz",
                        "country": "United States",
                        "country_code": "US",
                        "formatted": "Santa Cruz, CA, USA",
                        "latitude": 36.9741171,
                        "longitude": -122.0307963,
                        "raw_input": "Santa Cruz",
                        "state": "California",
                    },
                    "organization": "University of California",
                },
                {
                    "accreditation": {
                        "education": "Bachelor of Engineering",
                        "education_level": "bachelors",
                        "input_str": "Bachelor of Engineering in "
                        "Computer Engineering",
                        "match_str": "",
                    },
                    "dates": {
                        "completion_date": "2021-06-01",
                        "is_current": False,
                        "raw_text": "Aug 2017 - Jun 2021",
                        "start_date": "2017-08-01",
                    },
                    "grade": {
                        "metric": "CGPA",
                        "raw": "CGPA: 8.26/10.00",
                        "value": "8.26/10.00",
                    },
                    "id": 30417450,
                    "organization": "K.J Somaiya Institute of Engineering & I.T, "
                    "University of Mumbai",
                },
            ],
            "work_experience": [
                {
                    "dates": {
                        "end_date": "2023-08-16",
                        "is_current": True,
                        "months_in_position": 22,
                        "raw_text": "Oct 2021- Present",
                        "start_date": "2021-10-01",
                    },
                    "id": 54501556,
                    "job_description": "• Managed an SQL database, "
                    "implemented an eficient CI/CD "
                    "pipeline, and created and maintained "
                    "more than 100 REST HTTP \n"
                    "endpoints using Pytest-Python, Jest, "
                    "and Selenium for automated "
                    "testing. \n"
                    "• Leveraged Google OAuth2 to "
                    "integrate the authentication with "
                    "VueJS and Flask, resulting in a "
                    "seamless user experience for \n"
                    "approximately 3,00,000 students "
                    "across all 10 UC campuses. \n"
                    "• Implemented scalable "
                    "infrastructure using Apache HTTP "
                    "Server and Gunicorn on CentOS to "
                    "accommodate the high trafic demands "
                    "of the \n"
                    "UC BASIC NEEDS \n"
                    "website, resulting in a 30% increase "
                    "in website capacity. ",
                    "job_title": "Web Developer and DevOps",
                    "location": {
                        "city": "Santa Cruz",
                        "country": "United States",
                        "country_code": "US",
                        "formatted": "Santa Cruz, CA, USA",
                        "latitude": 36.9741171,
                        "longitude": -122.0307963,
                        "raw_input": "Santa Cruz, California",
                        "state": "California",
                    },
                    "occupation": {
                        "classification": {
                            "major_group": "PROFESSIONAL " "OCCUPATIONS",
                            "minor_group": "Information " "Technology " "Professionals",
                            "soc_code": 2134,
                            "sub_major_group": "SCIENCE, "
                            "RESEARCH, "
                            "ENGINEERING "
                            "AND "
                            "TECHNOLOGY "
                            "PROFESSIONALS",
                            "title": "Programmers "
                            "and software "
                            "development "
                            "professionals ",
                        },
                        "emsi_id": "ET4A53629A7191960D",
                        "job_title": "Web Developer and DevOps",
                        "job_title_normalized": "DevOps Developer",
                        "management_level": "Low",
                    },
                    "organization": "CASFS, UCSC",
                },
                {
                    "dates": {
                        "end_date": "2023-06-01",
                        "is_current": False,
                        "months_in_position": 17,
                        "raw_text": "Jan 2022 - Jun 2023",
                        "start_date": "2022-01-01",
                    },
                    "id": 54501557,
                    "job_description": "• Taught Introduction to Scientific "
                    "Computing \n"
                    "(ASTR 119), \n"
                    "Internet of Things \n"
                    "(CSE 157), \n"
                    "Programming Abstractions: Python \n"
                    "(CSE 30-01), \n"
                    "Beginning Programming in Python \n"
                    "(CSE 20-01), \n"
                    "Principles of Computer Systems "
                    "Design \n"
                    "(CSE 130-01), \n"
                    "Systems and C \n"
                    "programming \n"
                    "(CSE 13S-02) \n"
                    "consistently receiving positive "
                    "feedback on evaluations. ",
                    "job_title": "TeachingAssistant",
                    "location": {
                        "city": "Santa Cruz",
                        "country": "United States",
                        "country_code": "US",
                        "formatted": "Santa Cruz, CA, USA",
                        "latitude": 36.9741171,
                        "longitude": -122.0307963,
                        "raw_input": "Santa Cruz, California",
                        "state": "California",
                    },
                    "occupation": {"job_title": "TeachingAssistant"},
                    "organization": "CSE, UCSC",
                },
                {
                    "dates": {
                        "end_date": "2020-07-01",
                        "is_current": False,
                        "months_in_position": 3,
                        "raw_text": "Apr 2020 - Jul 2020",
                        "start_date": "2020-04-01",
                    },
                    "id": 54501558,
                    "job_description": "• Improved company productivity by "
                    "deploying an Admin Analytics "
                    "Dashboard on an AWS EC2 Ubuntu using "
                    "MERN Stack and \n"
                    "GraphQL HTTP endpoint, reducing the "
                    "need to manually write multiple REST "
                    "endpoints, saving significant time "
                    "and efort and \n"
                    "deployed leveraging Nginx and "
                    "Apache. \n"
                    "• Resulted in a 50% increase in "
                    "data-driven decision-making by 500 "
                    "employees and reduced latency by "
                    "300% using GraphQL compared to "
                    "traditional REST endpoints, measured "
                    "employing Google Lighthouse. ",
                    "job_title": "Software Developer",
                    "location": {
                        "city": "Solapur",
                        "country": "India",
                        "country_code": "IN",
                        "formatted": "Solapur, Maharashtra, India",
                        "latitude": 17.6599188,
                        "longitude": 75.9063906,
                        "raw_input": "Solapur, India",
                        "state": "Maharashtra",
                    },
                    "occupation": {
                        "classification": {
                            "major_group": "PROFESSIONAL " "OCCUPATIONS",
                            "minor_group": "Information " "Technology " "Professionals",
                            "soc_code": 2134,
                            "sub_major_group": "SCIENCE, "
                            "RESEARCH, "
                            "ENGINEERING "
                            "AND "
                            "TECHNOLOGY "
                            "PROFESSIONALS",
                            "title": "Programmers "
                            "and software "
                            "development "
                            "professionals ",
                        },
                        "emsi_id": "ETE2AD3A1C11B4EC9B",
                        "job_title": "Software Developer",
                        "job_title_normalized": "Software " "Developer",
                        "management_level": "Low",
                    },
                    "organization": "Primary Health Centre Piliv, Under "
                    "Zilla Parishad",
                },
            ],
        }
        # pprint(res)
        # print(type(res))
        # print(res)
        response = jsonify(res)
        # response = jsonify(message="ok")
        response.status = 200
        return response
    except Exception as e:
        response = jsonify(message=e)
        response.status = 500
        return response


def pdf_to_base64(file_path):
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read())
        encoded_pdf = encoded_string.decode("utf-8")
        if encoded_pdf:
            print("Success")
        return jsonify(pdfBase64=encoded_pdf)


# Not in use ... replace this with sending work exp, edu and tokens for the form.
# @app.route("/resume", methods=["GET"])
# def sendResume():
#     try:
#         file_path = upload_folder + "/Yash_Chinmay_Gandhi_CV.pdf"
#         pdf = pdf_to_base64(file_path)
#         return pdf
#     except Exception as e:
#         response = jsonify(message=e)
#         response.status = 500
#         return response


@app.route("/updatetokens", methods=["POST"])
def update_tokens():
    try:
        data = json.loads(request.form["updatedtokens"])
        print(data)
        r = exiftool_editor.modify_and_save_metadata(
            os.path.join(upload_folder, "sample.pdf"), data
        )
        pprint(r)
        rr = ganache_connecter(r)
        response = jsonify(rr=rr)
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify(message=e)
        response.status = 401
        return response


@app.route("/protected", methods=["GET"])
def protected():
    session_token = request.headers["Authorization"].split(" ")[1]

    try:
        descope_client = DescopeClient(project_id="P2Txkg4qcMNQyXeT5TBoRwIogRch")
        jwt_response = descope_client.validate_session(session_token=session_token)
        print("Successful Validation")

        response = jsonify(message="Secret Code, Validated!")
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify(message=e)
        response.status = 401
        return response


if __name__ == "__main__":
    app.run(debug=True)
