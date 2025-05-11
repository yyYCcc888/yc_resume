import streamlit as st

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Sales Assistant
    **Industrial Securities** | *August 2023 - September 2023*
    
    - Sought IPO information, distribution and underwriting opportunities for business cooperation
    - Extracted and analyzed financial data of various public funds based on investment strategies
    - Communicated with clients and promoted appropriate financial products based on requirements
    """)
    
    st.markdown("""
    ### Industry Research Analyst
    **China Securities** | *April 2022 - May 2022*
    
    - Conducted comprehensive IDC industry research analyzing upstream, midstream and downstream companies
    - Performed fundamental analysis using Wind data for leading IDC companies
    - Calculated and analyzed financial ratios using Excel for comparative industry analysis
    - Applied Dupont analysis and PE valuation methods for company valuation
    - Independently produced comprehensive industry research reports
    """)
    
    st.markdown("""
    ### Member of Planning Department
    **HK Culture Association of SCU** | *September 2020 - July 2024*
    
    - Drafted event planning documents including announcements, manuscripts, and meeting minutes
    - Developed and managed detailed event execution plans and budgets
    - Organized major events including Cantonese Singing Competition with 200 participants
    """)
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R
        - **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn
        - **Machine Learning:** Scikit-learn, XGBoost, NLP
        - **Data Visualization:** Tableau, Power BI, Seaborn, Plotly, Word Clouds
        - **Statistical Analysis:** Sentiment Analysis, Regression Analysis, Cluster Analysis
        - **Design Tools:** Canva, Adobe Photoshop, Figma
        - **Office Suite:** Microsoft Office
        - **AI Tools:** ChatGPT, Deepseek, Copilot
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Presentation Skills, Technical Writing, Report Writing
        - **Analytical Thinking:** Data-driven Decision Making
        - **Project Management:** Task Prioritization, Timeline Management
        - **Research:** Market Research, Competitive Analysis
        - **Teamwork:** Strong Collaborative Spirit
        - **Adaptability:** Quick Learning, Problem-solving
        """)
    
    st.markdown("---")
