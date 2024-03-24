import requests
import json
from helpers import Exceptions as Ex

class Client:
    @staticmethod
    def request_pair_rate(src: str, dst: str) -> float:
        resp = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={src}&tsyms={dst}")
        resp.raise_for_status()

        try:
            return float(json.loads(resp.content)[dst])
        except (KeyError, TypeError):
            raise Ex.ProviderConversionError(f"unable to retrieve rate for {src} {dst}")


if __name__ == "__main__":
    print(Client.request_pair_rate("RUB", "USD"))
