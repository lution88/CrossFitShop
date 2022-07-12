# CrossFitShop
평소 즐겨하는 운동인 크로스핏의 장비 쇼핑몰입니다.

## 프로젝트 Description
### 1. 프로젝트명
    : CrossFitShop
### 2. 프로젝트 계기
    : Django REST Framework 로 쇼핑몰을 구상해 보던 중 평소 하는 운동인 크로스핏 제품을 파는 쇼핑몰을 제작하기로 결심.
### 3. 프로젝트 서비스 설명
    : 판매자의 경우 판매할 제품 조회, 등록, 수정, 삭제 가능
      구매자의 경우 구매하고 싶은 제품 조회, 찜, 구매 가능
      제품마다 판매자가 설정한 날짜동안만 제품 거래 가능.
---
## DATABASE 모델링
<a href="https://www.figma.com/file/e2djlW5nxbh7JVixjTUVFn/%ED%81%AC%EB%A1%9C%EC%8A%A4%ED%95%8F_%EC%87%BC%ED%95%91%EB%AA%B0?node-id=0%3A1">![img.png](img.png)</a>
---
## 구현기능
| `User`     |  `Product`   |`Review` |
|------------|:------------:|-------------:|
| - 유저 정보 조회 | - product 조회 |- review 조회 |
| - 유저 회원 가입 | - product 생성 |- review 생성 |
| - 유저 정보 수정 | - product 수정 |- review 수정 |
| - 유저 정보 삭제 | - product 삭제 |- review 삭제 |
| - 유저 로그인   | - wish(찜) 생성 |- comment 조회 |
| - 유저 로그아웃  | - wish(찜) 삭제 |- comment 생성 |
| -  |      -       |  - comment 수정 |
| -  |      -       |  - comment 삭제 |

---
## 기술스택
<p dir="auto">
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/9caad9a9b63e2b7bddba6f8f091f5e367845ba821a82b0034b0b4748fff7fa04/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d79656c6c6f77"><img src="https://camo.githubusercontent.com/9caad9a9b63e2b7bddba6f8f091f5e367845ba821a82b0034b0b4748fff7fa04/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d79656c6c6f77" data-canonical-src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=yellow" style="max-width: 100%;"></a> 
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/4d74b36962a1b06aed5f035f2f95f131059b2b551c7e6d81630f7df7831b9f80/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/4d74b36962a1b06aed5f035f2f95f131059b2b551c7e6d81630f7df7831b9f80/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&amp;logo=django&amp;logoColor=white" style="max-width: 100%;"></a>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/a9a95986631c3d4945a63d42d2864e3918a834d672d907e174a29f743a1bc3f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/a9a95986631c3d4945a63d42d2864e3918a834d672d907e174a29f743a1bc3f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/git-F05032?style=for-the-badge&amp;logo=git&amp;logoColor=white" style="max-width: 100%;"></a>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/e6f0ce6b8ea91992107c852e6b014c1bebfdf8edf67f74e1390394e6d2175b5e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f626f6f7473747261702d3739353242333f7374796c653d666f722d7468652d6261646765266c6f676f3d626f6f747374726170266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/e6f0ce6b8ea91992107c852e6b014c1bebfdf8edf67f74e1390394e6d2175b5e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f626f6f7473747261702d3739353242333f7374796c653d666f722d7468652d6261646765266c6f676f3d626f6f747374726170266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&amp;logo=bootstrap&amp;logoColor=white" style="max-width: 100%;"></a>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/12e622b9695e9c19ec5a936b1c35a62e9fc11f47fee3883af53dfe0e762068c8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d706f73746d616e266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/12e622b9695e9c19ec5a936b1c35a62e9fc11f47fee3883af53dfe0e762068c8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d706f73746d616e266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&amp;logo=postman&amp;logoColor=white" style="max-width: 100%;"></a>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/3d22c64f1b482b0ed7da89b651ffe59c7dde3c480cd7769a0f891a1cc399b11e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e6f74696f6e2d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d6e6f74696f6e266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/3d22c64f1b482b0ed7da89b651ffe59c7dde3c480cd7769a0f891a1cc399b11e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e6f74696f6e2d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d6e6f74696f6e266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/notion-000000?style=for-the-badge&amp;logo=notion&amp;logoColor=white" style="max-width: 100%;"></a>
</p>

---
