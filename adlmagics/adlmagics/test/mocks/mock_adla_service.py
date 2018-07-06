from datetime import datetime
from uuid import uuid4

from adlmagics.models.adla_account import AdlaAccount
from adlmagics.models.adla_job import AdlaJob

class MockAdlaService:
    def __init__(self, token_service):
        self.__token_service = token_service

    def retrieve_accounts(self):
        return [AdlaAccount(str(ix)) for ix in range(10)]

    def submit_job(self, account, job_submission):
        return AdlaJob(str(uuid4()), job_submission.name, "USql", "mock_submitter", job_submission.parallelism, job_submission.priority, datetime.now(), datetime.now(), datetime.now(), "mock_state", "mock_result", account)

    def retrieve_job(self, account, job_id):
        return AdlaJob(job_id, "mock_job_name", "USql", "mock_submitter", 5, 100, datetime.now(), datetime.now(), datetime.now(), "mock_state", "mock_result", account)

    def retrieve_jobs(self, account, filter, page_index, page_job_number):
        if not self.__token_service.logged_in_user:
            raise UserNotLoggedInError()

        return [AdlaJob(str(uuid4()), "mock_job_name_%d" % (ix), "USql", "mock_submitter", 5, 100, datetime.now(), datetime.now(), datetime.now(), "mock_state", "mock_result", account) for ix in range(10)]