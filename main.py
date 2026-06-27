from crewai import Crew, Process
from agents import create_research_team, create_tasks

def run_research_pipeline(topic_name):
    print(f"🕵️‍♂️ Initializing AI Agents for topic: '{topic_name}'...\n")
    
    # ۱. ساخت ایجنت‌ها
    researcher, writer = create_research_team()
    
    # ۲. ساخت تسک‌ها بر اساس موضوع ورودی
    tasks = create_tasks(topic_name, researcher, writer)
    
    # ۳. تشکیل تیم چندعاملی
    crew = Crew(
        agents=[researcher, writer],
        tasks=tasks,
        process=Process.sequential, # اجرای زنجیره‌ای و گام‌به‌گام
        verbose=True
    )
    
    print("🚀 Team is collaborating... Please wait.")
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    # موضوع تحقیق را اینجا مشخص کن
    target_topic = "The Rise of Small Language Models (SLMs) in 2026"
    
    final_report = run_research_pipeline(target_topic)
    
    print("\n" + "="*40)
    print("📝 FINAL PERSIAN TECHNICAL REPORT")
    print("="*40 + "\n")
    print(final_report)