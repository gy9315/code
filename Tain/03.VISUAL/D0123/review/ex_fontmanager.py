import matplotlib.font_manager  as fm
# 시스템에 설치된 모든 폰트 경로 확인
for font in fm.findSystemFonts(fontpaths=None, fontext='ttf'):
    print(font)


# # 특정 폰트 이름으로 경로 검색
# nanum_fonts = [f for f in font_manager.findSystemFonts() if 'Nanum' in f]
# print("Nanum 폰트 경로:", nanum_fonts)
