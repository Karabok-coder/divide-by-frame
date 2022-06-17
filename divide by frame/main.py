from PIL import Image
import cv2
from sys import argv
from progress.bar import Bar

script, src, from_frame = argv
number_frame = 0
is_true = False

cap = cv2.VideoCapture(src)
length_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

bar = Bar('Process', max = length_video - int(from_frame))

while True:
    _, frame = cap.read()

    if int(from_frame) == number_frame: is_true = True

    number_frame += 1

    if is_true:
        im = Image.fromarray(frame)
        im.save(str(number_frame) + '.png')
        bar.next()

    length_video -= 1
    if length_video < 1: break

bar.finish()
print('Done')
