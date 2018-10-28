import os
import sys
import glob
from typing import List

from wand.image import Image


class ImageConverter:
    """
    Manages image file conversions to other formats
    """

    HEIC = '.heic'
    JPG = '.jpg'
    PNG = '.png'
    GIF = '.gif'

    ALLOWED_EXTS = [HEIC, JPG, PNG, GIF]

    def __init__(self, files: List[str]):
        self.files = files

    def _check_files_exist(self) -> None:
        for file in self.files:
            if not os.path.isfile(file):
                print(f"{file} not found!")
                exit(1)

    @staticmethod
    def _get_target_file(file: str, to_ext: str) -> str:
        return os.path.splitext(file)[0] + to_ext

    @staticmethod
    def _save(img: Image, to_file: str) -> None:
        with img.clone() as out_img:
            out_img.save(filename=to_file)
            print(f"Saved file: {to_file}")

    def convert(self, to_ext: str) -> None:
        self._check_files_exist()
        for file in self.files:
            to_file = self._get_target_file(file, to_ext)
            with Image(filename=file) as img:
                self._save(img, to_file)

    def convert_to_jpg(self) -> None:
        self.convert(ImageConverter.JPG)

    def convert_to_png(self) -> None:
        self.convert(ImageConverter.PNG)

    def convert_to_gif(self) -> None:
        self.convert(ImageConverter.GIF)


def validate_args():
    if len(sys.argv) < 2:
        print(f"Usage: {__file__} <file1|directory1> [file2|directory2] [...]")
        exit(1)

    arg = sys.argv[1]
    files = []
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            files.append(arg)
        elif os.path.isdir(arg):
            for ext in ImageConverter.ALLOWED_EXTS:
                files_in_dir = glob.glob(os.path.join(arg, '*' + ext))
                files.extend([file for file in files_in_dir])
    return files


def main():
    files = validate_args()
    ImageConverter(files).convert_to_jpg()


if __name__ == '__main__':
    main()
