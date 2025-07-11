# -*- coding: utf-8 -*-
"""Augmentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N7YIOdbCgZ5bpoiGl06GYwKlPAFcQNyu
"""

from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array

img_path='/content/f3.jpeg'
img=load_img(img_path)
img_array=img_to_array(img)

img_array=img_array.reshape((1,)+img_array.shape)

datagen=ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

augmented_images=datagen.flow(img_array,batch_size=1)

def visualize_augmented_images(generator,num_images):
  fig,axes=plt.subplots(1,num_images,figsize=(20,20))
  for i in range(num_images):
    batch=next(generator)
    aug_image=batch[0]
    axes[i].imshow(aug_image)
    axes[i].axis('off')
  plt.show()

visualize_augmented_images(augmented_images,10)

def visualize_augmented_images_with_original(original_image, generator, num_images):
    fig, axes = plt.subplots(1, num_images + 1, figsize=(20, 20))

    # Display original image (clip and convert to uint8 for safety)
    img = np.clip(original_image, 0, 255).astype('uint8')
    axes[0].imshow(img)
    axes[0].set_title("Original")
    axes[0].axis('off')

    for i in range(1, num_images + 1):
        batch = next(generator)
        aug_img = batch[0]

        # Some generators normalize images to [0,1], scale back if needed
        if aug_img.max() <= 1.0:
            aug_img = (aug_img * 255).astype('uint8')
        else:
            aug_img = np.clip(aug_img, 0, 255).astype('uint8')

        axes[i].imshow(aug_img)
        axes[i].set_title(f"Augmented {i}")
        axes[i].axis('off')

    plt.show()

visualize_augmented_images_with_original(img_array[0], augmented_images, 1)

