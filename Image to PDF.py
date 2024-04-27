from PIL import Image
image_path = Image.open("rohit.jpg")
image_path = image_path.convert("RGB")
image_path.save("rohit.pdf")
