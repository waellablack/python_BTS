logs = [('192.168.1.1', '2024-09-12 12:15:10'),('192.168.1.2', '2024-09-12 12:16:15'),('192.168.1.1', '2024-09-12 12:20:20'),('192.168.1.3', '2024-09-12 12:30:25'),('192.168.1.1', '2024-09-12 12:35:30')]
nb_connexion = sum(1 for log in logs.values() if log == "3" )
tentative_connexion = 0
for log in logs: 


#     if log in logs :
#         connexion.append(log)
#         tentative_connexion += 1
#     else : 
#         connexion = 1
# print(tentative_connexion)
# print(connexion)



#     if log[0] >= 3 :
#         connexion.append(log[0])
#         tentative_connexion += 1
#     else : 
#         connexion = 1
# print(tentative_connexion)
# print(connexion)


# connexion = []
# tentative_connexion = 0
# for log in logs:
#     if log in connexion:
#         connexion += 1
#     else:
#         connexion = 1



