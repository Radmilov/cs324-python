import xlsxwriter

def z01():
    try:
        workbook = xlsxwriter.Workbook('Raspored.xlsx')
        worksheet = workbook.add_worksheet()
        schedule = (
            ['CS101', 'Petak 19:00'],
            ['IT101',   'Sreda 16:15'],
            ['MA101',  'Ponedeljak 17:30'],
            ['NT101',    'Utorak 18:15'],
        )
        row = 0
        col = 0
        for course, time in (schedule):
            worksheet.write(row, col,     course)
            worksheet.write(row, col + 1, time)
            row += 1

        worksheet.write(row, 0, 'Total count of courses')
        worksheet.write(row, 1, '=COUNTA(B1:B4)')

        workbook.close()
    except Exception as e:
        print(e)


def z02(array):
    tmp = 0
    i = 0
    for int in array:
        if isinstance(int, list):
            raise ValueError("Array element is a list. Please provide a valid array")
        if isinstance(int, dict):
            raise ValueError("Array element is a dict. Please provide a valid array")
        if isinstance(int, str):
            raise ValueError("Array element is a str. Please provide a valid array")
        if isinstance(int, tuple):
            raise ValueError("Array element is a tuple. Please provide a valid array")
        tmp += int
        i += 1

    return tmp / i