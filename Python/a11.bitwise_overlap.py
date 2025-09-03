import numpy as np, cv2

imgDir = '/home/aa/hongOpenCV/Data/'

image = cv2.imread(imgDir + 'kids.png', cv2.IMREAD_COLOR)
logo = cv2.imread(imgDir + 'logo.png', cv2.IMREAD_COLOR)
if image is None or logo is None: raise Exception("file read error")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

masks = [cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) for m in masks]

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_mask_mask = cv2.bitwise_not(fg_pass_mask)

(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W - w) // 2 + 120, (H - h) // 2 + 80
roi = image[y:y + h, x:x + w]

foregroud = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
background = cv2.bitwise_and(roi, roi, mask=bg_mask_mask)

dst = cv2.add(foregroud, background)
image[y:y + h, x:x + w] = dst

cv2.imshow("background", background)
cv2.imshow("foreground", foregroud)
cv2.imshow("dst", dst)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

