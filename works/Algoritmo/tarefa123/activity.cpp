// #include <stdio.h>
#include <iostream>
#include <chrono>
#include <thread>
// #include <string>
#include <typeinfo>


//1) Qual tipo de variável você utilizaria para trabalhar com os seguintes dados?
/*
a) Ano de nascimento de um usuário;
>> Utilizaria a variavel tipo int exemplo: int year = 25 por lidar com numeros

b) Média das notas de um aluno durante o bimestre;
>> Utilizaria tipo float para lidar com casas decimais: float noteStunt = 65.85

c) Letras.
>> Utilizado para lidar com strings char: char studentName = ''
*/

//2) Crie um algoritmo em pseudocódigo e fluxograma para:

//(a) - Jogar um jogo

// using namespace std;

// int main()
// {
//     int use;
//     string options[] = {"Start", "Credits","Exit"};

//     cout << "Digite: " << endl << "0° Start" << endl << "1° Credits" << endl << "2° Exit" << endl;
//     cin >> use;
//     cout << "Carregando..." << endl;

//     if(use >= 0 && use < 3){
//         if(options[use] == "Start"){
//             std::this_thread::sleep_for(std::chrono::seconds(5));
//             cout << "Jogo Carregado!" << endl;
//         }else if(options[use] == "Credits"){
//             cout << "Criado Por: Wagner De Souza Mendes" << endl;
//         }else{
//             std::this_thread::sleep_for(std::chrono::seconds(5));
//             cout << "Jogo Finalizado." << endl;
//         }
//     }else{
//         printf("Por favor adiciona valores validos ");
//         cout << "Digite: " << endl << "0° Start" << endl << "1° Credits" << endl << "2° Exit" << endl;
//     }

//     return 0;
// }

//b) Vir para a faculdade;

// using namespace std;

// int main()
// {
//     char home;
//     cout << "Disponíbilidade: s para (SIM) n para (Não).";
//     cin >> home;

//     if(home == 's'){
//         cout << "Aluno Wagner presente." << endl;
//     }else if(home == 'n'){
//         cout << "Aluno Wagner não presente." << endl;

//     }else{
//         cout << "Por favor digite um valor valido!" << endl;
//     }

//     return 0;
// }

//c) Calcular a média entre dois números.

// using namespace std;

// int main(){

//     int noteOne;
//     int noteTwo;

//     cout << "Primeira nota: ";
//     cin >> noteOne;
//     cout << "Segunda nota: ";
//     cin >> noteTwo;

//     int median = (noteOne + noteTwo) / 2;

//     cout << "Sua média é: " << median << " pontos" << endl;

//     return 0;
// }