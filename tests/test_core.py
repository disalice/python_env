import pytest

from sample_project.core import calculate_average_age


def test_calculate_average_age_success():
    """正常に平均年齢が計算できることを検証します。"""
    # 準備 (Given)
    users = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 40},
        {"name": "Charlie", "age": 30},
    ]

    # 実行 (When)
    result = calculate_average_age(users)

    # 検証 (Then)
    assert result == 30.0


def test_calculate_average_age_empty_list():
    """空のリストが渡されたときに、適切なエラーが発生することを検証します。"""
    with pytest.raises(ValueError, match="ユーザーリストが空です。"):
        calculate_average_age([])


# パラメータ化テスト: 複数の異常系パターンを効率的にテストする
@pytest.mark.parametrize(
    "invalid_users, expected_error_msg",
    [
        ([{"name": "Alice", "age": -5}], "無効な年齢が含まれています。"),  # 負の数
        ([{"name": "Bob", "age": "thirty"}], "無効な年齢が含まれています。"),  # 文字列
        ([{"name": "Charlie"}], "無効な年齢が含まれています。"),  # ageキーが欠落
    ],
)
def test_calculate_average_age_invalid_data(invalid_users, expected_error_msg):
    """無効なデータが含まれる場合に、適切なエラーが発生することを検証します。"""
    with pytest.raises(ValueError, match=expected_error_msg):
        calculate_average_age(invalid_users)
