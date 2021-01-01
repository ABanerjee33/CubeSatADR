
Space Debris - v1 2020-12-31 8:22 PM
==============================

This dataset was exported via roboflow.ai on January 1, 2021 at 7:10 PM GMT

It includes 566 images.
Space-debris are annotated in Tensorflow TFRecord (raccoon) format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)
* Auto-contrast via adaptive equalization

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip


