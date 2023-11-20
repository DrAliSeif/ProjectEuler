import numpy as np
def calculate_Multiples (number_of_Multiples,end_of_number):
    list_of_Multiples=[]
    for i in range (1,end_of_number):
        if i%number_of_Multiples==0:
            list_of_Multiples.append(i)
    return list_of_Multiples

def final_list(previous_list,list_of_Multiples):
    return previous_list+list_of_Multiples

def main():
    last_number=1000
    n=[]
    n=final_list(n,calculate_Multiples(3,last_number))
    n=final_list(n,calculate_Multiples(5,last_number))
    print(np.sum(list(set(n))))

if __name__=="__main__":
    main()
