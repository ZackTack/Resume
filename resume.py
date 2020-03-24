# Text
Name = "Zhehao Xu"
Title = "Graduate Student"
ContactHeader = "CONTACT"
Contact = """
+1 226-975-3600
z352xu@uwaterloo.ca
1297 Marlborough Court, Oakville, Ontario
https://www.linkedin.com/in/zhehaoxu/
https://github.com/ZackTack"""
SelfIntro = """
Recent graduated student who obtained Master of Engineering degree with 
Software Engineering diploma in Electrical & Computer Engineering and 
prepared to contribute abilities to IT-related role while further developing 
acquired skills and gaining real-world experience. Highly organized, 
responsible and well-versed in Python."""
ProjectsHeader = "PROJECTS/PUBLICATIONS"
ProjectOneTitle = "Overwatch Data Mining Project"
ProjectOneDesc = """
\u2022 Found out elements that effected the match results the most with 83% 
prediction accuracy on match results in Overwatch video game by constructing 
and training a random forest classifier using Kaggle dataset along with pandas, 
scikit-learn in python
\u2022 Learned how to preprocess raw data, construct and tune parameters of the 
random forest classifier and also other potential classifiers including multi-
layer perceptron, svm classifiers"""
ProjectTwoTitle = "Autonomous Driving Lane Detection System"
ProjectTwoDesc = """
\u2022 Developed a lane detection system in a team of 3 members based on fully 
convolutional neural network that could highlight safe areas for the vehicle 
during the driving
\u2022 In charged of testing the trained neural network and evaluated its 
performance on self-recorded on-road videos in Windsor
\u2022 Implemented the system to a raspberry pi
\u2022 Learned knowledge about convolutional neural network, Keras, Matplotlib 
and other useful machine learning related libraries, and raspberry pi including
how to operate it and implement the system onto it"""
WorkHeader = "EXPERIENCE"
WorkOneTitle = "Project Coordinator/GIANTECH Engineering (known as GIA)"
WorkOneTime = "2017-10 - 2017-12"
WorkOneDesc = """
\u2022 Created learning programs in Gnowbe app including inert gas system (IGS),
inert gas generator(IGG), Kyma powermeters
\u2022 Developed logo concepts for "GIA Methods" under GIANTECH Engineering
 and been selected as one of the best designs"""
EduHeader = "EDUCATION"
EduOneTitle = "University of Waterloo, Master of Engineering"
EduOneTime = "2018-09 - 2019-12"
EduOneDesc = "\u2022 Electrical & Computer Engineering, Software Engineering Diploma"
EduTwoTitle = "University of Windsor, Bachelor of Applied Science"
EduTwoTime = "2014-09 - 2018-08"
EduTwoDesc = "\u2022 Electrical Engineering, Outstanding Scholarship"
SkillsHeader = "SKILLS"
SkillsDesc = """
Hard Skills:
- Python (Expert)
- Pandas (Expert)
- NumPy (Expert)
- Scikit-Learn (Expert)
- TensorFlow (Advanced)
- Data Visualization (Advanced)
- Data Manipulation (Expert)
- Git (Intermediate)
- MySQL (Advanced)
- Excel (Expert)

Soft Skills:
- Critical Thinking (Expert)
- Problem Solving (Advanced)
- Interpersonal Skill (Advanced)"""
LanguageHeader = "LANGUAGE"
LanguageDesc = """
- Chinese (Native)
- English (Fluent)
"""
# Setting style for bar graphs
import matplotlib.pyplot as plt

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#003459', alpha=0.85, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# set header color
header_color = '#00A7E1'

# remove axes
plt.axis('off')

# add text
plt.annotate(Name, (.02, .94), weight='bold', fontsize=20)
plt.annotate(Title, (.02, .91), weight='regular', fontsize=14)
plt.annotate(SelfIntro, (.02, .809), weight='regular', fontsize=9)
plt.annotate(ContactHeader, (.7, .97), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(Contact, (.7, .9), weight='regular', fontsize=8, color='#ffffff')

project_section_pt = .76
plt.annotate(ProjectsHeader, (.02, project_section_pt), weight='bold', fontsize=10, color=header_color)
plt.annotate(ProjectOneTitle, (.02, project_section_pt - .03), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (.04, project_section_pt - .153), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (.02, project_section_pt - .189), weight='bold', fontsize=10)
plt.annotate(ProjectTwoDesc, (.04, project_section_pt - .345), weight='regular', fontsize=9)

work_section_pt = .36
plt.annotate(WorkHeader, (.02, work_section_pt), weight='bold', fontsize=10, color=header_color)
plt.annotate(WorkOneTitle, (.02, work_section_pt - .03), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02, work_section_pt - .05), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04, work_section_pt - .12), weight='regular', fontsize=9)

education_section_pt = .185
plt.annotate(EduHeader, (.02, education_section_pt), weight='bold', fontsize=10, color=header_color)
plt.annotate(EduOneTitle, (.02, education_section_pt - .03), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02, education_section_pt - .05), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduOneDesc, (.04, education_section_pt - .07), weight='regular', fontsize=9)
plt.annotate(EduTwoTitle, (.02, education_section_pt - .105), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.02, education_section_pt - .125), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduTwoDesc, (.04, education_section_pt - .145), weight='regular', fontsize=9)

plt.annotate(SkillsHeader, (.7, .83), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7, .52), weight='regular', fontsize=10, color='#ffffff')

plt.annotate(LanguageHeader, (.7, .46),weight='bold', fontsize=10, color='#ffffff')
plt.annotate(LanguageDesc, (.7, .38),weight='regular',fontsize=10, color='#ffffff')

plt.savefig('Resume(ZhehaoXu).pdf', dpi=300, bbox_inches='tight')
plt.show()
