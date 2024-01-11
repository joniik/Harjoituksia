from pydub import AudioSegment
import os
import sys
from pydub.effects import normalize
from scipy.signal import butter, sosfilt

file_path = r"C:\Users\mobjo\Desktop\Koulujutut\Python\Randomit\Oma_Bassbooster\Biisit\Arabian Nights.mp3"

def bass_boost(audio_segment, boost_factor=2):
    channels = audio_segment.split_to_mono()

    boosted_channels = [channel.low_pass_filter(60) * boost_factor for channel in channels]
    boosted_audio = AudioSegment.from_mono_audiosegments(boosted_channels[0], boosted_channels[1])

    return boosted_audio

if os.path.exists(file_path):

    sound1 = AudioSegment.from_file(file_path, format="mp3")
    boosted_sound = bass_boost(sound1, boost_factor=2)

    normalized_sound = bass_boost(boosted_sound)
    normalized_sound = normalized_sound + 12

    normalized_sound.export(r"C:\Users\mobjo\Desktop\Koulujutut\Python\Randomit\Oma_Bassbooster\Biisit\Arabian Nights BOOSTED.mp3", format="mp3")
else:
    print(f"The file '{file_path}' does not exist.")
    print (sys.path[0])