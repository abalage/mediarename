from rename_media_files.views.metadata_printer import MetadataPrinter


def test_print_file_paths_image(capsys, image_metadata_list):
    printer = MetadataPrinter(image_metadata_list)
    printer.print_file_paths()
    captured = capsys.readouterr()
    assert "File: images/photo1.jpg" in captured.out
    assert "File: images/photo2.png" in captured.out


def test_print_file_paths_audio(capsys, audio_metadata_list):
    printer = MetadataPrinter(audio_metadata_list)
    printer.print_file_paths()
    captured = capsys.readouterr()
    assert "File: audio/song1.mp3" in captured.out
    assert "File: audio/song2.wav" in captured.out


def test_print_file_paths_video(capsys, video_metadata_list):
    printer = MetadataPrinter(video_metadata_list)
    printer.print_file_paths()
    captured = capsys.readouterr()
    assert "File: videos/movie1.mp4" in captured.out
    assert "File: videos/movie2.avi" in captured.out


def test_print_metadata_list_image(capsys, image_metadata_list):
    printer = MetadataPrinter(image_metadata_list)
    printer.print_metadata_list()
    captured = capsys.readouterr()
    assert "File: images/photo1.jpg" in captured.out
    assert "  Creation date: 2023-01-01" in captured.out
    assert "  Modification date: 2023-01-02" in captured.out
    assert "  File type: image" in captured.out
    assert "  MIME type: image/jpeg" in captured.out


def test_print_metadata_list_audio(capsys, audio_metadata_list):
    printer = MetadataPrinter(audio_metadata_list)
    printer.print_metadata_list()
    captured = capsys.readouterr()
    assert "File: audio/song1.mp3" in captured.out
    assert "  Creation date: 2022-05-01" in captured.out
    assert "  Modification date: 2022-05-02" in captured.out
    assert "  File type: audio" in captured.out
    assert "  MIME type: audio/mpeg" in captured.out


def test_print_metadata_list_video(capsys, video_metadata_list):
    printer = MetadataPrinter(video_metadata_list)
    printer.print_metadata_list()
    captured = capsys.readouterr()
    assert "File: videos/movie1.mp4" in captured.out
    assert "  Creation date: 2021-07-01" in captured.out
    assert "  Modification date: 2021-07-02" in captured.out
    assert "  File type: video" in captured.out
    assert "  MIME type: video/mp4" in captured.out
