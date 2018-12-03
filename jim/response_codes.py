class Response_Code:
    info = {
        "base": 100,
        "important": 101
    }
    success = {
        "ok": 200,
        "created": 201,
        "accepted": 202
    }
    client_error = {
        "wrong_json": 400,
        "unauthorized": 401,
        "auth_fail": 402,
        "forbidden": 403,
        "not_found": 404,
        "conflict": 409,
        "gone": 410
    }
    server_error = {
        "default_server_error": 500
    }