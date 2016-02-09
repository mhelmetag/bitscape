import random
from PIL import Image

class Mirror:
    '''Mirror BitArt Generator'''
    def __init__(self, size):
        self.image_format = 'PNG'

        # sizing
        self.final_image_size = (size, size)

        # colors
        self.background_color = (200, 200, 200)
        self.pattern_color = self.rgb_color_sample()

    # generate base and crop squares from random grid and recolors and repastes them
    def generate_image(self):
        base_image_size = (200, 200)

        grid_arr = self.create_grid()
        grid_samples = self.choose_random_grid(grid_arr)
        image = Image.new('RGB', base_image_size, self.background_color)

        self.draw_blocks(image, grid_samples)
        self.mirror_image(image)
        image = self.resize_image(image)

        return image


    # generate an array of grid tuples like [(x1, y1, x2, y2), (x3, y3, x4, y4), ...]
    def create_grid(self):
        grid_arr = []

        for x in range(1, 5):
            for y in range(1 ,9):
                bx1 = x * 20
                by1 = y * 20
                bx2 = bx1 + 20
                by2 = by1 + 20
                grid_arr.append((bx1, by1, bx2, by2))

        return grid_arr

    # choose a few random squares from the grid array
    def choose_random_grid(self, grid_arr):
        k = random.randint(8, 24)
        grid_samples = random.sample(grid_arr, k)

        return grid_samples

    # draw blocks with from sampled grid arr
    def draw_blocks(self, image, grid_samples):
        for sample in grid_samples:
            image.paste(self.pattern_color, sample)

    # mirror right half to right half
    def mirror_image(self, image):
        left_box = (20, 20, 100, 180)
        right_box = (100, 20, 180, 180)

        left_copy = image.crop(left_box)
        left_copy = left_copy.rotate(180)
        image.paste(left_copy, right_box)

    # sample a random-ish rgb color that fits the pastel theme
    def rgb_color_sample(self):
        r = random.randint(120, 240)
        g = random.randint(120, 240)
        b = random.randint(120, 240)

        return (r, g, b)

    def resize_image(self, image):
        if image.size == self.final_image_size:
            return image
        else:
            new_image = image.resize(self.final_image_size)
            return new_image

    def test(self):
        image = self.generate_image()
        image.save('test.png')
