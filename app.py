from pathlib import Path

import streamlit as st

from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Stephen Simmons"
PAGE_ICON = ":wave:"
NAME = "Stephen Simmons"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "larrysimmons1@live.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com/in/stephensimmonsda/",
    "GitHub": "https://github.com/MrSimmons2u/Stephen_Simmons_Repository",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 12+ years of demonstrated excellence in Data Analytics
- ✔️ Leverages Python, R, Advanced SQL to Extract, Tranform and Load data
- ✔️ Performs Statistical Analysis to produce Impactful Insights that enhance Financial and Operational Decision-Making
- ✔️ Clearly Communicates Meaningful Insights to Technical and Non-Technical Stakeholders
- ✔️ Microsoft Excel Power-User
- ✔️ Leverages Power BI and Tableau to convert analyses to Data Visualizations for powerful storytelling
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, R, SQL, VBA
- 📊 Data Visulization: Power BI, Tableau, MS Excel, Dashboard Reporting
- 📚 Modeling: Financial modeling, Logistic regression, linear regression, decision trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | Millennial Advisors**")
st.write("10/2020 - Present")
st.write(
    """
- ► Orchestrated ERP system integration (Microsoft Business Central), streamlining data flow and reducing process times by 20%, enhancing overall efficiency in financial reporting and compliance across the 5 business units.
- ► Streamlined and automated daily, weekly, and monthly reports using SQL and Python, reducing report generation time by 40% and enhancing team productivity.
- ► Crafted and implemented Business Intelligence (BI) reports, increasing decision-making efficiency by 40%, critical for producing client reports and internal strategic planning.
- ► Automated ETL processes, bolstering data accuracy and reducing manual errors by 95%, ensuring high data integrity for all financial analyses and reports.
- ► Analyzed and optimized financial reporting systems, improving system performance by 25%, crucial for the accuracy in client financial statements and tax filings.
- ► Leveraged data visualization tools like Tableau and Power BI to develop interactive dashboards, providing real-time insights to stakeholders, resulting in an average 25% increase in operational efficiency.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Enterprise Analytics Specialist | Ad Astra**")
st.write("09/2019 - 01/2021")
st.write(
    """
- ► Designed data pipelines to securely stream and transform data from various sources into Amazon Redshift (Data Warehouse), facilitating prompt, robust reporting and increasing operational efficiency by an average of 35% per department.
- ► Leveraged PostgreSQL to Extract data from various sources, maintained data pipelines for loading data into Azure Data Lake Storage (ADLS) for further processing and automated transformation, bolstering data accuracy and reducing manual errors by 95%.
- ► Analyzed and optimized financial reporting systems, improving system performance by 25%, crucial for accuracy in client billing and revenue reporting for state and local government agency clients.
- ► Developed interactive dashboards and digital forms to streamline data collection and enhance reporting efficiency, improving data accessibility for financial decision-making.
- ► Engineered database tables and designed database schemas for automated workflows that optimized data management processes, ensuring data integrity and timely availability.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Budget Analyst III | National Institute of Health**")
st.write("05/2018 - 08/2019")
st.write(
    """
- ► Authored and executed gap analyses on major health initiatives, leveraging data analytics to pinpoint and rectify financial inconsistencies, enhancing the strategic allocation of resources and optimizing budget management.
- ► Oversaw financial operations for health projects with budgets surpassing $1M, applying rigorous analytical methodologies to ensure fiscal compliance and budget precision.
- ► Utilized statistical tools to analyze and mitigate financial risks, achieving a 30% reduction in risk factors and bolstering financial stability in federally funded health projects.
- ► Engineered and executed earned value management reports, identifying cost-saving opportunities that led to a 25% budget reduction across multiple projects through strategic financial planning.
- ► Analyzed project performance data to produce Schedule Variance Reports, utilizing insights to boost project completion rates by 20%.
- ► Implemented Work Breakdown Structures to enhance data reporting processes, ensuring detailed coverage, and bolstering stakeholder communication within public health initiatives.
- ► Managed extensive datasets over 50 TB, significantly enhancing the data governance and operational efficiency within healthcare business analytics.
- ► Ensured full compliance with HIPAA standards during the processing and analysis of large-scale health data, maintaining stringent data privacy and security protocols.
- ► Developed sophisticated data categorization techniques to elevate the precision and utility of analytical reports, supporting strategic decision-making processes.
- ► Employed regression analysis and Principal Component Analysis (PCA) to identify operational inefficiencies, enhancing program efficiency by 25% in health management.
- ► Analyzed and refined departmental budgets, identifying, and eliminating unnecessary expenditures, resulting in a 15% cost savings which were reallocated to vital research endeavors.
- ► Conducted thorough financial audits using data analytics, identifying cost inefficiencies, and implementing corrective measures to reduce overhead by 10%.
- ► Led data-driven research to pinpoint and initiate high-return projects, aligning with organizational strategic objectives to enhance public health outcomes.
- ► Utilized advanced data modeling techniques to forecast financial needs with high accuracy, providing robust support for strategic fiscal planning.
- ► Performed in-depth cost analysis for special projects, using data insights to achieve a 12% cost reduction while maintaining project quality and deliverables.
- ► Directed targeted ad hoc analyses, reallocating $500k based on data-driven insights to maximize the impact and effectiveness of key health projects.
"""
)
# --- JOB 4
st.write('\n')
st.write("🚧", "**Systems Analyst | Yellow Ribbon Fund (Non-Profit)**")
st.write("06/2015 - 07/2018")
st.write(
    """
- ► Coordinated with cross-functional teams, program directors and the Board of Directors to develop annual programmatic and operational budgets totaling over $1.2M, aligning financial strategies with organizational goals.
- ► Processed and recorded payments via cash, check, and credit card, and performed bank deposits, enhancing financial transaction efficiency and accuracy.
- ► Managed vendor relationships and contracts, successfully negotiated net terms and discounts for early payment, optimizing operational costs and improving contract terms.
- ► Administered sick leave/vacation leave for salaried employees and hourly pay for part-time workers and contractors, ensuring accuracy and compliance in payroll processing.
- ► Verified, processed, and submitted reimbursements for all employees and contractors, maintaining accurate and timely financial compensations.
- ► Maintained the general ledger by entering and reconciling financial data and journal entries into a central database, ensuring accuracy and detailed financial reporting.
- ► Produced management reports and conducted financial analyses for submission to the Board of Directors, providing critical insights for strategic decision-making.
- ► Implemented a new data management system using Microsoft Access, reducing data retrieval time by 40% and improving data accuracy by 25%.
- ► Streamlined IT processes using Microsoft SharePoint, decreasing system downtime by 30% and enhancing staff productivity by 20%.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Business Analyst | Business & Financial Solutions**")
st.write("03/2010 - 06/2015")
st.write(
    """
- ► Orchestrated daily stand-up meetings for a 7-member analyst team, enhancing project alignment and efficiency in task distribution, fostering a collaborative and productive work environment.
- ► Developed tailored tax strategies that resulted in an average of 20% savings for clients, maintaining a client satisfaction rate of 95% by effectively addressing unique financial situations and optimizing tax liabilities.
- ► Prepared and filed 100+ tax returns annually for both individuals and businesses, achieving a 99% accuracy rate and consistently minimizing fiscal liabilities through meticulous analysis and strategic planning.
- ► Delivered comprehensive bookkeeping services, which streamlined financial processes for clients, leading to a 25% reduction in billing discrepancies and maintaining a high client retention rate of 90%.
- ► Successfully advocated in tax resolution cases with a 90% success rate, significantly reducing tax obligations for clients by employing strategic dispute resolutions and negotiations with tax authorities.
- ► Oversaw the organization-wide rollout of a practice management system, leading training sessions for 7 users and achieving a user satisfaction score of 5/5 through effective implementation and support, leading to a 100% adoption rate.
- ► Managed and analyzed financial data for a portfolio of more than 300 individual clients and 100 business clients using QuickBooks Online, leading to a 15% increase in client satisfaction.
- ► Conducted detailed business performance analyses and provided actionable insights that improved client business profitability by an average of 10% annually.
- ► Spearheaded the implementation of CCH ATX tax software, resulting in a 20% reduction in tax preparation time and increased accuracy of filings.

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")