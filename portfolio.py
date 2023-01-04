# ==================== IMPORTING LIB/MODULES NEEDED 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
# ==================== SETTING OUR PAGE LAYOUT 
st.set_page_config(page_title = "Personal portfolio website", page_icon = ":simple_smile:", layout = "wide")

# ==================== OUR FUNCTION TO HOLD AND VERIFY OUR ASSETS 
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ==================== USING OUR LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ==================== LOADING OUR ASSETS 
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_bzgbs6lx.json")
image_one = Image.open("images/img1.jpg")
mapesa_project = Image.open("images/img2.jpg")


# =================== HEADER SECTION 
with st.container():
    st.subheader("Hi, I am Francis :wave:")
    st.title("A Software Engineer from Kenya")
    st.write("I am a result-oriented and performance-based Software Engineer eager to contribute to your team’s success through hard work, attention to detail, problem-solving skills, and teamwork. As I’m a fast learner with a collaborative mindset for collaboration. I’m an excellent problem solver, analytical and critical thinker with a resilient attitude to succeed.")
    st.write("[Learn more](https://linkedin.com/in/devnjoro)")


# =================== SKILLS SECTION 
with st.container():
    st.write("---")
    st.header("Skiils")
    # st.write("##")
    l_column, m_column, r_column = st.columns((1, 1, 1))

    with l_column:
        st.subheader("Programming")
        st.write(
            """
            - Python.        
            - JavaScript. 
            - HTML5 & CSS3    
            - React.js, Node.js
            - Flask, Numpy, Pandas 
            """
            )

    with m_column:
        st.subheader("Cloud technologies")
        st.write(
            """
            - Linux
            - AWS Cloud
            - Git & Github
            - Docker & Kubernetes
            - CI/CD tools (Gitlab, CircleCi)
            """
        )

    with r_column:
        st.subheader("Databases technologies")
        st.write(
            """
            - SQL & PostgreSQL
            - MongoDB
            - DynamoDB, S3 bucket and etc.
            """
        )
        
    st.markdown("[View my Resume](https://njorogef770.hackerresume.io/c46595e3-b308-4194-a93c-ad6f62f0a89e)")

# =================== WHAT I DO 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        # st.write("##")
        st.write(
            """
            - Designing, developing and maintaining software systems
            - Evaluating and testing new software programs
            - Optimizing software for speed and scalability
            - Writing and testing code
            - Analysing and visualizing of data to derive insights
            - API development and integration
            """
            )
        st.write("[View my work](https://github.com/Frank6496)")

    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")


# =================== MY PROJECTS/WORK 
# PROJECT 1
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        #insert images
        st.image(image_one)

    with text_column:
        st.subheader("An image filtering Microservice")
        st.write(
            """
            It is a simple cloud application that allows users to register and log into a web client, 
            post photos to the feed, and process photos using an image filtering microservice.
            In this project I refactored a Monolith Image Filtering Application to Microservices 
            using Docker Container, CI/CD and deploying Kubernetes Clusters
            """
            )
        st.markdown("[Click me](https://github.com/Frank6496/An-Image-filtering-microservice-application)") # A link to the project build demo

# PROJECT 2
with st.container():
    # st.write("---")
    # st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(mapesa_project)
    with text_column:
        st.subheader("Mapesa")
        st.write(
            """
            It's a payment web platform that can enable users to register and send money to each 
            other within the platform. They top up their accounts through a mobile banking provider,
             and can now transfer amongst themselves by using either an email or a phone number 
             registered on the platform.
            """
        )
        st.markdown("[Click me](https://mapesa.vercel.app/)")


# =================== CONTACT DETAILS FORM 
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ 
    contact_form = """
    <form action="https://formsubmit.co/57376504e8d2b30b282333fc52f62cd6" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()