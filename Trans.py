
def app():
    
    import streamlit as st
    from langchain import PromptTemplate
    from langchain.llms import OpenAI
    from langchain_community.llms import OpenAI
    from languages import languages
    
    
    import os
    import openai 

    openai.api_key =os.getenv("OPENAI_API_KEY")
    template = """
        Translation Task

        You are tasked with translating a piece of text from one language to another. Your goal is to accurately convey the meaning, tone, and nuances of the original text while ensuring fluency and coherence in the translated output.
        
        Below is the sentence, tone, and dialect:
        DETECT: {detect}
        TARGET: {target}
        SENTENCE: {sentence}

        YOUR RESPONSE:
    """

    prompt = PromptTemplate(
        input_variables = ["Detected", "target", "sentence"],
        template=template,
    )

    def load_LLM():
        """Logic for loading the chain you want to use should go here."""
        llm = OpenAI(temperature = 0.5)
        return llm

    llm = load_LLM()

    st.title("Henitech Language Translator")
    st.markdown("For EASY AND QUICK LANGUAGE TRANSLATION, use Henitech Language Translator for seamless communication across borders. It effortlessly breaks down linguistic barriers to foster global understanding and connection")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(image='techh.jpg', width=700, caption='Henitech')

    def get_text():
        source_text = st.text_area(label="", placeholder="Enter text to translate:", key="sentence_input")
        return source_text
    
    sentence_input = get_text()

    col1, col2 = st.columns(2)
    with col1:
        detect_text = st.selectbox('Detected language', languages)
    with col2:
        target_language = st.selectbox("Select target language:", languages)
    # Translate button
    col1, col2, col3 = st.columns(3)
    with col2:
        translate_button = st.button("Translate")

    if sentence_input:
        prompt_with_sentence = prompt.format(detect=detect_text, target=target_language, sentence=sentence_input)

        formatted_sentence = llm(prompt_with_sentence)

    if translate_button:        
        st.text_area(label="Your Translated Sentence:", value=formatted_sentence, height=100)
            
   