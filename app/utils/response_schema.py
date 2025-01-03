from flask import jsonify


def return_json_response(message, data, status_code):
    response = jsonify({
        "message": message,
        "data": data,
        "status_code": status_code
    })

    return response
