# Naver_Blog_Automation
네이버 블로그 자동화 도구
## 개요
- 네이버 블로그가 성장함에 따라 이웃의 수도 관리하기 힘들 정도로 증가하기 시작했다.
- 이웃을 관리하기 위한 자동화 도구의 필요성 증가
##  기능
- 네이버 자동 로그인
- 이웃 포스트 목록 출력
- 이웃 포스트에 댓글 달기
- 내 포스트에 달린 댓글에 대댓글 달기
## 사용법
- pyenv 설치 및 가상환경 설정
```bash
curl https://pyenv.run | bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

source ~/.bashrc  # 또는 source ~/.zshrc

pyenv install 3.12.2

pyenv virtualenv 3.12.2 naver_blog_automation

pyenv activate naver_blog_automation

pyenv deactivate
```
- 추후 완성되면 정리
