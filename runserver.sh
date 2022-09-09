cd ~/Desktop/odoo_dev/odoo
source ./env/bin/activate
python3 odoo-bin --addons-path=addons,~/Desktop/odoo_dev/projectExam/addonrafi -d kawakadodb --update all
deactivate
