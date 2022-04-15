import sys

def eligibility():
    n = int(input())
    for _ in range(n):
        name, study, birthday, courses = input().split()
        study_year = int(study.split("/")[0])
        birth_year = int(birthday.split("/")[0])
        if study_year >= 2010 or birth_year >= 1991:
            print(name, "eligible")
        elif int(courses) >= 41:
            print(name, "ineligible")
        else:
            print(name, "coach petitions")



eligibility()
