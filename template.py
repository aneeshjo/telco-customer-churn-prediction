
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
PACKAGE_NAME = "telco_customer_churn_prediction"

folders = [
    "config",
    "data/raw",
    "data/external",
    "data/interim",
    "data/processed",
    "notebooks",
    f"src/{PACKAGE_NAME}/components",
    f"src/{PACKAGE_NAME}/pipelines",
    f"src/{PACKAGE_NAME}/config",
    f"src/{PACKAGE_NAME}/utils",
    f"src/{PACKAGE_NAME}/exceptions",
    "tests",
    "docs",
    "artifacts",
]

files = [
    f"src/{PACKAGE_NAME}/__init__.py",
    f"src/{PACKAGE_NAME}/components/__init__.py",
    f"src/{PACKAGE_NAME}/pipelines/__init__.py",
    f"src/{PACKAGE_NAME}/config/__init__.py",
    f"src/{PACKAGE_NAME}/utils/__init__.py",
    f"src/{PACKAGE_NAME}/exceptions/__init__.py",
    "config/config.yaml",
    "config/params.yaml",
    "config/schema.yaml",
    "config/logging.yaml",
    "tests/__init__.py",
    "README.md",
    "requirements.txt",
    "setup.py",
    ".gitignore",
]

for folder in folders:
    (PROJECT_ROOT / folder).mkdir(
        parents=True,
        exist_ok=True,
    )

for file_path in files:
    path = PROJECT_ROOT / file_path
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()
        print(f"Created file: {file_path}")

# Remove directories created by the earlier incorrect template.
old_package = PROJECT_ROOT / "src" / "Telco Churn Prediction"

if old_package.exists():
    import shutil
    shutil.rmtree(old_package)
    print("Removed obsolete package directory.")

print("Project template created successfully.")
