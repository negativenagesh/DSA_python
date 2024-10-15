from moviepy.editor import *
from IPython.display import Audio, display, FileLink

#from moviepy.editor import *: This line imports all classes and functions from the moviepy.editor module. The moviepy library is used for video editing and manipulation in Python.
# Specify the path to your video file

video_path =r"C:\Users\pubgp\OneDrive\Documents\EDA\Interstellar Ringtone 🎧❤.mp4"

# Load the video clip

video_clip=VideoFileClip(video_path)

#video_clip: This is a variable that will store the video clip object. It's created by loading the video located at video_path using the VideoFileClip constructor from the moviepy.editor module. This line loads the video into memory for further processing.
# Extract the audio from the video clip

audio_clip=video_clip.audio

#audio_clip: This variable stores the audio portion extracted from the video clip. It's obtained by accessing the audio attribute of the video_clip object. This step separates the audio from the video.
# Specify the output MP3 file name

output_mp3_file='interstellar.mp3'

# Write the audio to an MP3 file

audio_clip.write_audiofile(output_mp3_file)
audio_clip.write_audiofile(output_mp3_file): 

# This line writes the audio data from audio_clip to an MP3 file with the name specified in output_mp3_file. It effectively saves the extracted audio as an MP3 file.
# MoviePy - Writing audio in interstellar.mp3
# MoviePy - Done.

video_clip.close():

# This line closes the video clip, releasing the associated resources.

audio_clip.close():

# This line closes the audio clip, releasing its resources.
# Display a download link for the converted MP3 file

display(FileLink(output_mp3_file, result_html_prefix="Click here to download: "))
# Click here to download: interstellar.mp3
