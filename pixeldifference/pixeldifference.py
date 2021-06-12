"""
Name: PixelDifference
Author: Paul Biswell
Version: 1.0.0
Link: https://github.com/pbiswell/pixeldifference
"""

from PIL import Image
import logging

class PixelDifference:
    def __init__(self, img1, img2, convert2Hex=False, ignoreSize=False):
        self.img1 = img1
        self.img2 = img2
        self.convert2Hex = convert2Hex
        self.ignoreSize = ignoreSize
        self.total = 0
        self.percentage = 0
        self.pixels = 0
        self.Setup()
        
    def Percentage(self, part, full):
        """ Returns percentage """
        return 100 * float(part)/float(full)
        
    def ConvertRGB(self, pixels):
        """ Converts RGB to Hexadecimal Eg. #FFFFFF """
        return f"#{''.join(f'{hex(c)[2:].upper():0>2}' for c in pixels)}"
        
    def Setup(self):
        # Sort out and check sizes
        width1, height1 = self.img1.size
        width2, height2 = self.img2.size
        checkingwidth = min(width1, width2)
        checkingheight = min(height1, height2)
        
        # Make sure images have width and height
        if 0 in {checkingwidth, checkingheight}:
            logging.error(
                "Width or height of one or both images is 0.")
            return
        
        if (width1, height1) != (width2, height2) and self.ignoreSize is False:
            logging.error("Images are not the same size. To check partial size, do PixelDifference(img1, img2, ignoreSize=True)")
        else:
            # Check all pixels
            pix1 = self.img1.load()
            pix2 = self.img2.load()
            ii = 0             
            for i in range(checkingwidth):
                for j in range(checkingheight):
                    if self.convert2Hex:
                        if self.ConvertRGB(pix1[i, j]) != self.ConvertRGB(pix2[i, j]):
                            ii += 1
                    elif pix1[i, j] != pix2[i, j]:
                        ii += 1
            # Results
            self.total = checkingwidth * checkingheight
            self.pixels = ii
            self.percentage = self.Percentage(ii, self.total)