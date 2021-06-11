import numpy as np
import PIL
import PIL.Image
from matplotlib import pyplot as plt


def exe3():
    # exe 3.1
    img = PIL.Image.open("lena.jpg").convert('L')
    img_seq = img.getdata()
    img_arr = np.array(img_seq).reshape(256, 256) * (1.0 / 255)
    u, s, vh = np.linalg.svd(img_arr)
    print(s)

    # exe 3.2
    # p = 256
    p = 256
    k = 2
    while k <= p:
        new_arr = np.dot(np.dot(u[:, :k], np.diag(s[:k])), vh[:k, :])
        y = np.asarray(new_arr * 255, dtype=np.uint8)
        w = PIL.Image.fromarray(y, mode='L')
        w.save("out_" + str(k) + ".png")
        k = k * 2

    # exe 3.3

    plt.plot(range(1, p+1), s)
    plt.xlabel("k")
    plt.ylabel("singular value")
    plt.show()


if __name__ == '__main__':
    exe3()
