import pytest
import weather


def test_get_temperature(mocker):
    mock_get = mocker.patch("weather.requests.get")
    mock_get.return_value.json.return_value = {"temp": 18}
    result = weather.get_temperature("ბათუმი")
    assert result == 18
    mock_get.assert_called_once_with(
        weather.URL, params={"city": "ბათუმი"}, timeout=5
    )


@pytest.mark.parametrize(
    "temp, expected",
    [
        pytest.param(30, "თბილისი: 30°C, ცხელა", id="hot"),
        pytest.param(25, "თბილისი: 25°C, ცხელა", id="hot-border"),
        pytest.param(15, "თბილისი: 15°C, კარგი ამინდია", id="nice"),
        pytest.param(0, "თბილისი: 0°C, ყინავს", id="freezing-border"),
        pytest.param(-7, "თბილისი: -7°C, ყინავს", id="freezing"),
    ],
)
def test_weather_message(monkeypatch, temp, expected):
    monkeypatch.setattr(weather, "get_temperature", lambda city: temp)
    assert weather.weather_message("თბილისი") == expected