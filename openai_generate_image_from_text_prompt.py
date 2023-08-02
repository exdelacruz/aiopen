# -*- coding: utf-8 -*-

import urllib.request
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import openai
import os
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image
import os
import urllib.request
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import openai

# Set your OpenAI API Key here. Replace "YOUR_API_KEY" with your actual API key.
openai.api_key = "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"

def generate_image(input_string): 
  response = openai.Image.create(
    prompt=input_string,
    n=1,
    size="512x512"
  )
  image_url = response['data'][0]['url']
  return image_url

if __name__ == "__main__":
    input_string = "a bird in the branch of the tree"
    output = generate_image(input_string)
    print(f"Input: {input_string}\nOutput: {output}")

    urllib.request.urlretrieve(output, 'output.png')
    img = Image.open('output.png')
    img_array = np.array(img)

    plt.figure(figsize=(9, 9))
    ax = plt.axes(xticks=[], yticks=[])
    ax.imshow(img_array)
    plt.show()
