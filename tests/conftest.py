import pytest
from rename_media_files.config.config import FileMetadata


@pytest.fixture
def temp_media_files(tmp_path):
    """
    Creates a temporary directory with dummy media files for testing.
    Returns the directory path and a list of file paths.
    """
    files = []
    # Create dummy image, audio, and video files
    image_file = tmp_path / "test_image.jpg"
    image_file.write_bytes(b"dummy image data")
    files.append(str(image_file))

    audio_file = tmp_path / "test_audio.mp3"
    audio_file.write_bytes(b"dummy audio data")
    files.append(str(audio_file))

    video_file = tmp_path / "test_video.mp4"
    video_file.write_bytes(b"dummy video data")
    files.append(str(video_file))

    other_file = tmp_path / "test_other.txt"
    other_file.write_text("dummy text data")
    files.append(str(other_file))

    return str(tmp_path), files


@pytest.fixture
def image_metadata_list():
    return [
        FileMetadata(
            file_path="images/photo1.jpg",
            creation_date="2023-01-01",
            modification_date="2023-01-02",
            file_type="image",
            mime_type="image/jpeg"
        ),
        FileMetadata(
            file_path="images/photo2.png",
            creation_date="2023-02-01",
            modification_date="2023-02-02",
            file_type="image",
            mime_type="image/png"
        )
    ]


@pytest.fixture
def audio_metadata_list():
    return [
        FileMetadata(
            file_path="audio/song1.mp3",
            creation_date="2022-05-01",
            modification_date="2022-05-02",
            file_type="audio",
            mime_type="audio/mpeg"
        ),
        FileMetadata(
            file_path="audio/song2.wav",
            creation_date="2022-06-01",
            modification_date="2022-06-02",
            file_type="audio",
            mime_type="audio/wav"
        )
    ]


@pytest.fixture
def video_metadata_list():
    return [
        FileMetadata(
            file_path="videos/movie1.mp4",
            creation_date="2021-07-01",
            modification_date="2021-07-02",
            file_type="video",
            mime_type="video/mp4"
        ),
        FileMetadata(
            file_path="videos/movie2.avi",
            creation_date="2021-08-01",
            modification_date="2021-08-02",
            file_type="video",
            mime_type="video/x-msvideo"
        )
    ]


def test_image_metadata_list_fixture(image_metadata_list):
    assert len(image_metadata_list) == 2
    assert image_metadata_list[0].file_type == "image"
    assert image_metadata_list[1].mime_type == "image/png"


def test_audio_metadata_list_fixture(audio_metadata_list):
    assert len(audio_metadata_list) == 2
    assert audio_metadata_list[0].file_type == "audio"
    assert audio_metadata_list[1].mime_type == "audio/wav"


def test_video_metadata_list_fixture(video_metadata_list):
    assert len(video_metadata_list) == 2
    assert video_metadata_list[0].file_type == "video"
    assert video_metadata_list[1].mime_type == "video/x-msvideo"
