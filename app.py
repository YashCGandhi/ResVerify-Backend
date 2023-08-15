import json
import os
from flask import Flask, jsonify, request, send_file
import base64
from descope import (
    REFRESH_SESSION_TOKEN_NAME,
    SESSION_TOKEN_NAME,
    AuthException,
    DeliveryMethod,
    DescopeClient,
)

app = Flask(__name__)

try:
    path = os.path.dirname(os.path.abspath(__file__))
    upload_folder = os.path.join(path, "assets")
    os.makedirs(upload_folder, exist_ok=True)
    app.config["UPLOAD_FOLDER"] = upload_folder
except Exception as e:
    app.logger.info("Error in creating upload folder:")
    app.logger.error("Exception occured: {}".format(e))


@app.route("/resume", methods=["POST"])
def getResume():
    try:
        file = request.files["resume"]
        path_assets = os.path.join(upload_folder, file.filename)
        file.save(path_assets)
        response = jsonify(message="Success")
        response.status_code = 200
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
        response = jsonify(message="Ok")
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
