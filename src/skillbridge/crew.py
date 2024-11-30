from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from skillbridge.tools.PDFReader import PDFReader
from crewai_tools import SerperDevTool
import os

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key="AIzaSyBfdNcouDXMkGsGzHESIO_hoAlvVLzZlMA"
)

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class Skillbridge():
	"""Skillbridge crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# @before_kickoff # Optional hook to be executed before the crew starts
	# def pull_data_example(self, inputs):
	# 	# Example of pulling data from an external API, dynamically changing the inputs
	# 	inputs['extra_data'] = "This is extra data"
	# 	return inputs

	# @after_kickoff # Optional hook to be executed after the crew has finished
	# def log_results(self, output):
	# 	# Example of logging results, dynamically changing the output
	# 	print(f"Results: {output}")
	# 	return output


	@agent
	def resume_summarizer(self):
		return Agent(
			config=self.agents_config['resume_summarizer'],
			verbose=True,
			llm= llm
		)

	@task
	def summarization_task(self):
		reader = PDFReader()
		return Task(
			config=self.tasks_config['summarization_task'],
			output_file='outputs/output1.md',
			tools= [reader.read_pdf],
			async_execution= True
		)

	@agent
	def web_scraper(self):
		return Agent(
			config= self.agents_config['web_scraper'],
			verbose=True,
			llm=llm
		)
	
	@task
	def scrapping(self):
		os.environ['SERPER_API_KEY'] = 'b3197a6a1d8c22fcde3036c2f4a46f02fe81a86c'
		tool = SerperDevTool(search_url="https://google.serper.dev/search")
		return Task(
			config= self.tasks_config['scraping_task'],
			output_file='outputs/output2.md',
			tools = [tool],
			async_execution = True
		) 

	@agent
	def strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['strategist'],
			verbose=True,
			llm=llm
		)


	@task
	def guidance_task(self) -> Task:
		return Task(
			config=self.tasks_config['guidance_task'],
			output_file='outputs/output.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Skillbridge crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
