import os
import dateutil.parser
import ffmpeg

from time import strftime, strptime, localtime
from pprint import pprint # for printing Python dictionaries in a human-readable way
from PIL import Image
from rename_media_files.config.config import AppArgs

__all__ = ['main']

def main(args: AppArgs) -> str:
    datetime_format = '%Y%m%d_%H%M%S'

    def convert_epoch_to_datetime(epoch):
        # `epoch` is returned by lstat (int)
        return strftime(datetime_format, localtime(epoch))

    def convert_creation_time_to_datetime(ctime):
        # `ctime` is returned by ffprobe (str)
        parsed = dateutil.parser.parse(ctime)
        rc = parsed.strftime(datetime_format)
        return rc

    def convert_creation_time_to_datetime_exif(ctime):
        # `ctime` is returned by PIL.Image.getexif (str)
        # 2006:09:09 20:36:30
        parsed = strptime(ctime, "%Y:%m:%d %H:%M:%S")
        return strftime(datetime_format, parsed)

    def get_datetime_of_file(path):
        lstat = os.lstat(path)
        return convert_epoch_to_datetime(lstat.st_ctime)

    def parse_metadata(path):
        try:
            # try videos first
            ctime = ffmpeg.probe(path)["format"]["tags"]["creation_time"]
            rc = convert_creation_time_to_datetime(ctime)
        except KeyError:
            if args['verbose']:
                print(path + " => No such key is available. Falling back to image parsing.")
            with Image.open(path) as im:
                exif = im.getexif()
                if args['verbose']:
                    print(path + " => Exif data: " + str(exif.get(306)))
                rc = convert_creation_time_to_datetime_exif(exif.get(306))
        return rc

    if args['input']:
        # `input` is a list, elements are files
        pprint(args['input'])
        for item in args['input']:
            if os.path.isfile(item):
                dt = parse_metadata(item)
                print(item + " => Parsed datetime: " + dt)
            else:
                print(item + " is not a file, you may need to use globs")
    else:
        print(args)

    return "Renaming completed successfully."