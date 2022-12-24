# pip install mysql-connector-python beautifulsoup4 selenium webdriver-manager lxml
# pip install pandas matplotlib seaborn plotly plotly-express xlrd openpyxl
# ref: http://mahaljsp.asuscomm.com/index.php/2019/08/30/python_dailycash/

"""
資料庫建置
CREATE TABLE `dailycash` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `draw` varchar(10) COLLATE utf8mb3_unicode_ci NOT NULL,
  `d1` int DEFAULT NULL,
  `d2` int DEFAULT NULL,
  `d3` int DEFAULT NULL,
  `d4` int DEFAULT NULL,
  `d5` int DEFAULT NULL,
  `n1` int DEFAULT NULL,
  `n2` int DEFAULT NULL,
  `n3` int DEFAULT NULL,
  `n4` int DEFAULT NULL,
  `n5` int DEFAULT NULL,
  `sales` int DEFAULT NULL,
  `prizes` int DEFAULT NULL,
  `1st` int DEFAULT NULL,
  `2nd` int DEFAULT NULL,
  `3rd` int DEFAULT NULL,
  `4th` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `date_UNIQUE` (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci COMMENT='今彩539, d12345 獎號順序, n12345大小排序, sales銷售額, prizes總獎金, 1234獎項對應 8M, 20k, 300, 50'
"""

'''
setup auto run script in Windows using Task Schedule
https://www.jcchouinard.com/python-automation-using-task-scheduler/
'''