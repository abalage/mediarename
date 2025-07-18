# mediarename

A package to mass rename media files based on their metadata.

## Features

- Batch renaming of media files (images, audios and videos) using metadata (e.g., EXIF, modification date)
- Supports various file types
- Command-line interface

## Installation

You need Python 3.11 or newer.

TODO: not released yet on pypi, use manual installation.

```sh
pip install mediarename
```

Or clone the repository and install locally:

```sh
git clone https://github.com/abalage/mediarename.git
cd mediarename
pipx install .
```

## Usage

After installation, use the CLI tool:

```sh
mediarename [OPTIONS] <directory>
```

Replace `<directory>` with the path containing your media files.

For more options, run:

```sh
mediarename --help
```

## License

GNU General Public License v3

## Links

- [Homepage](https://github.com/abalage/mediarename)
- [Changelog](https://github.com/abalage/mediarename/blob/master/changelog.md)
- [Report Issues](https://github.com/abalage/mediarename/issues)

---

Author: Balázs NÉMETH
