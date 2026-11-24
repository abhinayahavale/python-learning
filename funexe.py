cat_name = input("enter your cat's name:")
daily_naps=int(input("how many naps did your cat take today?"))
weekly_naps = daily_naps * 7
print("cat's name:", cat_name)
print("daily naps:", daily_naps)
print("weekly naps:",weekly_naps)

work_skills=["knocking pens off desks",
             "Ignoring important emails",
             "sleeping during meetings"]

for skill in work_skills:
    print("skill:",skill)

cat={
    "name": cat_name,
    "daily_naps": daily_naps,
    "best_work_skill": work_skills[0]
}

print(cat)

if daily_naps >=5:
    print(cat_name, "is a hard worker!")
else:
    print(cat_name, "need to improve its nap performance!")

def introduce_cat(name,job_tittle):
    return " meet " + name + ", the " + job_tittle + "!"
print(introduce_cat(cat["name"],"senior director of Ignoringn emails"))


