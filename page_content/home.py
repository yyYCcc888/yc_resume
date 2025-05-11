import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>CHAN, Yin Sen (YC)</h4>
        <p>MSc in Marketing (Big Data Marketing)<br>
        Chinese University of Hong Kong<br>
        Tsuen Wan NT, HKSAR<br>
        <a href="mailto:1378188281@qq.com">1378188281@qq.com</a><br>
        +852 59584365 (HK), +86 15980247560 (Mailand China)</p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "WechatIMG1624.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a soon-to-graduate master's student in Marketing with a focus on Big Data Analytics. During my undergraduate studies in Finance at Sichuan University, I built a solid foundation in finance and honed my data analysis and market research skills through internships and projects. My internships at CITIC Securities and Industrial Securities allowed me to conduct in-depth industry analyses and propose valuable market insights and development suggestions.

        In my master's program, I further developed my expertise in marketing and data analysis, mastering techniques such as social media analysis, machine learning, and customer analytics. Through practical projects, I utilized tools like Python and R Studio to conduct thorough analyses of marketing activities and market trends, gaining extensive project experience.

        I am passionate about data-driven decision-making and possess strong learning and teamwork abilities, enabling me to adapt quickly to various challenges. I look forward to applying my professional skills in the field of marketing or data analysis and contributing to a dynamic team.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Machine Learning: Scikit-learn, XGBoost, NLP
        - Data Visualization: Tableau, Power BI, Seaborn, Plotly, Word Clouds
        - Statistical Analysis: Sentiment Analysis, Regression Analysis, Cluster Analysis
        - Communication: Presentation Skills, Technical Writing, Report Writing
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 