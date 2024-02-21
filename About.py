import streamlit as st

def app():
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(image='Pic1.jpeg', width=300)
    
    st.write("Daniel Henshaw is a dynamic professional with a passion for Computer Science, and cutting-edge technology. He holds a degree from the University of Port Harcourt, Nigeria, where he majored in Mathematics and Computer Science, graduating with Upper Credit (2.1) honors. Throughout his academic journey, Daniel distinguished himself as a diligent and innovative student, consistently exploring the intersection of mathematics, computation, and data science. His academic prowess and commitment to excellence paved the way for numerous successful projects in the fields of Machine Learning and Data Science.Driven by a quest for knowledge and a relentless pursuit of excellence, Daniel has embarked on various projects that leverage the power of technology to solve real-world problems. His contributions to the realm of Machine Learning and Data Science have not only showcased his technical proficiency but also underscored his ability to conceptualize and execute impactful initiatives. With a keen eye for detail and a thirst for innovation, Daniel Henshaw continues to push the boundaries of what's possible in the realm of technology. His dedication to his craft and his unwavering commitment to personal and professional growth serve as a testament to his potential to make a meaningful impact in the ever-evolving landscape of mathematics and computer science.")

