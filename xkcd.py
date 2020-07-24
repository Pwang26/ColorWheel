import tkinter
import colorsys
import math

# Make the window large so that we can see more detail.
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000
BIG_CIRCLE_RADIUS = 450
DATA_FILE = 'small.txt'
DOT_SIZE = 4


def main():
    # get a drawing canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'XKCD Colors')

    dataset = load_data()
    while True:
        query = input('Color name: ')
        query = query.lower()
        if query == 'clear':
            canvas.delete("all")
        elif query in dataset:
            colors = dataset[query]
            display_colors(canvas, colors)
        elif query == '':
            break
        canvas.update()


def display_colors(canvas, color_list):
    for color in color_list:
        r = color[0]
        g = color[1]
        b = color[2]
        plot_color(canvas, r, g, b)


def plot_color(canvas, r, g, b):
    hsv = colorsys.rgb_to_hsv(r / 256, g / 256, b / 256)

    radius = BIG_CIRCLE_RADIUS * hsv[1]

    theta = hsv[0] * math.pi * 2.0

    x = CANVAS_WIDTH / 2.0 + radius * math.cos(theta)
    y = CANVAS_HEIGHT / 2.0 - radius * math.sin(theta)

    color_str = colorstr_from_rgb(r, g, b)
    plot_pixel(canvas, x, y, color_str)


def plot_pixel(canvas, x, y, color_str):
    # Create a 1x1 rectangle
    canvas.create_oval(x, y, x+DOT_SIZE, y+DOT_SIZE,
                       fill=color_str, outline=color_str)


def load_data():
    data = {}
    file = open(DATA_FILE)
    n_colors = 0
    for line in file:
        line = line.strip()
        add_color(data, line)
        n_colors += 1
    # print(len(data), n_colors)
    file.close()
    return data


def add_color(data, line):
    parts = line.split(',')
    color_name = parts[0]
    color_rgb = color_from_line(line)
    if color_name not in data:
        data[color_name] = []
    data[color_name].append(color_rgb)


def color_from_line(line):
    parts = line.split(',')
    r = int(parts[1])
    g = int(parts[2])
    b = int(parts[3])
    return [r, g, b]


def colorstr_from_rgb(red, green, blue):
    assert 0 <= red <= 256
    assert 0 <= green <= 256
    assert 0 <= blue <= 256
    return "#%02x%02x%02x" % (red, green, blue)

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.


def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()