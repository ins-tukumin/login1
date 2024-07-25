import streamlit as st

# 各グループに対応するURLを定義します
group_urls = {
    "group1": "https://ragepre.streamlit.app/",
    "group2": "https://llmrel.streamlit.app/",
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

# セッション状態を初期化
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_id = ""
    st.session_state.group = ""

# 参加者のリストを読み込む
participants = load_participants('participants.txt')

if st.session_state.logged_in:
    st.success(f"ログイン済み: {st.session_state.user_id}")
    group_url = group_urls.get(st.session_state.group)
    if group_url:
        group_url_with_id = f"{group_url}?user_id={st.session_state.user_id}"
        st.markdown(f'こちらのURLをクリックしてください: <a href="{group_url_with_id}" target="_blank">リンク</a>', unsafe_allow_html=True)
    else:
        st.write("対応するグループURLが見つかりません。")
else:
    user_id = st.text_input("IDを半角で入力してください")
    if st.button("ログイン"):
        if user_id:
            group = participants.get(user_id)
            if group:
                st.session_state.logged_in = True
                st.session_state.user_id = user_id
                st.session_state.group = group
                # st.success(f"ログイン成功: {user_id}")
                st.experimental_rerun()
            else:
                st.write("無効なIDです。もう一度お試しください。")

