import openai
import user_input

# Set your OpenAI API key
api_key = "put your key here"
openai.api_key = api_key

def fact_check(text_to_check):
    prompt = f"Fact-check the following information:\n\n\"{text_to_check}\"\n\nIs the information provided above accurate? Please provide a yes or no answer and include any relevant details or explanations."

    try:
        # Use the GPT-3.5 model to fact-check the text
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-0613",
            prompt=prompt,
            max_tokens=1000,  # Adjust max_tokens as needed
            n=1
        )

        # Extract the model's response
        analysis_result = response.choices[0].text.strip()

        return analysis_result

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    text_to_check = user_input.input_func()
    result = fact_check(text_to_check)
    print("Fact-check Result:")
    print(result)
