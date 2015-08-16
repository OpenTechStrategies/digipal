#!/bin/bash
# Runs regular tasks

#env_path="$1"
SHOW_HELP=1

# CD to project dir (based on the bash path)
DIR_PRJ=$( cd "$( dirname "$0" )" && pwd )/..
cd $DIR_PRJ

while getopts ":p:e:i" opt; do
  case $opt in
    e)
      echo "Activate ENV $OPTARG"
      source $OPTARG/bin/activate
      SHOW_HELP=0
      ;;
    p)
      # upgrade the code
      python digipal/repo.py -a -e "$OPTARG" pull
      SHOW_HELP=0
      ;;
    i)
      python manage.py dpsearch index
      #python manage.py dpsearch index_facets --if=manuscripts,images,scribes,hands,texts
      ##python manage.py dpsearch index_facets --if=manuscripts,images,scribes,hands,texts

      # This takes 1 hour!
      ##python manage.py dpsearch index_facets --if=graphs
      SHOW_HELP=0
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

if [ "$SHOW_HELP" == "1" ]
  then
    echo "Usage: bash crontab.sh [-COMMAND1 OPTION1] [-COMMAND2 OPTION2] [...]"
    echo "Runs a regular DigiPal job. You can call it from your crontab."
    echo ""
    echo "Accepts one or more of the following commands:"
    echo "  -e ENV_PATH  activate the virtual env located at ENV_PATH"
    echo "  -p EMAIL     update the code from the repositories and restart DigiPal."
    echo "                 Send an email to EMAIL on error."
    echo "  -i           REINDEX the content"

    exit 0
fi

exit

if [ ! -f manage.py ]
    then
        echo "ERROR: manage.py not found."
	exit
fi

if [ -n "$env_path" ]
    then
        source $env_path/bin/activate

        # upgrade the code
        email="$2"
        if [ ! -z "$email" ]
            then
                python digipal/repo.py -a -e "$email" pull
        fi
        
        # Reindexing
        python manage.py dpsearch index
        #python manage.py dpsearch index_facets --if=manuscripts,images,scribes,hands,texts
        ##python manage.py dpsearch index_facets --if=manuscripts,images,scribes,hands,texts
        
        # This takes 1 hour!
        ##python manage.py dpsearch index_facets --if=graphs
        
        # Bye
        deactivate
fi


