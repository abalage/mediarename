class MetadataPrinter:
    def __init__(self, metadata_list: list):
        self.metadata_list = metadata_list

    def print_file_paths(self) -> None:
        for metadata in self.metadata_list:
            print(f"File: {metadata.file_path}")

    def print_metadata_list(self) -> None:
        for metadata in self.metadata_list:
            print(f"File: {metadata.file_path}")
            print(f"  Creation date: {metadata.creation_date}")
            print(f"  Modification date: {metadata.modification_date}")
            print(f"  File type: {metadata.file_type}")
            print(f"  MIME type: {metadata.mime_type}")
            #print("-" * 40)