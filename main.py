import array
import csv
import os
import re
import time

import cv2
import face_recognition
import lxml
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField

app = Flask(__name__, template_folder='template',
            static_folder='template/assets')
app.config['UPLOAD_FOLDER'] = 'static'
app.config['SECRET_KEY'] = 'supersecretkey'

path = 'images'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


class uploadFileForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Upload File')


encodeList = np.loadtxt('train.txt')


@app.route('/', methods=['GET', "POST"])
@app.route('/pt', methods=['GET', "POST"])
def home():
    form = uploadFileForm()
    if form.validate_on_submit():
        file = form.file.data  # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                  app.config['UPLOAD_FOLDER'], secure_filename('test.jpg')))

        imgtest = face_recognition.load_image_file('static/test.jpg')
        imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)
        encodetest = face_recognition.face_encodings(imgtest)[0]
        matches = face_recognition.compare_faces(encodeList, encodetest)
        faceDis = face_recognition.face_distance(encodeList, encodetest)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            facedis = faceDis[matchIndex]

        data = []
        data.append(f'Player Name: {name}')
        data.append(f'FaceDis: {facedis}')
        try:
            link = f"https://www.google.com/search?q={name}+premier+league.com+stats"
            source = requests.get(link).text
            page = BeautifulSoup(source, "lxml")
            page = page.find("div", class_="kCrYT")
            link = page.find("a", href=re.compile(
                r"[/]([a-z]|[A-Z])\w+")).attrs["href"]

        except:
            link = f"https://www.google.com/search?q={name}+pl+stats"
            source = requests.get(link).text
            page = BeautifulSoup(source, "lxml")
            page = page.find("div", class_="kCrYT")
            link = page.find("a", href=re.compile(
                r"[/]([a-z]|[A-Z])\w+")).attrs["href"]

        spl_word = '&sa'
        res = link[7:].partition(spl_word)[0]
        if "stats" in res:
            res = res.replace('stats', 'overview')

        sta = res.replace('overview', 'stats')
        source = requests.get(sta).text
        page = BeautifulSoup(source, "lxml")
        side = page.find("div", class_="label").text

        ###
        name = page.find("div", class_="name t-colour").text
        position = page.find("div", class_="info").text.strip()
        club = "No longer part of EPL"

        if "Club" in side:
            a = page.find_all("div", class_="info")
            club = page.find("div", class_="info").text.strip()
            position = a[1].text.strip()

        #####
        stats = page.find_all("div", class_="topStat")
        basic = []
        for i in range(len(stats)):
            basic.append(stats[i].text.strip())
        basic_stats = []

        for k in range(len(basic)):
            basic_stats.append(basic[k].split("\n"))

        ####
        source2 = requests.get(res).text
        page2 = BeautifulSoup(source2, "lxml")
        personal_details = page2.find("div", class_="playerInfo")
        pd = personal_details.find_all("div", class_="info")
        ####
        nationality = personal_details.find(
            "span", class_="playerCountry").text
        dob = pd[1].text.strip()

        fin = page.find_all("div", class_="normalStat")
        final = []
        for j in range(len(fin)):
            final.append(fin[j].text.strip())

        for k in range(len(final)):
            data.append(final[k].split("\n"))

        return render_template('predict.html', data=data)

    return render_template('upload.html', form=form)


app.run(host='0.0.0.0', port=8080)
