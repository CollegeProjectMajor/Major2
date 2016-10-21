import pymysql
import xlwt
import xlrd
from xlrd import open_workbook
import random

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='aanchal07', db='major1', autocommit=True)
cur = conn.cursor()
# wb = open_workbook("training-set/training_set.xls")
# for s in wb.sheets():
# 	for row in range(1, s.nrows):
# 		stri = "INSERT INTO training_set(factor1, factor2, red, green, nir, mir, rs1, rs2, dem, decision) 
#VALUES ('%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%s')" 
#% (s.cell(row,0).value, s.cell(row,1).value, s.cell(row,2).value, s.cell(row,3).value, s.cell(row,4).value, s.cell(row,5).value,s.cell(row,6).value, s.cell(row,7).value, s.cell(row,8).value, s.cell(row,9).value)
# 		cur.execute(stri)

counter = 1
while (counter <= 150):
	stri = "INSERT INTO test_set(factor1, factor2, red, green, nir, mir, rs1, rs2, dem, id) VALUES ('%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')" % (random.randint(0, 531), random.randint(0, 468), random.randint(3, 185), random.randint(17, 146), random.randint(0, 248), random.randint(0, 255), random.randint(0, 252), random.randint(0, 255), random.randint(0, 252), counter)
	cur.execute(stri)
	counter += 1

