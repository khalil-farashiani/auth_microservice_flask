from flask import current_app


DEBUG_MSG_CODE = {
    "100": "OK",
    "101": "Unsupported Media Type",
    "102": "DataBase Error",
    "103": "Resource Not Found",
    "104": "Request Validation Failed",
    "105": "Empty Data Supplied",
    "106": "Resource Conflict",
    "107": "Not Implemented",
    "108": "Resource Expired",
    "109": "Bad Desired Status",
    "110": "Token Encryption Error",
    "111": "Resource Not Matched",
    "112": "Header Not Specified",
    "113": "Token Validation Error",
    "114": "Invalid Token Data",
    "115": "Controller Allowed Roles Not Found",
    "116": "Resource Access Denied",
    "117": "Role Not Found"
}

def jsonify(state={}, metadata={}, status=200, code=100, headers={}):
    data = state
    data.update(metadata)
    if current_app.debug:
        data["message"] = DEBUG_MSG_CODE[str(code)]
    data["code"] = code
    return data, status, headers