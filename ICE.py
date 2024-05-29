#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install bing-image-downloader')
from bing_image_downloader import downloader 
get_ipython().system('pip install pillow')

import os


# In[14]:


import os


# In[25]:


def download_images(query, limit, output_dir):
    try:
        downloader.download(query, limit=limit, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60)
    except Exception as e:
        print(f"An error occurred while downloading images for query '{query}': {e}")
        
def display_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            with Image.open(image_path) as img:
                img.show()

if __name__ == "__main__":
    download_images("Nicolas Cage Face", 5, "data/cage")  # Limiting to 5 images for display
    display_images("data/cage")
    
    download_images("Men's Faces", 5, "data/others")  # Limiting to 5 images for display
    display_images("data/others")


# In[ ]:




