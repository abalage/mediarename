from rename_media_files.controllers.rename_media_files import main
from rename_media_files.controllers.rename_media_files import AppArgs


class DummyModel:
    def __init__(self, files, datetime_format):
        self.metadata = [f"meta-{f}" for f in files]


class DummyRenameFiles:
    def __init__(self):
        self.called = False
        self.last_metadata = None

    def __call__(self, metadata):
        self.called = True
        self.last_metadata = metadata


dummy_rename_files = DummyRenameFiles()


def make_args(temp_media_files, verbose=True):
    dir_path, _ = temp_media_files
    return AppArgs(
        input=dir_path,
        datetime_format="%Y-%m-%d",
        dry_run=False,
        verbose=verbose
    )


def test_main_invokes_metadata_and_rename(monkeypatch, temp_media_files):
    args = make_args(temp_media_files)
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.MediaFilesModel", DummyModel
    )
    dummy_print_metadata_list_called = {"called": False}

    def dummy_print_metadata_list(metadata):
        dummy_print_metadata_list_called["called"] = True

    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.print_metadata_list", dummy_print_metadata_list
    )
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.rename_files", dummy_rename_files
    )
    dummy_rename_files.called = False

    main(args)
    assert dummy_rename_files.called
    assert dummy_print_metadata_list_called["called"]


def test_main_with_no_files(monkeypatch, temp_media_files):
    args = make_args(temp_media_files)
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.get_files_from_input", lambda x: []
    )
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.MediaFilesModel", DummyModel
    )
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.print_metadata_list", lambda x: None
    )
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.rename_files", dummy_rename_files
    )
    dummy_rename_files.called = False

    main(args)
    assert not dummy_rename_files.called


def test_main_non_verbose(monkeypatch, temp_media_files):
    args = make_args(temp_media_files, verbose=False)
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.MediaFilesModel", DummyModel
    )
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.print_metadata_list", lambda x: None
    )
    monkeypatch.setattr(
        "rename_media_files.controllers.rename_media_files.rename_files", dummy_rename_files
    )
    dummy_rename_files.called = False

    main(args)
    assert dummy_rename_files.called
