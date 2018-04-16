from PIL import Image
import shutil, os


class ImageCropper:

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


source = '/Users/user/PycharmProjects/instgram1/media/photos/'

destination = '/Users/user/PycharmProjects/instgram1/media/photos/crop_x1'
"""
for files in os.listdir(source):
    if files.endswith('.png' or '.jpg' or '.jpeg' or '.gif'):
        cropper = ImageCropper()
        cropped = cropper.crop_x1(source + files)
"""
