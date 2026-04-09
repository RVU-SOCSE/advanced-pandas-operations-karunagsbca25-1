Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
=========== RESTART: C:/Users/karun/OneDrive/Desktop/python/prg 13.py ==========
Employee Details:
   EmployeeID     Name   Department
0         101    Alice           HR
1         102      Bob  Engineering
2         103  Charlie  Engineering
3         104    David           HR
4         105      Eva    Marketing

Employee Salaries:
   EmployeeID  Salary
0         101   50000
1         102   70000
2         103   80000
3         104   55000
4         105   60000

Sales Region 1:
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350

Sales Region 2:
        Date Region  Sales
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310

Average Salary per Department:
Department
Engineering    75000.0
HR             52500.0
Marketing      60000.0
Name: Salary, dtype: float64

Merged Employee Data:
   EmployeeID     Name   Department  Salary
0         101    Alice           HR   50000
1         102      Bob  Engineering   70000
2         103  Charlie  Engineering   80000
3         104    David           HR   55000
4         105      Eva    Marketing   60000
Stock Prices Data:
            Price
Date             
2024-01-01    150
2024-01-02    155
2024-01-03    152
2024-01-04    158
2024-01-05    160

Market Volume Data:
        Date  Volume
0 2024-01-01    1000
1 2024-01-02    1100
2 2024-01-03    1050
3 2024-01-04    1150
4 2024-01-05    1200

Joined Stock Prices and Market Volume Data:
Empty DataFrame
Columns: [Price, Date, Volume]
Index: []

Consolidated Sales Data:
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310
