import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('hier hoort de key')
worksheet = sh.sheet1

# res = worksheet.get_all_records()
# res = worksheet.get_all_values()
# res = worksheet.row_values(1)
# res = worksheet.get('A2:C2')

# user = ["Susan", 25, "Sydney"]
# worksheet.insert_row(user, 3)

# print(res)

# worksheet.update_cell(6, 2, 28)

# worksheet.delete_rows(1)
