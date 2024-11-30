import os
import streamlit as st
from skillbridge.crew import Skillbridge

# Directory to store uploaded files
UPLOAD_DIR = "uploaded_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Streamlit app
def main():
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
                st.success("Processing complete! Check the output files.")
            except Exception as e:
                st.error(f"An error occurred while running the Skillbridge crew: {e}")

if __name__ == "__main__":
    main()
