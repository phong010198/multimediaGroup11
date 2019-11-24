from scipy import fftpack
from scipy import misc
from matplotlib import pyplot

# tạo cửa sổ hiện thị ảnh
fig = pyplot.figure(figsize=(10, 3))

# tạo ảnh mẫu
face = misc.face()
pyplot.imsave("input.png", face, format="png")

# đọc ảnh
image = pyplot.imread("input.png", format="png")

# thêm ảnh trước khi biến đổi Fourier vào cửa sổ
ax1 = fig.add_subplot(1, 3, 1)
pyplot.imshow(image)

# áp dụng biến đổi Fourier
fft_data = fftpack.fft2(image)
#chuyển kết từ dạng số phức về ảnh dạng số thực 
fft_image = fft_data.astype(float)

# thêm ảnh sau khi biến đổi Fourier vào cửa sổ
ax2 = fig.add_subplot(1, 3, 2)
pyplot.imshow(fft_image)

# áp dụng biến đổi Fourier ngược
ifft_data = fftpack.ifft2(fft_data)
#chuyển kết từ dạng số phức về ảnh dạng số thực 
ifft_image = ifft_data.astype(float)

# thêm ảnh sau khi biến đổi Fourier vào cửa sổ
ax3 = fig.add_subplot(1, 3, 3)
pyplot.imshow(ifft_image)

# hiển thị cửa sổ kết quả
ax1.title.set_text("Input")
ax2.title.set_text("fft2")
ax3.title.set_text("ifft2")
pyplot.show()

