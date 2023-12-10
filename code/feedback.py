def capture_feedback(user_feedback, feedback_history):
    feedback_history.append(user_feedback)
    # You may want to store feedback_history persistently, like in a database or file.
    # Return a confirmation or success message.
    return "Feedback captured successfully."

def view_feedback(feedback_history):
    # Display or analyze feedback data.
    return feedback_history
