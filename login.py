import streamlit as st

# 各グループに対応するURLを定義します
group_urls = {
    "groupa": "https://llmrel.streamlit.app/",
    "groupb": "https://llmrel.streamlit.app/",
    "groupc": "https://ragrel.streamlit.app/",
    "groupd": "https://ragrel.streamlit.app/",
    "groupe": "https://llmrel.streamlit.app/",
    "groupf": "https://llmrel.streamlit.app/",
    "groupg": "https://ragepre.streamlit.app/",
    "grouph": "https://ragepre.streamlit.app/",
    "xxxx": "https://openai.com/chatgpt/"
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
        pass  # ファイルが見つからない場合でもエラーを表示しない

    # リストにないIDには "xxxx" を割り当てる
    for user_id, group in participants.items():
        if not group:
            participants[user_id] = "xxxx"
    
    return participants
    
# Streamlitアプリケーションのレイアウト
st.title("ログインページ")

# 参加者のリストを読み込む
participants = load_participants('group_assignment.txt')

user_id = st.text_input("学籍番号を半角で入力してください")
if st.button("ログイン"):
    if user_id:
        group = participants.get(user_id, "xxxx")
        group_url = group_urls.get(group, group_urls["xxxx"])
        group_url_with_id = f"{group_url}?user_id={user_id}&group={group}"
        #st.success(f"ログイン成功: {user_id}")
        st.markdown(f'こちらのURLをクリックしてください: <a href="{group_url_with_id}" target="_blank">リンク</a>', unsafe_allow_html=True)
    else:
        st.write("学籍番号を入力してください。")
