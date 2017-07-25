#!/bin/bash
(hive -f test_report1.sql ;hive -f test_report2.sql) | mail -s "report1" ben.thompson.j@gmail.com