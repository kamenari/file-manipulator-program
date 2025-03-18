from .guess_number_game import play_game


def main():
    """
    数当てゲームのメインエントリーポイント。
    ユーザーの入力を受け付け、ゲームの実行を制御します。

    ゲームの流れ:
    1. ユーザーから数値の範囲と試行回数を入力
    2. play_game関数を呼び出してゲームを実行
    3. 結果を表示し、続けてプレイするか確認
    4. エラー発生時は適切なメッセージを表示
    """
    print("数当てゲームへようこそ！")

    while True:
        try:
            # ゲームの設定値を入力
            min_value = int(input("最小値を入力してください: "))
            max_value = int(input("最大値を入力してください: "))
            max_attempts = input(
                "最大試行回数を入力してください（制限なしの場合はEnter）: "
            )

            # 最大試行回数の設定（入力がない場合はNone）
            max_attempts = int(max_attempts) if max_attempts else None

            # ゲームを実行し、結果を取得
            success, attempts = play_game(min_value, max_value, max_attempts)

            # ゲーム結果の表示
            if success:
                print(f"おめでとうございます！{attempts}回で正解を当てました！")
            else:
                print(
                    f"残念ながら、{attempts}回以内に正解を当てることができませんでした。"
                )

            # 継続確認
            play_again = input("もう一度プレイしますか？(y/n): ")
            if play_again.lower() != "y":
                break

        except ValueError as e:
            # 数値変換エラーや範囲の検証エラーの処理
            print(f"エラー: {str(e)}")
        except Exception as e:
            # 予期せぬエラーの処理
            print(f"予期せぬエラーが発生しました: {str(e)}")

    print("ゲームを終了します。ありがとうございました！")


if __name__ == "__main__":
    main()
