# mock_llm.py — 6~12주차용 모의 LLM 모듈
import random

def mock_llm_call(system, user_message, temperature=0.2, max_tokens=500):
    """실제 API와 동일한 인터페이스를 갖는 모의 함수.
    13주차에 이 함수의 내부만 실제 Anthropic 호출로 교체한다."""

    # FIXED: 20% 확률로 불량 응답 반환
    if random.random() < 0.2:
        malformed_responses = [
            # 유형 1: 코드펜스 포함
            '```json\n{"category": "배송", "sentiment": "긍정", "score": 4}\n```',
            # 유형 2: 사족 포함
            '물론입니다! 분석 결과는 다음과 같습니다. {"category": "배송", "sentiment": "긍정", "score": 4}',
            # 유형 3: 잘린 JSON
            '{"category": "배송", "sentim',
        ]

        return {
            "text": random.choice(malformed_responses),
            "stop_reason": "end_turn",
            "usage": {"input_tokens": 120, "output_tokens": 35}
        }

    reviews_keywords = {
        "배송": '{"category": "배송", "sentiment": "긍정", "score": 4}',
        "환불": '{"category": "환불", "sentiment": "부정", "score": 2}',
        "품질": '{"category": "품질", "sentiment": "긍정", "score": 5}',
    }
    for keyword, canned in reviews_keywords.items():
        if keyword in user_message:
            return {"text": canned, "stop_reason": "end_turn",
                    "usage": {"input_tokens": 120, "output_tokens": 35}}
    return {"text": '{"category": "기타", "sentiment": "중립", "score": 3}',
            "stop_reason": "end_turn",
            "usage": {"input_tokens": 120, "output_tokens": 35}}
