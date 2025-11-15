import streamlit as st

variants = ['Show me text', 'Show me widget', 'Show me interesting calculations']

st.title("hey nigga!")

selected_option = st.selectbox("Choose option:", variants)

if selected_option == 'Show me text':
    st.write("You chose:", selected_option)
    st.write("The most fckin boring text in da world")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    if st.button('Earn money'):
        st.write("Suck my penis idiot GUGUGAGA")
elif selected_option == 'Show me widget':
    femboyvalue = st.slider('How much of a femboy are you on a scale of 1 to 10?', 1, 10, 10)
    if femboyvalue < 5:
        st.error("SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI SORA AI")
    elif femboyvalue == 10:
        st.success('Good boy <3')
    elif 10 > femboyvalue > 4:
        st.write('Mhm, noted')
elif selected_option == 'Show me interesting calculations':
    user_month = (st.text_input("Number of your month of birth"))
    if user_month == '':
        st.info("Write your month of birth as a number (1-12)")
    elif 12 >= int(user_month) >= 1:
        if int(user_month) == 12:
            conceivemonth = "March"
        elif int(user_month) == 1:
            conceivemonth = "April"
        elif int(user_month) == 2:
            conceivemonth = "May"
        elif int(user_month) == 3:
            conceivemonth = "June"
        elif int(user_month) == 4:
            conceivemonth = "July"
        elif int(user_month) == 5:
            conceivemonth = "August"
        elif int(user_month) == 6:
            conceivemonth = "September"
        elif int(user_month) == 7:
            conceivemonth = "October"
        elif int(user_month) == 8:
            conceivemonth = "November"
        elif int(user_month) == 9:
            conceivemonth = "December"
        elif int(user_month) == 10:
            conceivemonth = "January"
        elif int(user_month) == 11:
            conceivemonth = "February"
        st.write(f'Congratulations, you were most likely conceived in {conceivemonth}.')
    else:
        st.error("Please enter a valid month number (1-12).")
