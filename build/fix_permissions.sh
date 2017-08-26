cd /home/digipal

# reset permission to www-data
chown -R www-data:www-data ../digipal
chmod -R ug+rw ../digipal
chmod -R o-rw ../digipal

# grant permissions to project/shared folder to world
chmod o+rw -R digipal_project
chmod o+x digipal_project

# special permission requirements for psql on its database folder
# special permission requirements for psql on its database folder
if [ -e "digipal_project/database" ]; then
    chown postgres:postgres -R digipal_project/database
    chmod u+rw -R digipal_project/database
    chmod u+x digipal_project/database
    chmod go-rwx digipal_project/database
fi
