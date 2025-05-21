from pocketsphinx import LiveSpeech

speech = LiveSpeech(keyphrase='stop', kws_threshold=1e-20)
for phrase in speech:
    try:
        print(phrase.segments(detailed=True)[0][0])
    except Exception as e:
        print(e)