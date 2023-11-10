import time
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

# MIDI note-on message (Note 60, Velocity 100, Channel 1)
note_on = [0x90, 60, 100]

# MIDI note-off message (Note 60, Velocity 0, Channel 1)
note_off = [0x80, 60, 0]

try:
    # Send the note-on message
    midi_out.send_message(note_on)
    print("Note-On message sent.")

    # Wait for 1 second
    time.sleep(1)

    # Send the note-off message
    midi_out.send_message(note_off)
    print("Note-Off message sent.")

except KeyboardInterrupt:
    print("\nKeyboardInterrupt: Stopping MIDI output.")

finally:
    # Close the MIDI port
    midi_out.close_port()
    del midi_out
    print("MIDI port closed.")
