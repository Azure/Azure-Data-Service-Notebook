DESCRIPTION  = "Azure Data Lake management magics for Jupyter Notebook"
NAME         = "adlmagics"
VERSION      = "0.0.1"
PACKAGES     = ["adlmagics",
               "adlmagics/magics/adla",
               "adlmagics/magics/adls",
               "adlmagics/magics/azure",
               "adlmagics/magics/session",
               "adlmagics/models",
               "adlmagics/services"]
AUTHOR        = ""
AUTHOR_EMAIL  = ""
URL           = "https://github.com/Azure/Azure-Data-Service-Notebook"
DOWNLOAD_URL  = "https://github.com/Azure/Azure-Data-Service-Notebook"
LICENSE       = "MIT"

from distutils.core import setup

setup(name = NAME,
      version = VERSION,
      description = DESCRIPTION,
      author = AUTHOR,
      author_email = AUTHOR_EMAIL,
      url = URL,
      download_url = DOWNLOAD_URL,
      license = LICENSE,
      packages = PACKAGES,
      include_package_data = True,
      classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Jupyter",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6"],
      install_requires = [
          "ipython>=5.3.0",
          "notebook>=5.0.0",
          "ipykernel>=4.6.1",
          "pandas>=0.20.1",
          "adal>=0.5.0",
          "azure-mgmt-resource>=1.2.2",
          "azure-mgmt-datalake-analytics>=0.3.0",
          "azure-mgmt-datalake-store>=0.3.0",
          "azure-datalake-store>=0.0.18"])