import streamlit as st
import pandas as pd
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Arka Sain | Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin-top: 0;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1E88E5;
        border-bottom: 2px solid #1E88E5;
        padding-bottom: 10px;
        margin-top: 30px;
    }
    .skill-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .project-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .contact-link {
        color: #1E88E5;
        text-decoration: none;
        font-weight: bold;
    }
    .contact-link:hover {
        text-decoration: underline;
    }
    .education-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .experience-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .profile-pic {
        border-radius: 50%;
        margin-bottom: 15px;
    }
    .image-placeholder {
        background-color: #e0e0e0;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #616161;
        font-weight: bold;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# Profile photo implementation
def load_profile_photo():
    """
    This function loads your profile photo.

    To use your own photo:
    1. Create a folder named 'images' in the same directory as this app.py file
    2. Add your profile photo as 'profile.jpg' in that folder
    3. The app will automatically detect and use it

    If the photo isn't found, it will use a placeholder.
    """
    try:
        if os.path.exists("photo.jpg"):
            image = Image.open("photo.jpg")
            return image
        else:
            return None
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None


# Helper function to create placeholders when images aren't available
def image_placeholder(width, height, text="Image Placeholder"):
    st.markdown(f"""
    <div class="image-placeholder" style="width: {width}px; height: {height}px;">
        <p>{text}</p>
    </div>
    """, unsafe_allow_html=True)


# Define navigation
def navigation():
    menu = ["Home", "Skills", "Education", "Experience", "Projects", "Certifications", "Achievements", "Contact"]
    choice = st.sidebar.radio("Navigation", menu)
    return choice


# Main content
def main():
    choice = navigation()

    # Load profile photo
    profile_photo = load_profile_photo()

    # Profile info for the sidebar
    with st.sidebar:
        # Display photo in sidebar if available
        if profile_photo is not None:
            st.image(profile_photo, width=200, use_column_width=True)

        st.markdown("### Connect With Me")
        st.markdown("📱 +91 7410173864")
        st.markdown("📧 [Email](mailto:arka.sain24-26@bibs.co.in)")
        st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/arka-sain-4060812b4)")
        st.markdown("💻 [GitHub](https://github.com/Arkasain)")

    # Home
    if choice == "Home":
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown('<p class="main-header">Arka Sain</p>', unsafe_allow_html=True)
            st.markdown('<p class="sub-header">Data Analyst & MBA Student</p>', unsafe_allow_html=True)

            st.markdown("""
            ### About Me

            I am an aspiring data professional currently pursuing PGP + MBA in Business Analytics & Data Science.
            With a background in Computer Applications (BCA) and hands-on experience in data science, 
            I am passionate about transforming data into actionable insights and business solutions.

            My technical expertise includes Python, SQL, Power BI, and various data analysis tools.
            I'm currently gaining practical experience as a Data Science Intern at Prodigy InfoTech.
            """)

            st.markdown("### Professional Summary")
            st.markdown("""
            * Data Analysis professional with strong analytical skills
            * Expertise in data visualization and business intelligence tools
            * Background in business analytics and computer applications
            * Currently pursuing MBA in Business Analytics & Data Science
            """)

        with col2:
            st.markdown("### Data Professional")
            # Display profile photo if available, otherwise use placeholder
            if profile_photo is not None:
                st.image(profile_photo, width=300, caption="Arka Sain")
            else:
                image_placeholder(300, 300, "Profile Photo Not Found.\nAdd your photo to images/profile.jpg")
                st.info("To add your profile photo: Create a folder named 'images' and add your photo as 'profile.jpg'")

    # Skills
    elif choice == "Skills":
        st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="skill-box">', unsafe_allow_html=True)
            st.markdown("### Programming Languages")
            st.markdown("* Python")
            st.markdown("* SQL")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown('<div class="skill-box">', unsafe_allow_html=True)
            st.markdown("### Data Analysis")
            st.markdown("* Data Analysis and Interpretation")
            st.markdown("* Data Visualization")
            st.markdown("* Critical Thinking")
            st.markdown("* Marketing Analytics")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="skill-box">', unsafe_allow_html=True)
            st.markdown("### Technologies & Tools")
            st.markdown("* Power BI")
            st.markdown("* Tableau")
            st.markdown("* Advanced Excel")
            st.markdown("* MySQL")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown('<div class="skill-box">', unsafe_allow_html=True)
            st.markdown("### Python Libraries")
            st.markdown("* Pandas")
            st.markdown("* NumPy")
            st.markdown("* Seaborn")
            st.markdown("* Matplotlib")
            st.markdown("* Scikit Learn")
            st.markdown("</div>", unsafe_allow_html=True)

        # Skills visualization
        st.markdown("### Skills Proficiency")

        skills_data = {
            'Skill': ['Python', 'SQL', 'Power BI', 'Tableau', 'Excel', 'Data Analysis', 'Machine Learning'],
            'Proficiency': [85, 80, 90, 75, 85, 80, 70]
        }

        df = pd.DataFrame(skills_data)
        st.bar_chart(df.set_index('Skill'))

    # Education
    elif choice == "Education":
        st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)

        st.markdown('<div class="education-box">', unsafe_allow_html=True)
        st.markdown("### PGP + MBA - Business Analytics & Data Science")
        st.markdown("**Bengal Institute of Business Studies - VU**")
        st.markdown("*2024 - Present*")
        st.markdown("**Score:** 77%")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="education-box">', unsafe_allow_html=True)
        st.markdown("### BCA (Hons)")
        st.markdown("**Burdwan Institute of Management and Computer Science**")
        st.markdown("*Completed in 2024*")
        st.markdown("**Score:** 61%")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="education-box">', unsafe_allow_html=True)
        st.markdown("### Higher Secondary Education (Science)")
        st.markdown("**Raina Swami Bholananda Vidyayatan**")
        st.markdown("*Completed in 2021*")
        st.markdown("**Score:** 71%")
        st.markdown("</div>", unsafe_allow_html=True)

        # Education Timeline
        st.markdown("### Education Timeline")

        education_data = {
            'Year': [2021, 2024, 2026],
            'Degree': ['Higher Secondary', 'BCA', 'MBA'],
            'Progress': [100, 100, 40]
        }

        df = pd.DataFrame(education_data)
        st.line_chart(df.set_index('Year')['Progress'])

    # Experience
    elif choice == "Experience":
        st.markdown('<p class="section-header">Work Experience</p>', unsafe_allow_html=True)

        st.markdown('<div class="experience-box">', unsafe_allow_html=True)
        st.markdown("### Data Science Intern")
        st.markdown("**Prodigy InfoTech**")
        st.markdown("*March 28, 2025 - Present*")
        st.markdown("""
        **Responsibilities:**
        * Conduct data cleaning and exploratory data analysis (EDA) on diverse datasets
        * Derive insights and patterns that guide decision-making
        * Apply statistical methods and machine learning techniques to analyze data
        * Present findings and recommendations to stakeholders
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        # Skills developed during experience
        st.markdown("### Skills Developed During Work Experience")

        skills_data = {
            'Skill': ['Data Cleaning', 'EDA', 'Statistical Analysis', 'Data Visualization', 'Presentation'],
            'Growth': [90, 85, 75, 80, 70]
        }

        df = pd.DataFrame(skills_data)
        st.bar_chart(df.set_index('Skill'))

    # Projects
    elif choice == "Projects":
        st.markdown('<p class="section-header">Projects</p>', unsafe_allow_html=True)

        st.markdown('<div class="project-box">', unsafe_allow_html=True)
        st.markdown("### Sales Analysis (SQL)")
        st.markdown("**Awesome Chocolate**")
        st.markdown("""
        * Analyzed sales data to identify trends and optimize performance
        * Designed SQL queries to extract insights, improving revenue forecasting
        * Implemented data-driven recommendations for business optimization
        """)

        if st.button("View SQL Project Details"):
            st.code("""
            -- Sample SQL Queries from the Project

            -- Total Sales by Product
            SELECT 
                p.product_name,
                SUM(s.amount) as total_sales
            FROM 
                sales s
            JOIN 
                products p ON s.product_id = p.id
            GROUP BY 
                p.product_name
            ORDER BY 
                total_sales DESC;

            -- Monthly Sales Trends
            SELECT 
                DATE_FORMAT(s.sale_date, '%Y-%m') as month,
                SUM(s.amount) as monthly_sales
            FROM 
                sales s
            GROUP BY 
                month
            ORDER BY 
                month;
            """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="project-box">', unsafe_allow_html=True)
        st.markdown("### Sales & Business Insights Dashboard (Power BI)")
        st.markdown("""
        * Created an interactive dashboard for data-driven decision making
        * Integrated multiple data sources for real-time business performance tracking
        * Designed KPI visualizations for tracking sales performance, customer metrics, and product insights
        """)

        if st.button("View Dashboard Preview"):
            # Use placeholder for dashboard image
            image_placeholder(800, 400, "Dashboard Preview")
        st.markdown("</div>", unsafe_allow_html=True)

    # Certifications
    elif choice == "Certifications":
        st.markdown('<p class="section-header">Certifications</p>', unsafe_allow_html=True)

        certifications = [
            {
                "title": "Data Analytics Job Simulation",
                "organization": "BCG X Forage",
                "link": "https://www.theforage.com/simulations/bcg/data-science-ccdz"
            },
            {
                "title": "SQL and Relational Databases",
                "organization": "IBM Developer Skills Network",
                "link": "https://courses.cognitiveclass.ai/certificates/6b84e91bb90d407cbb3ecdd399040885"
            },
            {
                "title": "Machine Learning with Python",
                "organization": "E&ICT Academy, IIT Kanpur",
                "link": "#"
            },
            {
                "title": "Python for Data Science",
                "organization": "IBM Developer Skills Network",
                "link": "https://courses.cognitiveclass.ai/certificates/ff558b0ba77a47aab8473dc6791b97fb"
            },
            {
                "title": "Certificate of Participation",
                "organization": "BIBS & Anand Learning Academy",
                "link": "#"
            }
        ]

        col1, col2 = st.columns(2)

        for i, cert in enumerate(certifications):
            if i % 2 == 0:
                with col1:
                    st.markdown(f"""
                    <div style="background-color: #f0f2f6; border-radius: 10px; padding: 15px; margin-bottom: 15px;">
                        <h3>{cert['title']}</h3>
                        <p><strong>Issuing Organization:</strong> {cert['organization']}</p>
                        <p><a href="{cert['link']}" target="_blank">View Certificate</a></p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                with col2:
                    st.markdown(f"""
                    <div style="background-color: #f0f2f6; border-radius: 10px; padding: 15px; margin-bottom: 15px;">
                        <h3>{cert['title']}</h3>
                        <p><strong>Issuing Organization:</strong> {cert['organization']}</p>
                        <p><a href="{cert['link']}" target="_blank">View Certificate</a></p>
                    </div>
                    """, unsafe_allow_html=True)

    # Achievements
    elif choice == "Achievements":
        st.markdown('<p class="section-header">Achievements</p>', unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #f0f2f6; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
            <h3>Sports Achievement</h3>
            <p>Played in OLE COLLEGE Tournament in 2025.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #f0f2f6; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
            <h3>IBM TECHNOVATE EVENT</h3>
            <p>3RD RUNNER UP & received goodies</p>
        </div>
        """, unsafe_allow_html=True)

    # Contact
    elif choice == "Contact":
        st.markdown('<p class="section-header">Contact Me</p>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            ### Get In Touch

            Feel free to reach out to me for any data analysis projects, 
            collaborations, or opportunities.

            - 📱 Phone: +91 7410173864
            - 📧 Email: [arka.sain24-26@bibs.co.in](mailto:arka.sain24-26@bibs.co.in)
            - 🔗 LinkedIn: [www.linkedin.com/in/arka-sain-4060812b4](https://www.linkedin.com/in/arka-sain-4060812b4)
            - 💻 GitHub: [github.com/Arkasain](https://github.com/Arkasain)
            """)

        with col2:
            st.markdown("### Send Me a Message")

            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")

            if st.button("Send Message"):
                st.success("Thank you for your message! I'll get back to you soon.")


if __name__ == "__main__":
    main()
