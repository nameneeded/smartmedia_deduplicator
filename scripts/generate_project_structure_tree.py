import os
import datetime
import shutil

EXCLUDED_DIRS = {
    '.git', 'venv', '.flash', '.env', '__pycache__', 
    '.pytest_cache', '.mypy_cache', 'node_modules', 'dist', 'build'
}
OUTPUT_FILE = "project_structure.md"
PREVIOUS_DIR = "docs/previous"


def get_project_root():
    """
    Attempts to find the Git repository root.
    If not found, assumes this script is inside a `scripts/` folder and goes up one level.
    """
    current_path = os.path.dirname(os.path.abspath(__file__))

    # Try to find .git
    search_path = current_path
    while True:
        if os.path.isdir(os.path.join(search_path, ".git")):
            return search_path
        parent = os.path.dirname(search_path)
        if parent == search_path:
            break  # Reached root
        search_path = parent

    # Fallback: go up from scripts/
    print("⚠️  Git repo not found, assuming script is inside /scripts/ and backing up to project root.")
    return os.path.abspath(os.path.join(current_path, ".."))


def generate_tree(root_path, exclude_dirs):
    lines = []

    def walk_dir(path, prefix=""):
        entries = sorted(os.listdir(path))
        entries = [e for e in entries if e not in exclude_dirs]

        for idx, entry in enumerate(entries):
            full_path = os.path.join(path, entry)
            connector = "└── " if idx == len(entries) - 1 else "├── "
            lines.append(f"{prefix}{connector}{entry}")

            if os.path.isdir(full_path):
                extension = "    " if idx == len(entries) - 1 else "│   "
                walk_dir(full_path, prefix + extension)

    lines.append(".")
    walk_dir(root_path)
    return "\n".join(lines)


def save_tree_with_header(content, filepath):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"# Project structure as of {timestamp}\n\n```text\n"
    footer = "\n```"
    with open(filepath, "w") as f:
        f.write(header + content + footer)


def main():
    project_root = get_project_root()
    docs_path = os.path.join(project_root, "docs")
    output_path = os.path.join(docs_path, OUTPUT_FILE)
    previous_dir = os.path.join(docs_path, "previous")

    os.makedirs(previous_dir, exist_ok=True)

    # Backup previous version if it exists
    if os.path.exists(output_path):
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(previous_dir, f"project_structure_{ts}.md")
        shutil.copy2(output_path, backup_file)
        print(f"📦 Backed up old project structure to {backup_file}")

    # Generate and save new version
    tree_output = generate_tree(project_root, EXCLUDED_DIRS)
    save_tree_with_header(tree_output, output_path)
    print(f"✅ Updated project structure written to {output_path}")


if __name__ == "__main__":
    main()