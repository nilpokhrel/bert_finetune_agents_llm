# from agents.llm_engine import LlmQueryEngine
# import  agents.agent_instructs  as instructions
import llm_engine
import agent_instructs as instructions

class AGENTS:
    "Customized and very specific Agent for Process Task and workflow"
    llm_agent_engine = llm_engine.LlmQueryEngine()
    
    def __init__(self, agent_name):
        self.agent_name = agent_name
    
    def process_refiner(self, query_text):
        formatted_process_refiner_prompt = instructions.primary_process_identifier_agent_prompt.format(instructions.task_type_definitions2) 
        refined_process = AGENTS.llm_agent_engine.query_engine(query_text, system_response_query=formatted_process_refiner_prompt)
        self.refined_process = refined_process

    def process_classifier(self, refined_user_process):
        formatted_process_classifier_prompt = instructions.detailed_task_classifier_agent_prompt.format(refined_user_process) 
        classified_process = AGENTS.llm_agent_engine.query_engine(formatted_process_classifier_prompt)
        self.classified_process = classified_process
    
    def agent_process_classifier(self, user_query):
        self.process_refiner(user_query)
        self.process_classifier(self.refined_process)
        return self.classified_process


if __name__ == '__main__':
    ag1 = AGENTS()
    ag1.agent_process_classifier(' I want to sent information to Manager.')
    
    # example of output will be like this
    """
    User text:  The Product Manager outlines the objectives of the new insurance scheme and identifies the target demographics. The Senior Underwriter reviews and approves the proposal to proceed with model development.
    
    agent refined text:  The Senior Underwriter reviews and approves the proposal.
    
    original label:  Approval
    classified label:  Approval
    """
    pass
