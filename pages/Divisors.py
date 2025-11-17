import streamlit as st

st.title("🔢 약수 계산기")

number = st.number_input("숫자를 입력하세요:", min_value=1, step=1)

def get_divisors(n: int):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if st.button("약수 구하기"):
    divisors = get_divisors(number)
    st.success(f"🔍 {number}의 약수는 다음과 같습니다:")
    st.write(divisors)
