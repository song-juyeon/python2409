# import my_module
# my_module.나라친구()

# import tour.jeonnam
# tour.jeonnam.채리()
#
# from tour import jeonnam
# jeonnam.채리()
#
# from tour.jeonnam import 채리
# 채리()

# import tour.jeonnam as tj
# tj.채리()
#
# from tour import jeonnam as je
# je.채리()
#
# from tour.jeonnam import 채리 as cherry
# cherry()

from tour import *
jeonnam.채리()            #__init__에 __all__에 넣어야 실행 가능
gp = gangwondo.GangwondoPackage()
print(gp)