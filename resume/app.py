from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Create PDF
file_path = "/mnt/data/Diploma_Student_Resume.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("<b><font size=16>Resume</font></b>", styles["Title"]))
elements.append(Spacer(1, 12))

# Personal Info
personal_info = """
<b>Name:</b> [Your Full Name]<br/>
<b>Mobile:</b> +91-XXXXXXXXXX<br/>
<b>Email:</b> yourmail@example.com<br/>
<b>Address:</b> [Your City, State]
"""
elements.append(Paragraph(personal_info, styles["Normal"]))
elements.append(Spacer(1, 12))

# Career Objective
elements.append(Paragraph("<b>Career Objective</b>", styles["Heading2"]))
elements.append(Paragraph("To start my career in a reputed organization where I can utilize my skills and knowledge, gain practical experience, and contribute to the company’s growth while enhancing my own abilities.", styles["Normal"]))
elements.append(Spacer(1, 12))

# Education Table
elements.append(Paragraph("<b>Education</b>", styles["Heading2"]))
education_data = [
    ["Qualification", "College/Institute", "Board/University", "Year", "Percentage/CGPA"],
    ["Diploma in [Branch]", "[Your Polytechnic Name]", "[Board Name]", "[Year]", "[XX%]"],
    ["10th (High School)", "[Your School Name]", "[Board Name]", "[Year]", "[XX%]"]
]
table = Table(education_data, hAlign="LEFT")
table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                           ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                           ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                           ("GRID", (0, 0), (-1, -1), 1, colors.black),
                           ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]))
elements.append(table)
elements.append(Spacer(1, 12))

# Technical Skills
elements.append(Paragraph("<b>Technical Skills</b>", styles["Heading2"]))
elements.append(Paragraph("- Programming Languages: C, C++, Java / Python<br/>- Web Technologies: HTML, CSS, JavaScript, PHP<br/>- Database: MySQL<br/>- Tools: MS Office, AutoCAD", styles["Normal"]))
elements.append(Spacer(1, 12))

# Academic Projects
elements.append(Paragraph("<b>Academic Projects</b>", styles["Heading2"]))
elements.append(Paragraph("<b>Project Title:</b> [Your Project Name]<br/>Developed a Student Management System using PHP and MySQL to store student data and manage records.", styles["Normal"]))
elements.append(Spacer(1, 12))

# Internship
elements.append(Paragraph("<b>Internship / Training</b>", styles["Heading2"]))
elements.append(Paragraph("<b>Company/Institute Name:</b> [Company Name] – [Location]<br/><b>Duration:</b> [Start – End Month/Year]<br/><b>Role:</b> Intern<br/><b>Key Learnings:</b> Basics of networking, web development, etc.", styles["Normal"]))
elements.append(Spacer(1, 12))

# Achievements
elements.append(Paragraph("<b>Achievements</b>", styles["Heading2"]))
elements.append(Paragraph("- Secured [Rank/Percentage] in Diploma.<br/>- Participated in Coding Contest/Technical Fest.<br/>- Certification in Web Development/Python/AutoCAD.", styles["Normal"]))
elements.append(Spacer(1, 12))

# Personal Details
elements.append(Paragraph("<b>Personal Details</b>", styles["Heading2"]))
elements.append(Paragraph("Date of Birth: [DD/MM/YYYY]<br/>Gender: [Male/Female]<br/>Languages Known: Hindi, English<br/>Hobbies: Coding, Reading, Playing Cricket", styles["Normal"]))
elements.append(Spacer(1, 12))

# Declaration
elements.append(Paragraph("<b>Declaration</b>", styles["Heading2"]))
elements.append(Paragraph("I hereby declare that the above information is true to the best of my knowledge and belief.", styles["Normal"]))
elements.append(Spacer(1, 24))
elements.append(Paragraph("Place: [City]<br/>Date: [DD/MM/YYYY]<br/><br/>Signature: ____________", styles["Normal"]))

# Build PDF
doc.build(elements)

file_path
