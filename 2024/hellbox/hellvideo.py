import cv2
import os

image_folder = 'C:\\Users\liam\Documents\Python Scripts\AOCmaster\\2024\hellbox'
video_name = 'hellvid.avi'

images = [img for img in os.listdir(image_folder)[6300:6400] if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()