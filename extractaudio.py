import moviepy.editor as mp

clip = mp.VideoFileClip("C:\\Users\\Kunal Dhariwal\\Desktop\\videofile.mp4")
clip.audio.write_audiofile("C:\\Users\\Kunal Dhariwal\\Desktop\\audio.wav")
