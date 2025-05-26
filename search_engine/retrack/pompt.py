import openai
import os
import json
from retrack import get_file_path, get_sentence

def generate_subattribute_prompt(predicted_attribute):
    if predicted_attribute.lower() == "variable":
        prompt = "Continuous on the previous target word, does this variable belongs to Scalar, Vector, or Matrix? The answer should only contain the options without other words."
    elif predicted_attribute.lower() == "constant" or predicted_attribute == "Operator":
        prompt = "Continuous on the previous target word, does this variable belongs to Local, Global, or Discipline specified? The answer should only contain the options without other words."
    elif predicted_attribute.lower() == "unit descriptor":
        prompt = ''
    else:
        raise ValueError("Invalid predicted attribute") #TODO: handle this error automatically later
    return prompt

def get_config(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config["api_key"], config["model"], config["max_tokens"]
    
def get_related_contents(file_path):
    sentences = []
    with open(file_path, 'r') as file:
        for line in file:
            sentences.append(line.strip())
    return sentences

def evaluate(predicted_results, baselines, weight):
    score = 0
    if len(predicted_results) != len(baselines):
        raise ValueError("The number of predicted results and target words are not equal")
    for i in range(len(predicted_results)):
        first_target = baselines[i].split()[0]
        first_predicted = predicted_results[i].split()[0]
        second_target = baselines[i].split()[1]
        second_predicted = predicted_results[i].split()[1]

        if first_target == first_predicted:
            score += weight
            if second_target == second_predicted:
                score += 1 - weight
    return score/len(predicted_results)

def extract_sentence(filename):
    sentences = []
    title = True 
    with open(filename, 'r',encoding='utf-8') as file:
        for line in file:
            if not title:
                elements = line.split(' ',5)
                if elements:
                    sentences.append(elements[-1][:-1])
            title = False 
    return sentences
if __name__ == "__main__":
    # Set up OpenAI API key
    api_key, model, max_tokens = get_config("config.json")
    openai.api_key = api_key
    database_path = 'test_database_demo.txt'
    # context_path = 'test_database_demo_contexts.txt'
    output_path = 'test_output_prediction.txt'
    file_paths,target_words, attributes = get_file_path(database_path)
    # related_contexts = get_related_contents(context_path)
    related_contexts = extract_sentence(database_path)
    predicted_results = []
    for i, word in enumerate(target_words):
        symbol = word
        #TODO:two options for related content: 1. from original database 2. retrack archive and modify the sentence length
        related_context = related_contexts[i]

        # Create a prompt for the GPT-3.5 model to classify the attribute
        prompt = f"You are an expert on STEM subjects and know the contents of papers in the ArXiv dataset. Now given a symbol of a target word and its related content: Symbol: {symbol}, Related Content: {related_context}. \n Please select the target word's attribute only from one of the below options: Variable, Constant, Operator, and Unit Descriptor. The answer should only contain the options without other words."

        # Use GPT-3.5 to predict the attribute
        response = openai.Completion.create(
            engine = model,  
            prompt = prompt,
            max_tokens= max_tokens,  
        )

        # Extract and display the predicted attribute
        predicted_attribute = response.choices[0].text.strip()
        print("Predicted Attribute:", predicted_attribute) 

        continue_prompt = generate_subattribute_prompt(predicted_attribute)
        if continue_prompt != '':
            print("Continue...")
            response = openai.Completion.create(
                engine= model, 
                prompt=continue_prompt,
                max_tokens= max_tokens,  
            )
            predicted_subattribute = response.choices[0].text.strip()
            print("     Predicted Subattribute:", predicted_subattribute)
            predicted_results.append(predicted_attribute + ' ' + predicted_subattribute)
        else: 
            predicted_results.append(predicted_attribute.lower())
    with open(output_path, 'w') as file:
        file.write('file_name                   word                   predicted_attribute' + '\n')
        for i,string in enumerate(predicted_results):
            file.write(file_paths[i] + ' ' + target_words[i] + '                   ' + string + '\n')

    # evaluate the prediction using the original dataset
    evaluate_score = evaluate(predicted_results, attributes, 1)
    print(f">>>>>>>>>>Evaluate score for {database_path} is : {evaluate_score:.2%}<<<<<<<<<<")
