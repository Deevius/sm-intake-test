import streamlit as st

def intake_chat():
    if "step" not in st.session_state:
        st.session_state.step = 0

    st.title("ScriptieMaster Intake Chat")
    st.write("Welkom! Laten we beginnen met enkele vragen over jouw scriptie.")

    st.sidebar.write("**Debug Info**")
    st.sidebar.write(f"Current Step: {st.session_state.step}")

    if st.session_state.step == 0:
        st.header("Persoonlijke Gegevens")
        naam = st.text_input("Wat is jouw naam?")
        mail = st.text_input("Wat is jouw e-mailadres?")
        telefoon = st.text_input("Wat is jouw telefoonnummer?")
        onderwijsinstelling = st.text_input("Wat is de naam van jouw onderwijsinstelling?")
        studie = st.text_input("Welke studie volg je?")

        if st.button("Volgende"):
            if naam and mail and telefoon and onderwijsinstelling and studie:
                st.session_state.naam = naam
                st.session_state.mail = mail
                st.session_state.telefoon = telefoon
                st.session_state.onderwijsinstelling = onderwijsinstelling
                st.session_state.studie = studie
                st.session_state.step = 1
            else:
                st.error("Vul alle velden in voordat je doorgaat.")

    elif st.session_state.step == 1:
        st.header("Huidige Status")
        status = st.text_input("Waar sta je momenteel in het scriptietraject? (Bijvoorbeeld: beginfase, onderzoek doen, schrijven, afronden)")

        if st.button("Volgende"):
            if status:
                st.session_state.status = status
                st.session_state.step = 2
            else:
                st.error("Vul het veld in voordat je doorgaat.")

    elif st.session_state.step == 2:
        st.write(f"Dank je! Je gaf aan dat je in de '{st.session_state.status}'-fase zit.")
        deadline = st.text_input("Wat zijn jouw deadlines? Heb je al een conceptversie of definitieve versie gepland?")

        if st.button("Volgende"):
            if deadline:
                st.session_state.deadline = deadline
                st.session_state.step = 3
            else:
                st.error("Vul het veld in voordat je doorgaat.")

    elif st.session_state.step == 3:
        st.write(f"Super! Het is goed om je deadline in gedachten te houden: {st.session_state.deadline}.")
        planning = st.radio("Heb je voor jezelf een scriptieplan gemaakt met tussentijdse deadlines?", ("Ja", "Nee"))

        if st.button("Volgende"):
            st.session_state.planning = planning
            st.session_state.step = 4

    elif st.session_state.step == 4:
        if st.session_state.planning == "Ja":
            st.write("Dat is fantastisch! Een goede planning is de sleutel tot succes.")
        else:
            st.write("Geen zorgen, we kunnen je helpen een planning op te stellen.")

        begeleiding = st.text_area("Hoe is het contact met je huidige scriptiebegeleider? Geeft deze voldoende begeleiding of mis je iets?")

        if st.button("Volgende"):
            if begeleiding:
                st.session_state.begeleiding = begeleiding
                st.session_state.step = 5
            else:
                st.error("Vul het veld in voordat je doorgaat.")

    elif st.session_state.step == 5:
        st.write(f"Dank je! Je gaf aan: '{st.session_state.begeleiding}'. Het is belangrijk dat je begeleiding krijgt die goed bij je past.")
        onderwerp = st.text_input("Wat is jouw onderwerp?")

        if st.button("Volgende"):
            if onderwerp:
                st.session_state.onderwerp = onderwerp
                st.session_state.step = 6
            else:
                st.error("Vul het veld in voordat je doorgaat.")

    elif st.session_state.step == 6:
        st.write(f"Interessant onderwerp: {st.session_state.onderwerp}.")
        uitdaging = st.text_area("Waar loop je het meest tegenaan in je scriptie?")

        if st.button("Volgende"):
            if uitdaging:
                st.session_state.uitdaging = uitdaging
                st.session_state.step = 7
            else:
                st.error("Vul het veld in voordat je doorgaat.")

    elif st.session_state.step == 7:
        st.write(f"Dank je. Je grootste uitdaging is: {st.session_state.uitdaging}.")
        hulpvraag = st.text_area("Wat is jouw hulpvraag of wat zijn jouw hulpvragen?")

        if st.button("Volgende"):
            if hulpvraag:
                st.session_state.hulpvraag = hulpvraag
                st.session_state.step = 8
            else:
                st.error("Vul het veld in voordat je doorgaat.")

    elif st.session_state.step == 8:
        st.write(f"Dank je! Jouw hulpvraag is: {st.session_state.hulpvraag}.")
        voortgang = st.slider("Op hoeveel % van de scriptie zit je nu ongeveer?", 0, 100, 0)

        if st.button("Volgende"):
            st.session_state.voortgang = voortgang
            st.session_state.step = 9

    elif st.session_state.step == 9:
        st.write(f"Je gaf aan dat je op ongeveer {st.session_state.voortgang}% van je scriptie zit.")
        tijd = st.number_input("Hoeveel tijd heb je zelf voor je scriptie (in uren per week)?", min_value=0, step=1)

        if st.button("Volgende"):
            st.session_state.tijd = tijd
            st.session_state.step = 10

    elif st.session_state.step == 10:
        st.write(f"Je hebt ongeveer {st.session_state.tijd} uur per week beschikbaar.")
        st.write("Op basis van jouw antwoorden bereken ik een passend advies.")
        resterend_percentage = 100 - st.session_state.voortgang
        geschatte_uren = int(resterend_percentage * 0.3)  # Schatting: 30% per uur

        if geschatte_uren < 10:
            pakket = "10 uur begeleiding"
        elif geschatte_uren <= 20:
            pakket = "20 uur begeleiding"
        else:
            pakket = "30 uur begeleiding"

        st.write(f"Advies: Je hebt waarschijnlijk {pakket} nodig om jouw scriptie succesvol af te ronden.")
        extra = st.text_area("Wil je nog iets aanpassen of extra toevoegen aan deze informatie?")
        if extra:
            st.write(f"Extra informatie toegevoegd: {extra}")

if __name__ == "__main__":
    intake_chat()
