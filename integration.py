import openai

# Set your OpenAI API key
openai.api_key = 'key'

def generate_job_ad(job_name, context_field1, context_field2):
    # Step 1: Get information from external tool using API call
    # Replace this with your actual API call to retrieve the job information
    job_info = get_job_info_from_external_tool()

    # Extract the relevant fields from the job_info
    job_name = job_info['job_name']
    context_field1 = job_info['context_field1']
    context_field2 = job_info['context_field2']

    # Step 2: Send fields to OpenAI API to generate job advert text
    prompt = f"Job: {job_name}\nContext1: {context_field1}\nContext2: {context_field2}\nGenerate job advert:"
    job_advert = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100  # Adjust the number of tokens as per your requirements
    ).choices[0].text.strip()

    # Step 3: Send the generated job advert back to the external tool
    # Replace this with your actual API call to send the job advert back

    return job_advert


# Placeholder function for getting job information from the external tool
def get_job_info_from_external_tool():
    # Replace this with your actual API call to retrieve job information
    job_info = {
        'job_name': 'Software Developer',
        'context_field1': 'Experience with Python programming',
        'context_field2': 'Knowledge of web development frameworks'
    }
    return job_info


# Example usage
job_name = "Software Engineer"
context_field1 = "Experience in cloud computing"
context_field2 = "Familiarity with machine learning algorithms"

generated_ad = generate_job_ad(job_name, context_field1, context_field2)
print(generated_ad)
