# PixelDifference - Pixel differences between two images

## Intro

This package is for comparing pixel differences between two images. It will check the same pixel positions on both images. This can be used to compare how different an image is to the original after compression or editing.

If one image is cropped, for example, you can use ignoreSize=True to only compare the area which is present in both images.

## Requirements

You need python3 and pillow to use this package.

```
pip install pillow
```

## Installation

```
pip install pixeldifference
```

## Usage

```python
# Import packages
from pixeldifference import PixelDifference
from PIL import Image

# Load two images from your device
# You need to change the image paths to your images
imageOne = Image.open('/path/to/imageOne.jpg', 'r')
imageTwo = Image.open('/path/to/imageTwo.jpg', 'r')

# Initialise
pd = PixelDifference(imageOne, imageTwo)

# The total number of pixels checked
totalpixels = pd.total

# The percentage of different pixels compared to the total checked area
percentdifferent = pd.percent

# The total number of different pixels in the checked area
pixelsdifferent = pd.pixels
```

## Advanced Settings

### Images of Different Size

This will compare an area which exists in both images. Use this if one image is cropped, for example.

```python
# Use ignoreSize=True
pd = PixelDifference(imageOne, imageTwo, ignoreSize=True)
```

### Compare Pixels in Hexadecimal (eg. #FFFFFF)

This will convert all the pixels to hexadecimal values, like #FFFFFF, before comparison. The default compares the RGB values.

```python
# Use convert2Hex=True
pd = PixelDifference(imageOne, imageTwo, convert2Hex=True)
```

## Features

- Compare two images for differences, pixel by pixel
- Compare pixels in RGB or hexadecimal values
- Use different sized images
- Image difference in pixels, and percentage of total area

## To Do

- Add image file size comparison
- Improve Readme
- Command line arguments
- More tests
- Handle images from string paths
- Performance tests/improvements
- Allow for more than 2 images

## Changes

-v1.0.0 (June 12th, 2021)

    Initial release