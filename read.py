import cv2 as cv

# Reading images using OpenCV
img = cv.imread('Photos/cat_large2.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

# Reading videos using OpenCV
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
