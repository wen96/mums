. "$(dirname "$0")/init.sh"

echo "Running linting on $ROOT_DIR ..."
. "$SCRIPTS_DIR/pylint.sh"

echo "Running django tests on $ROOT_DIR ..."
python manage.py test --testrunner="xmlrunner.extra.djangotestrunner.XMLTestRunner" --settings=settings.testing_ci
