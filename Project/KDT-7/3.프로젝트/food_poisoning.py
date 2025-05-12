import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
# 표현방식
a=[37,40]
plt.figure(figsize=(10,5))
# 평균 기온
plt.plot(range(2000,2024),[1,21,10,35,23,40,12,43,23,23,30,32,31,12,34,12,11,5,32,32,32,18,15,22],'tomato',label='Temperature')
# 식중독 균 위험 지역 표현
# 1. 병원성 대장균
a=[35,40]
plt.fill_between(range(2000,2024),a[0],a[1],color='lightgray',alpha=0.3,label='대장균 최적증식온도')
plt.text(pd.Series(range(2000,2024)).median(),y=sum(a)/len(a),s='대장균 증식구간',color='k')
# 2. 살모넬라
a=[35,37]
plt.fill_between(range(2000,2024),a[0],a[1],color='k',alpha=0.3,label='살모넬라 최적증식온도')
plt.text(pd.Series(range(2000,2024)).median()-5,y=sum(a)/len(a),s='살모넬라 증식구간',color='k')
a=[30,37]
plt.fill_between(range(2000,2024),a[0],a[1],color='green',alpha=0.3,label='장염비브리오 최적증식온도')
plt.text(pd.Series(range(2000,2024)).median()+5,y=sum(a)/len(a),s='장염비브리오 증식구간',color='k')
# for문 사용해서 하면 편해요(방법)
# [1] 누나가 올려준대로 DateFrame만들어서 사용하면 됩니다
# ----------------------------------------------------
# 예시를 들어주기 위해 이렇게 만들었어요
# ----------------------------------------------------
# 자료 표현 방법
# 1. 온도 없이 처음에는 각 식중독 균이 어떤 온도에서 활동하는지 단순 증식구간과 위험온도만 표현
#                                   |
#                                   |
#                                   V
# 2-1. 연도별 온도 표현
# 2-2. 최적증식온도 min value값을 평균, max value값을 평균 -> 증식구간을 새로 평균값을 표현
# 2-3. 위험 온도 평균, 새로 위험온도 표현
# ------------------------------------------------------------------------------------------------------
# 위험온도 표현
plt.plot(range(2000,2024),[37]*24,'--',c='lightgray')
plt.plot(range(2000,2024),[30]*24,'--',c='k')
plt.plot(range(2000,2024),[20]*24,'--',c='green')
plt.yticks(range(60)[::5])
plt.legend(loc=2)
plt.show()