from PIL import Image


class ImageCropper:
    """
    Crops original photo to 3 given sizes
    """
    def crop(self, photo, width, height):
        img = Image.open(photo)
        half_the_width = img.size[0] / 2
        half_the_height = img.size[1] / 2

        image = img.crop(
            (
                half_the_width - width,
                half_the_height - height,
                half_the_width + width,
                half_the_height + height,
            )
        )
        image.save(photo)

    def crop_x1(self, photo):
        return self.crop(photo, 150, 150)

    def crop_x2(self, photo):
        return self.crop(photo, 300, 300)

    def crop_x3(self, photo):
        return self.crop(photo, 450, 450)

    def crop_x05(self, photo):
        return self.crop(photo, 75, 75)
