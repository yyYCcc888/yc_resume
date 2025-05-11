import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume_CHAN, Yin Sen.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="CHAN_Yin_Sen_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("CHAN, Yin Sen (YC)")

    st.header("Contact Information")
    st.markdown("""
    - **Phone:** +852 56659168 | +86 15980247560
    - **Email:** 1378188281@qq.com
    - **Gender:** Female
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing (Big Data Marketing)**
    - Chinese University of Hong Kong
    - *August 2024 - October 2025*
    - **Main Modules:** Social Media Analytics, Machine Learning in Marketing, Customer Analytics, Integrated Marketing Communication, Marketing Analytics, Digital Marketing, Marketing Research

    **Bachelor of Economics in Finance**
    - Sichuan University
    - *September 2020 - June 2024*
    - **Main Modules:** International Investment, Security Investment, Financial Risk Management, Financial Statement Analysis, Financial Econometrics, Financial Engineering
    """)

    st.header("Professional Experience")
    st.markdown("""
    **Sales Assistant, Industrial Securities**
    - *August 2023 - September 2023*
    - Sought IPO information, distribution and underwriting opportunities for business cooperation
    - Extracted and analyzed financial data of various public funds based on investment strategies
    - Communicated with clients and promoted appropriate financial products based on requirements

    **Industry Research Analyst, China Securities**
    - *April 2022 - May 2022*
    - Conducted comprehensive IDC industry research analyzing upstream, midstream and downstream companies
    - Performed fundamental analysis using Wind data for leading IDC companies
    - Calculated and analyzed financial ratios using Excel for comparative industry analysis
    - Applied Dupont analysis and PE valuation methods for company valuation
    - Independently produced comprehensive industry research reports

    **Member of Planning Department, HK Culture Association of SCU**
    - *September 2020 - July 2024*
    - Drafted event planning documents including announcements, manuscripts, and meeting minutes
    - Developed and managed detailed event execution plans and budgets
    - Organized major events including Cantonese Singing Competition with 200 participants
    """)

    st.header("Research Projects")
    st.markdown("""
    **Exploration of CHAGEE's Olympics Marketing Campaign**
    - *December 2024*
    - Conducted STP analysis for CHAGEE
    - Utilized Octopus for social media data scraping and preprocessing
    - Performed sentiment analysis and keyword extraction using Python

    **Baidu Netdisk Marketing Analysis**
    - *November 2024*
    - Designed and executed user feedback surveys
    - Conducted descriptive analysis and multiple linear regression using R Studio
    - Developed choice models using Sawtooth for market share prediction
    """)

    st.header("Skills & Additional Information")
    st.markdown("""
    **Language Proficiency:**
    - English (IELTS 7.0)
    - Mandarin (Native Speaker)
    - Cantonese (Fluent in Listening)

    **Technical Skills:**
    - Office Suite
    - STATA
    - Python
    - R Studio
    - AI-driven tools

    **Achievements:**
    - Tennis: First place in team competition of 8th Sichuan University Tennis Tournament | Member of CUHK school tennis team
    - Piano: Grade 10 with Several National Awards
    """)

    st.markdown("---")