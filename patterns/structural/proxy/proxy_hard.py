import logging
from abc import ABC
from abc import abstractmethod

ALLOWED_TOKENS: set[str] = set(["abc"])


class IWebService(ABC):
    @abstractmethod
    def fetch_data(self, url: str) -> str:
        pass

    @abstractmethod
    def post_data(self, url: str, data: str) -> None:
        pass


class WebService(IWebService):
    def __init__(self, token: str) -> None:
        self.token = token

    def fetch_data(self, url: str) -> str:
        return f"Fetching data from {url}"

    def post_data(self, url: str, data: str) -> None:
        print(f"Posting {data} to {url}")


class WebServiceProxy(IWebService):
    def __init__(
        self,
        web_service: WebService,
        log: logging.Logger,
    ) -> None:
        self.ws = web_service
        self.log = log
        self.cache: dict[str, str] = dict()

    def check_token(self) -> None:
        if self.ws.token not in ALLOWED_TOKENS:
            self.log.error("Token not allowed")
            raise ValueError("Token not allowed")

    def fetch_data(self, url: str) -> str:
        self.log.debug(f"Try to ferch data from: {url}")
        self.check_token()
        if url not in self.cache:
            self.cache[url] = self.ws.fetch_data(url)
        return self.cache[url]

    def post_data(self, url: str, data: str) -> None:
        self.log.debug(f'Try to post data "{data}" to: {url}')
        self.check_token()
        return self.ws.post_data(url, data)


def client_code():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("WebServiceProxyLogger")

    real_ws = WebService("abc")
    proxy_ws = WebServiceProxy(real_ws, logger)

    print(proxy_ws.fetch_data("/api/data"))
    proxy_ws.post_data("/api/data", "New content")
