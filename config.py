from crewai import LLM

def get_llm(model_name="llama3.2:1b"):
    """تعریف مدل اولاما با ساختار استاندارد و بومی CrewAI"""
    return LLM(
        model=f"ollama/{model_name}",
        base_url="http://localhost:11434"
    )