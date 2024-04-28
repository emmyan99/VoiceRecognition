from picovoice import Picovoice
from picovoice import PicovoiceError
import pyaudio

#this code does not work i am keeping it for fun though

CHUNK_SIZE = 256 #number of frames signals are split into
SAMPLE_RATE = 16000  # Picovoice default sample rate, the number of frames per second
FORMAT = pyaudio.paInt16

def wake_word_callback():
    # wake word detected
    print("Wake word detected")

def inference_callback(inference):
    if inference.is_understood:
      intent = inference.intent
      slots = inference.slots
      # take action based on intent and slot values
      if intent == "jump":
        print("Detected intent: jump")
      else:
        print("Unsupported intent:", intent)
    else:
      # unsupported command
      pass

try:
    picovoice = Picovoice(
        access_key="",
        keyword_path="gaming-time_en_windows_v3_0_0.ppn",
        wake_word_callback=wake_word_callback,
        context_path="test1_en_windows_v3_0_0.rhn",
        inference_callback=inference_callback)
except PicovoiceError as e:
    print("Picovoice initialization failed:", e)  # Print the error message


def initialisePyAudio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,
                        channels=1,
                        rate=SAMPLE_RATE,
                        input=True,
                        frames_per_buffer=CHUNK_SIZE)
    # Get the number of audio I/O devices
    devices = audio.get_device_count()

    # Print the total number of devices
    print(f'Total number of devices: {devices}')
    return stream

def get_next_audio_frame(stream):
    #print("currently recording...")
    audio_frame = stream.read(CHUNK_SIZE)
    #print("Length of audio frame:", len(audio_frame))  # Print length of audio frame
    return audio_frame

stream = initialisePyAudio()
while True:
    audio_frame = get_next_audio_frame(stream)
    #print("its processing time!")
    picovoice.process(audio_frame)