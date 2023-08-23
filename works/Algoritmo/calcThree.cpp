#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;

/*
8) Escreva um programa que receba três números inteiros como entrada e exiba a soma e o produto desses 
números
*/

// int main(){

//     int x;
//     int y;
//     int z;
    
//     int some;
    
//     cout << "Digite o primeiro numero: ";
//     cin >> x;
//     cout << "Digite o segundo numero: ";
//     cin >> y;
//     cout << "Digite o terceiro numero: ";
//     cin >> z;
    
//     cout << (x + y + z);
    
//     return 0;
// }

/*
9) Desenvolva um programa que receba o nome e a idade de três pessoas e exiba o nome da pessoa mais 
velha.
*/

int main(){

    string nameOne;
    int ageOne;
    string nameTwo;
    int ageTwo;
    string nameThree;
    int ageThree;
    
    //1°
    cout << "Primeiro aluno: ";
    cin >> nameOne;
    cout << "Sua idade: ";
    cin >> ageOne;

    //2°
    cout << "Primeiro aluno: ";
    cin >> nameTwo;
    cout << "Sua idade: ";
    cin >> ageTwo;

    //3°
    cout << "Primeiro aluno: ";
    cin >> nameThree;
    cout << "Sua idade: ";
    cin >> ageThree;

    if(ageOne > ageTwo && ageOne > ageThree){
        cout << nameOne << " é mais velho.";
    }

    if(ageTwo > ageOne && ageTwo > ageThree){
        cout << nameTwo << " é mais velho.";
    }

    if(ageThree > ageTwo && ageThree > ageOne){
        cout << nameThree << " é mais velho.";
    }

    return 0;
}