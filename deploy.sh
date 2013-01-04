pg_dump -Fc --no-acl --no-owner -h localhost pjreddie > pjreddie/media/database.dump
git commit -a -m "Update database"
git push heroku master
heroku pgbackups:restore DATABASE "http://www.pjreddie.com/media/database.dump"
