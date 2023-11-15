from flask import Flask, request

password = request.form['password']

print(password)
