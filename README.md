
# Azure Data Service Notebook
Azure Data Service Notebook is a set of tool for working with Azure Data Service (including HDInsight, Azure Data Lake, etc)


# Feature
Azure Data Service Notebook currently provides a set of magic commands for users to access Azure Data Lake. Available magics are captured in the table below.

| Commands | Function |
|-----|-----|
|%adl login |Line magic to log in to Azure Data Lake.|
|%adl listaccounts|Line magic to list the Azure Data Lake analytic accounts for current user.|
|%adl listjobs|Line magic to list the Azure Data Lake jobs for a given account.|
|%%adl submitjob|Cell magic to submit a USQL job to ADL cluster.|
|%adl viewjob|Line magic to view job info.|
|%adl liststorefile|Line magic to list the Azure Data Lake store accounts.|
|%adl sample|Line magic to sample a given file, return results as Pandas DataFrame.|
|%adl logout|Line magic to log out.|


# Installation

- Download and Install [python 3.6+](https://www.python.org/downloads/)
- Install jupyter: `pip install jupyter` 
- Install azure packages fully : 
	`pip install azure`
-  Or just install the key packages : 
	- `pip install adla`
	- `pip install azure-mgmt-resource`
	- `pip install azure-mgmt-datalake-analytics` 
	- `pip install azure-mgmt-datalake-store` 
	- `pip install azure-datalake-store` 
- Copy the [adlmagic folder](https://github.com/ruixinxu/Azure-Data-Service-Notebook/tree/master/analytics_notebook/adlmagics) to local box. 


# Examples
- [adlmagics_demo.ipynb](https://github.com/ruixinxu/Azure-Data-Service-Notebook/blob/master/analytics_notebook/adlmagics/adlmagics_demo.ipynb), demo file of Azure Data Lake job control functions.



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
