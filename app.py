
import streamlit as st

# Custom CSS for Styling & Animations
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #ff9966, #ff5e62);
        font-family: 'Poppins', sans-serif;
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        background-color: #fff !important;
        color: #333 !important;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
    }
    .task-card {
        background: rgba(255, 255, 255, 0.8);
        padding: 12px;
        border-radius: 12px;
        box-shadow: 4px 4px 12px rgba(0,0,0,0.2);
        margin-bottom: 12px;
        font-size: 18px;
        transition: 0.3s ease-in-out;
    }
    .task-card:hover {
        transform: scale(1.05);
    }
    .delete-btn {
        background-color: red !important;
        color: white !important;
        border-radius: 8px;
        padding: 6px 10px;
        font-size: 16px;
        transition: 0.3s ease;
    }
    .delete-btn:hover {
        background-color: darkred !important;
        transform: scale(1.1);
    }
    .add-btn {
        background-color: green !important;
        color: white !important;
        border-radius: 8px;
        padding: 10px 15px;
        font-size: 16px;
        transition: 0.3s ease;
    }
    .add-btn:hover {
        background-color: darkgreen !important;
        transform: scale(1.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Session state to store tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title("✨ To-Do List ✨")

# Multiple tasks comma-separated input
new_tasks = st.text_area("Enter tasks :", "")

# Add multiple tasks button
if st.button("➕ Add Tasks", key="add", help="Click to add tasks"):
    tasks_list = [task.strip() for task in new_tasks.split(",") if task.strip()]
    if tasks_list:
        st.session_state.tasks.extend(tasks_list)
        st.success(f"✅ {len(tasks_list)} Tasks Added Successfully!")
        st.rerun()

# Display tasks and delete option with styling
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2])
        
        with col1:
            st.markdown(f'<div class="task-card">{task}</div>', unsafe_allow_html=True)

        if col2.button("❌ Delete", key=f"task_{index}", help="Remove this task"):
            st.session_state.tasks.pop(index)
            st.rerun()
else:
    st.info("No tasks added yet!")
