import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        st.error("Failed to load animation. Please check the URL.")
        return None
    return r.json()

# Load a fun animation from LottieFiles
lottie_animation = load_lottie_url("https://lottie.host/b633a7fe-541d-4d9c-a9e4-07bb4c4fd90a/anSgjpvT5e.json")

# Set the title of the web app
st.title("Mood Check-In")

# Display the animation if it was loaded successfully
if lottie_animation:
    st_lottie(lottie_animation, height=300)

# Display introductory text
st.write("Answer the following questions to help understand your current mood. Your responses are confidential.")

# Question 1: Emotional state over the past week
emotion = st.radio(
    "How have you been feeling emotionally over the past week?",
    ('Very Happy', 'Happy', 'Neutral', 'Sad', 'Very Sad')
)

# Question 2: Frequency of anxiety or stress
anxiety = st.radio(
    "Do you find yourself feeling anxious or stressed frequently?",
    ('Rarely', 'Sometimes', 'Often', 'Always')
)

# Question 3: Sleep quality
sleep = st.radio(
    "How well have you been sleeping recently?",
    ('Very Well', 'Well', 'Fair', 'Poor', 'Very Poor')
)

# Question 4: Interest in activities
interest = st.radio(
    "Have you lost interest in activities that you usually enjoy?",
    ('Not at all', 'A little', 'Somewhat', 'A lot', 'Completely')
)

# Question 5: Support from people around
support = st.radio(
    "Do you feel supported by the people around you?",
    ('Always', 'Often', 'Sometimes', 'Rarely', 'Never')
)

# Function to generate a friendly, story-telling response based on user input
def generate_response(emotion, anxiety, sleep, interest, support):
    if emotion == 'Very Sad':
        return "Oh dude, 😅 I know exactly what you're going through! I remember one time I was feeling super down, and then out of nowhere, my friend started doing this ridiculously silly dance. I was confused at first, but soon enough, I couldn't stop laughing and ended up joining in! Sometimes, it just takes something unexpected to turn things around. You've got this!"
    elif emotion == 'Sad':
        return "Hey there, 😊 it's okay to feel sad sometimes. You know, I once had a day where everything just felt off. I was feeling down, but then I decided to go for a walk, and I stumbled upon this street performer playing the guitar. I stood there for a while, listening, and by the end of it, I felt so much better. Music has a funny way of cheering us up, don't you think?"
    elif emotion == 'Very Happy':
        return "Wow, that's awesome! 🎉 I love hearing that you're feeling so great. You know, happiness is contagious. I remember one day I was in the best mood, and I ended up spreading that joy to everyone I met. Keep shining bright and sharing that positivity with others!"
    elif emotion == 'Happy':
        return "That's wonderful to hear! 😄 It's so important to cherish those happy moments. Just the other day, I was feeling pretty content, and I decided to treat myself to my favorite dessert. It made the day even sweeter! Keep enjoying those little things that make you smile."
    elif anxiety in ['Often', 'Always']:
        return "Stress can be such a drag, right? 😥 I used to get so worked up about everything, but then I found this trick where I just took five deep breaths whenever I felt overwhelmed. It sounds simple, but man, it really helps. Give it a try next time!"
    elif interest in ['A lot', 'Completely']:
        return "Losing interest in things you love can be tough. 😔 But you know what? Sometimes it just takes trying something new to reignite that spark. I once got into painting when I was feeling like that, and it opened up a whole new world for me. Maybe there's something out there just waiting for you to discover!"
    else:
        return "You're not alone, my friend. 😌 Everyone goes through ups and downs. I once read this quote that said, 'Stars can't shine without darkness.' Just remember that even if things feel tough right now, brighter days are ahead."

# Submit button
if st.button('Submit'):
    # Generate and display the suggestion
    suggestion = generate_response(emotion, anxiety, sleep, interest, support)
    st.subheader("Suggestion:")
    st.write(suggestion)

# Load and display a final funny animation or GIF
final_animation = load_lottie_url("https://lottie.host/321a00d9-a6a9-48e1-8970-31b7540b7858/5wDhsqUiLn.json")
if final_animation:
    st_lottie(final_animation, height=200)
