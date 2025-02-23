from flask import Flask, request, jsonify
import speech_recognition as sr
from io import BytesIO

app = Flask(__name__)

recognizer = sr.Recognizer()

@app.route('/chat', methods=['POST'])
def chat():
    if 'audio' not in request.files:
        return jsonify({"response": "No audio file found!"})

    audio_data = request.files['audio']

    try:
        audio = sr.AudioFile(BytesIO(audio_data.read()))
        with audio as source:
            audio_content = recognizer.record(source)

        command = recognizer.recognize_google(audio_content)
        print(f"User said: {command}")

        # ذخیره دستور در فایل
        with open("command.txt", "w") as f:
            f.write(command)

        return jsonify({"response": f"Command received: {command}"})

    except sr.UnknownValueError:
        return jsonify({"response": "Sorry, I couldn't understand."})
    except sr.RequestError:
        return jsonify({"response": "Failed to connect to the recognition service."})
    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)