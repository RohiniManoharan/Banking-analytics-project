import os
from dotenv import load_dotenv
# import namespaces
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

def main():

    try:
        load_dotenv()
        project_endpoint = os.getenv("PROJECT_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        # Initialize the OpenAI client
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://ai.azure.com/.default"
        )

        openai_client = OpenAI(
            base_url=project_endpoint,
            api_key=token_provider
        )

        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")

            if input_text.lower() == "quit":
                break

            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            # Get a response
            completion = openai_client.chat.completions.create(
                model=model_deployment,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a banking data analyst. 
        Explain below results in simple business language. 
        Focus on churn risk,balances,credit scores, and customer segments. 
        Use bullet points and short recommendations"""
                    },
                    {
                        "role": "user",
                        "content": input_text
                    }
                ]
            )

            print(completion.choices[0].message.content)

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()