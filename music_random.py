import time
import random
import rtmidi

# Create an RtMidiOut object
midi_out = rtmidi.MidiOut()

# Get the available MIDI output ports
available_ports = midi_out.get_ports()

if available_ports:
    # Open the first available MIDI output port
    midi_out.open_port(0)
    print(f"Using MIDI port: {available_ports[0]}")
else:
    print("No MIDI output ports available. Connect a MIDI device and try again.")
    exit()

# Define some variables
major_scale = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note numbers for a C major scale
tempo = 120  # Beats per minute
note_duration = 0.5  # Duration of each note in seconds


# Function to play a random note from the major scale
def play_random_note():
    note = random.choice(major_scale)
    velocity = random.randint(60, 100)  # Random velocity between 60 and 100
    midi_out.send_message([0x90, note, velocity])  # Note-on message
    time.sleep(note_duration)
    midi_out.send_message([0x80, note, 0])  # Note-off message


# Set the tempo in microseconds per quarter note
microseconds_per_beat = 60000000 / tempo

try:
    while True:
        play_random_note()
        time.sleep(microseconds_per_beat / 1000000)  # Sleep for one quarter note

except KeyboardInterrupt:
    print("\nKeyboardInterrupt: Stopping MIDI output.")

finally:
    # Close the MIDI port
    midi_out.close_port()
    del midi_out
    print("MIDI port closed.")
