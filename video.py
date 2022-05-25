import os
import moviepy.video.io.ImageSequenceClip

def create_video():
    image_folder='imgs'
    fps=1
    image_files = [os.path.join(image_folder,img)
                for img in os.listdir(image_folder)
                if img.endswith(".png")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile('evolucion_algoritmo.mp4')

if __name__ == '__main__':
    image_folder='imgs'
    for img in os.listdir(image_folder):
        print(img)