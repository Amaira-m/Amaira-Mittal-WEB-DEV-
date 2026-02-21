import streamlit as st


def run():
    st.title("What is your emotional quotient (EQ)🧠")

    #Header image
    st.image("images/header.jpg", caption="Feeling introspective?")

    st.header("The Quiz")

    score = 0

    #ques1
    st.subheader("1. Self-Awareness")
    q1 = st.radio( #NEW
    "When you feel angry at work or school, what is your immediate reaction?",
    ["I suppress it and say nothing", 
     "I snap back at the person.", 
     "I step back and analyse my feelings"]
    )

    if q1== "I step back and anaylyse my feelings":
        score +=10
    elif q1== "I suppress it and say nothing":
        score += 5
        

    #q2
    st.subheader("2. Emotional Regulation")
    q2 = st.slider( #NEW
        "On a scale of 1-5, how easily can you calm yourself down after a stressful incident?",
        1,5,1
    )

    score += q2

    #q3
    st.subheader("3. Empathy")
    st.image("images/empathy.jpg", width= 300)
    q3 = st.selectbox( #NEW
        "A friend tells you they are going through a tough time. You ...",
        ["Change the subject to cheer them up.",
         "Listen carefully and validate their feelings and emotions.",
         "Offer fixative advice right away."]
    )


    if q3 == "Listen carefully and validate their feelings and emotions.":
        score += 10
    elif q3 == "Offer fixative advice right away.":
        score += 5

    #ques 4
    st.subheader("4. Social Skills")
    q4 = st.number_input( #NEW
        "How many active listening techniques (eg. Mirroring behaviour, head nodds, etc.) do you conciously use in a conversation (Enter a number between 1-5)",
        min_value=0, max_value=5, step=1

    )

    score += (q4 * 2)


    #ques5
    st.subheader("5. Driver")
    st.image("images/driver.jpg", width=300)
    q5= st.multiselect( #NEW
        "Which of the following drive you to achieve your goals?",
        ["Curiosity to learn", "Fear of Failure", "External/materialistic rewards","Personal goals"]
    )


    if "Curiosity to learn" in q5:
        score += 5
    if "Personal growth" in q5:
        score += 5


    st.markdown("---")


   #ques 6 - EXTRA CREDIT
    st.subheader("6. Conflict Management")
    q7 = st.select_slider( #NEW
        "How do you handle disagreements?",
        options=["Avoidance", "Compromise", "Talk it out"]
    )
    
    if q7 == "Talk it out":
        score += 10
    elif q7 == "Compromise":
        score += 5
        
    #ques 7 - EXTRA CREDIT
    st.subheader("7. Resilience")
    q6 = st.toggle("Do you view failures as learning opportunities or speed bumps?", key="resilience_toggle") #NEW (Added tag)
    if q6:
        score += 10

    #ques 8 - EXTRA CREDIT
    st.subheader("8. Mindfulness")
    q8 = st.text_input("Briefly describe one emotion you felt throughout the day today", key="mindfulness_input") #NEW
    if len(q8) > 2:
        
        score += 5
        
    st.markdown("---")

    if st.button("Calculate My EQ", key="calc_button"):
        st.write("Calculating score...")
        
        my_bar = st.progress(0)
        for percent_complete in range(100):
            my_bar.progress(percent_complete + 1)

        st.subheader("Your Total Score: {}".format(score))

        if score >= 50:
            st.success("Result: High Emotional Intelligence!")
            st.write("You have a strong grasp of your own emotions and those of others.")
            st.balloons() #NEW
            
        elif score >= 25:
            st.info("Result: Average Emotional Intelligence")
            st.write("There is room to grow!!")
            
        else:
            st.warning("Result: Developing Emotional Intelligence")
            st.write("Focusing on self-awareness exercises could be very beneficial!!!!")

run()
