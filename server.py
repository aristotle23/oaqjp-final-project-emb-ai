from EmotionDetection import emotion_detector
from flask import Flask, request, render_template

app =  Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
@app.route("/emotionDetector")
def sent_detector():
    text = request.args.get('textToAnalyze')
    emotions = emotion_detector(text)

    description = 'For the given statement, the system response is anger: {}, disgust: {}, fear: {}, joy: {} and sadness: {}. The dominant emotion is {}.'. format(emotions['anger'], emotions['disgust'], emotions['fear'], emotions['joy'], emotions['sadness'], emotions['dominant_emotion'])

    return description, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
