import pvrhino
from picovoice import Picovoice
from picovoice import PicovoiceError
from pvrecorder import PvRecorder


def wake_word_callback():
    # wake word detected
    print("Wake word detected")

def inference_callback(inference):
    if inference.is_understood:
      intent = inference.intent
      slots = inference.slots
      # take action based on intent and slot values
      print(intent)
    else:
      print("XDD epic fail")
      # unsupported command
      pass

try:
    rhinoceros = pvrhino.create(
        access_key="",
        #keyword_path="gaming-time_en_windows_v3_0_0.ppn", #wake up word file
        #wake_word_callback=wake_word_callback,
        context_path="gamingintent_en_windows_v3_0_0.rhn") # file of intents
        #inference_callback=inference_callback)
except Exception as e:
    print("pvrhino initialization failed:", e)  # Print the error message

try:
    recorder = PvRecorder(
        frame_length=rhinoceros.frame_length,
        device_index=0)
    recorder.start()
except Exception as e:
    print("pvrec initialization failed:", e)  # Print the error message
    
for i, device in enumerate(PvRecorder.get_available_devices()):
            print('Device %d: %s' % (i, device))

def get_next_audio_frame(recorder):
    return recorder.read()

while True:
    audio_frame = get_next_audio_frame(recorder)
    #rhinoceros.process(audio_frame)
    is_finalized = rhinoceros.process(audio_frame)
    if is_finalized:
      # get inference if is_finalized is true
      inference = rhinoceros.get_inference()
      if inference.is_understood:
         # use intent and slots if inference was understood
         intent = inference.intent
         slots = inference.slots
         print(intent)
        

