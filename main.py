from PIL import Image

from graph import Graph
from resolution import Resolution

if __name__ == '__main__':
    graph = Graph()
    graph.__str__()
    graph.write_base_graph()

    image_file = Image.open("base_pic.bmp")  # open colour image
    image_file = image_file.convert('1')  # convert image to black and white
    image_file.save('base_pic.bmp')
#