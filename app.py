import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
import pickle
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from model import plotting



def create_app():
    app = Flask(__name__)

    @app.route('/upload', methods = ['GET', "POST"])
    def upload():
        if request.method == 'POST':
            ticker_name = request.form['ticker_name']
            output_file = plotting(ticker_name)

            return redirect(url_for('download'))


        return render_template('upload.html')
    
    @app.route('/download')
    def download():
        return render_template('view.html', plt_url = f"static/graph.png")
    
    return app