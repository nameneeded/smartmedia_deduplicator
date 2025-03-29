import os
import argparse

EXCLUDED_DIRS = {
    '.git', 'venv', '__pycache__', '.pytest_cache', 'node_modules',
    'dist', 'build', '.mypy_cache', '.idea', '.vscode', '.dogmatix'
}
TARGET_EXTENSIONS = {'.py', '.md', '.yaml', '.yml', '.json', '.txt'}
DEFAULT_OLD_NAME = "smartmedia_deduplicator"


def rename_project(root, old_name, new_name):
    files_updated = 0
    for dirpath, dirnames, filenames in os.walk(root):
        # Modify dirnames in-place to skip excluded directories
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]

        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext.lower() in TARGET_EXTENSIONS:
                file_path = os.path.join(dirpath, filename)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    if old_name in content:
                        updated_content = content.replace(old_name, new_name)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"🔄 Updated: {file_path}")
                        files_updated += 1

                except (UnicodeDecodeError, FileNotFoundError):
                    print(f"⚠️ Skipped non-text or unreadable file: {file_path}")

    print(f"\n✅ Rename complete. {files_updated} file(s) updated.")


def main():
    parser = argparse.ArgumentParser(
        description="Rename all references to the default project name."
    )
    parser.add_argument(
        "-n", "--name",
        help="New project name to apply",
        required=True
    )
    parser.add_argument(
        "-o", "--old",
        help="Old project name (default: smartmedia_deduplicator)",
        default=DEFAULT_OLD_NAME
    )
    args = parser.parse_args()

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"📁 Scanning project at: {project_root}")
    rename_project(project_root, args.old, args.name)


if __name__ == "__main__":
    main()