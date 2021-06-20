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

### Average Colour Distance

The following functions calculate colour difference between all pixels in two images, and provide averages.

#### Simple RGB Euclidean Distance

![Simple Euclidean Distance Formula](https://github.com/pbiswell/pixeldifference/blob/master/assets/SimpleEuclideanDistance.svg)

```
ed = PixelDifference(imageOne, imageTwo).EuclideanDistance()

# Average value
ed.average
# Minimum value
ed.min
# Maximum value
ed.max
# Median value
ed.median
# Time taken
ed.elapsed
```

#### More Accurate RGB Euclidean Distance

```
ed2 = PixelDifference(imageOne, imageTwo).EuclideanDistance2()

# Average value
ed2.average
# Minimum value
ed2.min
# Maximum value
ed2.max
# Median value
ed2.median
# Time taken
ed2.elapsed
```

#### Redmean

```
redmean = PixelDifference(imageOne, imageTwo).Redmean()

# Average value
redmean.average
# Minimum value
redmean.min
# Maximum value
redmean.max
# Median value
redmean.median
# Time taken
redmean.elapsed
```

### CIE76 - LAB Colour Distance



```
cie76 = PixelDifference(imageOne, imageTwo).CIE76()

# Average value
cie76.average
# Minimum value
cie76.min
# Maximum value
cie76.max
# Median value
cie76.median
# Time taken
cie76.elapsed
```

### Images of Different Size

Update 1.0.1: Will now automatically crop images to an area which exists in both images, starting at the top left corner.
### Image File Sizes

You can compare the file sizes of the images. File sizes are returned in bytes.

```python
pd = PixelDifference(imageOne, imageTwo)

# File size of image 1 in bytes
filesize1 = pd.filesize[0]

# File size of image 2 in bytes
filesize2 = pd.filesize[1]

# File size difference in bytes, of image 2 compared to image 1
# If image 2 is smaller, the result is negative
diff = pd.filesizedifference
```

### Time Elapsed

You can see how long it took to calculate with .elapsed

```python
pd = PixelDifference(imageOne, imageTwo)

# Elapsed time to calculate differences
pd.elapsed
```

## Features

- Compare two images for differences, pixel by pixel
- Use different sized images
- Image difference in pixels, and percentage of total area

## To Do

- Improve file size comparison
- Improve Readme
- Command line arguments
- More tests
- Handle images from string paths
- Performance tests/improvements
- Allow for more than 2 images
- More comparisons in LAB
- Code slow operations in C
- Get colour of specific pixels
- Transparency

## Changes

-v1.0.1 

    - Added file sizes and comparison
    Usage:
    pd.filesize[0]
    pd.filesize[1]
    pd.filesizedifference

    - Added time taken
    Usage:
    pd.elapsed

    - Added overall average percentage difference
    Usage:
    print(wa.overalldifference)

    - Added CIE76 distance
    - Added RGB simple euclidean distance
    - Added More accurate euclidean distance
    - Added Redmean

-v1.0.0 (June 12th, 2021)

    Initial release