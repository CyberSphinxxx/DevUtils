import sys

def convert_currency(amount, from_currency, to_currency):
    """
    Converts currency using mock exchange rates.
    """
    # Mock rates relative to USD
    rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.75,
        "JPY": 110.0,
        "CAD": 1.25,
        "AUD": 1.35,
        "PHP": 56.0
    }

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates or to_currency not in rates:
        print("Error: Currency not supported.")
        return

    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]

    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python currency_converter.py <amount> <from_currency> <to_currency>")
    else:
        try:
            amount = float(sys.argv[1])
            convert_currency(amount, sys.argv[2], sys.argv[3])
        except ValueError:
            print("Error: Invalid amount.")
