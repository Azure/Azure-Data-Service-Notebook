import setuptools
import re

name             = "adlmagics"
description      = "Azure Data Lake management magics for Jupyter Notebook"
long_description = ""
version          = ""
author           = "Vincent Feng"
author_email     = "ivincentfeng@live.com"
url              = "https://github.com/Azure/Azure-Data-Service-Notebook"
download_url     = "https://github.com/Azure/Azure-Data-Service-Notebook"
license          = "MIT"

with open("../README.md", "r") as f:
    long_description = f.read()

with open("adlmagics/version.py") as f:
    version_file = f.read()
    version_match = re.search(r"""^adlmagics_version = ['"]([^'"]*)['"]""", version_file)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
  name = name,
  version = version,
  description = description,
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = author,
  author_email = author_email,
  url = url,
  download_url = download_url,
  license = license,
  packages = setuptools.find_packages(),
  include_package_data = True,
  classifiers = [
    "Development Status :: 3 - Alpha",
    "Framework :: Jupyter",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3.6",
    "Operating System :: OS Independent"],
  install_requires = [
    "ipython>=5.3.0",
    "notebook>=5.0.0",
    "ipykernel>=4.6.1",
    "pandas>=0.20.1",
    "numpy",
    "adal",
    "azure-mgmt-resource",
    "azure-mgmt-datalake-analytics>=0.4.0,<=0.5.0",
    "azure-mgmt-datalake-store",
    "azure-datalake-store"])