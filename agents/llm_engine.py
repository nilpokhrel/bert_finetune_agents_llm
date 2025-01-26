
from openai import OpenAI
import openai
import os
import config

# get api keys
from dotenv import load_dotenv
load_dotenv()

openai_api_key = 'openai api key'# os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)


## AGENT BASE
class LlmQueryEngine:
    """ Text Processing Using AI
    """
    def __init__(self, gpt_model=None, temperature=0, debug=False):
        """Text Processing on Given Document or Prompt

        Args:
            gpt_model (str): Versions of LLM model
            user_question_query (str): Query on embedded documents/texts for semantic search/text extraction
            system_response_query (str, optional): How AI should answer. Defaults to None.
            temperature (int, optional): Tunning Parameter on creativity of AI. Defaults to 0.
            debug (bool, optional): To display information of Input/Output. Defaults to False.
        """

        self.gpt_model = gpt_model
        if self.gpt_model is None:
            self.gpt_model = config.GPT_VERSION
            
        self.debug = debug
        self.temperature = temperature

        if self.debug:
            print('User Question query: ')
            print(self.user_question_query)
            print('System Response query: ')
            print(self.system_response_query)

    def query_engine(self, user_question_query, system_response_query=None, max_out_tokens=None, show_response=False):
        
            """
            Accepts user query and request gpt api to return json answer response.
            Args:
                user_question_query (str, optional): Accepts user query string. Defaults to None.
                system_response_query (str, optional): String query for system. Defaults to None.
                temperature (int, optional): ranges from 0-10 where 0 means factual and 10 means imaginative. Defaults to 0.

            Raises:
                ValueError: User query is mandatory for any request to gpt api.

            Returns:
                json: LLM Model generated Output
            """

            self.user_question_query = user_question_query
            self.system_response_query = system_response_query

            if not self.user_question_query:
                raise ValueError('User query cannot have empty string or Null value.')

            if not self.system_response_query:
                self.system_response_query = 'You follow the given query.'
                
            params = {
                        "model": self.gpt_model,
                        "messages": [
                                        {'role': 'system', 'content': self.system_response_query},
                                        {'role': 'user', 'content': self.user_question_query}
                                    ],
                        'temperature': self.temperature
                     }
            # control output tokens 
            if max_out_tokens is not None:
                params["max_tokens"] = self.max_out_tokens
                
            try:
                response = client.chat.completions.create(**params)
                response = response.choices[0].message.content
            except  Exception as err:
                raise err('LLM server error: {err}')
            
            if show_response:
                print('LLM response for user query: ')
                print(response)
            return response

if __name__ == '__main__':
    # SAMPLE TEST 
    llm_agent = LlmQueryEngine()
    task = llm_agent.query_engine('Explain about Ontology.', system_response_query='Act as a Ontologist.',show_response=False)
    print(task)
    pass
