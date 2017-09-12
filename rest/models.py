# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import models

# Create your models here.

class Profile(models.Model)  # associated with user
    user = models.ForeignKey(User)
    email = models.EmailField()
    display_name = models.CharField(max_length=80)
    profile_picture = models.
    about_me = models.CharField(max_length=500)
    website = models.urlField()
    profile_link = models.urlField()

class Team(models.Model)
    team_admin=models.ForeignKey(User)
    checkinscheme = models.ForeignKey(CheckinScheme)

class CheckinScheme(models.Model)
    title = models.CharField(max_length=100)

class CheckinTextQuestion(models.Model)
    checkin_q = models_CharField(max_length=500)
    checkinScheme = models.ForeignKey(CheckinScheme)

class CheckinMultiQuestion(models.Model)
    checkin_q = models.CharField(max_length = 500)
    checkinScheme = models.ForeignKey(CheckinScheme)
    allowMultiple = models.BooleanField()

class CheckinMultiAns(models.Model)
    answerText = models.CharField(max_length=200)
    question = models.ForeignKey(CheckinMultiQuestion)

class UserCheckin()
    user = models.ForeignKey(User)
    date = models.DateField()
    CheckinSheme = models.ForeignKey()
    
class UserCheckinTextAnswer()
    checkin = models.ForeignKey(UserCheckin)
    question = models.ForeginKey(CheckinTextQuestion)
    
class userCheckinMultiAnswer()
    checkin = models.ForeignKey(UserCheckin)
    question = models.ForeignKey(CheckinMultiQuestion)
    answer = models.ForeignKey(CheckinMultiAns)

class WallPost(models.Model)
    author = models.ForeignKey(Profile)
    parentPost = models.oneToMany(WallPost)

class Task(models.Model)

class Timer(models.Model)
