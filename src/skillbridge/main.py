#!/usr/bin/env python
import sys
import warnings

from skillbridge.crew import Skillbridge

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    desired_role = 'Full stack Developer'
    desired_company = 'Amazon'
    inputs = {
        'current_job': 'Front End developer',
        'desired_role': 'Full Stack developer',
        'desired_company':'Amazon',
        'file_path': 'resume\prabal_b.pdf',
        'query' : f"{desired_role} job role at {desired_company}"
    }
    Skillbridge().crew().kickoff(inputs=inputs)



