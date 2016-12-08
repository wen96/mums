. "$(dirname "$0")/init.sh"

. "$SCRIPTS_DIR/pylint.sh"
coverage run --source='.' manage.py test
coverage report