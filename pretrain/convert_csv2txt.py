from io import StringIO
import pandas as pd
import os



# 데이터를 DataFrame으로 읽음

def convert(csv_filename):
  df = pd.read_csv(csv_filename)

  # 'doc_id' 기준으로 문서 병합
  grouped = df.groupby('doc_id').agg({
    'title': 'first',  # 'title'은 첫 번째만 유지
    'sentence': ' '.join  # 'sentence'는 문장들을 모두 합침
  }).reset_index()

  # 각 문서의 내용을 별도의 텍스트 파일로 저장
  filename = csv_filename.replace('csv','txt')
  if(os.path.exists(filename)):
    os.remove(filename)
    print("File was deleted : " + filename)
  for index, row in grouped.iterrows():
    with open(filename, 'a', encoding='utf-8') as file:
      file.write(f"{row['title']} {row['sentence']}\n") 

  print("Files have been saved : " + filename)

for filename in os.listdir(os.getcwd()):
  if filename.endswith('.csv'):  # 확장자가 .csv인 파일만 처리
    convert(filename)  

