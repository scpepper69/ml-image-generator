#coding:utf-8
import numpy as np
import cv2
import os,sys
from graphpipe import remote

args = sys.argv
print(args[1])

org_img=cv2.imread(args[1])
org_img_show=cv2.resize(org_img, (512,512))
org_pred=cv2.resize(org_img, (256,256))

# show org image
cv2.imshow('pix2pix', org_img_show)

# wait for checking org image
cv2.waitKey(0)

# Prepare & Predict colored image
generated_image = np.zeros((256, 256, 3), np.uint8) + 255
combined_image = np.concatenate([org_pred, generated_image], axis=1)
image_rgb = cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB)
pred = remote.execute_multi("http://130.61.99.135:9041", [image_rgb], ['image_tensor'], ['generate_output/output'])

# show colored image
image_bgr = cv2.cvtColor(pred[0][0], cv2.COLOR_RGB2BGR)
image_bgr = cv2.resize(image_bgr, (512,512))

clean = cv2.fastNlMeansDenoisingColored(image_bgr,None,10,10,7,21)

#cv2.imshow('pix2pix', image_bgr)
#cv2.waitKey(0)
cv2.imshow('pix2pix', clean)

# wait for checking colored image
cv2.waitKey(0)
