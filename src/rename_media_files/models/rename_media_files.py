import os

def rename_files(media_files_metadata, target_dir=None):
    for metadata in media_files_metadata:
        dt_str = metadata.creation_date
        ext = os.path.splitext(metadata.file_path)[1]
        new_name = f"{dt_str}{ext}"
        src = metadata.file_path
        # Always use the original directory
        dst_dir = os.path.dirname(src)
        dst = os.path.join(dst_dir, new_name)

        # Skip if already renamed
        if os.path.basename(src) == new_name:
            print(f"Already renamed: {src}")
            continue

        try:
            os.rename(src, dst)
            print(f"Renamed: {src} -> {dst}")
        except Exception as e:
            print(f"Rename failed for {src}: {e}")