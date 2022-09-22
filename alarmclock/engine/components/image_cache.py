from PIL import Image, ImageChops

class ImageCache():

    def __init__(self) -> None:
        """
        Creates a new image cache.
        """
        self.image = None

    def cache_if_changed(self, new_image: Image) -> bool:
        """
        Caches a new image if it differs from the existing cached image.

        Args:
            new_image (Image): The new image
        Returns:
            bool: Value indicating whether the new image differs from the cached image.
        """
        image_is_changed = (
            self.image == None 
            or ImageChops.difference(
                self.image, 
                new_image).getbbox() != None
        )
    
        if image_is_changed:
            self.image = new_image
        
        return image_is_changed
