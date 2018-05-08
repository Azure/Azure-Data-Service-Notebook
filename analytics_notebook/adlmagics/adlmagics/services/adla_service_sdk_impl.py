from azure.mgmt.resource.subscriptions import SubscriptionClient
from azure.mgmt.datalake.analytics import DataLakeAnalyticsAccountManagementClient
from azure.mgmt.datalake.analytics import DataLakeAnalyticsJobManagementClient
from azure.mgmt.datalake.analytics.job.models import JobInformation, USqlJobProperties, JobType
from uuid import uuid4

from exceptions import UserNotLoggedInError
from magics.adla.adla_consts import AdlaJobConsts
from models.adla_account import AdlaAccount
from models.adla_job import AdlaJob

class AdlaServiceSdkImpl:
    def __init__(self, token_service):
        self.__token_service = token_service

    def retrieve_accounts(self, page_index, page_account_number):
        if (not self.__token_service.logged_in_user):
            raise UserNotLoggedInError()

        accounts = []

        sub_client = SubscriptionClient(self.__token_service.credentials)
        for sub in sub_client.subscriptions.list():
            dla_client = DataLakeAnalyticsAccountManagementClient(self.__token_service.credentials, sub.subscription_id)
            accounts.extend([AdlaAccount(account.name) for account in dla_client.account.list()])

        accounts.sort(key = lambda account: getattr(account, "name"))

        skipped_account_number = page_index * page_account_number
        return accounts[skipped_account_number : skipped_account_number + page_account_number]

    def submit_job(self, account, job_submission):
        if (not self.__token_service.logged_in_user):
            raise UserNotLoggedInError()

        job_id = str(uuid4())
        job_client = DataLakeAnalyticsJobManagementClient(self.__token_service.credentials, AdlaJobConsts.adla_job_dns_suffix)

        job_props = USqlJobProperties(script = job_submission.script, runtime_version = job_submission.runtime)
        job_info = JobInformation(name = job_submission.name, type = AdlaJobConsts.adla_job_type, properties = job_props, degree_of_parallelism = job_submission.parallelism, priority = job_submission.priority)

        job = job_client.job.create(account, job_id, job_info)

        return AdlaJob(job.job_id, job.name, job.type.name, job.submitter, job.degree_of_parallelism, job.priority, job.submit_time, job.start_time, job.end_time, job.state.name, job.result.name)

    def retrieve_job(self, account, job_id):
        if (not self.__token_service.logged_in_user):
            raise UserNotLoggedInError()

        job_client = DataLakeAnalyticsJobManagementClient(self.__token_service.credentials, AdlaJobConsts.adla_job_dns_suffix)

        job = job_client.job.get(account, job_id)

        return AdlaJob(job.job_id, job.name, job.type.name, job.submitter, job.degree_of_parallelism, job.priority, job.submit_time, job.start_time, job.end_time, job.state.name, job.result.name)

    def retrieve_jobs(self, account, filter, page_index, page_job_number):
        if (not self.__token_service.logged_in_user):
            raise UserNotLoggedInError()

        job_client = DataLakeAnalyticsJobManagementClient(self.__token_service.credentials, AdlaJobConsts.adla_job_dns_suffix)

        skip = page_index * page_job_number
        if (skip == 0):
            skip = None

        jobs = job_client.job.list(account, filter = filter, top = page_job_number, skip = skip)

        return [AdlaJob(job.job_id, job.name, job.type.name, job.submitter, job.degree_of_parallelism, job.priority, job.submit_time, job.start_time, job.end_time, job.state.name, job.result.name) for job in jobs]

    @property
    def logged_in_user(self):
        return self.__token_service.logged_in_user