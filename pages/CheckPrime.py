import streamlit as st

st.title("🔍 소수 판별기")

number = st.number_input("숫자를 입력하세요:", min_value=1, step=1)

def is_prime(n: int):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if st.button("소수인지 확인하기"):
    if is_prime(number):
        st.success(f"🎉 {number}는 소수(Prime Number)입니다!")
    else:
        st.error(f"❌ {number}는 소수가 아닙니다.")
