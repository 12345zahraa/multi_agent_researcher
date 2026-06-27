# 🤖 Local Multi-Agent Research & Automation Reporting System

یک سیستم هوشمند و خودکار مبتنی بر معماری چندعاملی (Multi-Agent) که با استفاده از مدل‌های زبانی کوچک (SLM) به صورت ۱۰۰٪ محلی و رایگان، فرآیند تحقیق زنده در وب و تولید گزارش‌های مدیریتی به زبان فارسی را اتوماتیک می‌کند.



## 🌟 ویژگی‌های کلیدی (Key Features)

* **جستجوی زنده و بدون محدودیت زمان:** اتصال ایجنت محقق به اینترنت زنده از طریق ابزارهای بومی پایتون جهت استخراج اطلاعات به‌روز.
* **کاملاً محلی و آفلاین (100% Local & Secure):** اجرای تمام فرآیندها روی سیستم بومی با استفاده از مدل‌های Gemma2 و Llama3.2 بدون نیاز به اینترنت برای پردازش مدل و تضمین امنیت کامل داده‌های شرکت.
* **هزینه صفر (Zero-Cost AI):** حذف کامل هزینه‌های سنگین دلاری APIهای تجاری (مانند OpenAI یا Claude).
* **رابط کاربری بومی (Interactive UI):** دارای داشبورد گرافیکی شیک و مدرن با Streamlit مجهز به استایل‌های اختصاصی راست‌چین (RTL) برای نمایش اصولی زبان فارسی.

## 🏗️ ساختار ماژولار پروژه (Project Structure)

پروژه با رعایت اصول Clean Code و به صورت کاملاً ماژولار توسعه یافته است:

* `config.py`: مدیریت تنظیمات لود کردن مدل‌های محلی هوش مصنوعی از طریق Ollama.
* `agents.py`: تعریف دقیق نقش‌ها، اهداف، پیش‌زمینه کارمندان مجازی (Agents) و اتصال ابزارهای جستجو.
* `main.py`: هسته اصلی ارکستراسیون، تعریف تسک‌ها و اجرای خط لوله در محیط ترمینال.
* `app.py`: رابط کاربری گرافیکی پروژه توسعه‌یافته با Streamlit برای استفاده کاربران غیرفنی شرکت.

## 🛠️ تکنولوژی‌های استفاده شده (Tech Stack)

* **Multi-Agent Framework:** CrewAI
* **LLM Orchestration:** Ollama (Gemma2:2b & Llama3.2:1b)
* **Agentic Tools:** LangChain & DuckDuckGo Search API
* **Frontend:** Streamlit (Custom RTL CSS)
* **Language:** Python 3.12+

## 🚀 راهنمای راه‌اندازی (Installation & Running)

۱. ابتدا مخزن را کلون کنید و وارد پوشه پروژه شوید:
```bash
git clone [https://github.com/your-username/multi_agent_researcher.git](https://github.com/your-username/multi_agent_researcher.git)
cd multi_agent_researcher
۲. محیط مجازی را فعال کرده و نیازمندی‌ها را نصب کنید:
# Activation (Windows)
.\venv\Scripts\activate

# Install requirements
pip install crewai streamlit langchain-community pydantic
۳. مطمئن شوید مدل‌های زیر روی Ollama شما نصب هستند:
ollama run gemma2:2b
ollama run llama3.2:1b
۴. اجرای برنامه تحت وب:
python -m streamlit run app.py