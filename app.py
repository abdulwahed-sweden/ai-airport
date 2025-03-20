import streamlit as st
import pandas as pd

# تحميل البيانات
df = pd.read_csv("cleaned_international_airports.csv")

# واجهة المستخدم في Streamlit
st.title("✈️ International Airports Search")
st.write("🔍 ابحث عن المطارات حسب الدولة")

# إدخال اسم الدولة من المستخدم
country = st.text_input("🌍 أدخل اسم الدولة:")

# تصفية البيانات حسب الدولة
if country:
    result = df[df["Country"].str.contains(country, case=False, na=False)]
    st.write(result)
else:
    st.write("💡 أدخل اسم الدولة للبحث عن المطارات.")

# عرض البيانات الكاملة
st.write("📌 قائمة جميع المطارات المتاحة:")
st.dataframe(df)
