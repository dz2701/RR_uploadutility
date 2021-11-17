
file_data = OrderedDict()

file_data["title"] = str(input("title: \n"))
file_data["author"] = str(input("author: \n"))
file_data["pubdate"] = "October 17, 2021"
noofim = int(input("number of images?\n"))
number = int(input("number of json?:\n"))
file_data["img"] = []
for i in range (1,noofim+1):
    file_data["img"].append("https://firebasestorage.googleapis.com/v0/b/reserverecord-b2de5.appspot.com/o/images%2F{a}-{b}.png?alt=media&token=8a30dc10-a93e-460a-a0f4-2418d7956e04".format(a=number, b=i))
file_data['captions'] = []
file_data['content'] = """ “Being a new student in the middle of my high school career scared me, not gonna lie. Everyone here at Reserve was super welcoming! It feels like I’ve been here the whole time even though it’s only been a month .” – Andrea Belen ’23

 “I’m grateful to see so many new students this year because it takes the pressure off of being in an environment where everyone already knows each other. I also enjoy the food prepared by the terrific kitchen staff, especially the cookies!” –Charlotte Hooker ’23

 “The first thing I noticed about Reserve was that everyone is here for a reason, and that everyone has goals they are trying to reach as athletes and students.”

–Hannah McReynolds ’23""".replace("\n", "\n")

file_data['categories'] = []

for i in range(1, noofim+1):
    file_data['captions'].append(input("please tell me caption of picture number {}\n".format(i)))

while(1):
    inp = input("please input the category for this article. if end, enter 1.\n")
    if (inp == "1"): break
    file_data['categories'].append(inp)


with open('../{}.json'.format(number), 'w', encoding="utf-8") as f:
    json.dump(file_data, f, ensure_ascii=False, indent="\t")

