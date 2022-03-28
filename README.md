# WordCloud_Miata

I wanted to study Savagegeese series about four generations of miata: https://www.youtube.com/playlist?list=PLr-mTF1DFa-uYhVy6flJn83IiqLWgdssr

I downloaded .srt generated from the videos, created svg files with Inkscape of four generations profile cars and used Wordcloud module to put all together.

You will find 3 global variables in Miata_Wordcloud.py:
* SUB_FILE_PATH = the path to the subtitle text file from a youtube video
* MASK_IMAGE_PATH = the path to the mask image wordcloud should use to generate a new image
* STOP_WORDS_PATH =  list of words to exclude from the generated worldcloud

Tweak those files to change which generation of miata you want the worldcloud to be applied.

result of the script:
![Alt text](figure_test.png "Title")
example of what you can achieve for example (using gimp)
![Alt text](bitmap_1.png "Title")
