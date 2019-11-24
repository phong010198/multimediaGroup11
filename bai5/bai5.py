import matplotlib.pyplot as plt
from numpy import zeros

# khoi tao figure
fig = plt.figure(figsize=(5, 5))

# khởi tạo ma trận điểm ảnh rỗng
imga = zeros([800, 800, 3])
h = len(imga)
w = len(imga[0])

R = 0
G = 1
B = 2

# khởi tạo bàn cờ trắng đen
check = False
for y in range(h):
    if y % (h / 8) == 0:
        check = not check
    for x in range(w):
        if x % (w / 8) == 0:
            check = not check
        if check:
            imga[y][x][R] = 1
            imga[y][x][G] = 1
            imga[y][x][B] = 1
        else:
            imga[y][x][R] = 0
            imga[y][x][G] = 0
            imga[y][x][B] = 0

# lưu ảnh
plt.imsave("chessboard.png", imga, format="png")
# hiển thị ảnh
fig.add_subplot(2, 2, 1)
plt.imshow(imga)

# tạo ảnh gradient từ phải sang
for y in range(h):
    for x in range(w):
        imga[y][x][R] = 1  # red channel
        imga[y][x][G] = 0  # green channel
        imga[y][x][B] = x / float(w)  # blue channel

# lưu ảnh
plt.imsave("ngang.png", imga, format="png")
# hiển thị ảnh
fig.add_subplot(2, 2, 2)
plt.imshow(imga)

# tạo ảnh gradient từ trên xuống
for y in range(h):
    for x in range(w):
        imga[y][x][R] = 1  # red channel
        imga[y][x][G] = 0  # green channel
        imga[y][x][B] = y / float(h)  # blue channel

# lưu ảnh
plt.imsave("doc.png", imga, format="png")
# hiển thị ảnh
fig.add_subplot(2, 2, 3)
plt.imshow(imga)

# tạo ảnh gradient chéo
for y in range(h):
    for x in range(w):
        imga[y][x][R] = 1  # red channel
        imga[y][x][G] = 0  # green channel
        imga[y][x][B] = (x + y) / float(w + h)  # blue channel

# lưu ảnh
plt.imsave("cheo.png", imga, format="png")
# hiển thị ảnh
fig.add_subplot(2, 2, 4)
plt.imshow(imga)

# hiển thị
plt.show()