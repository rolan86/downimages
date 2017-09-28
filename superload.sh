#!/bin/sh
supervisorctl reread
supervisorctl update
supervisorctl start flask_project
