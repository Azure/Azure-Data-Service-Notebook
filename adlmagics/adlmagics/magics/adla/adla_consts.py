# the azure adla python api in default set the maximum request number
# for get account or job list is less than or equal to 2**31 -1 (the maximum number that int can represent)
# if greater than 2**31 -1, it would cause 500 error
DEFAULT_MAX_REQ_NUMBER = 2147483647
class AdlaJobConsts:
    adla_job_dns_suffix = "azuredatalakeanalytics.net"
    adla_job_type = "USql"