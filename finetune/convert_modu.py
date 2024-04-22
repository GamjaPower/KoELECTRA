# 주어진 데이터
data = {
    "form": "태안군의회, 2019년 군민중심’의정성과 빛났다!",
    "word": [
        {"id": 1, "form": "태안군의회,", "begin": 0, "end": 6},
        {"id": 2, "form": "2019년 군민중심 의정성과", "begin": 7, "end": 22},
        {"id": 3, "form": "빛났다!", "begin": 23, "end": 27}
    ],
    "NE": [
        {"id": 1, "form": "태안군의회", "label": "OGG_POLITICS", "begin": 0, "end": 5},
        {"id": 2, "form": "2019년", "label": "DT_YEAR", "begin": 7, "end": 12}
    ]
}

# 전체 텍스트를 공백으로 분리
tokens = data["form"].split()

# 태그 리스트 초기화
tags = ["O"] * len(tokens)

# NE 정보를 사용하여 태그 설정
for entity in data["NE"]:
    start = entity["begin"]
    end = entity["end"]
    label = entity["label"]

    # NE를 포함하는 토큰 찾기
    entity_tokens = data["form"][start:end+1].split()
    if entity_tokens:
        # 첫 토큰은 B 태그
        tags[tokens.index(entity_tokens[0])] = label + "-B"
        # 나머지 토큰은 I 태그
        for token in entity_tokens[1:]:
            if token in tokens:
                tags[tokens.index(token)] = label + "-I"

# 태그와 토큰을 출력
electra_data = " ".join(f"{token} {tag}" for token, tag in zip(tokens, tags))
print(electra_data)
