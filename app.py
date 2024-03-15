from src import CreateApp, socketio

app = CreateApp("dev")


@app.route("/")
def Home():
    return "Hello Flask!"


if (__name__ == "__main__"):
    debug = app.config["DEBUG"]
    port = app.config["PORT"]

    app.run(debug=debug, port=port, host="0.0.0.0")
    socketio.run(app)
