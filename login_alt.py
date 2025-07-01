from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'DEEPAK B', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Email: edudeepak2@gmail.com | Phone: +91 7204662895 | LinkedIn: https://rb.gy/wj1ciu', 0, 1,
                  'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_section(self, title, body):
        self.chapter_title(title)
        self.chapter_body(body)


# Create instance of FPDF class
pdf = PDF()

pdf.add_page()

# Professional Summary
pdf.add_section('PROFESSIONAL SUMMARY',
                'Aspiring Full-Stack Developer with expertise in Machine Learning. Proven experience in developing predictive models and web-based applications. Strong analytical, problem-solving, and communication skills. Passionate about continuous learning and personal growth.')

# Education
education_body = '''G M Institute of Technology, Davanagere
Bachelor of Engineering in Information Science and Engineering
CGPA: 9.01
Relevant Coursework: Web Development, Computer Network, Automata Theory, Data Mining, Software Testing, Software Engineering, Database Management System, Data Structures and Algorithms

Certifications:
- Programming in Java - NPTEL
- The Joy of Computing using Python - NPTEL
- Web Development - CodSoft'''
pdf.add_section('EDUCATION', education_body)

# Skills
skills_body = '''Programming Languages: Python, Java
Web Technologies: HTML, CSS
Machine Learning: Scikit-learn, Pandas, NumPy
Databases: SQL
Tools: Git, JIRA, Docker'''
pdf.add_section('SKILLS', skills_body)

# Projects
projects_body = '''House Price Prediction
May 2024 - Jul 2024
- Developed a machine learning model to predict house prices using Python, Pandas, NumPy, and Scikit-learn.
- Responsibilities: Data preprocessing, feature engineering, model evaluation.

Hostel Banking System
Oct 2023 - Nov 2023
- Created a web-based banking system for hostel management using PHP, MySQL, and HTML/CSS.
- Responsibilities: Database design, web development, user authentication.'''
pdf.add_section('PROJECTS', projects_body)

# Professional Experience
experience_body = '''Technologics Global Pvt Ltd, Bengaluru
Intern
Dec 2023 - Mar 2024
- Worked on various projects involving machine learning and full-stack development.
- Enhanced skills in data analysis, algorithm development, and application design.'''
pdf.add_section('PROFESSIONAL EXPERIENCE', experience_body)

# Achievements
achievements_body = '''- Developed and implemented a machine learning model that increased prediction accuracy by 15%.
- Successfully led a team project to develop a web-based application, improving user access by 30%.
- Received the "Outstanding Intern Award" for exceptional performance and contributions.'''
pdf.add_section('ACHIEVEMENTS', achievements_body)

# Additional Information
additional_info_body = '''Languages: Fluent in English; Conversational proficiency in Kannada.
Interests: Exploring new technologies, staying updated on current trends in machine learning and web development.'''
pdf.add_section('ADDITIONAL INFORMATION', additional_info_body)

# Save the PDF to file
output_path = "/mnt/data/Updated_Resume_Deepak.pdf"
pdf.output(output_path)

output_path
