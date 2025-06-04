class AccountRegistry:
    registry = []

    @classmethod
    def add_account(cls,account):
        cls.registry.append(account)

    @classmethod
    def search_by_pesel(cls,pesel):
        return list(filter(lambda account: account.pesel == pesel,cls.registry))[0] if len(list(filter(lambda account: account.pesel == pesel,cls.registry))) > 0 else None
    
    @classmethod
    def get_accounts_count(cls):
        return len(cls.registry)