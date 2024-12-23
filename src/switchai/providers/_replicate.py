from PIL import Image

from ..types import ImageGenerationResponse


class ReplicateImageGenerationResponseAdapter(ImageGenerationResponse):
    def __init__(self, response):
        images = []
        for image_file in response:
            pil_image = Image.open(image_file)
            images.append(pil_image)

        super().__init__(images=images)