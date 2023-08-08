import os
from flask import Flask, jsonify, request, send_file
import base64

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


@app.route("/resume", methods=["GET"])
def sendResume():
    try:
        file_path = upload_folder + "/Yash_Chinmay_Gandhi_CV.pdf"
        pdf = pdf_to_base64(file_path)
        return pdf
    except Exception as e:
        response = jsonify(message=e)
        response.status = 500
        return response


if __name__ == "__main__":
    app.run(debug=True)
