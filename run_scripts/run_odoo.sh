#!/bin/bash
python3 -m debugpy --listen 0.0.0.0:8888 /usr/bin/odoo --db_host=db --db_port=5432 --db_user=odoo --db_password=odoo --database=Odoo14 --limit-time-real=100000 -u my_test_002