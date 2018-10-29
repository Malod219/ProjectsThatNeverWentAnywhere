from moviepy.editor import *

def main():
	print("Make sure you are running this script while in the directory of the video...")
	nameOfFile=str(input("Input the name of the input file, and it's end file type\nI.E: HelloWorld.mp4\nmp4Splitter>"))
	nameOfOutput=str(input("Input the name of theoutput file, and it's end file type\nI.E: OutputWorld.mp4\nmp4Splitter>"))

	clip = VideoFileClip(nameOfFile)

	print("Current video is "+str(clip.duration)+",\nCutting at "+str(clip.duration/2)+" to "+str(clip.duration))
	clip = clip.subclip(clip.duration/2,clip.duration)

	clip.write_videofile(nameOfOutput)
	print("Finished! See "+nameOfOutput+" in the directory you are in!")

if __name__ == '__main__':
    main()
