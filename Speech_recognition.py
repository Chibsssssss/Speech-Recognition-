import speech_recognition as sr

def speech_from_audio(recognizer):

    speech = sr.Recognizer()
    
    with recognizer as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.record(source)

    
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }


    try:
        response["transcription"] = speech.recognize_google(audio)
    except sr.RequestError:
       
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        
        response["error"] = "Unable to recognize speech"

    return response


recognizer = sr.AudioFile("./audio_files/Chibueze2.wav")

speech_from_audio(recognizer)