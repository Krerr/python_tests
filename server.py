from socket import *
import sys
import json
import logging
import log.server_log_config

log = logging.getLogger("app.server")


def create_message(message, code, type="ok"):
    if(type == "ok"):
        if __debug__:
            log.debug("Вызвана функция create_message на сервере, возвращаем Ok")
        return {
            "response": code,
            "alert": message
        }
    elif(type == "error"):
        if __debug__:
            log.debug(
                "Вызвана функция create_message на сервере, возвращаем Error")
        return {
            "response": code,
            "error": message
        }


if __name__ == "__main__":
    socket = socket(AF_INET, SOCK_STREAM)
    if (len(sys.argv) > 1):
        socket.bind(('', int(sys.argv[1])))
    else:
        socket.bind(('', 7777))
    socket.listen(5)

    while True:
        conn, address = socket.accept()
        data = conn.recv(1024)
        if data:
            print('Сообщение: ', data.decode("utf-8"),
                  ', было отправлено клиентом:', address)
            message = create_message(
                "Запрос клиента корректно обработан", 200, type="ok")
            conn.send(json.dumps(message).encode("utf-8"))
        else:
            message = create_message("Некорректный json", 400, type="error")
            conn.send(json.dumps(message).encode("utf-8"))
        conn.close()
