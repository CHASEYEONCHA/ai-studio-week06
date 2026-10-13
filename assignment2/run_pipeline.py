
import csv
from pathlib import Path
from classify import classify_review

def main():
    csv_path = Path(__file__).with_name("reviews_sample.csv")

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        reviews = [row["review_text"] for row in reader]

    # 전체 리뷰 분류 및 집계
    total = 0
    failures = 0

    for row in reviews:
        total += 1
        result = classify_review(reviews)

        if result is None:
            failures += 1
            continue

    # 최종 결과 출력
    print(f"처리 {total}건 / 실패 {failures}건")

if __name__ == "__main__":
    main()