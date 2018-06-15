
# Azure Data Service Notebook (Alpha)
Azure Data Service Notebook is a set of extentions for working with Azure Data Service (e.g. Azure Data Lake, HDIsight, CosmosDB, Azure SQL and Azure Data Warehouse etc.) using [Jupyter Notebook](http://jupyter.org/).

**WARNING**: This SDK/CLI is currently in very early stage of development. It can and will change in backwards incompatible ways. 

Latest Version: `0.0.1a0` 
# Feature
Azure Data Service Notebook currently provides a set of [Jupyter Magic Functions](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html?#magic-functions) for users to access Azure Data Lake. Available magics are captured in the table below. Please click on the command name to see the syntax reference.

| Command | Function  |
|-----|-----|
|[%adl login](#adllogin) |Line magic<sup>[*](#myfootnote1)</sup> to log in to Azure Data Lake.|
|[%adl listaccounts](#adllistaccounts)|Line magic to list the Azure Data Lake Analytic accounts for current user.|
|[%adl listjobs](#adllistjobs)|Line magic to list the Azure Data Lake jobs for a given account.|
|[%%adl submitjob](#adlsubmitjob)|Cell magic<sup>[*](#myfootnote1)</sup> to submit a USQL job to Azure Data Lake cluster.|
|[%adl viewjob](#adlviewjob)|Line magic to view detailed job info.|
|[%adl liststoreaccounts](#adlliststoreaccounts)|Line magic to list the Azure Data Lake Store accounts.|
|[%adl liststorefolders](#adlliststorefolders)|Line magic to list the folders under a given directory.|
|[%adl liststorefiles](#adlliststorefiles)|Line magic to list the files under a given directory.|
|[%adl sample](#adlsample)|Line magic to sample a given file, return results as Pandas DataFrame.|
|[%adl logout](#adllogout)|Line magic to log out.|

<a name="myfootnote1">*</a>Please check [Magic Functions ](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html?#magic-functions) for detailed definiton of `Line magic` and `Cell magics`.

# Installation
- Download and Install [python 3.6+](https://www.python.org/downloads/)
- Install jupyter: 
		```pip install jupyter``` 
- Install adlmagic extention : 
		```pip install --no-cache-dir adlmagics```
# Examples
- [adlmagics_demo.ipynb](/adlmagics/00_adlmagics_demo.ipynb), demo file of `adlmgics` functions for Azure Data Lake job control and data exploration.
- [usql_samples.ipynb](/adlmagics/01_usql_samples.ipynb),  samples code of common U-SQL scenarios, e.g. query a TSV file, create a database, populate table, query table and create rowset in script.

# Feedback
- You can submit [bug report](https://github.com/Azure/Azure-Data-Service-Notebook/issues/new?template=bug_report.md) or [feature request](https://github.com/Azure/Azure-Data-Service-Notebook/issues/new?template=feature_request.md) directly in this repo. Our team will triage issues actively.

# Reference

<a name="adllogin"></a>

## %adl login

Line magic to login to Azure Data Lake service.

```
%adl login --tenant <tenant>
```

#### Input Parameters

|Name|Type |Example|Description|
|----|----|----|----|
|tenant `required`|string|microsoft.onmicrosoft.com| The value of this argument can either be an `.onmicrosoft.com` domain or the Azure object ID for the tenant. |

<a name="adllistaccounts"></a>

## %adl listaccounts

Line magic to enumerate the Azure Data Lake Analytic accounts for current user. The account list will be returned as Pandas DataFrame, you can call Pandas funtions directly afterward.

```
%adl listaccounts	--page_index
			--page_account_number
```

#### Input Parameters

|Name|Type |Example|Description|
|----|----|----|----|
|page_index `required`|int|0|The result page number. This must be greater than 0. Default value is 0.|
|page_account_number `required`|int|10|The number of results per page.|

<a name="adllistjobs"></a>

## %adl listjobs

Line magic to enumerate the Azure Data Lake jobs for a given account. The job list will be returned as Pandas DataFrame, you can call Pandas funtions directly afterward.

```
%adl listjobs	--account <azure data lake analytic account> 
		--page_index
		--page_account_number
```

#### Input Parameters

|Name|Type |Example|Description|
|----|----|----|----|
|account `required`|string|telemetryadla|The Azure Data Lake Analytics account to list the job from.|
|page_index `required`|int|0|The result page number. This must be greater than 0. Default value is 0.|
|page_account_number `required`|int|10|The number of results per page.|

<a name="adlsubmitjob"></a>

## %%adl submitjob

Cell magic to submit a U-SQL job to Azure Data Lake cluster.

```
%%adl submitjob	--account <zure data lake analytic account>
		--name <job name>
		--parallelism
		--priority
		--runtime
```
#### Input Parameters

|Name|Type |Example|Description|
|----|----|----|----|
|account `required`|string|telemetryadla|the Azure Data Lake Analytics account to execute job operations on.|
|name `required`|string|myscript|the friendly name of the job to submit.|
|parallelism |int|5|the degree of parallelism used for this job. This must be greater than 0, if set to less than 0 it will default to 1.|
|priority|int|1000|the priority value for the current job. Lower numbers have a higher priority. By default, a job has a priority of 1000. This must be greater than 0.|
|runtime|string|default|the runtime version of the Data Lake Analytics engine to use for the specific type of job being run.|

<a name="adlviewjob"></a>

## %adl viewjob

Line magic to view detailed job info.
```
%adl view job	--account <azure data lake analytic account>
		--job_id <job GUID to be viewed>
```
#### Input Parameters

|Name|Type |Example|Description|
|----|----|----|----|
|account `required`|string|telemetryadla|the Azure Data Lake Analytics account to execute job operations on.|
|job_id `required`|GUID|36a62f78-1881-1935-8a6a-9e37b497582d|job identifier. uniquely identifies the job across all jobs submitted to the service.|

<a name="adlliststoreaccounts"></a>
	
## %adl liststoreacconts	

Line magic to list the Azure Data Lake Store accounts.
```
%adl liststoreaccounts
```

<a name="adlliststorefolders"></a>

## %adl liststorefolders
Line magic to list the folders under a given directory.
```
%adl liststorefolders	--account <azure data lake store account>
			--folder_path 
```
#### Input Parameters

|Name|Type |Example|Description|
|----|----|----|----|
|account `required`|string|telemetryadls|the name of the Data Lake Store account.|
|folder_path `required`|string|root/data|the directory path under the Data Lake Store account.|

<a name="adlliststorefiles"></a>

## %adl liststorefiles
Line magic to list the files under a given directory.
```
%adl liststorefiles	--account <azure data lake store account>
			--folder_path
```
#### Input Parameters

|Name|Type |Example|Description|
|----|----|----|----|
|account `required`|string|telemetryadls|the name of the Data Lake Store account.|
|folder_path `required`|string|root/data|the directory path under the Data Lake Store account.|

<a name="adlsample"></a>

## %adl sample

Line magic to sample a given file, return results as Pandas DataFrame.

```
%adl sample	--account <azure data lake store account>
		--file_path 
		--file_type 
		--encoding 
		--row_number 
```
#### Input Parameters

|Name|Type |Example|Description|
|----|----|----|----|
|account `required`|string|telemetryadls|the name of the Data Lake Store account.|
|file_path `required`|string|root/data/sample.tsv|the file path to sample data from.|
|file_type |string|tsv|the type of the file to sample from. |
|encoding |string|UTF-8|encoding type of the file.|
|row_number|int|10|number of rows to read from the file.|

<a name="adllogout"></a>

## %adl logout

Line magic to log out.

```
%adl logout
```


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
