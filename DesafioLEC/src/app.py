from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

import rotas
