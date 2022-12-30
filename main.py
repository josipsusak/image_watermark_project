from PIL import Image, ImageDraw, ImageFont
import easygui


def watermark_text(input_image_path, text, pos):
    # Open the image you want to add watermark to
    image = Image.open(input_image_path)

    # Make the image editable
    edit_image = ImageDraw.Draw(image)

    # Add parameters for text fill, font, position ( creates watermark in top left corner)
    black = (3, 8, 12)
    font = ImageFont.load_default()
    edit_image.text(pos, text, fill=black, font=font)
    # Show the image using PIL
    image.show()
    # Save the image on output path
    image.save(easygui.filesavebox("Choose location to save your watermarked image:"))


if __name__ == "__main__":
    img = easygui.fileopenbox("Choose your image to watermark:")
    watermark_text(img, text="Watermarked image", pos=(0, 0))
