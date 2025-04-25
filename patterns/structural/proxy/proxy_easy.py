import logging
from abc import ABC
from abc import abstractmethod


ALLOWED_AUTH: set[tuple[str, str]] = set(
    [
        ("admin", "admin"),
    ]
)


class IDatabase(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass

    @abstractmethod
    def execute_query(self, query: str) -> str:
        pass


class Database(IDatabase):
    def __init__(
        self,
        login: str,
        password: str,
    ) -> None:
        self.login = login
        self.password = password

    def connect(self) -> str:
        return "Connected to the database"

    def execute_query(self, query: str) -> str:
        return f"Executing query: {query}"


class DatabaseProxy(IDatabase):
    def __init__(
        self,
        database: Database,
        log: logging.Logger,
    ) -> None:
        self.db = database
        self.log = log

    def check_auth(self) -> bool:
        if (self.db.login, self.db.password) not in ALLOWED_AUTH:
            self.log.error("Auth failed")
            return False
        return True

    def connect(self) -> str:
        self.log.debug("Try to connect")
        if self.check_auth():
            return self.db.connect()
        raise ValueError("Authentication failed")

    def execute_query(self, query: str) -> str:
        self.log.debug(f"Try to execute query: {query}")
        if self.check_auth():
            return self.db.execute_query(query)
        raise ValueError("Authentication failed")


def client_code():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("DatabaseProxyLogger")

    real_db = Database("admin", "admin")
    proxy_db = DatabaseProxy(real_db, logger)

    print(proxy_db.connect())
    print(proxy_db.execute_query("SELECT * FROM users"))
