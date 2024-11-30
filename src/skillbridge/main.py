import os
import streamlit as st
from skillbridge.crew import Skillbridge

# Directory to store uploaded files
UPLOAD_DIR = "uploaded_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Function to read markdown content from a file
def read_markdown_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Streamlit app
def main():
    # Navigation for pages
    page = st.sidebar.selectbox("Select a Page", ["User Input", "View Results"])

    # User Input Page
    if page == "User Input":
        st.title("Skillbridge - Job Role Analyzer")
        st.write("Enter the desired role and company, and upload your resume to analyze.")

        # Input fields
        desired_role = st.text_input("Enter Desired Role (e.g., Full Stack Developer):")
        desired_company = st.text_input("Enter Desired Company (e.g., Amazon):")
        
        # File uploader
        uploaded_file = st.file_uploader("Upload Your Resume (PDF only):", type=["pdf"])

        if st.button("Submit"):
            if not desired_role or not desired_company or not uploaded_file:
                st.error("Please provide all inputs and upload your resume.")
            else:
                # Save uploaded file
                file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())
                st.success(f"Resume uploaded and saved at: {file_path}")

                # Inputs for the Skillbridge crew
                inputs = {
                    "current_job": "Front End Developer",  # Placeholder value
                    "desired_role": desired_role,
                    "desired_company": desired_company,
                    "file_path": file_path,
                    "query": f"{desired_role} job role at {desired_company}"
                }

                st.write("Processing your inputs with the Skillbridge crew...")

                # Run the Skillbridge crew
                try:
                    Skillbridge().crew().kickoff(inputs=inputs)
                    st.success("Successful")
                except Exception as e:
                    st.error(f"An error occurred while running the Skillbridge crew: {e}")

    # Content Display Page
    elif page == "View Results":
        # Sidebar navigation for tabs
        selected_tab = st.sidebar.selectbox(
            "Select a Tab", ["Gaps Identified", "Resume Summary", "Web scraped"]
        )

        # Display content based on selected tab
        if selected_tab == "Gaps Identified":
            description = "THESE ARE THE FINAL GAPS IDENTIFIED AFTER COMPARING THE RESUME AND SCRAPED DATA"
            tab1_content = read_markdown_file("skillbridge/outputs/output.md")  # Path to your markdown file
            st.subheader("Description")
            st.write(description)
            st.markdown(tab1_content)

        elif selected_tab == "Resume Summary":
            description = "THIS IS THE SUMMARY OF THE RESUME"
            tab2_content = read_markdown_file("skillbridge/outputs/output1.md")  # Path to your markdown file
            st.subheader("Description")
            st.write(description)
            st.markdown(tab2_content)

        elif selected_tab == "Web scraped":
            description = "THIS IS THE CLEANED AND RELEVANT DATA OBTAINED USING AN LLM AFTER SCRAPING THE DATA "
            tab3_content = read_markdown_file("skillbridge/outputs/output2.md")  # Path to your markdown file
            st.subheader("Description")
            st.write(description)
            st.markdown(tab3_content)

if __name__ == "__main__":
    main()
