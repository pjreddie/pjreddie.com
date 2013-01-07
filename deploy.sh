/manage.py dumpdata core > pjreddie/core/fixtures/initial_data.json
git commit -a -m "Update fixtures"
git push heroku master
heroku run python manage.py migrate
