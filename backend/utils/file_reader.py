import os
import json
def read_file(file_path):
    try:
        if file_path.endswith(".ipynb"):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            cells = []
            for cell in data.get("cells", []):
                if cell.get("cell_type") == "code":
                    cells.append("".join(cell.get("source", [])))

            return "\n\n".join(cells[:20])
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    except Exception:
        return None