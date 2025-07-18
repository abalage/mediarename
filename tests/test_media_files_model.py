import pytest
import os
from datetime import datetime
from mediarename.models.media_files_model import MediaFilesModel
from mediarename.config.config import FileMetadata


def test_media_files_model_with_directory(temp_media_files):
    dir_path, files = temp_media_files
    # Pass the directory to MediaFilesModel
    model = MediaFilesModel(
        files=[os.path.join(dir_path, f) for f in os.listdir(dir_path)],
        datetime_format="%Y-%m-%d"
    )
    metadata = model.metadata
    assert len(metadata) == 4
    file_types = {m.file_type for m in metadata}
    assert "image" in file_types
    assert "audio" in file_types
    assert "video" in file_types
    assert "other" in file_types


def test_media_files_model_with_single_file(temp_media_files):
    _, files = temp_media_files
    # Test with a single file
    model = MediaFilesModel(
        files=[files[0]],
        datetime_format="%Y-%m-%d"
    )
    metadata = model.metadata
    assert len(metadata) == 1
    assert metadata[0].file_type == "image"
    assert metadata[0].file_path.endswith(".jpg")


def test_media_files_model_forbidden_datetime_format(temp_media_files):
    _, files = temp_media_files
    # Use forbidden characters in datetime_format
    with pytest.raises(ValueError):
        MediaFilesModel(files, datetime_format="Y|M:D*H")


def test_media_files_model_modification_date_format(temp_media_files):
    _, files = temp_media_files
    model = MediaFilesModel(files, datetime_format="%Y-%m-%d")
    for meta in model.metadata:
        # Should match the format
        try:
            datetime.strptime(meta.modification_date, "%Y-%m-%d")
        except ValueError:
            pytest.fail("Modification date format is incorrect")


def test_media_files_model_with_unknown_file_type(tmp_path):
    # Create a file with an unknown extension
    unknown_file = tmp_path / "file.unknown"
    unknown_file.write_bytes(b"data")
    model = MediaFilesModel([str(unknown_file)], datetime_format="%Y-%m-%d")
    metadata = model.metadata
    assert len(metadata) == 1
    assert metadata[0].file_type == "other" or metadata[0].file_type == "unknown"


def test_media_files_model_with_empty_file_list():
    model = MediaFilesModel([], datetime_format="%Y-%m-%d")
    assert model.metadata == []


def test_media_files_model_modification_date_is_filesystem(tmp_path):
    # Create a file and check modification date matches filesystem
    file = tmp_path / "test.txt"
    file.write_text("abc")
    model = MediaFilesModel([str(file)], datetime_format="%Y-%m-%d")
    metadata = model.metadata[0]
    fs_date = datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y-%m-%d")
    assert metadata.modification_date == fs_date


def test_media_files_model_invalid_file_path(tmp_path):
    # Pass a non-existent file path
    fake_file = tmp_path / "does_not_exist.jpg"
    with pytest.raises(FileNotFoundError):
        MediaFilesModel([str(fake_file)], datetime_format="%Y-%m-%d")


def test_media_files_model_property_returns_metadata(temp_media_files):
    _, files = temp_media_files
    model = MediaFilesModel(files, datetime_format="%Y-%m-%d")
    assert isinstance(model.metadata, list)
    assert all(isinstance(m, FileMetadata) for m in model.metadata)
