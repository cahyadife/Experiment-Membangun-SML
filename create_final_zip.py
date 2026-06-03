#!/usr/bin/env python3
"""Create the final submission zip with only the required top-level items."""

from pathlib import Path
import zipfile


INCLUDED_ITEMS = [
    'Eksperimen_SML_Cahyadi.txt',
    'Membangun_model',
    'Workflow-CI.txt',
    'Monitoring dan Logging',
]


def create_final_zip() -> Path:
    base_path = Path(__file__).resolve().parent
    output_zip = base_path / 'SMSML_Cahyadi.zip'

    if output_zip.exists():
        output_zip.unlink()

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for item_name in INCLUDED_ITEMS:
            item_path = base_path / item_name
            if not item_path.exists():
                raise FileNotFoundError(f'Missing required submission item: {item_path}')

            if item_path.is_file():
                zip_file.write(item_path, arcname=item_name)
                continue

            for file_path in item_path.rglob('*'):
                if file_path.is_file():
                    zip_file.write(file_path, arcname=file_path.relative_to(base_path))

    return output_zip


if __name__ == '__main__':
    final_zip = create_final_zip()
    print(f'Created: {final_zip}')
    print(f"Size: {final_zip.stat().st_size / (1024 * 1024):.2f} MB")
