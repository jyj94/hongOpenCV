import nump as np, cv2

theta = 20 * np.pi / 180
rot_mat = np.array([np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)], np.float32)

pts1 = np.array([(250, 30), (4000, 70), (350, 250), (150, 200)], np.float32)
nts2 = cv2.gemm(pts1, rot_mat, 1, None, 1, flags = cv2.GEMM_2_T)

for i (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print(f'pts1{i} = {pt1}, pst2{i} = {pt2}')

image = np.full((400, 500, 3), 255, np.uint8)
