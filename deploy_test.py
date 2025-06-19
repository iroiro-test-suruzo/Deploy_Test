import streamlit as st
import pandas as pd
import numpy as np

# タイトル
st.title("Deploy_Testアプリ")

# データの作成
st.subheader("売上データの例（架空）")
months = ["1月", "2月", "3月", "4月", "5月", "6月"]
sales = np.random.randint(100, 500, size=len(months))

# DataFrameにまとめる
df = pd.DataFrame({
    "月": months,
    "売上": sales
})

# データの表示
st.dataframe(df)

# 棒グラフの表示
st.subheader("月別売上の棒グラフ")
st.bar_chart(df.set_index("月"))

# 折れ線グラフ（比較用）
st.subheader("月別売上の折れ線グラフ")
st.line_chart(df.set_index("月"))
