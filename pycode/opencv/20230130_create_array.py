
import cv2
import numpy as np


print("create 1D array")
print("-" * 88)
blue_1d = np.zeros((2), np.uint8)
print("zeros 2")
print("blue_1d.dtype: ", blue_1d.dtype)
print("blue_1d.ndim: ", blue_1d.ndim)
print("blue_1d.shape: ", blue_1d.shape)
print("blue_1d.size: ", blue_1d.size)
print(f"blue_1d = \n{blue_1d}")


print("create 2D array")
print("-" * 88)
blue_2d = np.zeros((2, 3), np.uint8)
print("zeros 2x3")
print("blue_2d.dtype: ", blue_2d.dtype)
print("blue_2d.ndim: ", blue_2d.ndim)
print("blue_2d.shape: ", blue_2d.shape)
print("blue_2d.size: ", blue_2d.size)
print(f"blue_2d = \n{blue_2d}")

print("before modify >>>")
print("blue_2d[0, 0]", blue_2d[0,0])
print("blue_2d[0, 1]", blue_2d[0,1])
print("blue_2d[0, 2]", blue_2d[0,2])
print("blue_2d[1, 0]", blue_2d[1,0])
print("blue_2d[1, 1]", blue_2d[1,1])
print("blue_2d[1, 2]", blue_2d[1,2])

blue_2d[0,0] = 1
blue_2d[0,1] = 2
blue_2d[0,2] = 3
blue_2d[1,0] = 4
blue_2d[1,1] = 5
blue_2d[1,2] = 6

print("after modify >>>")
print(f"blue_2d = \n{blue_2d}")
print("blue_2d[0, 0]", blue_2d[0,0])
print("blue_2d[0, 1]", blue_2d[0,1])
print("blue_2d[0, 2]", blue_2d[0,2])
print("blue_2d[1, 0]", blue_2d[1,0])
print("blue_2d[1, 1]", blue_2d[1,1])
print("blue_2d[1, 2]", blue_2d[1,2])


print("create 3D array")
print("-" * 88)
blue = np.zeros((2, 3, 3), np.uint8)
print("zeros 2x3x3 >>>")
print("blue.dtype: ", blue.dtype)
print("blue.ndim: ", blue.ndim)
print("blue.shape: ", blue.shape)
print("blue.size: ", blue.size)
print(f"blue = \n{blue}")

blue_01 = np.zeros((3, 3, 3), np.uint8)
print("zeros 3x3x3 >>>")
print(f"blue_01 = \n{blue_01}")

blue_02 = np.zeros((3, 4, 3), np.uint8)
print("zeros 3x4x3 >>>")
print(f"blue_02 = \n{blue_02}")

blue_03 = np.zeros((3, 4, 5), np.uint8)
print("zeros 3x4x5 >>>")
print(f" before blue_03 = \n{blue_03}")

blue_03[0, 0, 0] = 10
blue_03[1, 0, 0] = 20
blue_03[0, 0, 4] = 30
blue_03[1, 0, 4] = 40

print(f" after blue_03 = \n{blue_03}")
print("blue_03[0, 0, 4]: ", blue_03[0, 0, 4])
print("blue_03[0][0][4]: ", blue_03[0][0][4])
print("blue_03[1, 0, 0]: ", blue_03[1, 0, 0])
print("blue_03[1][0][0]: ", blue_03[1][0][0])
print("blue_03[1, 0, 4]: ", blue_03[1, 0, 4])
print("blue_03[1][0][4]: ", blue_03[1][0][4])

print("create blue 3D array")

print("-" * 88)
blue_img = np.zeros((5, 9, 3), np.uint8)
blue_img[:, : , 0] = 255

print("blue_img 5x9x3 >>>")
print("blue_img.dtype: ", blue_img.dtype)
print("blue_img.ndim: ", blue_img.ndim)
print("blue_img.shape: ", blue_img.shape)
print("blue_img.size: ", blue_img.size)
print(f"blue_img = \n{blue_img}")
#cv2.imshow("blue image", blue_img)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

"""
print("-" * 88)
blue_01_img = np.zeros((50, 90, 3), np.uint8)
blue_01_img[:, : , 0] = 255

blue_01_img[20:30, :, 0] = 0

print("blue_01_img 50x90x3")
print(f"blue_01_img = \n{blue_01_img}")
cv2.imshow("blue 01 image", blue_01_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
print("-" * 88)
iron_man_id_head_img = cv2.imread("iron_man_id_head.jpg")

print("iron_man_id_head_img.dtype: ", iron_man_id_head_img.dtype)
print("iron_man_id_head_img.ndim: ", iron_man_id_head_img.ndim)
print("iron_man_id_head_img.shape: ", iron_man_id_head_img.shape)
print("iron_man_id_head_img.size: ", iron_man_id_head_img.size)
print(f"iron_man_id_head_img = \n{iron_man_id_head_img}")

iron_man_id_head_img[115:210, 110:210] = [255, 0, 255]
cv2.imshow("iron man image", iron_man_id_head_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

