def app():   
    import os
    import streamlit as st
    import openai
    from openai import OpenAI

    st.title("Chat With Henitech")
    st.markdown("With 'Chat With Henitech', you can unlock endless conversations– It is your AI companion for engaging and insightful discussions and your solutions provider.")
    st.markdown("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(image='CHAT.jpg', width=700, caption='Chat with Henitech')

    # Access the OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        st.error("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
        st.stop()

    client = OpenAI(api_key=api_key)

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask Henitech..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

