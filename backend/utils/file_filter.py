import os

ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".java", ".cpp", ".c", ".go", ".md", ".txt"
}

EXCLUDED_DIRS = {
    "node_modules", ".git", "dist", "build",
    "__pycache__", "venv", ".next"
}

MAX_FILE_SIZE = 200 * 1024  # 200 KB

def get_valid_files(repo_path):
    valid_files = []

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            ext = os.path.splitext(file)[1]

            if ext in ALLOWED_EXTENSIONS or ext =="":
                full_path = os.path.join(root, file)

                if os.path.getsize(full_path) <= MAX_FILE_SIZE:
                    relative_path = os.path.relpath(full_path, repo_path)
                    valid_files.append(relative_path)

    return valid_files