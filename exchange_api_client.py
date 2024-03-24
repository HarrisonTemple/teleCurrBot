import requests
import json
from helpers import Exceptions as Ex

class EAPIClient:
    @staticmethod
    def request_pair_rate(source: str, destination: str ):
        resp = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={source}&tsyms={destination}")
        resp.raise_for_status()

        try:
            return json.loads(resp.content)[destination]
        except KeyError:
            raise Ex.ProviderConversionError(f"unable to retrieve rate for {source} {destination}")


if __name__ == "__main__":
    print(EAPIClient.request_pair_rate("USD", "USD"))
