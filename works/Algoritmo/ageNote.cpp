#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

/*
10) Desenvolva um programa em C que solicite a nota final de um aluno em uma disciplina. O programa deve
calcular a média aritmética das notas e exibir a situação do aluno de acordo com as seguintes regras:
 • Média maior ou igual a 7: "Aprovado"
 • Média maior ou igual a 5 e menor que 7: "Recuperação"
 • Média menor que 5: "Reprovado
*/

int main(){

    int noteOne;
    int noteTwo;
    int median;

    cout << "Primeira nota: ";
    cin >> noteOne;
    cout << "Segunda nota: ";
    cin >> noteTwo;

    median = (noteOne + noteTwo) / 2;

    if(median > 70){
        cout << "Aprovado" << endl;
    }else if(median >= 50 && median < 70){
        cout << "Recuperação" << endl;
    }else{
        cout << "Reprovado" << endl;
    }

    return 0;
}

