from __future__ import unicode_literals
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from django.db import models

class LoginManager(models.Manager):
	def reg_val(self, postData):
		errors = {}
		##Check Firtname length & that it has no ints in it.
		if len(postData['fname']) < 2 or postData['fname'].isalpha() == False:
			errors['fname'] = "Please register correct fname"
		##Check Lastname length & that it has no ints in it.
		if len(postData['lname']) < 2 or postData['lname'].isalpha() == False:
			errors['lname'] = "Please register correct lname"
		##Checks that Email is a correct format.
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Incorrect email"
		##Check if the email already exist in the database.
		if User.objects.filter(email=postData['email']):
			errors['emailExist'] = "Email already in database"
		#Check that the Password & Confirm Password match.
		if postData['pw'] != postData['confPW']:	
			errors['noMatch'] = "Passwords do not match"
		##Checks the lenth of the password.
		if len(postData['pw']) < 8:
			errors['pw'] = "Password needs to be longer than 8 characters"
		##Adds user data to data base if no errors.
		if len(errors) < 1:
			hashedPW = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
			User.objects.create(fname=postData['fname'],lname=postData['lname'],email=postData['email'],pw=hashedPW)
		
		return errors

	def log_val(self, postData):
		errors ={}
		##Check that email is correct format & the length of email.
		if not EMAIL_REGEX.match(postData['email']) or postData['email'] < 1:
			errors['email'] = "Incorrect email, Please try again"
		##Checks length of password,
		if len(postData['pw']) < 1:
			errors['pw'] = "Please type a Password"
		##Checks hashed PW against PW in data base & Email againts email in database.
		if not bcrypt.checkpw(postData['pw'].encode(), User.objects.get(email=postData['email']).pw.encode()) and User.objects.get(email=postData['email']):
				errors['pw'] = "Incorrect signin"	
		return errors


class User(models.Model):
	fname = models.CharField(max_length=255)
	lname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pw = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = LoginManager()