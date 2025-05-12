import pandas as pd
url='https://en.wikipedia.org/wiki/Comparison_of_text_editors'
editor_table=pd.read_html(url,match='Developer')
print(len(editor_table))
# print(editor_table[0])
table_DF=pd.DataFrame(editor_table[0])
# multi col 한개로 줄이기
table_DF.columns=table_DF.columns.droplevel(level=0)
print(table_DF)