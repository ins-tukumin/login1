import streamlit as st

# 各グループに対応するURLを定義します
group_urls = {
    "group1": "https://www.yahoo.co.jp/",
    "group2": "https://www.microsoft.com/ja-jp/edge?form=MA13FJ",
    "group3": "https://www.google.com/maps"
}

# participants.txtファイルからIDとグループを読み込む関数
def load_participants(file_path):
    participants = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    user_id, group = line.split(',')
                    participants[user_id] = group
    except FileNotFoundError:
        st.error("参加者リストファイルが見つかりません。")
    return participants

# Streamlitアプリケーションのレイアウト
st.title("ログインページ")

# 参加者のリストを読み込む
participants = load_participants('participants.txt')

user_id = st.text_input("IDを入力してください")

if user_id:
    group = participants.get(user_id)
    if group:
        group_url = group_urls.get(group)
        if group_url:
            st.markdown(f'こちらのURLをクリックしてください: <a href="{group_url}" target="_blank">リンク</a>', unsafe_allow_html=True)
        else:
            st.write("対応するグループURLが見つかりません。")
    else:
        st.write("無効なIDです。もう一度お試しください。")

# アプリケーションを実行するには、以下のコマンドを使用します
# streamlit run app.py
