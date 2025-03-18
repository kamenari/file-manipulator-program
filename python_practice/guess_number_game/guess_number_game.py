from random import randint
from typing import Tuple, Optional


def validate_range(min_value: int, max_value: int) -> bool:
    """
    入力された数値の範囲が有効かどうかを検証します。

    Args:
        min_value (int): 最小値
        max_value (int): 最大値

    Returns:
        bool: 最小値が最大値以下の場合はTrue、それ以外はFalse

    検証内容:
    - 最小値が最大値以下であることを確認
    """
    return min_value <= max_value


def generate_target_number(min_value: int, max_value: int) -> int:
    """
    指定された範囲内でランダムな目標値を生成します。

    Args:
        min_value (int): 生成する乱数の最小値
        max_value (int): 生成する乱数の最大値

    Returns:
        int: 生成されたランダムな整数値

    注意:
    - randintは両端の値を含む範囲で乱数を生成します
    """
    return randint(min_value, max_value)


def compare_guess(guess: int, target: int) -> Tuple[bool, str]:
    """
    ユーザーの推測値と目標値を比較し、結果とヒントを返します。

    Args:
        guess (int): ユーザーが入力した推測値
        target (int): プログラムが生成した目標値

    Returns:
        Tuple[bool, str]:
            - 1番目の要素: 正解の場合はTrue、不正解の場合はFalse
            - 2番目の要素: ユーザーへのヒントメッセージ

    ヒントの種類:
    - 正解の場合: "正解です！"
    - 推測が小さい場合: "もっと大きい数字です"
    - 推測が大きい場合: "もっと小さい数字です"
    """
    if guess == target:
        return True, "正解です！"
    elif guess < target:
        return False, "もっと大きい数字です"
    else:
        return False, "もっと小さい数字です"


def play_game(
    min_value: int, max_value: int, max_attempts: Optional[int] = None
) -> Tuple[bool, int]:
    """
    数当てゲームの主要なロジックを実行します。

    Args:
        min_value (int): ゲームで使用する最小値
        max_value (int): ゲームで使用する最大値
        max_attempts (Optional[int]): 最大試行回数（Noneの場合は制限なし）

    Returns:
        Tuple[bool, int]:
            - 1番目の要素: ゲームの成功/失敗
            - 2番目の要素: 実際の試行回数

    処理の流れ:
    1. 入力された範囲の妥当性を検証
    2. 目標値をランダムに生成
    3. ユーザーからの入力を受け付け
    4. 入力値の範囲チェック
    5. 推測値と目標値の比較
    6. 結果に応じたフィードバック
    7. 試行回数の制限チェック

    Raises:
        ValueError: 最小値が最大値より大きい場合に発生
    """
    if not validate_range(min_value, max_value):
        raise ValueError("最小値は最大値以下である必要があります")

    target = generate_target_number(min_value, max_value)
    attempts = 0

    while True:
        try:
            # ユーザーからの入力を受け付け
            guess = int(
                input(f"{min_value}から{max_value}の間の数字を入力してください: ")
            )
            attempts += 1

            # 入力値の範囲チェック
            if not min_value <= guess <= max_value:
                print(f"入力値は{min_value}から{max_value}の間である必要があります")
                continue

            # 推測値の評価
            is_correct, message = compare_guess(guess, target)
            print(message)

            # 正解の場合
            if is_correct:
                return True, attempts

            # 試行回数制限のチェック
            if max_attempts and attempts >= max_attempts:
                return False, attempts

        except ValueError:
            print("有効な数字を入力してください")
