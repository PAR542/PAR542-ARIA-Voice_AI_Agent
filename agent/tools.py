import os

OUTPUT_DIR = "output"

def create_file(filename):
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        path = os.path.join(OUTPUT_DIR, filename)

        with open(path, "w") as f:
            f.write("")

        return f"✅ File created: {path}"

    except Exception as e:
        return f"❌ Error: {str(e)}"