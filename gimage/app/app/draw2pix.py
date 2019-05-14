#coding:utf-8
import numpy as np
import cv2
import os,sys
from graphpipe import remote

drawing = False

draw_img = np.zeros((512, 512, 3), np.uint8) + 255

def draw_circle(event, x, y, flags, param):
    global px, py, px, py, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        print('EVENT_LBUTTONDOWN')
        drawing = True
        px, py = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            print('EVENT_MOUSEMOVE')
            cv2.circle(draw_img, (x, y), 1, (0, 0, 0), -1)
            cv2.line(draw_img, (px, py), (x, y), (0, 0, 0), 2)
            px, py = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        print('EVENT_LBUTTONUP')
        cv2.circle(draw_img, (x, y), 1, (0, 0, 0), -1)


cv2.namedWindow('pix2pix')
cv2.setMouseCallback('pix2pix', draw_circle)

while True:
    cv2.imshow('pix2pix', draw_img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        print('Now coloring !')
        break

org_pred=cv2.resize(draw_img, (256,256))

# show org image
#cv2.imshow('pix2pix', org_img_show)

generated_image = np.zeros((256, 256, 3), np.uint8) + 255
combined_image = np.concatenate([org_pred, generated_image], axis=1)
image_rgb = cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB)

# Debug
#print(org_pred.shape)
#print(generated_image.shape)
#cv2.waitKey(0)
#cv2.imshow('pix2pix', combined_image)

# wait for checking org image
#cv2.waitKey(0)

# Predict colored image
pred = remote.execute_multi("http://130.61.99.135:9041", [image_rgb], ['image_tensor'], ['generate_output/output'])

print(pred[0][0].shape)
print(pred[0][0])

image_bgr = cv2.cvtColor(pred[0][0], cv2.COLOR_RGB2BGR)
image_bgr = cv2.resize(image_bgr, (512,512))

# show colored image
cv2.imshow('pix2pix', image_bgr)

# wait for checking colored image
cv2.waitKey(0)
