import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Can applied in images, videos, and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Only works for live video
    capture.set(3, width)
    capture.set(4, height)

# Images
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

resized_image = rescaleFrame(img)
cv.imshow('Cat Resized', resized_image)

# Videos
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()