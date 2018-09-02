# Python Image Converter
Converts image files between any types supported by [ImageMagick](https://www.imagemagick.org/) via [Wand](http://docs.wand-py.org/).

## Usage
Quickly take files via command line and convert them to `jpg`
```bash
python3 img-convert.py <file1> [file2] [...]
```

Conversion between some other file types is supported
```python
files = ['dog-pic.heic', 'other-photo.heic']
ic = ImageConverter(files)
ic.convert_to_jpg()
ic.convert_to_png()
ic.convert_to_gif()
```

Or if you're fancy, roll your own
```python
ic.convert('.tiff')  # ???
```

## Installation

#### For Windows
1. Download and install an [ImageMagick binary release](https://legacy.imagemagick.org/script/binary-releases.php#windows)
2. ```pip install Wand```

#### For Mac/Linux
1. I don't know, there's probably some package for it in homebrew/yum/apt-get.
2. Otherwise, choose a binary release of your flavor from the [ImageMagick website](https://legacy.imagemagick.org/script/binary-releases.php)
3. ```pip install Wand```
