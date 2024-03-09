import streamlit as st

st.header("Quiz Bot 🤖")

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")


nl(1)

st.markdown("""
            **Topic:** History, Movies, or Sports Quiz

            **Description:**
            Welcome to the History, Movies, or Sports Quiz! Test your knowledge about historical events, famous movies, or popular sports trivia. 
            This quiz consists of multiple-choice questions. Read each question carefully and select the most appropriate option. 
            Once you submit your answers, you cannot change them, so make sure to choose wisely!

            **Instructions:**
            - Read each question carefully before selecting an answer.
            - Click on the radio button next to the option you believe is correct.
            - Once you submit your answers, the quiz will be graded, and you will see your final score.

            Good luck and have fun!
            """)

# Create Placeholder to print test score
scorecard_placeholder = st.empty()
# Activate Session States
ss = st.session_state
# Initializing Session States
if 'counter' not in ss:
    ss['counter'] = 0
if 'start' not in ss:
    ss['start'] = False  # Initialize 'start' key to False
if 'stop' not in ss:
    ss['stop'] = False
if 'refresh' not in ss:
    ss['refresh'] = False
if "button_label" not in ss:
    ss['button_label'] = ['START', 'SUBMIT', 'RELOAD']
if 'current_quiz' not in ss:
    ss['current_quiz'] = []
if 'selected_options' not in ss:
    ss['selected_options'] = []
if 'grade' not in ss:
    ss['grade'] = 0

# Function to fetch quiz questions
# def fetch_quiz_questions():
#     import testing2
#     sample_questionss = testing2.mainz()
#     return sample_questionss

# Function to display a question
def display_question(question, question_number):
    # create container
    with st.container():
        number_placeholder = st.empty()
        question_placeholder = st.empty()
        options_placeholder = st.empty()

        # Display the fake question number
        number_placeholder.write(f"*Question {question_number}*")

        # display question based on question_number
        question_placeholder.write(f"**{question['question']}**")

        # list of options
        options = question['options']

        # track the user selection
        selected_option = options_placeholder.radio("", options, key=f"Q{question_number}")

        return selected_option

global I
I = 0

def display_quiz():
    global I
    question_number = 1  # Initialize question number
    selected_options = []  # List to store selected options for each question
    for question in ss['current_quiz']:
        selected_option = display_question(question, question_number)
        # Append the selected option for the current question
        selected_options.append(selected_option)
        I += 1
        question_number += 1  # Increment question number

    # Create a submit button
    submit_button = st.button("Submit")

    # If the submit button is clicked, stop the quiz and calculate the score
    if submit_button:
        ss['stop'] = True
        ss['selected_options'] = selected_options  # Store all selected options

        # Calculate score
        score = 0
        for selected_option, question in zip(selected_options, ss['current_quiz']):
            if selected_option == question['correct_answer']:
                score += 1

        ss['grade'] = score
        scorecard_placeholder.write(f"### **Your Final Score : {ss['grade']} / {len(ss['current_quiz'])}**")

        # Display the correct option of every question
        for question in ss['current_quiz']:
            st.write(f"Correct Answer: {question['correct_answer']}")

        
# Function to fetch quiz questions for sports category
def fetch_sports_quiz_questions():
    import quiz_sports
    sample_questions = quiz_sports.mainz()
    return sample_questions

# Function to fetch quiz questions for history category
def fetch_history_quiz_questions():
    import quiz_history
    sample_questions = quiz_history.mainz()
    return sample_questions

# Function to fetch quiz questions for movies category
def fetch_movies_quiz_questions():
    import quiz_movies
    sample_questions = quiz_movies.mainz()
    return sample_questions

if not ss['start']:
    # Add 3 buttons for selecting quiz category
    if st.button("Start Sports Quiz"):
        ss['start'] = True
        if not ss['current_quiz']:
            ss['current_quiz'] = fetch_sports_quiz_questions()

    if st.button("Start History Quiz"):
        ss['start'] = True
        if not ss['current_quiz']:
            ss['current_quiz'] = fetch_history_quiz_questions()

    if st.button("Start Movies Quiz"):
        ss['start'] = True
        if not ss['current_quiz']:
            ss['current_quiz'] = fetch_movies_quiz_questions()

# Trigger quiz_app function only if the quiz has started
if ss['start'] and not ss['stop']:
    display_quiz()


