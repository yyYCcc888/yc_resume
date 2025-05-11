import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing (Big Data Marketing)
    **Chinese University of Hong Kong** | *August 2024 - October 2025*

    - Relevant Coursework: Social Media Analytics, Machine Learning in Marketing, Customer Analytics, Integrated Marketing Communication, Marketing Analytics, Digital Marketing, Marketing Research
    
    ### Bachelor of Economics in Finance
    **Sichuan University** | *September 2020 - June 2024*
    
    - Graduated with Honors
    - Relevant Coursework: International Investment, Security Investment, Financial Risk Management, Financial Statement Analysis, Financial Econometrics, Financial Engineering
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    col1, col2, col3 = st.columns(3, gap="small")
    
    with col1:
        st.markdown("""
        ### IELTS 7.0
        **Cambridge** | *October 2023*
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    projects = [
        {
            "title": "The IMC Campaign for the 3CE and aespa Collaboration",
            "date": "January 2025",
            "description": "Developed a strategic IMC campaign to facilitate 3CE's brand transformation from value-oriented positioning to premium beauty segment through K-pop collaboration.",
            "achievements": [
                "Conducted STP analysis for the 3CE cosmetics brand",
                "Designed an IMC campaign to refresh brand image using 5 Box analysis method"
            ]
        },
        {
            "title": "Exploration of the Effectiveness of CHAGEE's Olympics Marketing Campaign",
            "date": "December 2024",
            "description": "Analyzed social media data to evaluate marketing campaign effectiveness.",
            "achievements": [
                "Utilized Python and Octopus to scrape and preprocess social media data from Weibo and Xiaohongshu",
                "Conducted sentiment analysis and keyword extraction using Python to evaluate consumer perceptions"
            ]
        },
        {
            "title": "Baidu Netdisk Marketing Analysis",
            "date": "November 2024",
            "description": "Comprehensive marketing analysis of Baidu Netdisk user preferences and market positioning.",
            "achievements": [
                "Designed and executed a survey to gather user feedback on various attributes",
                "Performed descriptive analysis and multiple linear regression using R Studio",
                "Developed a choice model using Sawtooth for market share prediction"
            ]
        },
        {
            "title": "Tourism and Economic Growth in Chengdu - VAR Model Analysis",
            "date": "January 2023",
            "description": "Statistical analysis of tourism's impact on Chengdu's economic growth.",
            "achievements": [
                "Analyzed time series data of GDP, Domestic Tourists and Tourism Income (2000-2020)",
                "Performed Smoothness test and Johansen cointegration test",
                "Conducted VAR modeling with impulse response and variance decomposition analysis"
            ]
        },
        {
            "title": "Interest Rate Parity Theory Deviation Analysis",
            "date": "October 2022",
            "description": "Analysis of USD-CNY exchange rate deviations from Interest Rate Parity theory.",
            "achievements": [
                "Analyzed exchange rate data using time series methods",
                "Created first-order and second-order difference line plots using STATA",
                "Provided recommendations for foreign exchange reserves and trading strategies"
            ]
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']} | *{project['date']}*", expanded=i==0):
            st.markdown(f"**description：** {project['description']}")
            st.markdown("**achievement：**")
            for achievement in project['achievements']:
                st.markdown(f"- {achievement}")
    
    st.markdown("---")