import openai
import streamlit as st

# Configure your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_response(messages):
    """Send a message to OpenAI GPT and get a response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Er is een fout opgetreden: {e}"

def chatbot_interface():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "system", "content": (
                "Je bent een behulpzame matchmaker die studenten helpt met hun scriptiebegeleiding. "
                "Gebruik relevante informatie van www.scriptiemaster.nl om vragen over begeleiding, diensten en tarieven te beantwoorden. "
                "Geef duidelijke, behulpzame antwoorden en verwijs naar de website als extra informatie nodig is."
            )}
        ]

    if "questions" not in st.session_state:
        st.session_state.questions = [
            "Wat is jouw naam?",
            "Wat is jouw e-mailadres?",
            "Wat is jouw telefoonnummer?",
            "Wat is de naam van jouw onderwijsinstelling?",
            "Welke studie volg je?",
            "Waar sta je momenteel in het scriptietraject? (Bijvoorbeeld: beginfase, onderzoek doen, schrijven, afronden)",
            "Wat zijn jouw deadlines? Heb je al een conceptversie of definitieve versie gepland?",
            "Heb je voor jezelf een scriptieplan gemaakt met tussentijdse deadlines?",
            "Hoe is het contact met je huidige scriptiebegeleider? Geeft deze voldoende begeleiding of mis je iets?",
            "Wat is jouw onderwerp?",
            "Waar loop je het meest tegenaan in je scriptie?",
            "Wat is jouw hulpvraag of wat zijn jouw hulpvragen?",
            "Op hoeveel % van de scriptie zit je nu ongeveer?",
            "Hoeveel tijd heb je zelf voor je scriptie (in uren per week)?"
        ]

    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0

    st.title("ScriptieMaster Matchmaker Chat")
    st.write("Welkom! Praat met onze matchmaker om jouw ideale scriptiebegeleiding te vinden.")

    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "assistant":
            st.markdown(f"**Matchmaker:** {message['content']}")
        elif message["role"] == "user":
            st.markdown(f"**Jij:** {message['content']}" )

    # Handle user input
    user_input = st.text_input("Stel je vraag of geef een antwoord:", key="user_input")

    if st.button("Verstuur"):
        if user_input.strip():
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            # Check if a question is being answered
            if st.session_state.current_question_index < len(st.session_state.questions):
                current_question = st.session_state.questions[st.session_state.current_question_index]
                st.session_state.answers[current_question] = user_input
                st.session_state.current_question_index += 1

                # Move to next question
                if st.session_state.current_question_index < len(st.session_state.questions):
                    next_question = st.session_state.questions[st.session_state.current_question_index]
                    st.session_state.chat_history.append({"role": "assistant", "content": next_question})
                else:
                    # All questions answered
                    st.session_state.chat_history.append({"role": "assistant", "content": "Bedankt! Hier is een samenvatting van je antwoorden:"})
                    summary = "\n".join([f"{q}: {a}" for q, a in st.session_state.answers.items()])
                    st.session_state.chat_history.append({"role": "assistant", "content": summary})

            else:
                # Handle freeform questions
                bot_response = generate_response(st.session_state.chat_history)
                st.session_state.chat_history.append({"role": "assistant", "content": bot_response})

                # Ask if the user wants to return to the questionnaire
                st.session_state.chat_history.append({"role": "assistant", "content": "Wil je doorgaan met de vragenlijst om tot een goed advies te komen?"})

    # Allow resumption of questionnaire
    if st.button("Ja, ga verder met de vragenlijst") and st.session_state.current_question_index < len(st.session_state.questions):
        next_question = st.session_state.questions[st.session_state.current_question_index]
        st.session_state.chat_history.append({"role": "assistant", "content": next_question})

if __name__ == "__main__":
    chatbot_interface()
