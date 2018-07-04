class MockTokenService:
    def __init__(self):
        self.tenant = "mock tenant"
        self.tenant_id = "mock tenant id"
        self.logged_in_user = "mock logged in user"
        self.token = "mock token"
        self.credentials = "mock credentials"

    def login(self, tenant):
        pass

    def logout(self):
        self.tenant = None
        self.tenant_id = None
        self.logged_in_user = None
        self.token = None
        self.credentials = None