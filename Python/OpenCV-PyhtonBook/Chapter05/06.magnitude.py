import numpy as np, cv2

x = np.array([1, 2, 3, 5, 10], np.float32)
y = np.array([2, 5, 7, 2, 9]).astype("float32")

mag = cv2.magnitude(x, y)
ang = cv2.phase(x, y)
pMag, pAng = cv2.cartToPolar(x, y)
x2, y2 = cv2.polarToCart(pMag, pAng)
