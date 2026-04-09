import streamlit as st
import random

st.title("⏳ Guess A Number Game ⌛️")

# store game state
if "random_num" not in st.session_state:
    st.session_state.random_num = random.randint(1, 13)
    st.session_state.attempt = 1
    st.session_state.game_over = False

# user input
name = st.text_input("Enter Your Name")

if name:
    st.write(f"Welcome {name} 😎")
    st.write("I am thinking of a number between 1 and 13 🧐")

    if not st.session_state.game_over:

        guess = st.number_input(
            f"Attempt {st.session_state.attempt} - Take a Guess",
            min_value=1,
            max_value=13,
            step=1
        )

        if st.button("Submit Guess"):

            if guess == st.session_state.random_num:
                st.success("🎉 Congratulations! Correct Guess 🎉")
                st.write(f"You guessed the number in {st.session_state.attempt} attempt(s).")
                st.balloons()
                st.session_state.game_over = True

            elif guess > st.session_state.random_num:
                st.warning("Your Guess Is Too HIGH ⬆️ Think Of A Smaller Number")
                st.session_state.attempt += 1

            elif guess < st.session_state.random_num:
                st.warning("Your Guess Is Too LOW ⬇️ Think Of A Bigger Number")
                st.session_state.attempt += 1

        # game over condition
        if st.session_state.attempt > 4 and not st.session_state.game_over:
            st.error("❌ GAME OVER! ❌")
            st.write(f"The Correct Number Was {st.session_state.random_num} ❇️")
            st.session_state.game_over = True

# restart button
if st.button("Restart Game"):
    st.session_state.random_num = random.randint(1, 13)
    st.session_state.attempt = 1
    st.session_state.game_over = False
