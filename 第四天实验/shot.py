from PIL import ImageGrab

def shot(path):
    pic = ImageGrab.grab()
    pic.save(path)


