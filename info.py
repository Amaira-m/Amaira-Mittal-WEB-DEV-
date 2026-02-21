import streamlit as st

#This File will contain the information to be displayed in your portfolio

#CHANGE BELOW
profile_picture = "Images/profile.jpg"
about_me = "Hii I'm Amaira! I am from Jaipur, India. I am an empathetic person and I loveeee dogs so much!!! I LOVE FOOD TOO "


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/amaira-mittal-138564253"
my_github_url = "https://github.com/spongebob-squarepants"
my_email_address = "amaira.m@gatech.edu"


education_data ={
    'Degree': 'Bachelor of Science in Industrial Engineering',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'May 2029',
    'GPA': '4.0 Duh'
}
course_data = {
    "code":["CS 1301", "APPH 1050", "MATH 1553", "PSYCH 1101"], 
    "names":["Intro to CS", "Science of Physical activity", "Linear Algebra", "General Psychology"], 
    "semester_taken":["1st", "1st", "1st", "1st"],
    "skills":["coding","walk to crc in 7 mins","how to solve made up math","not to self diagnose"],
    }
experience_data = {
    "Fitness enthusiast": (["Worked on creating a very doable and perfect fitness schedule for myself",
                                                                          "- Can do for you too! Consulting is free, just reach out"],"Images/fitness.jpg"),
    "Stylist":(["- Designed chic and absolute diva college outfits",
                                                           "- Inspired by pinterest"],"Images/stylist.jpg"),
    "Proffesional sleeper":(["- I can sleep 12+ hours a day and teach u how to do that too (happy ppl sleep more I think)"],"Images/sleep.jpg")

}

projects_data = {
    "CS1301 WEBDEV": "Built a website for my cs class and created a quiz on measuring emotional EQ (RESSURECTED THROUGH DEBUGGING)",
    "Cinema on Wheels": "Ideated a Cinema on Wheels and brought it to life!!!"
}

programming_data = {
    "Python": 70,
    "Java": 10,
    "C": 10,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🔍",
}
spoken_icons = {"French": "🇫🇷",
    "English": "🇬🇧",
    "HINDI": "🇮🇳"
}

#CHANGE BELOW
spoken_data = {
    "French": "Mildly Fluent",
    "English": "Fluent",
    "Hindi": "Fluent",
}
leadership_data = {
    "Eldest daughter of the family": (["- I basically do everything for everyone"],"Images/puff.jpg"),

}
activity_data={
    "Badminton and Dance": ["I play badminton! (and dance when i score a point!)"]
}
