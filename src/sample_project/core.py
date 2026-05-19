from typing import Any


def calculate_average_age(users: list[dict[str, Any]]) -> float:
    """ユーザーデータのリストから平均年齢を計算します。

    Args:
        users: ユーザー情報の辞書のリスト。
               例: [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]

    Returns:
        float: 計算された平均年齢。

    Raises:
        ValueError: リストが空の場合、または年齢に無効な値（負の数など）が含まれる場合。
    """
    if not users:
        raise ValueError("ユーザーリストが空です。")

    total_age = 0
    for user in users:
        age = user.get("age")

        # 年齢データが存在しない、または負の数の場合はエラーにする
        if age is None or not isinstance(age, (int, float)) or age < 0:
            raise ValueError("無効な年齢が含まれています。")

        total_age += age

    return total_age / len(users)
