from PIL import Image, ImageColor
import numpy as np

if __name__ == '__main__':
    canvas_width, canvas_height = 960, 540
    arr = np.zeros([canvas_height, canvas_width, 3], dtype=np.uint8)
    for x in range(canvas_width):
        for y in range(canvas_height):
            arr[y, x, 0] = 255
            arr[y, x, 1] = 255
            arr[y, x, 2] = 255
    i = 0
    with open('datasets/DS8.txt') as ds:
        for line in ds:
            [y, x] = list(map(int, line.split()))
            y = canvas_height - y - 1
            i += 1
            if x < canvas_width and y < canvas_height:
                arr[y, x, 0] = 0
                arr[y, x, 1] = 0
                arr[y, x, 2] = 0
    print(i)
    img = Image.fromarray(arr)
    img.save('images/canvas.png')
