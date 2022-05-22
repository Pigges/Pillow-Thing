# Pillow Thing
A simple script to do some image manipulation with the [PILLOW](https://python-pillow.org/) package, made in Python.

## Filters
| Filter          |                               Description                                |
|:----------------|:------------------------------------------------------------------------:|
| Gray scale      |       Very simple, removes the color and makes it black and whiteI       |
| Color shift     |   Shift the colors one step; red => green, green => blue, blue => red    |
| Invert color    |                   Inverts each color; 255 - value                    |
| Brighter (1-10) |                  Brighten the image by the value factor                  |
| Darker (1-10)   |                   Darken the image by the value factor                   |
| Noise (1-3)     |                Create noise in the image 1-3, little-much                |
| Pixelate (1-10) | Pixelate the image by downsizing it and then upscale it back to original |
| Blur (1-10)     |                Blur the image through the gaussian method                |