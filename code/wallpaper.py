"""
Functions to help creating wallpapers
"""
import pathlib
import skimage.io
import skimage.transform
import skimage.exposure


def save(rgb, folder, prefix):
    """
    Save 4k and 720p versions of the figure.
    """
    image = rgb.values[::-1, :, :3]
    
    # Rescale so that one of the sides matches the 4k resolution
    if image.shape[1] / image.shape[0] > 16 / 9:
        factor = 2160 / image.shape[0]
        shape = (2160, image.shape[1] * factor, image.shape[2])
    else:
        factor = 3840 / image.shape[1]
        shape = (image.shape[0] * factor, 3840, image.shape[2])
    image = skimage.exposure.rescale_intensity(
        skimage.transform.resize(image, shape),
        out_range="uint8",
    )

    # Crop to exactly 16:9
    x_offset = int((image.shape[1] - 3840) // 2)
    y_offset = int((image.shape[0] - 2160) // 2)
    image = image[y_offset:2160 + y_offset, x_offset:3840 + x_offset, :]
    assert image.shape[1] == 3840 and image.shape[0] == 2160

    # Make a 720p version
    image_720p = skimage.exposure.rescale_intensity(
        skimage.transform.resize(image, (720, 1280, image.shape[2])), 
        out_range="uint8",
    )

    # Save both to the desired folder
    folder = pathlib.Path(folder)
    skimage.io.imsave(folder / f"{prefix}.jpg", image, quality=100)
    skimage.io.imsave(folder / f"{prefix}-720p.jpg", image_720p, quality=95)
    return image, image_720p
