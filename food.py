import json
import random
import pandas as pd
from linebot import LineBotApi
from linebot.models import TextSendMessage

# linebotの情報が記録されたファイルを読み込む
file = open('info.json', 'r')
info = json.load(file)

# 使用するlinebotのAPIにアクセスする
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

# ボットに言ってもらいたい言葉のcsvを読み込む
df = pd.read_csv('wordlist.csv', index_col=0)

# botに実行してもらいたい処理を記述
def main():
    USER_ID = info['USER_ID']

    # 先にレシピを送信
    messages = TextSendMessage(text=random.choice(df.loc['food']))
    line_bot_api.push_message(USER_ID, messages=messages)

    # そのあとでメッセージを送信
    text = random.choice(df.loc['food_firsthalf']) + random.choice(df.loc['food_latterhalf']) + "\U0001F37D"
    messages = TextSendMessage(text=text)
    line_bot_api.push_message(USER_ID, messages=messages)


if __name__ == "__main__":
    main()
