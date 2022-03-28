import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import STOPWORDS, WordCloud


def read_sub_file(path: str) -> str:
    with open(path) as subtitle:
        text = subtitle.read()
    return text


def read_mask_image(path: str) -> np.ndarray:
    with Image.open(path) as image:
        mask = np.array(image)
    return mask


def generate_stopwords_set(path: str) -> set:
    with open(path) as file:
        stop_words = STOPWORDS
        stop_words.update(file.read().splitlines())
    return stop_words


def main() -> None:
    text = read_sub_file(
        "subtitle_files/Mazda Miata Documentaries NB EP3 Slow Evolution.txt"
    )

    mask = read_mask_image("mask_images/NB.png")

    stop_words = generate_stopwords_set("stop_words.txt")

    # Generate a word cloud image
    wordcloud = WordCloud(
        stopwords=stop_words,
        max_words=200,
        background_color=None,
        mode="RGBA",
        color_func=lambda *args, **kwargs: (0, 0, 0),
        mask=mask,
        include_numbers=True,
    ).generate(text)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("figure_test.png", transparent=True, dpi=300)


if __name__ == "__main__":
    main()
