
from pathlib import Path

from setuptools import find_packages, setup

NAME = "telco_customer_churn_prediction"
VERSION = "0.0.1"
AUTHOR = "ANEESH JOSE"
EMAIL = "aneeshjose012@gmail.com"

PROJECT_ROOT = Path(__file__).resolve().parent


def get_requirements_list() -> list[str]:
    """Read installable dependencies from requirements.txt."""
    requirements_file = PROJECT_ROOT / "requirements.txt"

    with requirements_file.open(encoding="utf-8") as file:
        requirements = [
            line.strip()
            for line in file
            if line.strip()
            and not line.lstrip().startswith("#")
            and line.strip() != "-e ."
        ]

    return requirements


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements_list(),
    python_requires=">=3.10",
)
