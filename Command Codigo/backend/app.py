from flask import Flask, jsonify
from flask_cors import CORS

from light import Light
from command import TurnOnCommand, TurnOffCommand
from remote_control import RemoteControl

app = Flask(__name__)
CORS(app)

light = Light()
remote = RemoteControl()


@app.route("/on")
def turn_on():

    command = TurnOnCommand(light)

    remote.set_command(command)

    result = remote.press_button()

    return jsonify({"message": result})


@app.route("/off")
def turn_off():

    command = TurnOffCommand(light)

    remote.set_command(command)

    result = remote.press_button()

    return jsonify({"message": result})


if __name__ == "__main__":
    app.run(debug=True)