import setuptools

name             = "adlmagics"
description      = "Azure Data Lake management magics for Jupyter Notebook"
long_description = ""
version          = "0.0.1"
packages         = ["adlmagics",
                    "adlmagics/magics/adla",
                    "adlmagics/magics/adls",
                    "adlmagics/magics/azure",
                    "adlmagics/magics/session",
                    "adlmagics/models",
                    "adlmagics/services"]
author           = "Vincent Feng"
author_email     = "ivincentfeng@live.com"
url              = "https://github.com/Azure/Azure-Data-Service-Notebook"
download_url     = "https://github.com/Azure/Azure-Data-Service-Notebook"
license          = "MIT"

with open("README.md", "r") as f:
    long_description = f.read()

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
    "azure-mgmt-datalake-analytics",
    "azure-mgmt-datalake-store",
    "azure-datalake-store"])