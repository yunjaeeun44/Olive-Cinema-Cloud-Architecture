# Olive-Cinema-Cloud-Architecture

## 📽️ 프로젝트 소개
> 글로벌 영화 예매 플랫폼 혁신을 위한 클라우드 아키텍처 설계

![image](https://github.com/user-attachments/assets/a506e1ab-70f8-4349-b4de-1ea8ddfb49fe)

해당 프로젝트는 전 세계적으로 영화관을 운영하는 글로벌 체인으로, 고객들에게 최고의 영화 경험을 제공하는 것을 목표로 하고 있습니다.  
또한 글로벌 사용자들에게 안정적이고 빠른 서비스를 보장하며, 운영 효율성을 극대화하고자 합니다. 해당 서비스의 요구사항을 파악하여 AWS 아키텍처를 설계하고 비용 최적화 전략, 보안 및 모니터링 전략을 세우고자 합니다.

LipRead PPT (https://github.com/yunjaeeun44/Olive-Cinema-Cloud-Architecture/blob/main/발표%20PPT.pdf)  

<br/>

## 📚프로젝트 기간
2024.12.15 ~ 2024.12.26  

<br/>

## 🛠️ Architecture 소개
![image](https://github.com/user-attachments/assets/69bd7559-de8a-4042-97cb-f123025f5e02)


### 📍Run 파트
![image](https://github.com/user-attachments/assets/8a836022-9d64-4f58-a2a8-10393a7e66da)
<br/>
- **ECS + Fargate**
   - 영화 예매, 좌석 선택과 같은 기본적인 기능 수행
   - 서비스의 확장성과 운영 편의성을 고려해 컨테이너와 서버리스 서비스 활용
   - CPU 사용량 지표를 통한 ECS의 서비스 규모를 오토스케일링
   - Application Load Balancing을 사용하여 서비스의 태스크 간에 트래픽을 고르게 분산
-  **SQS + lambda**
   - 결제가 완료되면 사용자에게 결제 알림을 위한 이메일을 전송
   - SQS에 메시지가 추가되면 Lambda 비동기 호출
   - SQS FIFO를 통해 정확히 1회 처리되도록 구성
-  **RDS + Proxy**
   - 데이터의 일관성을 위해 RDS, 고가용성을 위해 다중 AZ DB 인스턴스로 배포
   - Proxy를 추가해, 연결 풀을 사용함으로서 서버리스 애플리케이션이 수많은 DB 연결을 만드는 것을 방지
- **CloudFront + Lambda@edge**
   - 프론트엔드의 경우 s3로 정적 웹 호스팅
   - 지역마다 특정 데이터를 제공하기위해 CDN 서비스 활용
   - 사용자의 지리적 위치를 토대로 Lambda@edge가 S3의 특정 경로로 리다이렉션 진행
  <br/>
### 📍Ops 파트
![image](https://github.com/user-attachments/assets/25be5ed4-9267-4511-9729-a8ceadfbac7d)
<br/>
- **DataDog**
   - ECS를 모니터링하기 위한 플랫폼으로서 데이터독을 선택
   - 태스크 내부의 메인 컨테이너에 추가로 Datadof Agent 컨테이너를 추가해 매트릭을 집계하고 데이터독을 통해 모니터링을 하는 방식
- **SNS + ChatBot + Slack**
   - 슬랙을 통해 자동으로 리소스에 대한 알림이 가도록 구현
   - RDS와 ECS의 경보 혹은 이벤트를 SNS에 메세지를 전송하면, chatbot이 메세지를 받아 슬랙에 알림을 보내는 방식
    <br/>
### 📍Build 파트
![image](https://github.com/user-attachments/assets/a02c5243-2d5b-4aed-90ac-4241fb84cbee)
<br/>
- **Code Series**
