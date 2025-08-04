import subprocess
import chardet

def read_clean_package_names(file_path):
    # Detect encoding
    with open(file_path, 'rb') as raw_file:
        raw_data = raw_file.read()
        detected = chardet.detect(raw_data)
        encoding = detected['encoding'] or 'utf-8'

    # Read and clean package names
    with open(file_path, 'r', encoding=encoding) as f:
        return {
            line.strip().split("==")[0].lower()
            for line in f
            if line.strip() and not line.startswith("#")
        }

# Step 1: Read required packages
required = read_clean_package_names("requirements.txt")

# Step 2: Get installed packages
installed_raw = subprocess.check_output(["pip", "freeze"], text=True)
installed = {
    line.strip().split("==")[0].lower()
    for line in installed_raw.splitlines()
    if line.strip()
}

# Step 3: Find extras
extra = installed - required

# Step 4: Uninstall extras
for pkg in sorted(extra):
    print(f"Uninstalling: {pkg}")
    subprocess.call(["pip", "uninstall", "-y", pkg])

print("\n✅ All unnecessary packages removed.")