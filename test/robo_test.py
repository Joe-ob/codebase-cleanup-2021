
# TODO: import some code
from conftest import mock_msft_response, mock_amzn_response
from pandas import DataFrame


# TODO: test the code
from app.robo import process_data, summarize_data, prepare_data_for_charting


def test_fetch(parsed_googl_response):
    response_keys = list(parsed_googl_response.keys())
    assert "Meta Data" in response_keys
    assert "Time Series (Daily)" in response_keys

    daily_prices = list(parsed_googl_response["Time Series (Daily)"].values())[0]
    price_keys = list(daily_prices.keys())
    assert price_keys == ["1. open", "2. high", "3. low", "4. close", "5. volume"]

def test_process(parsed_googl_response, parsed_oops_response):
    googl_df = process_data(parsed_googl_response)
    assert isinstance(googl_df, DataFrame)
    assert len(googl_df) == 100
    assert list(googl_df.columns) == ["date", "open", "high", "low", "close", "volume"]

    assert process_data(parsed_oops_response) is None
