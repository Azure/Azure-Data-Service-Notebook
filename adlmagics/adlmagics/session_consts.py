from adlmagics.models.session_item import SessionItem

session_null_value = None

session_tenant = SessionItem("tenant", session_null_value)
session_user = SessionItem("user", session_null_value)

session_adla_account = SessionItem("adla.account", session_null_value)

session_adls_account = SessionItem("adls.account", session_null_value)

session_job_runtime = SessionItem("job.runtime", "default")
session_job_priority = SessionItem("job.priority", 100)
session_job_parallelism = SessionItem("job.parallelism", 5)

session_paging_numberperpage = SessionItem("paging.numberperpage", 10)

session_file_encoding = SessionItem("file.encoding", "utf-8")
