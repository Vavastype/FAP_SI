#include <iostream>
#include <fstream>
using namespace std;

//4) Crie um algoritmo em C que imprima a seguinte mensagem “Formativa 1” 100 vezes (Utilize for).

int main() {
    const string txt = "Técnicas de programação\nFormativa 1\n1) Qual tipo de variável você utilizaria para trabalhar com os seguintes dados?\na) Ano de nascimento de um usuário;\nb) Média das notas de um aluno durante o bimestre;\nc) Letras.\n2) Crie um algoritmo em pseudocódigo e fluxograma para:\na) Jogar um jogo;\nb) Vir para a faculdade;\nc) Calcular a média entre dois números.\n3) Crie um algoritmo em C que imprima a seguinte mensagem “Formativa 1”.\n4) Crie um algoritmo em C que imprima a seguinte mensagem “Formativa 1” 100 vezes (Utilize for).\n5) Crie um algoritmo em C que receba dois números informado pelo usuário e imprima as somas dos\nnúmeros em seguida.\n6) Crie um programa em C que leia a idade de uma pessoa e verifique se ela é criança (idade menor que 12\nanos), adolescente (idade entre 12 e 17 anos), adulto (idade entre 18 e 64 anos) ou idoso (idade igual ou\nsuperior a 65 anos). Em seguida, exiba a mensagem correspondente.\n7) Elabore um programa em C que receba a altura e o peso de uma pessoa e calcule o seu Índice de Massa\nCorporal (IMC). O IMC é calculado através da fórmula: IMC = peso / (altura * altura). Em seguida, exiba a\nclassificação de acordo com a tabela abaixo:\n • Abaixo do peso: IMC < 18.5\n • Peso normal: 18.5 <= IMC < 24.9\n • Sobrepeso: 25 <= IMC < 29.9\n • Obesidade: IMC >= 30\n8) Escreva um programa que receba três números inteiros como entrada e exiba a soma e o produto desses\nnúmeros.\n9) Desenvolva um programa que receba o nome e a idade de três pessoas e exiba o nome da pessoa mais\nvelha.\n10) Desenvolva um programa em C que solicite a nota final de um aluno em uma disciplina. O programa deve\ncalcular a média aritmética das notas e exibir a situação do aluno de acordo com as seguintes regras:\n • Média maior ou igual a 7: \"Aprovado\"\n • Média maior ou igual a 5 e menor que 7: \"Recuperação\"\n • Média menor que 5: \"Reprovado\";\n";

    for(int i = 0; i <= 100; i++){
        cout << txt << i << endl;
    }

    return 0;
}
