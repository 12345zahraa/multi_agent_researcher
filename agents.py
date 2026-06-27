from crewai import Agent, Task
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from config import get_llm

# ۱. تعریف ابزار جستجوی وب
@tool("DuckDuckGo Search")
def web_search_tool(query: str) -> str:
    """Search the internet for latest information on a given topic."""
    search = DuckDuckGoSearchRun()
    return search.run(query)

def create_research_team():
    # ۲. فراخوانی مدل‌های موجود روی سیستم شما
    llm_english = get_llm("llama3.2:1b")  # ایجنت محقق
    llm_persian = get_llm("gemma2:2b")     # ایجنت نویسنده (جایگزین qwen)

    # ۳. تعریف ایجنت محقق
    researcher = Agent(
        role="Senior AI Researcher",
        goal="Search the live internet and find the latest breakthroughs about the given topic.",
        backstory="You are an expert AI researcher. You have access to search tools to scan the web for real-time technical insights.",
        tools=[web_search_tool],
        verbose=True,
        allow_delegation=False,
        llm=llm_english,
    )

    # ۴. تعریف ایجنت نویسنده فارسی (با استفاده از gemma2)
    writer = Agent(
        role="Persian Technical Writer",
        goal="Translate, enrich, and write a comprehensive technical report in Persian (Farsi).",
        backstory="You are a professional tech blogger fluent in Persian. You turn raw search summaries into structured Persian articles.",
        verbose=True,
        allow_delegation=False,
        llm=llm_persian,
    )
    
    return researcher, writer

def create_tasks(topic, researcher, writer):
    task1 = Task(
        description=f"Use your search tool to find recent information about '{topic}'. Extract 3 key breakthroughs, advantages, and real-world use cases.",
        expected_output="A bullet-point summary of the top 3 live insights found on the web in English.",
        agent=researcher,
    )

    task2 = Task(
        description="Take the English live summary from the researcher and write a professional, structured technical report in Persian. Use proper Markdown formatting.",
        expected_output="A complete markdown article written entirely in Persian (Farsi).",
        agent=writer,
    )
    
    return [task1, task2]