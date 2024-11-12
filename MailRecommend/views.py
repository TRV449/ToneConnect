from rest_framework.views import APIView
from rest_framework.response import Response
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# .env 파일에서 API 키 로드
load_dotenv()


class GenerateKeywordsAPIView(APIView):
    def post(self, request):
        # POST 요청으로부터 데이터 가져오기
        keywords_str = request.data.get('keywords', '')

        if not keywords_str:
            return Response({"error": "Keywords not provided"}, status=400)

        # LangChain 구성
        llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=os.getenv("GPT_API"))

        # 프롬프트 템플릿 정의
        system_message = (
            "너는 이제부터 교수님에게 이론적이고 학문적인 내용이나 공적인 일로 질문을 하고 싶은 학생이야. "
            "앞으로 내가 하는 모든 말에 대해 다음과 같은 특징을 만족하도록 말을 바꿔줘:\n"
            "1. 문장이 간결하고 단도직입적이어야 해.\n"
            "2. 어투는 최대한 정중하게 해야 해. 이모지 등은 사용을 자제해야 해.\n"
            "3. 마무리는 감사 인사와 본인 이름 (OOO 올림) 등으로 마무리하는 것이 좋아.\n"
            "4. 중요한 내용은 빠뜨리지 않도록 변환해줘.\n"
            "5. 대신, 높은 수준의 어휘 사용.\n"
            "6. 허례허식도 상관 없으니 최대한 예의를 지키는 말투로.\n"
            "7. 같은 내용이라도 조금 길면 좋아.\n"
            "8. 모든 메일의 시작에는 자신의 소속과 이름같은게 들어가야 해. 만약 원문에 그런 내용이 없다면 'OOO의 OOO입니다.'와 같이 써놔.\n"
            "9. 일정 조율과 같이 찾아뵈어야 할 때는 능동적인 태도가 중요해. 만약 원문에 그런 정보가 없는데 일정 조율이 필요하면 다음과 같이 작성해:\n"
            "   아래에 제가 가능한 시간을 표기해두었습니다.\n"
            "   XX월 XX일 X요일 XX:XX~XX:XX\n"
            "   근데 그래도 너무 학생들이 안쓸 것 같은 높은 수준의 어휘는 자제하도록 하자."
        )

        user_message = (
            "{keywords}이 주제로 공손한 메일을 작성하려고 해. "
            "이 때 {keywords} 다음에 나올 만한 키워드가 뭐가 있을까? "
            "각 키워드에 인덱스를 부여해서 반환해줘. "
            "예를 들어, 1: 과제 질문, 2: 문안 인사 이런식으로. "
            "너의 다른 응답은 필요 없고 저렇게만 주면 돼 3~7개 사이의 선택지로 줘."
            "이미 키워드에 포함되어 있는 단어는 제외해줘."
        )

        # ChatPromptTemplate 생성
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message),
            ("user", user_message)
        ])

        # LLMChain 생성
        chain = LLMChain(llm=llm, prompt=prompt)

        # Chain 실행
        response = chain.invoke({"keywords": keywords_str})

        # 결과를 JSON 응답으로 반환
        return Response({'response': response})


class GenerateMailAPIView(APIView):
    def post(self, request):
        # POST 요청으로부터 데이터 가져오기
        keywords_str = request.data.get('keywords', '')

        if not keywords_str:
            return Response({"error": "Keywords not provided"}, status=400)

        # LangChain 구성
        llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=os.getenv("GPT_API"))

        # 프롬프트 템플릿 정의
        system_message = (
            "너는 이제부터 교수님에게 이론적이고 학문적인 내용이나 공적인 일로 질문을 하고 싶은 학생이야. "
            "앞으로 내가 하는 모든 말에 대해 다음과 같은 특징을 만족하도록 말을 바꿔줘:\n"
            "1. 문장이 간결하고 단도직입적이어야 해.\n"
            "2. 어투는 최대한 정중하게 해야 해. 이모지 등은 사용을 자제해야 해.\n"
            "3. 마무리는 감사 인사와 본인 이름 (OOO 올림) 등으로 마무리하는 것이 좋아.\n"
            "4. 중요한 내용은 빠뜨리지 않도록 변환해줘.\n"
            "5. 대신, 높은 수준의 어휘 사용.\n"
            "6. 허례허식도 상관 없으니 최대한 예의를 지키는 말투로.\n"
            "7. 같은 내용이라도 조금 길면 좋아.\n"
            "8. 모든 메일의 시작에는 자신의 소속과 이름같은게 들어가야 해. 만약 원문에 그런 내용이 없다면 'OOO의 OOO입니다.'와 같이 써놔.\n"
            "9. 일정 조율과 같이 찾아뵈어야 할 때는 능동적인 태도가 중요해. 만약 원문에 그런 정보가 없는데 일정 조율이 필요하면 다음과 같이 작성해:\n"
            "   아래에 제가 가능한 시간을 표기해두었습니다.\n"
            "   XX월 XX일 X요일 XX:XX~XX:XX\n"
            "   근데 그래도 너무 학생들이 안쓸 것 같은 높은 수준의 어휘는 자제하도록 하자."
        )

        user_message = (
            "{keywords}이 주제로 메일을 작성하도록 해. 제목은 쓰지 말고, 본문만 작성하는거야."
        )

        # ChatPromptTemplate 생성
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message),
            ("user", user_message)
        ])

        # LLMChain 생성
        chain = LLMChain(llm=llm, prompt=prompt)

        # Chain 실행
        response = chain.invoke({"keywords": keywords_str})

        # 결과를 JSON 응답으로 반환
        return Response({'response': response})
