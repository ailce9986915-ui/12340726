import streamlit as st

# 1. 設定初始菜單與購物車
menu = {
    "大麥克": 130,
    "麥脆雞": 60,
    "薯條": 50,
    "可樂": 40
}

if 'cart' not in st.session_state:
    st.session_state.cart = {}

st.title("🍔 簡易點餐系統")

# 2. 顯示菜單與加入購物車按鈕
st.subheader("菜單列表")
cols = st.columns(len(menu))
for i, (item, price) in enumerate(menu.items()):
    if cols[i].button(f"{item}\n${price}"):
        if item in st.session_state.cart:
            st.session_state.cart[item] += 1
        else:
            st.session_state.cart[item] = 1
        st.rerun()

# 3. 顯示購物車與結帳
st.divider()
st.subheader("🛒 您的購物車")

if not st.session_state.cart:
    st.write("目前購物車是空的")
else:
    total = 0
    for item, qty in st.session_state.cart.items():
        price = menu[item] * qty
        total += price
        st.write(f"{item} x {qty} = ${price}")
    
    st.write(f"### 總金額: ${total}")
    
    if st.button("結帳確認"):
        st.success(f"結帳成功！總共付款 ${total}")
        st.session_state.cart = {} # 清空購物車
        st.rerun()

# 4. 清除購物車按鈕
if st.button("清空購物車"):
    st.session_state.cart = {}
    st.rerun()
