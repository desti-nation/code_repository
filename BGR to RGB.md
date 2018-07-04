Conversion between any/all of BGR, RGB, and GBR may be necessary when working with

- [Matplotlib](https://www.scivision.co/tag/#matplotlib) `pyplot.imshow()`: `M x N x 3` image, where last dimension is RGB.
- [OpenCV](https://www.scivision.co/tag/#opencv) `cv2.imshow()`: `M x N x 3` image, where last dimension is BGR
- Scientific Cameras: some output `M X N x 3` image, where last dimension is GBR

Python BGR to RGB code: [RGB_BGR_GBR_conv.py](https://github.com/scivision/pyimagevideo/)

### BGR to RGB

OpenCV image to Matplotlib

```
rgb = bgr[...,::-1]

```

### RGB to BGR

Matplotlib image to OpenCV

```
bgr = rgb[...,::-1]

```

### RGB to GBR

```
gbr = rgb[...,[2,0,1]]

```

### Axis order for Python images

- 3-D: W x H x 3, where the last axis is color (e.g. RGB)
- 4-D: W x H x 3 x 1, where the last axis is typically an alpha channel