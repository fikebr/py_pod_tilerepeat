import os
import sys

from PIL import Image


def open_image(imagefile):
    return Image.open(imagefile)


def tile_image(image, times):
    # Calculate the size of the new image
    tile_width = image.width * times
    tile_height = image.height * times

    # Create a new image with white background
    tile_image = Image.new("RGBA", (tile_width, tile_height), (255, 255, 255, 0))

    for x in range(times):
        for y in range(times):
            # Paste the image into the new image
            tile_image.paste(image, (x * image.width, y * image.height))

    return tile_image


def main(imagefile, times=3):
    if not os.path.exists(imagefile):
        print("Image file does not exist.")
        return

    folder = os.path.dirname(imagefile)
    basename = os.path.basename(imagefile)
    filename, ext = os.path.splitext(basename)
    newfilename = f"{filename}_tiled_x{times}{ext}"
    newfilefull = os.path.join(folder, newfilename)

    image = open_image(imagefile)

    newimage = tile_image(image, times)

    newimage.save(newfilefull, dpi=(300, 300))  # Save the collage


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 3 or "--help" in sys.argv:
        script_filename = os.path.basename(__file__)
        print(f"Usage: python {script_filename} <imagefile> [times]")
        sys.exit(1)

    imagefile = sys.argv[1]
    if len(sys.argv) == 3:
        times = sys.argv[2]
    else:
        times = 3

    main(imagefile, int(times))
