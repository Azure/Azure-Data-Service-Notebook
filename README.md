
# Azure Data Service Notebook (Alpha)
Azure Data Service Notebook is a set of extentions for working with Azure Data Service (e.g. Azure Data Lake, HDIsight, CosmosDB, Azure SQL and Azure Data Warehouse etc.) using [Jupyter Notebook](http://jupyter.org/).

**WARNING**: This SDK/CLI is currently in very early stage of development. It can and will change in backwards incompatible ways. 

Latest Version: `0.0.1a0` 
# Feature
Azure Data Service Notebook currently provides a set of [Jupyter Magic Functions](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html?highlight=magic#magic-functions) for users to access Azure Data Lake. Available magics are captured in the table below. Please click on the command name to see the syntax reference.

| Command | Function  |
|-----|-----|
|[%adl login](#adllogin) |Line magic<sup>[*](#myfootnote1)</sup> to log in to Azure Data Lake.|
|%adl listaccounts|Line magic to list the Azure Data Lake Analytic accounts for current user.|
|%adl listjobs|Line magic to list the Azure Data Lake jobs for a given account.|
|%%adl submitjob|Cell magic<sup>[*](#myfootnote1)</sup> to submit a USQL job to Azure Data Lake cluster.|
|%adl viewjob|Line magic to view detailed job info.|
|%adl liststorefile|Line magic to list the Azure Data Lake Store accounts.|
|%adl sample|Line magic to sample a given file, return results as Pandas DataFrame.|
|%adl logout|Line magic to log out.|

<a name="myfootnote1">*</a> Please check [Magic Functions ](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html?highlight=magic#magic-functions
) for detailed definiton of `Line magic` and `Cell magics`.

# Installation
- Download and Install [python 3.6+](https://www.python.org/downloads/)
- Install jupyter: `pip install jupyter` 
- Install adlmagic extention : 
	`pip install --no-cache-dir adlmagics`

# Examples
- [adlmagics_demo.ipynb](/adlmagics/00_adlmagics_demo.ipynb), demo file of `adlmgics` functions for Azure Data Lake job control and data exploration.
- [usql_samples.ipynb](/adlmagics/01_usql_samples.ipynb),  samples code of common U-SQL scenarios, e.g. query a TSV file, create a database, populate table, query table and create rowset in script.

# Feedback
- You can submit [bug report](https://github.com/Azure/Azure-Data-Service-Notebook/issues/new?template=bug_report.md) or [feature request](https://github.com/Azure/Azure-Data-Service-Notebook/issues/new?template=feature_request.md) directly in this repo. Our team will triage issues actively.

#Reference
<a name="adllogin"></a>
###%adl login
Line magic to login to Azure Data Lake service.

`%adl login --tenant <tenant>
`  
####Required Parameters
|Name|Example|Description|
|----|----|----|
|tenant `required`|microsoft.onmicrosoft.com| The value of this argument can either be an `.onmicrosoft.com` domain or the Azure object ID for the tenant. |

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
