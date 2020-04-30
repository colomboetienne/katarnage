import textile
import string
import random
import json
from os import walk

template = """MIME-Version: 1.0
Date: Tue, {0} {7}:36:19 +0200
Message-ID: <CAEV={1}@mail.gmail.com>
Subject: {2}
From: {3} <{4}>
To: {5}
Content-Type: multipart/alternative; boundary="000000000000ea411605a457660c"

--000000000000ea411605a457660c
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

--000000000000ea411605a457660c
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

{6}

--000000000000ea411605a457660c--
"""
#28 Apr 2019

letters = string.ascii_lowercase

(_, _, filenames) = walk('./jsons/').next()

# mail_date = "28 Apr 2019"
# subject = "un sujet"
# from_name = "Charles Darwin"
# from_mail = "charlesDarwin@gmail.com"
# to_mail = "davidlefevre2047@gmail.com"
# body = textile.textile("""un example de boundary
# foobar""")
uniq_id = ''.join(random.choice(letters) for i in range(45))
hour = 1
for myfile in filenames:
    myfilename = myfile.split('.')[0]
    print myfilename
    with open('./jsons/'+ myfilename + '.json', 'r') as json_file:
        data = json.load(json_file)

    hour += 1
    if not data['same']:
        uniq_id = ''.join(random.choice(letters) for i in range(45))
        hour = 1


    body = textile.textile(data['body'])
    body = body.encode(encoding='UTF-8',errors='strict')
    print body
    test = template.format(
        data['date'],
        uniq_id,
        data['subject'],
        data['from_name'],
        data['from_mail'],
        data['to_mail'],
        body,
        hour,
        )

    with open("./output/" + myfilename + '.eml', "w") as le_mail:
        le_mail.write(test)
