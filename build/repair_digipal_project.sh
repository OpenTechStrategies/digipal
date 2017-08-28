# Scenario: user has enabled or changed the folder of the docker data volume.
# That's the content of digipal_project.
# This script repair the content of digipal_project, add the missing parts.
cd /home/digipal

# Recreate content of digipal_project if empty (e.g. enabled volume in kitematic)
if [ ! -e "digipal_project/__init__.py" ]; then
    git checkout digipal_project
    
    # TODO: restore archetype.zip under digipal_project
fi

# configure and copy default DB into digipal_project
if [ ! -e "digipal_project/database" ]; then
    mkdir digipal_project/database
fi

PG_CONFIG_PATH=`find /etc -iname postgresql.conf`
PG_CONFIG_PATH_ORIGINAL="$PG_CONFIG_PATH.bk"
if [ ! -e "$PG_CONFIG_PATH_ORIGINAL" ]; then
    # make a copy of the original psql config file
    cp $PG_CONFIG_PATH $PG_CONFIG_PATH_ORIGINAL
    # psql data directory = digipal_project/database
    sed -i -E "s@data_directory.*@data_directory = '/home/digipal/digipal_project/database'@g" $PG_CONFIG_PATH
fi
# get the path the original data directory
PG_ORIGINAL_DATA_DIR=`grep 'data_directory' $PG_CONFIG_PATH_ORIGINAL | sed -E "s@data_directory.*=.*'(.*)'.*@\1@g"`

if [ ! -e "digipal_project/database/PG_VERSION" ]; then
    # database is missing, let's copy it from the original psql data dir
    rm -rf digipal_project/database/*
    cp -r $PG_ORIGINAL_DATA_DIR/* digipal_project/database/.
    # Create the database, the user and allow local and remote access using md5 auth.
    # Fixes issue with Django accessing the DB
    # Adjust PostgreSQL configuration so that remote connections to the database are possible.
    # RUN /etc/init.d/postgresql start &&\
    
    source build/fix_permissions.sh
    
    service postgresql start
    echo "Recreate database and user"
    su postgres -c /bin/bash <<"EOF" 
        psql -c "CREATE USER app_digipal WITH PASSWORD 'dppsqlpass';" &&\
        createdb -E 'utf-8' -T template0 -O app_digipal digipal &&\
        sed -i 's/local\s*all\s*all\s*peer/local    all    all    md5/' $(psql -c "SHOW hba_file;" | grep conf | xargs) &&\
        echo "host all  all    0.0.0.0/0  md5" >> $(psql -c "SHOW hba_file;" | grep conf | xargs)
EOF

    # TODO: restore archetype.sql or archetype.sql in digipal_project
    if [ -e "digipal_project/archetype.sql"]; then
        
    fi

    service postgresql stop
fi

source build/fix_permissions.sh
