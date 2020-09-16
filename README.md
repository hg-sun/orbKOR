# orbKOR란?
문장 내 단어 간의 의존 관계(dependency)를 활용하여 자체적으로 설정한 구문 규칙에 따라 텍스트에서 필요한 구문 규칙을 추출할 수 있는 시스템

### 개발 관리

- **Image Build**

```bash
docker build . -t hg-sun/orbkor:v1.0 -f Dockerfile --built-arg PORT=18000 
```

- **Run Container**
```bash
docker run -it -p 18000:18000 -name orbkor hg-sun/orbkor:v1.0 
```




