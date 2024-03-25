class Exceptions:
    class ProviderConversionError(Exception):
        pass

    class BadInputError(Exception):
        pass


supported_currencies = {"USD": "US Dollar", "RUB": "Russian Rouble", "EUR": "Euro",
                        "CHF": "Swiss Franc", "CNY": "Chinese Yuan", "AUD": "Australian Dollar",
                        "JPY": "Japanese Yen", "KRW": "Korean Won", "GBP": "British Pound",
                        "BTC": "Bitcoin", "ETH": "Ethereum", "DOGE": "Doge coin", "SOL": "Solana"}

def get_readable_currencies() -> str:
    result = ""
    for x, y in supported_currencies.items():
        result += f"{x} - {y}\n"
    return result
