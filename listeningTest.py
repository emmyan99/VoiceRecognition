import pyaudio

# Function to listen to audio
def listen_to_audio(duration=5, channels=1, rate=44100, chunk=1024, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()
    
    # Open stream
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)
    
    print("Listening...")

    # Listen for specified duration
    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        print(data)  # Print the audio data
        
    print("Finished listening.")

    # Stop and close the stream
    stream.close()
    audio.terminate()

# Main function
if __name__ == "__main__":
    duration = 5  # Specify the duration of listening in seconds
    listen_to_audio(duration)
