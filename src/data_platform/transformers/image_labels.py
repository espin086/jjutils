import io
import os
import sys

import pandas as pd
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

titles = ["the_predator"]
frame_count = 3581


def annotate_frame(frame):
    """
    Anotates an image using Google Cloud Vision
    """
    results = []
    frame = frame
    # loads image into memory
    with io.open(frame, "rb") as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    # Performs image detection
    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:
        results.append(label.description)
    return results


def main(frame):
    results = annotate_frame(frame)
    return results


if __name__ == "__main__":
    frame_path = sys.argv[1]
    print(main(frame_path))
