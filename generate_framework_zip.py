import zipfile
import os

def zip_project(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if ['.git', '.idea'] in root:
                    continue
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, source_dir)
                zipf.write(filepath, arcname)

if __name__ == "__main__":
    root_path = r"C:\Repos\ai-collab-template"
    project_path = os.path.join(root_path, "ai-collab-template")
    output_zip = os.path.join(root_path, "ai-collab-template.zip")

    zip_project(project_path, output_zip)
    print(f"\n✅ Framework project zipped successfully:\n{output_zip}")