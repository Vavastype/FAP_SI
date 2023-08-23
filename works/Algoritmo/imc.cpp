#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

/*
7) Elabore um programa em C que receba a altura e o peso de uma pessoa e calcule o seu Índice de Massa 
Corporal (IMC). O IMC é calculado através da fórmula: IMC = peso / (altura * altura). Em seguida, exiba a 
classificação de acordo com a tabela abaixo:
 • Abaixo do peso: IMC < 18.5
 • Peso normal: 18.5 <= IMC < 24.9
 • Sobrepeso: 25 <= IMC < 29.9
 • Obesidade: IMC >= 30

*/

int main(){

    double weight;
    double height;
    
    int some;
    
    cout << "Digite sua altura: ";
    cin >> height;
    cout << "Digite seu peso: ";
    cin >> weight;
    
    cout << std::setprecision(4) << (weight / height) / height;
    
    return 0;
}