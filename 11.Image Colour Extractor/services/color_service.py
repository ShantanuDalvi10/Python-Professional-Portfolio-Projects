from PIL import Image
import numpy as np

def extract_top_colors(image):

    img_rgb = image.convert("RGB")

    img_array = np.array(img_rgb)
    img_array = img_array.reshape(-1,3)

    unique_colors,counts = np.unique(img_array,axis=0,return_counts=True)


    sorted_counts = np.argsort(counts)[::-1]

    top_10_indices = sorted_counts[:10]


    top_10_colors = unique_colors[top_10_indices]
    top_10_counts = counts[top_10_indices]

    colors = []

    for color ,count in zip(top_10_colors,top_10_counts):
        hex_code = "#{:02X}{:02X}{:02X}".format(*color)
        color_data = {
            "rgb":tuple(color),
            "frequency":int(count),
            "hex":f"{hex_code}"
        }
        colors.append(color_data)
    return colors

