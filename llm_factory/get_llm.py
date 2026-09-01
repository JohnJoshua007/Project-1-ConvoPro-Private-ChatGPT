# from llama_index.llms.ollama import Ollama
#
# from config.settings import Settings
#
# settings = Settings()
# OLLAMA_URL = settings.OLLAMA_URL
#
# # Module-level cache for model and instance
# _current_model_name = None
# _current_llm_instance = None
#
#
# def get_ollama_llm(model_name: str):
#     global _current_model_name, _current_llm_instance
#     if _current_model_name == model_name and _current_llm_instance is not None:
#         return _current_llm_instance
#     llm = Ollama(base_url=OLLAMA_URL, model=model_name)
#     _current_model_name = model_name
#     _current_llm_instance = llm
#     return llm
#
#
# # Example usage
# # check_llm = get_ollama_llm(model_name="llama3:latest")
# # print(check_llm)
# # print(type(check_llm))



from llama_index.llms.gemini import Gemini
from config.settings import Settings

settings = Settings()
GOOGLE_API_KEY = settings.GOOGLE_API_KEY

# Module-level cache for model and instance
_current_model_name = None
_current_llm_instance = None


def get_gemini_llm(model_name: str = None):
    """
    Returns a Gemini LLM instance. If model_name is not provided,
    falls back to the default GEMINI_MODEL from settings.
    """
    global _current_model_name, _current_llm_instance

    if model_name is None:
        model_name = settings.GEMINI_MODEL

    # Return cached instance if the same model is requested
    if _current_model_name == model_name and _current_llm_instance is not None:
        return _current_llm_instance

    # Create a new Gemini instance
    llm = Gemini(
        model=f"models/{model_name}",          # e.g., "models/gemini-1.5-flash"
        api_key=GOOGLE_API_KEY,
        temperature=0.7,
    )

    _current_model_name = model_name
    _current_llm_instance = llm
    return llm


# Example usage
# check_llm = get_gemini_llm(model_name="gemini-1.5-flash")
# print(check_llm)
# print(type(check_llm))