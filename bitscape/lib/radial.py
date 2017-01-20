from math import sin, cos, degrees

from PIL import Image, ImageDraw


class Radial(object):
    def __init__(self, size, seed_color):
        self.image_format = 'PNG'

        # sizing
        self.final_image_size = (size, size)

        # coloring
        self.background_color = (200, 200, 200)
        self.seed_color = seed_color

    def generate_image(self):
        base_image_size = (500, 500)
        image = Image.new('RGB', base_image_size, self.background_color)
        self.draw_center(image)
        image = self.resize_image(image)
        return image

    def draw_center(self, image):
        draw = ImageDraw.Draw(image)
        draw.ellipse(
            (25, 25, 175, 175), outline=(100, 100, 100),
            fill=(100, 100, 100)
        )

    def spiral(self, image, revolutions):
        for revoltion in revolutions:
            self.draw_revolution

    def radian_range(self):
        list((math.degrees(x) for x in range(0, 360) if x % self.increments == 0))

    def draw_revolution(self, image)
        # x = cx + r * cos(a)
        # y = cy + r * sin(a)

    def resize_image(self, image):
        if image.size == self.final_image_size:
            return image
        else:
            new_image = image.resize(self.final_image_size)
            return new_image

    def test(self):
        image = self.generate_image()
        image.save('test.png')
