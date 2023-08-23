#include <iostream>
#include <fstream>
using namespace std;

/*
6) Crie um programa em C que leia a idade de uma pessoa e verifique se ela é criança (idade menor que 12 
anos), adolescente (idade entre 12 e 17 anos), adulto (idade entre 18 e 64 anos) ou idoso (idade igual ou 
superior a 65 anos). Em seguida, exiba a mensagem correspondente.
*/

int main(){

    int age;

    cout << "Digite sua idade atual: ";
    cin >> age;
    
    if(age < 12){
        cout << "Criança";
    }else if(age >= 12 && age <= 17){
        cout << "Adolescente";
    }else if(age >= 18 && age <= 64){
        cout << "adulto";
    }else{
        cout << "Idoso";
    }


    return 0;
}