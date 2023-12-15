import streamlit as st
import requests
import json

json_data = ""

def get_chatbot_response(prompt):
    api_key = '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'
    endpoint = 'https://api.openai.com/v1/chat/completions'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a creative teacher.'}, {'role': 'user', 'content': prompt}],
    }

    response = requests.post(endpoint, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']

def main():
    global json_data  

    st.title("Edwisely Hook Bot")

    predefined_prompt = (
        "Imagine you're a creative teacher aiming to captivate students' interest in a topic. Your goal is to explain the concept in a simple and engaging manner. I want you to provide me with 6 requirements.I want the output in a single JSON format file. Keep the output of each part in a separate object, and don't intermix the outputs. create a one-liner hook for each of the six parts, keep the one-liner really creative and interesting, and put it as the heading for all the six parts. The content part of each part must and should be 200 words.The first step is to share a relevant quote or mention a notable figure related to the topic, second thing is to pose thought-provoking questions that transport students to a parallel world, making the subject more intriguing. The third thing is to, present statistics using numbers and figures to enhance comprehension. The fourth part, if applicable, provides real-life applications or examples to make the topic more tangible."
        "The Fifth part, add a touch of humor with a clever, sarcastic joke related to the subject. The sixth part, the most crucial part is to narrate a real story on that topic which has occured in the past or if not found craft a eye catching story that seamlessly introduces and explains the topic. Your narrative should be easy to follow, keeping the language simple and ensuring that the concept of that topic is being taught with story. Feel free to infuse creativity into the story, maintaining a balance between capturing attention and delivering educational content. Embrace creative freedom to shape the storyline for maximum impact,The length of the story must be 500 words at minimum. Generate a captivating one-liner in bold text for each of the six parts and then give the content. Keep these one-liners interesting and eye-catching to keep the reader's attention alive.Take enough time and Generate the output considering all the requirements according to the prompt,I want the output to be in JSON Format. Keep the key names as 'one_liner' and 'content',  and The topic is"
    )

    user_input = st.text_input("You:", "")

    if st.button("Ask"):
        prompt = f"{predefined_prompt}\nUser: {user_input}"
        bot_response = get_chatbot_response(prompt)
        json_data = bot_response

        
        if json_data:
            data = json.loads(json_data)

            
            def display_content(heading, content, key):
                st.markdown(f"<h2 style='font-weight: bold;'>{heading}</h2>", unsafe_allow_html=True)
            
                half_content=content[:150]
            
                with st.expander(half_content):
                    st.markdown(f"<h3 style='font-size:18px;'>{content}</h3>", unsafe_allow_html=True)

            for section, values in data.items():            
                display_content(values['one_liner'], values['content'], key=section)
                st.markdown("---")  

if __name__ == "__main__":
    main()
