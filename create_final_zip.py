#!/usr/bin/env python3
"""
Create final zip file dengan struktur root yang benar
"""

import zipfile
import os
from pathlib import Path

def create_final_zip():
    """Buat zip file dengan struktur yang benar (tanpa wrapper folder)"""
    
    base_path = Path(__file__).parent
    organized_dir = base_path / "Submission_Organized" / "Submission_Organized"
    output_zip = base_path / "Eksperimen_SML_Submission_Final.zip"
    
    if not organized_dir.exists():
        # Try alternative path
        organized_dir = base_path / "Submission_Organized"
    
    print(f"Creating final zip from: {organized_dir}")
    print(f"Output: {output_zip}")
    
    if output_zip.exists():
        output_zip.unlink()
    
    # Create zip with files at root level
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(organized_dir):
            for file in files:
                file_path = Path(root) / file
                # Get relative path from organized_dir
                arcname = file_path.relative_to(organized_dir)
                zipf.write(file_path, arcname)
                print(f"  + {arcname}")
    
    print(f"\n✅ Final zip created: {output_zip}")
    print(f"File size: {output_zip.stat().st_size / (1024*1024):.2f} MB")
    
    # Verify zip contents
    print("\n📋 Zip contents structure:")
    with zipfile.ZipFile(output_zip, 'r') as zipf:
        for info in sorted(zipf.filelist):
            print(f"  {info.filename}")

if __name__ == "__main__":
    try:
        create_final_zip()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
