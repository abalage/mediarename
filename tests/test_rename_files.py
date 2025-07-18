import os
from mediarename.models.rename_files import rename_files


def test_rename_files_with_image_metadata(tmp_path, image_metadata_list):
    # Create dummy files based on metadata
    for meta in image_metadata_list:
        file_path = tmp_path / os.path.basename(meta.file_path)
        file_path.write_bytes(b"dummy data")
        meta.file_path = str(file_path)

    rename_files(image_metadata_list)

    # Check that files are renamed
    for meta in image_metadata_list:
        ext = os.path.splitext(meta.file_path)[1]
        expected_name = f"{meta.creation_date}{ext}"
        expected_path = os.path.join(tmp_path, expected_name)
        assert os.path.exists(expected_path)


def test_rename_files_with_audio_metadata(tmp_path, audio_metadata_list):
    # Create dummy files based on metadata
    for meta in audio_metadata_list:
        file_path = tmp_path / os.path.basename(meta.file_path)
        file_path.write_bytes(b"dummy audio")
        meta.file_path = str(file_path)

    rename_files(audio_metadata_list)

    # Check that files are renamed
    for meta in audio_metadata_list:
        ext = os.path.splitext(meta.file_path)[1]
        expected_name = f"{meta.creation_date}{ext}"
        expected_path = os.path.join(tmp_path, expected_name)
        assert os.path.exists(expected_path)


def test_rename_files_with_video_metadata(tmp_path, video_metadata_list):
    # Create dummy files based on metadata
    for meta in video_metadata_list:
        file_path = tmp_path / os.path.basename(meta.file_path)
        file_path.write_bytes(b"dummy video")
        meta.file_path = str(file_path)

    rename_files(video_metadata_list)

    # Check that files are renamed
    for meta in video_metadata_list:
        ext = os.path.splitext(meta.file_path)[1]
        expected_name = f"{meta.creation_date}{ext}"
        expected_path = os.path.join(tmp_path, expected_name)
        assert os.path.exists(expected_path)


def test_rename_files_skips_already_renamed(tmp_path, image_metadata_list):
    # Use the first image metadata from the fixture
    meta = image_metadata_list[0]
    file_path = tmp_path / f"{meta.creation_date}.jpg"
    file_path.write_bytes(b"dummy data")
    meta.file_path = str(file_path)
    # Should not rename, file already matches target name
    rename_files([meta])
    assert os.path.exists(file_path)


def test_rename_files_handles_missing_file(tmp_path, image_metadata_list):
    # Use the first image metadata from the fixture and set its path to a non-existent file
    meta = image_metadata_list[0]
    meta.file_path = str(tmp_path / "nonexistent.jpg")
    # Should not raise, even though file is missing
    rename_files([meta])
    assert True
