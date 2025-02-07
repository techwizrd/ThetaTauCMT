#!/bin/bash
# chmod +x backup.sh
# from django.core.management import call_command
# call_command('dbbackup', '--encrypt', '--noinput')
# call_command('dbrestore', '--decrypt', '--noinput',
#              '--passphrase=%passphrase%', database='default')

if [[ $1 == "" ]]; then
  echo 'You must provide database encryption passphrase'
  exit 1
fi

PASSPHRASE=$1

RESTORE_TEST=${2:-true}

source virtualenvwrapper.sh

echo "Backup production to local drive"
if ! workon thetatauCMT; then
  echo "An error occurred setting thetatauCMT"
  exit
fi
export GNUPGHOME="/home/Venturafranklin/thetatauCMT/secrets"
export DBBACKUP_STORAGE_LOCATION="/home/Venturafranklin/thetatauCMT/database_backups"
if ! python manage.py dbbackup --encrypt --noinput --clean; then
  echo "An error occurred backing up database"
  exit
fi

if [ "$RESTORE_TEST" = true ]; then
  deactivate

  echo "Restore test restore to staging"
  if ! workon testCMT; then
    echo "An error occurred setting testCMT"
    exit
  fi
  export GNUPGHOME="/home/Venturafranklin/thetatauCMT/secrets"
  export DBBACKUP_STORAGE_LOCATION="/home/Venturafranklin/thetatauCMT/database_backups"
  if ! python manage.py dbrestore --database default --decrypt --noinput --passphrase=$PASSPHRASE; then
    echo "An error occurred restoring database"
    exit
  fi

  echo "De-identify staging database"
  export DBBACKUP_STORAGE_LOCATION="/home/Venturafranklin/testCMT/database_backups"
  python manage.py anonymize_db
  python manage.py dbbackup --noinput --clean --servername DEIDENTIFED

  deactivate
else
  echo "Skipping restore test"
fi

echo "Backup production to Google Cloud"
if ! workon thetatauCMT; then
  echo "An error occurred setting thetatauCMT"
  exit
fi
export GNUPGHOME="/home/Venturafranklin/thetatauCMT/secrets"
export DBBACKUP_LOCAL="False"
if ! python manage.py dbbackup --encrypt --noinput; then
  echo "An error occurred backing up database to remote"
  exit
fi
