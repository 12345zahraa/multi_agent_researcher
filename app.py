import streamlit as st
from agents import create_research_team, create_tasks
from crewai import Crew, Process

# ۱. تنظیمات ظاهری صفحه وب
st.set_page_config(page_title="دستیار تحقیق هوشمند چندعاملی", page_icon="🤖", layout="wide")

# ۲. تزریق کد CSS اصلاح‌شده برای راست‌چین کردن (RTL)
st.markdown("""
    <style>
    body, div, p, h1, h2, h3, h4, h5, h6, li, span {
        direction: RTL !important;
        text-align: right !important;
    }
    .stTextInput th, .stTextInput td, .stTextInput input {
        direction: RTL !important;
        text-align: right !important;
    }
    ul {
        list-style-position: inside !important;
        padding-right: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 سیستم چندعاملی تحقیق و گزارش‌نویسی خودکار")
st.write("موضوع مورد نظر خود را وارد کنید تا ایجنت‌های هوشمند به صورت محلی تحقیق کرده و گزارش فارسی تحویل دهند.")

# کادر ورود موضوع به صورت راست‌چین
topic = st.text_input("موضوع تحقیق را اینجا بنویسید:", placeholder="مثلاً: کاربرد مدل‌های زبانی کوچک در سال ۲۰۲۶")

if st.button("شروع فرآیند تحقیق و تولید گزارش"):
    if not topic:
        st.warning("لطفاً ابتدا یک موضوع وارد کنید.")
    else:
        with st.spinner("⏳ ایجنت‌های هوشمند در حال سرچ در اینترنت و نگارش گزارش هستند... لطفاً منتظر بمانید (این فرآیند ممکن است ۱ الی ۳ دقیقه زمان ببرد)"):
            try:
                # بیدار کردن ایجنت‌ها
                researcher, writer = create_research_team()
                
                # ساخت تسک‌ها بر اساس موضوعی که کاربر تایپ کرده
                tasks = create_tasks(topic, researcher, writer)
                
                # تشکیل تیم (Crew)
                crew = Crew(
                    agents=[researcher, writer],
                    tasks=tasks,
                    process=Process.sequential,
                    verbose=True
                )
                
                # اجرای فرآیند و گرفتن خروجی نهایی
                result = crew.kickoff()
                
                # نمایش خروجی نهایی به صورت شیک و راست‌چین در سایت
                st.success("✅ گزارش با موفقیت آماده شد!")
                st.markdown("### 📋 گزارش فنی و مدیریتی نهایی:")
                st.markdown(result.raw)
                
            except Exception as e:
                st.error(f"خطایی در اجرای سیستم رخ داد: {e}")